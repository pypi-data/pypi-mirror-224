from xml.dom.minidom import parse

#from numpy import array as nparray
#from numpy import savetxt, pi, loadtxt, genfromtxt, reshape
#from collections import OrderedDict
#from re import search
from copy import deepcopy

from os.path import dirname, realpath

from pyIBA.main_idf import main_idf
from pyIBA.codes.NDF import NDF



class IDF(main_idf, NDF):
	"""If a file path is given, the information is loaded from an existing file 
	(i.e. it calls ``load_file()``). Otherwise, it creates a blank object (i.e.
	it call ``new_file()``).
		
		Args:
		    filepath (str, optional, default = ''): Path to the IDF file, if '' 
		    the IDF object is blank
	"""
	def __init__(self, filepath = ''):
		"""Initializes an IDF object. If a file path is given, the 
		information is loaded from an existing file. Otherwise, it
		creates a blank object.
		
		Args:
		    filepath (str, optional, default = ''): Path to the IDF file, if '' the IDF object is blank
		"""
		self.executable_dir = dirname(realpath(__file__)) + '/'

		if filepath != '':
			self.load_file(filepath)
			# self.file_path = filepath
			# self.path_dir = '/'.join(filepath.split('/')[:-1]) + '/'
			# self.file_name = filepath.split('/')[-1]
		else:
			self.new_file()


	
	def load_file(self, filename):
		"""
		Loads data from a IDF file into an IDF object.
		
		Args:
		    filename (str): path to the IDF file.
		"""

		self.file = parse(filename)
		self.file_name = filename.split('/')[-1].split('.')[0]
		self.path_dir = '/'.join(filename.split('/')[:-1]) + '/'
		if self.path_dir == '/':
			self.path_dir = ''

		self.file_path = filename
		self.name = self.file_name.split('.')[0]

		self.user = self.get_user()
		self.description = self.get_notes()
		self.dataxy_files = []
		self.geo_files = []
		self.str_files = []
		self.prf_files = []
		self.spc_files = []
		self.simulation_group = []
		self.shared_charge = []
		self.sim_version_history = []
		
	   
	def new_file(self):
		"""
		Creates a new IDF file.
		"""
		self.file = parse(self.executable_dir + 'aux_files/idf_style.xml')
		self.path_dir = ''
		self.file_path = ''
		self.file_name = ''
		self.name = ''
		self.user = self.get_user()
		self.description = self.get_notes()
		self.dataxy_files = []
		self.geo_files = []
		self.str_files = []
		self.prf_files = []
		self.spc_files = []
		self.simulation_group = []
		self.shared_charge = []


	def copy(self):
		return deepcopy(self)
