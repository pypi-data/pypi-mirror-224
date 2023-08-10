
from numpy import array as nparray
from numpy import savetxt, pi, loadtxt, genfromtxt
from matplotlib.pyplot import subplots, pause as pltpause


from collections import OrderedDict
from re import search

from pyIBA.auxiliar import *


from traceback import print_exc

class main_idf:
	"""Main engime of pyIDF. This classes contains all of the methods
	to edit the fundamental XML schema for the IDF files. Note that the
	analysis entries have their own distinct classes and XML schemas.

	"""
	
	def get_user(self):
		""" 		
		Function to get the user's name from the IDF object.

		Returns: 
			The user's name.
			TYPE: str
		"""
		return get_xml_entry(self.file,'user') or ''

	def get_notes(self):
		notes_entry = get_xml_section(self.file, 'notes')[0]
		note_entries = get_xml_section(notes_entry, 'note')
		
		notes = []

		for n in note_entries:
			note = n.firstChild
			if note is None:
				note = ''
			else:
				note = n.firstChild.nodeValue
			notes.append(note)
			
		return notes

	####################### Methods to set Note and User  #######################
	
	def set_user(self, user):
		users_entry = get_xml_section(self.file, 'users')[0]
		
		self.change_node_value(user, users_entry, 'user')
		self.user = get_xml_entry(self.file,'user')

	def set_note(self, note, append = False):
		"""Sets a note related to the the IDF file. 
		If append is True the note will be append to the notes add previously.
		
		Args:
			note (str): A string with the note
			append (bool, optional): If True, the note is appended to the existing notes, 
				if False the exiting notes will be overwritten. Defaults to False
		"""
		notes_entry = get_xml_section(self.file, 'notes')[0]
		
		if append is False:
			self.remove_nodes(notes_entry, 'note')
		self.change_node_value(note, notes_entry, 'note', append=append)
		self.description = self.get_notes()
		
	
	
		


	## Methods for getting the spectra
	
	def get_spectrum(self, spectra_id=0):
		"""Gets the XML entry regarding spectrum[spectra_ID].
		Mostly to be used internally.
		
		Args:
			spectra_id (int, optional): ID of the spectrum, default is 0
		
		Returns: 
			DOM Element or None: The XML entry of spectrum[spectra_id].
			
		"""

		spectra = get_xml_section(self.file, 'spectra')
		if spectra is None: 
			print('Spectra entry missing from file')
			return
		
		spectrum = spectra[0].getElementsByTagName('spectrum')
		 # print(spectrum)
		if spectra_id >= len(spectrum): 
			print('Wrong spectra id')
			return
		
		return spectrum[spectra_id]

	def get_simulation(self, spectra_id=0, simulation_id = 0):
		"""Gets the XML entry regarding simulation[simulation_id] of spectrum[spectra_ID].
		Note that one spectrum can have multiple simulations. For instance:

		.. code-block:: python

			self.get_simulation(spectra_id = 0, simulation_id = 2)

		returns the XML entry of simulation 2 from spectrum 0.
		Mostly to be used internally.
		
		Args:
			spectra_id (int, optional): ID of the spectrum, default is 0
			simulation_id (int, optional): ID of the simulation in spectrum_id, default is 0
		
		Returns:
			DOM Element or None: The XML entry of simulation[simulation_id]
		"""

		spectra = self.get_spectrum(spectra_id=spectra_id)
		if spectra_id >= self.get_number_of_spectra(): 
			print('Wrong spectra id')
			return
		
		
		simulations_entry = self.get_section(spectra, 'simulations', create_if_not_found = ['process', 'simulations'])[0]

		# simulations = simulations_entry.getElementsByTagName('simulation')
		simulations = self.get_section(simulations_entry, 'simulation', 
											  create_if_not_found = ['simulation'])

		if simulation_id >= len(simulations):
			print('Wrong simulation id')
			return

		return simulations[simulation_id]
	
	def append_simulation_entry(self, total_simulations, spectra_id = 0):
		"""Change the total number of simulation entries of spectrum = spectra_id.
		
		Args:
			total_simulations (int): New total number of simulations.
			spectra_id (int, optional): Spectrum ID to perform the change. Defaults to 0.
		"""
		spectrum = self.get_spectrum(spectra_id=spectra_id)
		simulations_entry = self.get_section(spectrum, 'simulations', 
											   create_if_not_found = ['process', 'simulations'])[0]
		simulation_entries = self.get_section(simulations_entry, 'simulation', 
											  create_if_not_found = ['simulation'])

		nsimulations = len(simulation_entries)

		if total_simulations >= nsimulations:
			for i in range(total_simulations - nsimulations):
				self.create_element(simulations_entry, 'simulation')

	def remove_simulation_entry(self, spectra_id, simulation_id):
		"""Deletes simulation[spectra_id, simulation_id]
		
		Args:
			spectra_id (int): ID of the spectrum to delete.
			simulation_id (int): ID of the simulation to delete.

		"""

		spectrum = self.get_spectrum(spectra_id=spectra_id)
		simulations_entry = self.get_section(spectrum, 'simulations', 
											   create_if_not_found = ['process', 'simulations'])[0]
		# simulation_entries = self.get_section(simulations_entry, 'simulation', 
											  # create_if_not_found = ['simulation'])

		simulation_entry = self.get_simulation(spectra_id = spectra_id, simulation_id = simulation_id)
		
		simulations_entry.removeChild(simulation_entry)
		print('Simulation deleted')

				
	def get_number_of_simulations(self, spectra_id = 0):
		"""Gets the total number of simulations in spectrum[spectra_id]. 
		
		Args:
			spectra_id (int, optional:) Spectrum ID to get the number of simulations from.
		
		Returns:
			int: Number of simulations.
		"""
		spectra = self.get_spectrum(spectra_id=spectra_id)
		simulations = get_xml_section(spectra, 'simulations')
		if simulations is None:
			return 0

		simulation = simulations[0].getElementsByTagName('simulation')

		return len(simulation)


	def get_dataxy(self, spectra_id = 0):
		"""Gets the spectral data regarding spectrum[spectra_id].
		
		Example:
			A typical use for this command would be::
				
				#load IDF file
				idf_file = IDF(file_path)

				#get spectrum channels and counts
				xx, yy = idf_file.get_dataxy()
				
				#plot using matplotlib
				plt.figure()
				plt.plot(xx,yy)

			where a plot with the spectrum should show up.
		
		Args:
			spectra_id (int, optional): Spectrum ID on the IDF file
		
		Returns:
			Two numpy arrays: xx (x-values), yy (y-values)
		"""

		technique = self.get_technique(spectra_id=spectra_id)
		if technique in ['RBS', 'NRA', 'ERDA', None]:
			type_data = 'simpledata'
			x_tag = 'x'
			y_tag = 'y'
		elif technique == 'PIXE':
			type_data = 'linedata'
			x_tag = 'line'
			y_tag = 'y'
		elif technique == 'SIMS':
			return self.get_SIMS_data(spectra_id=spectra_id)
		else:
			return [0], [0]


		spec = self.get_spectrum(spectra_id=spectra_id)
		section = get_xml_section(spec, type_data)[0]

		xx = get_xml_section(section, x_tag)
		yy = get_xml_section(section, y_tag)
		
		if xx is None or yy is None: return
		
		xx = xx[0].firstChild.nodeValue.split()
		yy = yy[0].firstChild.nodeValue.split()

		if x_tag != 'line':
			xx = nparray(xx).astype('float')

		yy = nparray(yy).astype('float')


		return xx, yy


####################### Methods to work with spectrum data #######################

	def delete_spectrum(self, spectra_id = 0):
		"""Deletes spectrum[spectra_id]
		
		Args:
			spectra_id (int, optional): ID of the spectrum to delete.
		"""

		spectra_entry = get_xml_section(self.file, 'spectra')[0]
		spectrum_entry = self.get_spectrum(spectra_id=spectra_id)
		spectra_entry.removeChild(spectrum_entry)
		print('spectra deleted')

	def append_spectrum_entry(self, total_spectra):
		"""Change the total number of spectra.
		
		Args:
			total_spectra (int): New total number of spectra.
		"""

		spectra = self.get_section(self.file, 'spectra', create_if_not_found = ['sample', 'spectra'])[0]            
		spectrum_entries = self.get_section(spectra, 'spectrum', create_if_not_found=['spectrum'])

		nspectra = len(spectrum_entries)
		
		if total_spectra >= nspectra:
			for i in range(total_spectra - nspectra):
				self.create_element(spectra, 'spectrum')
				
	def get_number_of_spectra(self):
		"""Gets the total number of spectra in the IDF file. 
		
		Returns:
			int: Number of spectra.
		"""

		spectra = get_xml_section(self.file, 'spectra')

		spectrum = spectra[0].getElementsByTagName('spectrum')
		
		return len(spectrum)
		
	def set_spectrum_file_name(self, file_name, spectra_id = 0):
		"""Sets the name of the spectrum for identification proposes (e.g plot legends)
		
		Args:
			file_name (str): Name of the spectrum
			spectra_id (int, optional): ID of the spectrum to set the name.
		"""
		spectra = self.get_section(self.file, 'spectra', create_if_not_found=['sample', 'spectra'])
		
		spectrum_entry= self.get_spectrum(spectra_id=spectra_id)
		data_entry = self.create_tree_on_parent(['data', 'datafile'], spectrum_entry)
		self.change_node_value(file_name, data_entry, 'filename')
		
	def get_spectrum_file_name(self, spectra_id=0):
		"""Gets the name of the spectrum.

		Example:
			Set the label of the plot corresponding spectrum 1 (see also ``self.get_data_xy()``)::
				
				#load xx, yy data
				xx, yy = idf_file.get_dataxy(spectra_id = 1)

				#get the name
				name = idf_file.get_spectrum_file_name(spectra_id = 1)

				#plot
				plt.plot(xx, yy, label = name)
		
		Args:
			spectra_id (int, optional): Description
		
		Returns:
			TYPE: Description
		"""
		spectrum_entry= self.get_spectrum(spectra_id=spectra_id)
		return get_xml_entry(spectrum_entry, 'filename')

	def get_all_spectra_filenames(self):
		"""Gets the list with the names of all spectra
		
		Returns:
			array of strings: Entry i contains the name of spectra_id = i
		"""
		nspectra = self.get_number_of_spectra()

		names = []
		for i in range(nspectra):
			name = self.get_spectrum_file_name(spectra_id=i)
			if name is None:
				name = 'Spectrum %i' %(i+1)
			elif name[-3:] in ['odf', 'dat', 'txt']:
				name = '%i: %s' %(i, name[:-4])
			else:
				name = '%i: %s' %(i, name)

			names.append(name)

		return names

	def set_spectrum_data(self, data_x, data_y, spectra_id = 0, simulation = False):
		"""Sets the xx, yy data of spectrum[spectra_ID]
		
		Args:
			data_x (TYPE): array with the xx values (e.g. channels)
			data_y (TYPE): array with the yy values (e.g. counts)
			spectra_id (int, optional): ID of the spectrum to set xx, yy
			simulation (bool, optional): Note used as of now
		
		Returns:
			DOM Element or None: The XML entry of spectrum[spectra_id].
		"""
		spectra = self.get_section(self.file, 'spectra', create_if_not_found=['sample', 'spectra'])
		
		spectrum_entry= self.get_spectrum(spectra_id=spectra_id)
		data_entry = self.create_tree_on_parent(['data', 'simpledata'], spectrum_entry)

		xaxis_entry = self.create_tree_on_parent(['xaxis'], data_entry)
		yaxis_entry = self.create_tree_on_parent(['yaxis'], data_entry)
		self.change_node_value('energy', xaxis_entry, 'axisname')
		self.change_node_value('channel', xaxis_entry, 'axisunit')
		self.change_node_value('yield', yaxis_entry, 'axisname')
		self.change_node_value('counts', yaxis_entry, 'axisunit')
			   
		data_x = [str(s) for s in data_x]
		data_y = [str(s) for s in data_y]

		x_string = ' '.join(data_x)
		y_string = ' '.join(data_y)

		self.change_node_value(x_string, data_entry, 'x')
		self.change_node_value(y_string, data_entry, 'y')

		return spectrum_entry

	def set_spectrum_data_from_file(self, file_name, save_file_name = True, mode = 'channels vs yield', spectra_id = 0, simulation = False):
		"""Read the spectrum data from the file and sets it on the IDF file.

		Example:
			Load experimental data from file and plot it (see also ``self.get_dataxy()`` and 
			``self.get_spectrum_file_name()``::
				
				#create a blank IDF file
				idf_file = IDF()

				#set the spectrum data from the txt file
				idf_file.set_spectrum_data_from_file(path_to_exp_data.txt)

				#load and plot the data using the file name as label
				xx, yy = self.get_dataxy()
				plt.figure()
				plt.plot(xx, yy, label = idf_file.get_spectrum_file_name())
				plt.legend()

				
		Args:
			file_name (str): Path to the file with the data
			save_file_name (bool, optional, default = True): If True, saves the original file name
			mode (str, optional, default = 'channels vs yield'): Mode of the data file options:

				mode = 'channels vs yield' if txt file has two columns (xx, yy)

				mode = '8 columns' if txt file has 8 columns with yields and assumes linear xx-scale

			spectra_id (int, optional): ID of the spectrum to change
			simulation (bool, optional): Not used as of now
		
		Returns:
			DOM Element or None: The XML entry of spectrum[spectra_id].
		"""
		channels, yields = load_spectrum_from_file(file_name, mode = mode)

		spectrum_entry = self.set_spectrum_data(channels, yields, spectra_id = spectra_id, simulation = simulation)

		if save_file_name:
			name = file_name.split('/')[-1]
			self.set_spectrum_file_name(name, spectra_id = spectra_id)

		return spectrum_entry

	def load_pixe_data_from_file(self, file_name, spectra_id = 0):
		spectra = self.get_section(self.file, 'spectra', create_if_not_found=['sample', 'spectra'])
		
		spectrum_entry= self.get_spectrum(spectra_id=spectra_id)

		# add data
		data_entry = self.create_tree_on_parent(['data', 'linedata'], spectrum_entry)
		xaxis_entry = self.create_element(data_entry, 'xaxis')
		yaxis_entry = self.create_element(data_entry, 'yaxis')

		self.change_node_value('xrayline', xaxis_entry, 'axisname')
		self.change_node_value('', xaxis_entry, 'axisunit')
		
		self.change_node_value('yield', yaxis_entry, 'axisname')
		self.change_node_value('counts', yaxis_entry, 'axisunit')
		
		
		xray_lines, xray_area = read_pixe_file(file_name)
		
		self.change_node_value(' '.join(xray_lines), data_entry, 'line')
		self.change_node_value(' '.join(xray_area), data_entry, 'y')
		
		
		# add the cpixe output file (NDF input) as it is
		data_entry = self.create_tree_on_parent(['data', 'datafile'], spectrum_entry)
		
		self.change_node_value(file_name.split('/')[-1], data_entry, 'filename')
		self.change_node_value('Windows GUPIX Version 2.2.0', data_entry, 'fileformat')
				
		with open(file_name, 'r') as file:
			lines = ';'.join(file.readlines())
		
		self.change_node_value(lines, data_entry, 'filesource')

	def get_PIXE_file(self, spectra_id = 0):
		spec = self.get_spectrum(spectra_id = spectra_id)
		if spec is None: return

		data_file_text = self.get_section(spec, 'datafile')[0]
		file_source = get_xml_entry(data_file_text, 'filesource')
		
		return file_source.replace(';','')

	def set_SIMS_from_file(self, file_name, save_file_name = True, spectra_id = 0):
		data_list = load_SIMS_file(file_name)
		self.set_SIMS_data(data_list, spectra_id = spectra_id)

		if save_file_name:
			name = file_name.split('/')[-1]
			self.set_spectrum_file_name(name, spectra_id = spectra_id)

	def set_SIMS_data(self, data_list, spectra_id = 0):
		spectrum_entry= self.get_spectrum(spectra_id=spectra_id)
		
		try:
			data_node = self.get_section(spectrum_entry, 'data')[0]
			self.remove_nodes(data_node, 'multipledata')
		except Exception as e:
			pass
		
		data_entry = self.create_tree_on_parent(['data', 'multipledata'], spectrum_entry)

		xaxis_entry = self.create_element(data_entry, 'xaxis')
		self.change_node_value('depth', xaxis_entry, 'axisname')
		self.change_node_value('umr', xaxis_entry, 'axisunit')
		
		multipledata_entry = self.create_element(data_entry, 'multipledataentries')
		
		for line in data_list:
			line2write = [str(e) for e in line]
			line2write = '\t'.join(line2write)
			self.change_node_value(line2write, multipledata_entry, 'multipledataentry', append=True)
		
	def get_SIMS_data(self, spectra_id = 0):
		spec = self.get_spectrum(spectra_id=spectra_id)
		
		particles_entry = get_xml_section(spec, 'masslist')[0]
		
		particles = self.get_SIMS_particles(spectra_id = spectra_id)
		
		data_entry = get_xml_section(spec, 'multipledataentries')[0]
		depth_lines_entry = get_xml_section(data_entry, 'multipledataentry')
		
		depth_lines = [d.firstChild.nodeValue.split() for d in depth_lines_entry]
		
		depth = [float(d[0]) for d in depth_lines]

		sims_data = {}
		for i,p in enumerate(particles):
			sims_data[p] = [float(d[i+1]) for d in depth_lines]
		
			
		return depth, sims_data
			
	def get_SIMS_particles(self, spectra_id):
		spec = self.get_spectrum(spectra_id=spectra_id)
		
		particles_entry = get_xml_section(spec, 'masslist')[0]
		
		particles = get_xml_entry(particles_entry, 'detectedparticles').split()
		
		return particles

	def set_SIMS_calibration(self, calibration_dic, spectra_id = 0):
		spec = self.get_spectrum(spectra_id = spectra_id)
		
		# calibration
		timecalibration_entry = self.get_section(spec, 'timecalibration', 
					 create_if_not_found = ['calibrations', 'timecalibrations', 'timecalibration'])[0]
		#remove old ones:
		try:
			self.remove_nodes(timecalibration_entry, 'timecalibration')
		except:
			pass
		
		self.change_node_value(calibration_dic['particle'], timecalibration_entry, 'calibrationparticle')
		self.change_node_value(calibration_dic['mode'], timecalibration_entry, 'timecalibrationmode')
		
		calibrationparameters_entry = self.get_section(timecalibration_entry, 'calibrationparameters',
					  create_if_not_found = ['calibrationparameters'])[0]
		

		attributes = {
			'units': ''
		}
		self.change_node_value('%s %s'%(calibration_dic['a'], calibration_dic['b']), calibrationparameters_entry, 
							   'calibrationparameter', attributes = attributes)




######################  Methods to set beam parameters  ##################################### 
			
	def set_beam_particles(self, particle, spectra_id = 0):
		"""Sets the beam particle of spectrum[spectra_id = 0]
		
		Args:
			particle (str): Beam particle
			spectra_id (int, optional): ID of the spectrum to change
		"""

		#choose the spectra to change
		spec = self.get_spectrum(spectra_id=spectra_id)
		#get the parent element with the child to be changed
		beam = self.get_section(spec, 'beam', create_if_not_found = ['beam'])[0]
		self.change_node_value(particle, beam, 'beamparticle')

	def get_beam_particles(self, spectra_id=0):
		"""Gets the beam particles of spectrum[spectra_id = 0]
		
		Args:
			spectra_id (int, optional): ID of the spectrum to read from
		
		Returns:
			str: Name of the beam particle
		"""

		spec = self.get_spectrum(spectra_id=spectra_id)

		incident_particle = get_xml_entry(spec, 'beamparticle')

		
		return incident_particle

	def set_beam_energy(self, energy, spectra_id = 0):
		"""Sets the beam energy
		
		Args:
			energy (float): The energy of the beam in keV
			spectra_id (int, optional): ID of the spectrum

		"""
		spec = self.get_spectrum(spectra_id=spectra_id)
		beam = self.get_section(spec, 'beam', create_if_not_found = ['beam'])[0]
		
		attributes = {
			'units': 'keV'
		}
		self.change_node_value(energy, beam, 'beamenergy', attributes = attributes)
		
	def get_beam_energy(self, spectra_id = 0):
		"""Gets the beam energy and the FWHM in keV
		
		Args:
			spectra_id (int, optional): ID of the spectrum
		
		Returns:
			float, float: The first and second floats are the energy and FWHM of the beam, respectively
		"""
		spec = self.get_spectrum(spectra_id=spectra_id)
		if spec is None: return
		
		energy_value, energy_units = get_xml_entry(spec, 'beamenergy', attribute='units')
		if energy_value == '': energy_value = None

		if energy_value != None:
			energy_value = float(energy_value)
	
			if energy_units == 'MeV':
				energy_value *= 1e3
			elif energy_units == 'meV':
				energy_value *= 1e-3
			elif energy_units == 'GeV':
				energy_value *= 1e6            
			
		
		beam_FWHM = None
		beamspread = get_xml_section(spec, 'beamenergyspread')
		

		if beamspread != None:
			beamspread = beamspread[0]
			
			if beamspread.firstChild != None:
				beam_mode = beamspread.getAttribute('mode')
				beam_units = beamspread.getAttribute('units')
				if beamspread.firstChild.nodeValue != '':
					beam_FWHM = float(beamspread.firstChild.nodeValue)

				if beam_units == 'MeV':
					beam_FWHM *= 1e3
				elif beam_units == 'meV':
					beam_FWHM *= 1e-3
				elif beam_units == 'GeV':
					beam_FWHM *= 1e6  

				if 'FWHM' not in beam_mode:
					print('Warning: Beam spread mode not specified to be FWHM')
			
			
		return energy_value, beam_FWHM

	def set_beam_energy_spread(self, fwhm, spectra_id = 0):
		"""Sets the FWHM of the beam
		
		Args:
			fwhm (float): The FWHM of the beam in keV
			spectra_id (int, optional): ID of the spectrum
		"""
		spec = self.get_spectrum(spectra_id=spectra_id)
		beam = self.get_section(spec, 'beam', create_if_not_found = ['beam'])[0]
		
		attributes = {
			'mode': 'FWHM',
			'units': 'keV'
		}
		self.change_node_value(fwhm, beam, 'beamenergyspread', attributes = attributes)
		
	def set_charge(self, charge, spectra_id = 0):  
		"""Sets the charge
		
		Args:
			charge (float): The charge
			spectra_id (int, optional): ID of the spectrum
		"""

		#choose the spectra to change
		spec = self.get_spectrum(spectra_id=spectra_id)
		#get the parent element with the child to be changed
		beam = self.get_section(spec, 'beam', create_if_not_found = ['beam'])[0]
		self.change_node_value(charge, beam, 'charge')

	def get_charge(self, spectra_id = 0):
		"""Gets the charge of the experiment
		
		Args:
			spectra_id (int, optional): ID of the spectrum

		Returns:
			float: The charge
		"""
		spec = self.get_spectrum(spectra_id=spectra_id)
		if spec is None: return
		beam_entry = get_xml_section(spec, 'beam')
		if beam_entry is None: return
		beam_entry = beam_entry[0]

		charge = get_xml_entry(beam_entry, 'charge')

		return charge
	

######################  Methods to set geometry parameters  ##################################### 

	def set_geometry_type(self, geometry_type, spectra_id = 0):
		"""Sets the experiment geometry (IBM, Cornell, General)
		
		Args:
			geometry_type (str): the geometry
			spectra_id (int, optional): Spectrum ID to set the geometry
		"""
		spec = self.get_spectrum(spectra_id=spectra_id)
		geometry_ele = self.get_section(spec, 'geometry', create_if_not_found = ['geometry'])[0]

		self.change_node_value(geometry_type, geometry_ele, 'geometrytype')
		
	def get_geometry_type(self, spectra_id = 0):
		"""Gets the experiment geometry along with the angles.
		
		Args:
			spectra_id (int, optional): Spectrum ID to get the geometry from
		
		Returns:
			str, array, float: Name of the geometry, [incident angle, scattering angle], exit angle
		"""
		spec = self.get_spectrum(spectra_id = spectra_id)
		if spec is None: return None, [None, None], None

		geometry = get_xml_section(spec, 'geometry')
		if geometry is None: return None, [None, None], None
		
		geometry = geometry[0]
		if geometry.firstChild != None:
			geo_type = get_xml_entry(geometry, 'geometrytype')
			
			angle_i, angle_i_units = get_xml_entry(geometry, 'incidenceangle', attribute='units')
			if angle_i_units == 'rad':
				print('Incident angle given in radians, converted to degrees')
				angle_i *= 180/pi
			
			
			angle_s, angle_s_units = get_xml_entry(geometry, 'scatteringangle', attribute='units')
			if angle_s_units == 'rad':
				print('Scattering angle given in radians, converted to degrees')
				angle_s *= 180/pi
			
			
			angle_e, angle_e_units = get_xml_entry(geometry, 'exitangle', attribute='units')
			if angle_e_units == 'rad':
				print('Scattering angle given in radians, converted to degrees')
				angle_e *= 180/pi
			
		else:
			print('Geometry not given, assuming imb and theta_i = 0, theta_s = 160')
			angle_i = 0
			angle_s = 160
			angle_e = 0
		
		return geo_type, [angle_i, angle_s], angle_e

	def set_incident_angle(self, angle, spectra_id = 0):
		"""Sets the incident angle
		
		Args:
			angle (float): Incident angle in degrees
			spectra_id (int, optional): ID of the spectrum

		"""

		spec = self.get_spectrum(spectra_id=spectra_id)
		geometry_ele = self.get_section(spec, 'geometry', create_if_not_found = ['geometry'])[0]

		
		attributes = {
			'units': 'degree'
		}
		self.change_node_value(angle, geometry_ele, 'incidenceangle', attributes = attributes)
		
	def set_scattering_angle(self, angle, spectra_id = 0):
		"""Sets the scattering angle
		
		Args:
			angle (float): Scattering angle in degrees
			spectra_id (int, optional): ID of the spectrum
		"""

		spec = self.get_spectrum(spectra_id=spectra_id)
		geometry_ele = self.get_section(spec, 'geometry', create_if_not_found = ['geometry'])[0]
		
		attributes = {
			'units': 'degree'
		}
		self.change_node_value(angle, geometry_ele, 'scatteringangle', attributes = attributes)
		
	def set_exit_angle(self, angle, spectra_id = 0):
		"""Sets the exit angle
		
		Args:
			angle (TYPE): Exit angle in degrees
			spectra_id (int, optional): ID of the spectrum
		"""

		spec = self.get_spectrum(spectra_id=spectra_id)
		geometry_ele = self.get_section(spec, 'geometry', create_if_not_found = ['geometry'])[0]
		
		attributes = {
			'units': 'degree'
		}
		self.change_node_value(angle, geometry_ele, 'exitangle', attributes = attributes)
	
	
	def get_geo_parameters(self, spectra_id = 0):
		"""Gets the entire set of parameters in a dictionary with the following format::
			
			params = {
				'mode': 19,
				'window': [100, 1500],
				'projectile': 'He',
				'beam_energy': 2000,
				'beam_FWHM': 17,
				'geometry': 'ibm',
				'angles': [0, 160], # [incident, scattering]
				'dect_solid': 7.2,
				'energy_calib': [1, 0], # [m, b], E = m * channel + b,
				'charge': 5           
			}

		Each of these parameters can be obtained individually using the appropriate methods::

			params['window']= [self.get_window_min(), self.get_window_max()]
			params['projectile'] = self.get_beam_particles()
			params['beam_energy'], params['beam_FWHM'] = self.get_beam_energy()
			params['geometry'], params['angles'], _ = self.get_geometry_type()
			params['dect_solid'] = self.get_detector()
			params['energy_calib'] = self.get_energy_calibration()
			params['charge'] = self.get_charge()
		
		Args:
			spectra_id (int, optional): ID of the spectrum
		
		Returns:
			dictionary or None: Dictionary with the geometry parameters
		
		Raises:
			e: If data is missing
		"""

		technique = self.get_technique(spectra_id=spectra_id)
		
		if technique in ['RBS', 'NRA', 'ERDA', 'PIXE', None]:
			params = OrderedDict()
			params = {
				'mode': 19,
				'window': [100, 1500],
				'projectile': 'He',
				'beam_energy': 2000,
				'beam_FWHM': 20,
				'geometry': 'ibm',
				'angles': [0, 160], # theta_i, theta_s
				'dect_solid': 10,
				'energy_calib': [1, 0], # m,b 
				'charge':1          
			}
			
			try:
				params['window']= [self.get_window_min(spectra_id=spectra_id), self.get_window_max(spectra_id=spectra_id)]
				params['projectile'] = self.get_beam_particles(spectra_id = spectra_id)
				params['beam_energy'], params['beam_FWHM'] = self.get_beam_energy(spectra_id = spectra_id)
				params['geometry'], params['angles'], _ = self.get_geometry_type(spectra_id = spectra_id)
				params['dect_solid'] = self.get_detector(spectra_id = spectra_id)
				params['energy_calib'] = self.get_energy_calibration(spectra_id = spectra_id)
				params['charge'] = self.get_charge(spectra_id = spectra_id)
			except Exception as e:
				print('Error: Missing data')
				# print_exc()

		elif technique == 'SIMS':
			params = OrderedDict()
			params['window']= [self.get_window_min(spectra_id=spectra_id), self.get_window_max(spectra_id=spectra_id)]
			params['projectile'] = self.get_beam_particles(spectra_id = spectra_id)
			params['beam_energy'], params['beam_FWHM'] = self.get_beam_energy(spectra_id = spectra_id)
			params['geometry'], params['angles'], _ = '',['', ''],''
			params['dect_solid'] = self.get_detector(spectra_id = spectra_id)
			params['energy_calib'] = self.get_energy_calibration(spectra_id = spectra_id)

			if params['beam_FWHM'] is None:
				params['beam_FWHM'] = ''


		else:
			return None

		return params


	def set_geo_parameters(self, params, spectra_id = 0):
		"""Sets the entire set of parameters to IDF from a dictioanry params (see also 
		``get_geo_parameters()``)

		The input params is a dictionary with the following entries::

			pairs = {'beam_energy': self.set_beam_energy,
				'beam_FWHM': self.set_beam_energy_spread,
				'projectile': self.set_beam_particles,
				'charge': self.set_charge,
				'dect_solid': self.set_detector_solid_angle,
				'geometry': self.set_geometry_type,
				'angles': [self.set_incident_angle, self.set_scattering_angle],
				'energy_calib': self.set_energy_calibration
				}

		Note that it is acceptable for params to have more entries than the ones above, meaning
		that the output of ``get_geo_parameters()`` can be used as input here.
		
		Args:
			params (dictionary): A dictionary with the geometry parameters
			spectra_id (int, optional): ID of the spectrum to edit
		"""
		pairs = {'beam_energy': self.set_beam_energy,
			'beam_FWHM': self.set_beam_energy_spread,
			'projectile': self.set_beam_particles,
			'charge': self.set_charge,
			'dect_solid': self.set_detector_solid_angle,
			'geometry': self.set_geometry_type,
			'angles': [self.set_incident_angle, self.set_scattering_angle],
			'energy_calib': self.set_energy_calibration
			}
		
		for key, item in pairs.items():
			if key == 'angles':
				item[0](params[key][0], spectra_id = spectra_id)
				item[1](params[key][1], spectra_id = spectra_id)
				continue
			
			#handle energy_calib
			if isinstance(params[key], list):
				item(params[key][0], params[key][1], spectra_id = spectra_id)
			else:
				item(params[key], spectra_id = spectra_id)
				
			
		
	def unify_geo_parameters(self, master_id = 0, target_id = 'All'):
		"""Copies the geometry parameters from one spectrum (with index *master_id*) to 
		all other spectra in the IDF file.
		
		Args:
			master_id (int, optional): spectra_id of the spectrum with the information to be copied
		"""
		nspectra = self.get_number_of_spectra()
		
		params_master = self.get_geo_parameters(spectra_id = master_id)
		technique_master = self.get_technique(spectra_id = master_id)
		reactions_master = self.get_reactions(spectra_id = master_id)

		if target_id == 'All':
			for i in range(0, nspectra):
				self.set_technique(technique_master, spectra_id=i)
				self.set_reactions_list(reactions_master, spectra_id= i)		
				self.set_geo_parameters(params_master, spectra_id = i)

		else:
			self.set_technique(technique_master, spectra_id=target_id)
			self.set_geo_parameters(params_master, spectra_id = target_id)		
			self.set_reactions_list(reactions_master, spectra_id= target_id)			


				

	####################  Methods to set the detector specifications ################################
	
	def set_detector_solid_angle(self, angle, spectra_id = 0):
		"""Sets the detector solid angle
		
		Args:
			angle (float): solid angle in msr
			spectra_id (int, optional): ID of the spectrum
		"""
		spec = self.get_spectrum(spectra_id=spectra_id)
		detector_ele = self.get_section(spec, 'detector', create_if_not_found = ['detection','detector'])[0]
		
		attributes = {
			'units': 'msr'
		}
		self.change_node_value(angle, detector_ele, 'solidangle', attributes = attributes)

	def get_detector(self, spectra_id = 0):
		"""Gets the detector solid angle
		
		Args:
			spectra_id (int, optional): ID of the spectrum
		
		Returns:
			float: Detector solid angle
		
		Todo:
			Add shape, dimension and type of detector
		"""		
		spec = self.get_spectrum(spectra_id = spectra_id)
		if spec is None: return
		
		detector = get_xml_section(spec, 'detector')
		if detector is None: return
					 
		det_solid_angle = get_xml_entry(detector[0], 'solidangle')
			
		return det_solid_angle

	
	#####################  Methods to set energy calibration  ######################################
	
	def set_energy_calibration(self, m, b, append = False, spectra_id = 0, reaction_id = 0):
		"""Set energy calibration assuming a linear relation between energy and channels:

			E = m * channel + b		 

		Args:
			m (float): m parameter in keV/channel
			b (float): b parameter in keV
			append (bool, optional, default False): If True appends the calibration instead of overwriting a previous one
			spectra_id (int, optional): ID of the spectrum
		"""
		spec = self.get_spectrum(spectra_id=spectra_id)

		calibrations_ele = self.get_section(spec, 'energycalibrations', 
												 create_if_not_found = ['calibrations','energycalibrations'])[0]
						
		calibrations = self.get_section(calibrations_ele, 'energycalibration', 
												 create_if_not_found = ['energycalibration'])

		if reaction_id >= len(calibrations):
			return
		calibration = calibrations[reaction_id]


		# energycalib_ele = self.get_section(spec, 'energycalibration', 
		# 										 create_if_not_found = ['calibrations','energycalibrations','energycalibration'])[0]
		
		reactions = self.get_reactions(spectra_id=spectra_id)
		if reactions is not None:
			self.change_node_value(reactions[reaction_id]['exitparticle'], calibration, 'calibrationion')
		self.change_node_value('energy', calibration, 'calibrationmode')
		
		
		if append == False:
			calibration_param_ele = self.get_section(calibration, 'calibrationparameters', 
				 create_if_not_found = ['calibrationparameters'])[0]
		else:
			calibration_param_ele = self.create_element(calibration, 'calibrationparameters')
		
		#remove old ones:
		try:
			self.remove_nodes(calibration_param_ele, 'calibrationparameter')
		except:
			pass

		attributes = {
			'units': 'keV'
		}
		self.change_node_value(b, calibration_param_ele, 'calibrationparameter', attributes = attributes)
	
		attributes = {
			'units': 'keV/channel'
		}
		self.change_node_value(m, calibration_param_ele, 'calibrationparameter', attributes = attributes,
							  append = True)


	def set_energy_calibration_file(self, file_path, append = False, spectra_id = 0):
		"""Adds an energy calibration file to IDF. This is useful for instance in PIXE and SIMS. 
		See also Examples section for more information.
		
		Args:
			file_path (str): Path to the calibration file
			spectra_id (int, optional): ID of the spectrum
		"""
		spec = self.get_spectrum(spectra_id=spectra_id)
		energycalib_ele = self.get_section(spec, 'energycalibration', 
												 create_if_not_found = ['calibrations','energycalibrations','energycalibration'])[0]


		self.change_node_value('other', energycalib_ele, 'calibrationmode')
		
		with open(file_path, 'r', errors='replace') as file:
			file_lines = file.readlines()
		
		calibration_param_ele = self.get_section(energycalib_ele, 'calibrationparameters', 
			 create_if_not_found = ['energycalibration','calibrationparameters'])[0]

		#remove old ones:
		if append == False:
			try:
				self.remove_nodes(calibration_param_ele, 'calibrationparameter')
			except:
				pass

		attributes = {
				'filename': file_path.split('/')[-1]
			}
		self.change_node_value(' '.join(file_lines[:-1]), calibration_param_ele, 'calibrationparameter', attributes = attributes)


	def get_energy_calibration(self, spectra_id = 0, reaction_id = 0):
		"""Gets the energy calibration parameters. See also ``self.set_energy_calibration()``.
		
		Args:
			spectra_id (int, optional): ID of the spectrum
		
		Returns:
			array(2): Array with the parameters [m, b]
		"""
		technique = self.get_technique(spectra_id=spectra_id)

		if technique in ['RBS', 'NRA', 'ERDA', None]:
			spec = self.get_spectrum(spectra_id = spectra_id)
			if spec is None: return
			
			param_b = 0
			param_m = 1
			
			calibration = get_xml_section(spec, 'energycalibration')
			if reaction_id >= len(calibration): reaction_id = len(calibration) - 1

			if calibration is None: return [None, None]
			else: calibration = calibration[reaction_id]
			if calibration is [None, None]: return
			
			param = get_xml_section(calibration, 'calibrationparameter')

			if param is None: return [None, None]
			elif param[0].firstChild is None: return [None, None]
			elif param[1].firstChild is None: return [None, None]

			if '' in [p.firstChild.nodeValue for p in param]: return [None, None]
			if None in [p.firstChild.nodeValue for p in param]: return [None, None]

			
			if param[0].getAttribute('units') == 'keV':
				param_b = float(param[0].firstChild.nodeValue)
				param_m = float(param[1].firstChild.nodeValue)
			else:
				param_m = float(param[0].firstChild.nodeValue)
				param_b = float(param[1].firstChild.nodeValue)
		
		elif technique == 'PIXE':
			spec = self.get_spectrum(spectra_id = spectra_id)
			if spec is None: return
			
			calibration = get_xml_section(spec, 'energycalibration')

			if calibration is None: return None
			else: calibration = calibration[0]
			
			param_b, param_m = get_xml_entry(calibration, 'calibrationparameter', attribute = 'filename')
			

		elif technique == 'SIMS':
			spec = self.get_spectrum(spectra_id = spectra_id)
			if spec is None: return
			
			param_b = 0
			param_m = 1
			
			calibration = get_xml_section(spec, 'timecalibration')[0]
			if calibration is [None, None]: return
			
			params  = get_xml_section(calibration, 'calibrationparameter')[0]
			params = params.firstChild.nodeValue.split()
			param_m = params[0]
			param_b = params[1]
		else:
			param_m = '-'
			param_b = '-'
		
		return [param_m, param_b]

	####################  Methods to set elements, profiles and reactions  ###################################
	
	def set_elements(self, elements):
		"""Sets the elements of the sample.

		The input ``elements`` is a dictionary with dim(number of elements + 1), with one of
		entries being the number of elements (with keyword "nelements")::

			elements['nelements'] = '2'

		and the others the the elements parameters. 
		The keyword each element is its ID and the contents of each molecule entry are also a
		dictionary containing the element's name, minimum and maximum possible concentrations, 
		minimum and maximum possible depths::

			elements[0] = {'name': '1H',
							'density': '',
							'concentrationmin': '0',
							'concentrationmax': '200000',
							'depthmin': '0',
							'depthmax': '0.02'}
			elements[1] = {'name': 'Mo 2 O 3',
						'density': '',
						'concentrationmin': '0',
						'concentrationmax': '200000',
						'depthmin': '0',
						'depthmax': '0.1'}

		Note the spaces in the molecular formula. 

		**Note for NDF users**: See Section 4.2 of the `NDF Manual <../../source/NDF_MANUAL_100a.pdf>`__
		for a description of each parameter. Moreover, if you want to fit the stoichiometry 
		you need to include '?=' after the element, for instance::

			elements[1]['name'] = 'Mo ?=2 O ?=3'

		Note:
			Previous self.set_molecules()

		Args:
			elements (dictionary): Dictionary with the information about the sample composition.
		"""
		elements_element = self.create_tree(['elementsandmolecules', 'molecules'])

		self.change_node_value(elements['nelements'], elements_element, 'nmolecules')

		try:
			self.remove_nodes(elements_element, 'molecule')
		except:
			pass

		profile = self.get_profile()
		for mol_id, params in elements.items():
			if mol_id == 'nelements':
				continue

			molecule_element = self.create_element(elements_element, 'molecule')
			
			self.change_node_value(params['name'], molecule_element, 'name')
			self.change_node_value(params['density'], molecule_element, 'density', attributes = {'units': '1e22at/cm3'})
			self.change_node_value(params['concentration'][0], molecule_element, 'concentrationmin')
			self.change_node_value(params['concentration'][1], molecule_element, 'concentrationmax')
			self.change_node_value(params['depth'][0], molecule_element, 'depthmin')
			self.change_node_value(params['depth'][1], molecule_element, 'depthmax')


			if profile != None and mol_id < len(profile['names']):
				profile['names'][mol_id] = params['name']


		if profile != None:
			self.set_profile(profile)



	def set_profile(self, profile_dic):
		"""Sets the depth profile of the sample. 
		
		The ``profile_dic`` is a dictionary with dim(number of layers + **2**). One of the entries, 
		``profile_dic['nlayers']``, contains the number of layers and it is there to simply some parts
		of the NDF related code. Another entry, ``profile_dic['nlayers']``, is reserved for the names of
		the elements.

		The other dictionary entries have the information of each layer and are themselves dictionaries.
		Therefore, ``profile_dic`` should look like the following::
			
			profile_dic = {
				'nlayers': '3',
				'names': ['Co 0.45 Pt 0.55', 'Si 1 O 2', 'Si'],
				0: {'thickness': 390,     'concentrations': [100, 0,  0]}, 
				1: {'thickness': 700,     'concentrations': [ 0, 100, 0]}, 
				2: {'thickness': 4000000, 'concentrations': [ 0,  0, 100]} 				
			}

		The *concentrations* array contains the concentration of each element on the layer. The order of
		the values follows the *names* array, i.e. layer 1 is the concentration of element 1 (CoPt), etc...
		
		**Note on nested dictionaries**: If you want to change, for instance, the concentrations of layer 1
		you can do it by::

			profile_dic[1]['concentrations'] = [50, 50, 0]

		or if you want to change the name of the 1st element::

			profile_dic['names'][0] = 'Co 1 Pt 1'


		Args:
			profile_dic (dictionary): Dictionary with the data on the depth profile of the sample
		"""
		layers_entry = self.create_tree(['structure', 'layeredstructure'])

		self.change_node_value(profile_dic['nlayers'], layers_entry, 'nlayers')

		try:
			self.remove_nodes(layers_entry, 'layers')
		except Exception as e:
			pass
			#print(e)

		layer_entries = self.create_element(layers_entry, 'layers')



		for key, ele in profile_dic.items():
			if key in ['nlayers', 'names']:
				continue

			layer_entry = self.create_element(layer_entries, 'layer')
			self.change_node_value(ele['thickness'], layer_entry, 'layerthickness', 
								   attributes={'units':'1e15at/cm2'})

			layerelements_entry = self.create_element(layer_entry, 'layerelements')

			# loop elements
			for i,c in enumerate(ele['concentrations']):
				if i + 1 > len(profile_dic['names']):
					break
					
				element_entry = self.create_element(layerelements_entry, 'layerelement')

				name = profile_dic['names'][i]
				self.change_node_value(name, element_entry, 'name')
				self.change_node_value(c, element_entry, 'concentration', attributes={'units':'fraction'})
					

	def set_min_thickness(self, value):
		"""Sets the minimum thickness of the sample
		
		Args:
			value (float): Minimum thickness of the layer
		"""
		sample_entry = get_xml_section(self.file, 'sample')[0]
		struct_entry = get_xml_section(sample_entry, 'layeredstructure')[0]

		# min_thickness_entry = self.create_tree_on_parent(['minthickness'], struct_entry)

		self.change_node_value(value, struct_entry, 'minthickness')

	def set_max_thickness(self, value):
		"""Sets the maximum possible thickness of the sample
		
		Args:
			value (float): Maximum possible thickness of the layer
		"""
		sample_entry = get_xml_section(self.file, 'sample')[0]
		struct_entry = get_xml_section(sample_entry, 'layeredstructure')[0]

		# min_thickness_entry = self.create_tree_on_parent(['minthickness'], struct_entry)

		self.change_node_value(value, struct_entry, 'maxthickness')


	def get_min_thickness(self):
		"""Gets the minimum possible thickness of the sample
		
		Returns:
			float: minimum possible thickness of the sample

		Todo:
			Change the return format to float!
		"""
		sample_entry = get_xml_section(self.file, 'sample')[0]
		struct_entry = get_xml_section(sample_entry, 'layeredstructure')
		
		if struct_entry is None: return '0'
		struct_entry = struct_entry[0]

		value = get_xml_entry(struct_entry, 'minthickness')

		if value is None:
			return '0'
		
		return value

	def get_max_thickness(self):
		"""Gets the maximum possible thickness of the sample
		
		Returns:
			float: maximum possible thickness of the sample

		Todo:
			Change the return format to float!
		"""
		sample_entry = get_xml_section(self.file, 'sample')[0]
		struct_entry = get_xml_section(sample_entry, 'layeredstructure')

		if struct_entry is None: return '0'
		struct_entry = struct_entry[0]

		value = get_xml_entry(struct_entry, 'maxthickness')

		if value is None:
			return '0'
		
		return value



	def set_reactions(self, reactions_dic, append = True, mode = 'reactionlist', spectra_id = 0, linked_calibrations = True):
		"""Sets the reaction list associated with the chosen technique (see ``self.set_technique()``).
		Mode defines

		The ``reactions_dic`` is a dictionary with the information on a given reaction. 
		It can be of two types depending on the ``mode``. When ``mode = 'reactionlist'``, 
		used with most techniques, ``reactions_dic`` is of type::

			reactions_dic =	{'initialtargetparticle': 'Be', 
					 'incidentparticle': '3He', 
					 'exitparticle': '1H', 
					 'finaltargetparticle': '11B', 
					 'reactionQ': '10321.90'}

		The above is a typical NRA reaction in a Be sample. Note that multiple reactions
		can be added to the same spectrum by leaving ``append = True``.

		Note that for RBS one does not need to define ``reactions_dic``.

		When ``mode = 'masslist'``, mostly used for SIMS, the above dictionary becomes::

			reactions_dic = {'detectedparticles': '1H 2H Be 12C Ni Mo W'}


		Args:
			reactions_dic (dictionary): Dictionary with the details of each reaction
			append (bool, optional): If True it appends the reaction to the existing reactions
			mode (str, optional, defaults to 'reactionlist'): Defines the reaction mode, either 
			'reactionlist' or 'masslist'
			spectra_id (int, optional): ID of the spectrum
		"""
		spec = self.get_spectrum(spectra_id = spectra_id)
		reactions = self.get_section(spec, mode, create_if_not_found=['reactions',mode])[0]
		calibrations = self.get_section(spec, 'energycalibrations', create_if_not_found=['energycalibrations'])[0]

		
		if mode == 'reactionlist':
			if append is False:
				try:
					self.remove_nodes(reactions, 'reaction')
					if linked_calibrations: self.remove_nodes(calibrations, 'energycalibration')
				except:
					pass

			reaction = self.create_element(reactions, 'reaction')

			self.change_node_value(capitalize_atom(reactions_dic['initialtargetparticle']), reaction, 'initialtargetparticle')
			self.change_node_value(capitalize_atom(reactions_dic['incidentparticle']), reaction, 'incidentparticle')
			self.change_node_value(capitalize_atom(reactions_dic['exitparticle']), reaction, 'exitparticle')
			self.change_node_value(capitalize_atom(reactions_dic['finaltargetparticle']), reaction, 'finaltargetparticle')
			self.change_node_value(capitalize_atom(reactions_dic['reactionQ']), reaction, 'reactionQ', attributes={'units':'keV'})

			if linked_calibrations: self.create_element(calibrations, 'energycalibration')
		elif mode == 'masslist':
			try:
				self.remove_nodes(reactions, 'reaction')
			except:
				pass
			
			self.change_node_value(reactions_dic['detectedparticles'], reactions, 'detectedparticles')

			
		else:
			print('Reaction mode not recognized')


	def set_reactions_list(self, reactions, spectra_id=0):
		"""
		Sets an entire list of reactions to the specified spectrum. 
		
		The method initializes the spectrum with the first reaction from the list without appending 
		(i.e., replacing any existing reactions). Subsequent reactions in the list are appended to the spectrum.
		
		This is a convenience method built atop the base `set_reactions` method to handle lists of reactions 
		efficiently without requiring multiple explicit calls by the user.
		
		Args:
			reactions (list of dictionaries): A list of reaction dictionaries. Each dictionary should adhere 
											to the structure expected by the `set_reactions` method.
			spectra_id (int, optional): ID of the spectrum to which the reactions are being added. Defaults to 0.
		
		Examples:
			To set multiple reactions for a given spectrum:
			
			reactions_list = [
				{'initialtargetparticle': 'Be', ...},
				{'initialtargetparticle': 'H', ...},
				...
			]
			obj.set_reactions_list(reactions_list, spectra_id=5)
		"""
		
		# Initialize the spectrum with the first reaction without appending
		self.set_reactions(reactions[0], append=False, spectra_id=spectra_id)
		
		# Append the subsequent reactions from the list to the spectrum
		for r in reactions[1:]:
			self.set_reactions(r, spectra_id=spectra_id)

	

	def get_reactions(self, spectra_id = 0):
		"""Gets the reaction list of spectrum[spectra_id]

		It returns a list with the reactions dictionaries (see also ``self.set_reactions()``). For
		instance, a NRA reaction list with two reactions (*D(3He, 1H)4He* and *Be(3He, 1H)11B*) 
		the method outputs::

			reactions = [
				{'initialtargetparticle': 'D',
				  'incidentparticle': '3He',
				  'exitparticle': '1H',
				  'finaltargetparticle': '4He',
				  'reactionQ': '18352',
				  'code': 'D(3He, 1H)4He 18.35'},
				{'initialtargetparticle': 'Be',
				  'incidentparticle': '3He',
				  'exitparticle': '1H',
				  'finaltargetparticle': '11B',
				  'reactionQ': '10321.90',
				  'code': 'Be(3He, 1H)11B 10.32'}
				]

		
		Args:
			spectra_id (int, optional): ID of the spectrum
		
		Returns:
			list: List of dictionaries defining the reactions
		"""
		spec = self.get_spectrum(spectra_id = spectra_id)
		reactions = self.get_section(spec, 'reactions')
		if reactions is None:
			return None
		else:
			reactionlist = self.get_section(reactions[0], 'reaction')

		if reactionlist is None:
			return None
		
		reactions = []
		for r in reactionlist:
			reaction = {
				'initialtargetparticle': get_xml_entry(r, 'initialtargetparticle'),
				'incidentparticle': get_xml_entry(r, 'incidentparticle'),
				'exitparticle': get_xml_entry(r, 'exitparticle'),
				'finaltargetparticle': get_xml_entry(r, 'finaltargetparticle'),
				'reactionQ': get_xml_entry(r, 'reactionQ'),                
			}
			for key, value in reaction.items():
				if value == '':
					reaction[key] = None
				elif value == 'None':
					reaction[key] = None


			if reaction['reactionQ'] is None:
				reaction['reactionQ'] = ''
			else:
				reaction['reactionQ'] = '%0.2f' %(float(reaction['reactionQ']))

			if (reaction['initialtargetparticle'] is not None ) and (reaction['finaltargetparticle'] is not None):
				reaction['code'] = '%s(%s, %s)%s %s' %(
						reaction['initialtargetparticle'], reaction['incidentparticle'], reaction['exitparticle'], 
						reaction['finaltargetparticle'], reaction['reactionQ'])
			else:
				if None in [reaction['incidentparticle'], reaction['exitparticle']]:
					reaction['code'] = ''
				else:
					reaction['code'] = '(%s, %s)' %(reaction['incidentparticle'], reaction['exitparticle'])


			reactions.append(reaction)

		return reactions
	

	def set_technique(self, technique, spectra_id = 0):
		"""Sets the experimental technique of the spectrum[spectra_id]
		
		Args:
			technique (str): Name of the technique
			spectra_id (int, optional): ID of the spectrum
		"""
		spec = self.get_spectrum(spectra_id = spectra_id)
		reactions = self.get_section(spec, 'reactions', create_if_not_found=['reactions'])[0]
		
		reaction = self.change_node_value(technique, reactions, 'technique')

	def get_technique(self, spectra_id=0):
		"""Gets the experimental technique of spectrum[spectra_id]
		
		Args:
			spectra_id (int, optional): ID of the spectrum
		
		Returns:
			str: Name of the technique
		"""
		spec = self.get_spectrum(spectra_id = spectra_id)
		reactions = self.get_section(spec, 'reactions', create_if_not_found=['reactions'])[0]
		technique = get_xml_entry(reactions, 'technique')
		
		if technique == None:
			technique = 'RBS'

		return technique


		
## Methods for the str parameters
	
	def get_nelements(self):
		"""Ĝets the number of elements in the sample
		
		Returns:
			int: The number of elements in the sample
		"""
		elements = get_xml_section(self.file, 'molecules')
		if elements:
			return int(get_xml_entry(elements[0], 'nmolecules'))
		
	def get_elements(self):
		"""Gets the elements in the sample (see also ``self.set_elements()``)

		It returns a dictionary in which the keywords are the name of the elements and the
		items the information of each element. For a sample of CoPt/SiO2/Si the returned 
		dictionary is::

			{'nelements': 3,
			 'CoPt': 
				 {'ele_id': 0,
				  'name': 'Co 0.45 Pt 0.55',
				  'density': '',
				  'concentration': ['0', '5000'],
				  'depth': ['0', '1']},
			 'Si 1 O 2': 
				 {'ele_id': 1,
				  'name': 'Si 1 O 2',
				  'density': '',
				  'concentration': ['0', '5000'],
				  'depth': ['0', '1']},
			 'Si': 
				 {'ele_id': 2,
				  'name': 'Si',
				  'density': '',
				  'concentration': ['100', '10000000'],
				  'depth': ['0', '1']}
			}
		
		Returns:
			dictionary: A dictionary of dictionaries, each defining an element
		"""
		elements_entry = get_xml_section(self.file, 'molecules')
		if elements_entry is None: return
		
		elements_subentry = get_xml_section(elements_entry[0], 'molecule')
		if elements_subentry is None: return
		
		# elements = OrderedDict()
		elements = {'nelements': len(elements_subentry)}
		for i,mol in enumerate(elements_subentry):
			# name = mol.getElementsByTagName('name')[0].firstChild.nodeValue 
			name = get_xml_entry(mol, 'name')
			if name is None: name = ''

			if get_xml_entry(mol, 'density') not in ['', None]:
				density = float(get_xml_entry(mol, 'density'))
				den_units = mol.getElementsByTagName('density')[0].getAttribute('units')

				if den_units != '1e22at/cm3':
					print('Wrong density units in %s, converted to 1e22at/cm3'%name)
					unit = float(den_units.split('at')[0])
					density *= 1e22/unit
			else:
				density = ''

			min_con = self.get_min_concentration(mol)
			max_con = self.get_max_concentration(mol)
			min_depth = self.get_min_depth(mol)
			max_depth = self.get_max_depth(mol)
			
			elements[i] = {
				'name': name,
				'density': density,
				'concentration': [min_con, max_con],
				'depth'  : [min_depth, max_depth]
			}
		
		return elements


	def get_min_concentration(self, molecule_entry):
		"""Gets the minimum concentration from the XML molecule entry. To be used internally.
		Use ``self.get_elements()`` instead.
		
		Args:
			molecule_entry (DOM XML entry): XML entry of a given molecule
		
		Returns:
			str: Value to the minimum concentration
		"""
		if molecule_entry is None: return '0'

		value = get_xml_entry(molecule_entry, 'concentrationmin')

		if value is None:
			return '0'
		
		return value

	def get_max_concentration(self, molecule_entry):
		"""Gets the maximum concentration from the XML molecule entry. To be used internally.
		Use ``self.get_elements()`` instead.
		
		Args:
			molecule_entry (DOM XML entry): XML entry of a given molecule
		
		Returns:
			str: Value to the maximum concentration
		"""	
		if molecule_entry is None: return '0'

		value = get_xml_entry(molecule_entry, 'concentrationmax')

		if value is None:
			return '0'
		
		return value

	def get_min_depth(self, molecule_entry):
		"""Gets the minimum element depth from the XML molecule entry. To be used internally.
		Use ``self.get_elements()`` instead.
		
		Args:
			molecule_entry (DOM XML entry): XML entry of a given molecule
		
		Returns:
			str: Value to the minimum element depth concentration
		"""	
		if molecule_entry is None: return '0'

		value = get_xml_entry(molecule_entry, 'depthmin')

		if value is None:
			return '0'
		
		return value

	def get_max_depth(self, molecule_entry):	
		"""Gets the maximum element depth from the XML molecule entry. To be used internally.
		Use ``self.get_elements()`` instead.
		
		Args:
			molecule_entry (DOM XML entry): XML entry of a given molecule
		
		Returns:
			str: Value to the maximum element depth concentration
		"""		
		if molecule_entry is None: return '0'

		value = get_xml_entry(molecule_entry, 'depthmax')

		if value is None:
			return '0'
		
		return value



## Methods for the prf parameters

	def get_nlayers(self):
		"""Gets the number of layers of the sample
		
		Returns:
			int: the number of layers
		"""
		layers_entry = get_xml_section(self.file, 'layeredstructure')
		if layers_entry:
			return int(get_xml_entry(layers_entry[0], 'nlayers'))
	
	def get_profile(self):
		"""Gets the depth profile of the sample.

		It returns a *profile_dic* identical to the input of ``self.set_profile()``::

			profile_dic = {
					'nlayers': '3',
					'names': ['Co 0.45 Pt 0.55', 'Si 1 O 2', 'Si'],
					0: {'thickness': 390,     'concentrations': [1, 0, 0]}, 
					1: {'thickness': 700,     'concentrations': [0, 1, 0]}, 
					2: {'thickness': 4000000, 'concentrations': [0, 0, 1]} 				
					}
		

		Note:
			Previous ``self.get_layers()``

		Returns:
			dictionary: Dictionary with the data on the depth profile of the sample
		"""
		layers_entry = get_xml_section(self.file, 'layeredstructure')
		if layers_entry is None: return
		
		layers = {'nlayers':0, 'names':[]}
		
		layers_subentry = get_xml_section(layers_entry[0], 'layer')
		if layers_subentry is None: return
		
		for i, layer in enumerate(layers_subentry):
			elements = []
			concentrations = []
			
			thickness, thick_unit = get_xml_entry(layer, 'layerthickness', attribute='units')
			if thick_unit != '1e15at/cm2':
				print('Wrong thickness units in layer %i, converted to 1e15at/cm2'%i)
				thick_unit = float(thick_unit.split('at')[0])
				thickness = float(thickness)
				thickness *= 1e15/thick_unit
			
			for ele in layer.getElementsByTagName('layerelement'):
				elements.append(get_xml_entry(ele,'name'))
				concentrations.append(get_xml_entry(ele, 'concentration'))
			
			# concentrations = self.get_elements_elements_concentrations(elements)
			

			layers[i] = {
				'thickness': thickness,
				#'elements' : elements,
				'concentrations': concentrations
			}

		layers['nlayers'] = i
		layers['names'] = elements

		return layers
 
	def get_elements_molecules_concentrations(self, layer_elements):
		"""Deprecated, will be removed soon
		
		"""
		concentrations = [0]*self.get_nelements()
		elements_str = self.get_elements()
		work_elements = layer_elements[:] # to avoid changing the original list
		xx = False    

		for i,element in enumerate(elements_str):
			clean_ele_list = []
			for e in element.split():
				if e.isalpha():
					clean_ele_list.append(e)

			 # print(layer_elements)
			 # print(clean_ele_list)

			if len(clean_ele_list)>1:  
				for e in clean_ele_list:                  
					if e in work_elements:
						xx = True
					else:
						xx = False
						break

			if xx:
				concentrations[i] = 1
				for e in clean_ele_list:
					work_elements.remove(e)


		for e in work_elements:
			ele_id = elements_str[e]['ele_id']
			concentrations[ele_id]= 1

		return concentrations







####################  Methods to save the IDF file  ###########################################

	def save_idf(self, filename):
		"""Saves the IDF state into a file

		This command is what produces the IDF file. Notice that any modification done to the IDF()
		object is not stored in the file until ``self.save_idf()`` is issued.

		Example:
			Load an existing file, perform some changes to the parameters and save it again::

				#load a IDF file
				idf_file = IDF('path/to/file.idf')

				#change some parameters
				idf_file.set_charge(5)
				idf_file.set_beam_energy(2000)
				#....
				
				#save file by overwriting the previous file (i.e. *save*)
				idf_file.save_idf('path/to/file.idf')

				#or if you want to create a new file (i.e. *save as*)
				idf_file.save_idf('path/to/new_file.idf')

		
		Args:
			filename (str): Path to save the path. Warning: it overwrites existing files
		
		Returns:
			IDF: Returns the existing IDF object
		"""
		with open(filename, 'w') as file:
			self.file.writexml(file, encoding='utf-8')

		self.path_dir = '/'.join(filename.split('/')[:-1]) + '/'
		if self.path_dir == '/':
			self.path_dir = ''


		self.file_name = filename.split('/')[-1]#.split('.')[0]
		self.name = self.file_name.split('.')[0]
		self.file_path = filename
		


		return self #IDF(filename)



###################  Methods to manipulate xml files  #################################
	
	def change_node_value(self, value, parent, keyword, attributes = {}, append = False):
		"""Changes the value of the XML node. Not intended to be used directly and the *set_*
		methods should be used instead.

		Example:
			To change the beam the 'beamenergy' node on the XML file, including the attributes
			do::
				
				#get the correct spectrum XML section 
				spec = idf_file.get_spectrum(spectra_id=1)

				#get the beam section of the spectrum entry
				beam = idf_file.get_section(spec, 'beam', create_if_not_found = ['beam'])[0]
				
				#define the attributes dictionary
				attributes = {
					'units': 'keV'
				}

				#change the note
				idf_file.change_node_value(energy, beam, 'beamenergy', attributes = attributes)

			However, is much better and controlled to simply use::

				idf_file.set_beam_energy(energy, spectra_id = 1):
		
		
		Args:
			value (str or float): Value to insert in the XML node
			parent (DOM XML Element): XML parent of the node to be changed
			keyword (str): xml keywork of the node to be changed
			attributes (dict, optional): Dictionary with the attributes of the node
			append (bool, optional): If True it appends the new node to the existing ones on the parent
		"""
		# Create new element
		element = self.file.createElement(keyword)
		# Create new node
		node = self.file.createTextNode(str(value))
		
		# Add attributes
		for key, value in attributes.items():
			element.setAttribute(key, value)
		
		# Append the node to the new element
		element.appendChild(node)

		# get the child to be changed
		element2change = get_xml_section(parent, keyword)

		if element2change is None:       
			parent.appendChild(element)
		elif append:
			parent.appendChild(element)
		else:
			#replace the child with the new element
			parent.replaceChild(element, element2change[0])
			
	def remove_nodes(self, parent, keyword):
		"""Removes a XML node
		
		Args:
			parent (DOM XML Element): Parent of the node to be removed
			keyword (str): Keyword of the node to be removed
		"""
		element2remove = get_xml_section(parent, keyword)
		for ele in element2remove:
			parent.removeChild(ele)
		
	def create_element(self, parent, keyword):
		"""Creates a XML node
		
		Args:
			parent (DOM XML Element): Parent of the node to be added
			keyword (str): Keyword of the node to be added
		
		Returns:
			TYPE: DOM XML Element
		"""
		element = self.file.createElement(keyword)
		parent.appendChild(element)
		return element
	
	def create_tree(self, tree, prefix = ''):
		"""Creates a tree of parents in the XML, starting from the 'sample' element. 
		See also ``self.create_tree_on_parent()``.
		
		*tree* is a list with the multiple parents of the tree.

		Example:
		
			For instance, to create the XML structure::
				
				<sample>
					<structure>
						<layeredstructure>
							<layers>
								<layer>
									

			we do::

				tree = ['structure','layeredstructure', 'layers', 'layer']
				idf_file.create_tree(tree)

		Args:
			tree (list): List with the keywords of the parents forming the tree.
			prefix (str, optional): A prefix that is added to all of the parents keywords
		
		Returns:
			XML Element: The last element of the tree just created
		"""
		sample_element = get_xml_section(self.file, 'sample')[0]
		
		element_parent = sample_element
		for key in tree:
			element = get_xml_section(element_parent, prefix + key)
			if element is None:
				self.create_element(element_parent, prefix + key)
				
			element_parent = get_xml_section(element_parent, prefix + key)[0]
		
		# returns the last element created
		return element_parent
	

	def create_tree_on_parent(self, tree, parent, prefix = '', replace = False):
		"""Creates a tree of parents in the XML, starting from the *parent* element.
		See also ``self.create_tree()``.

		*tree* is a list with the multiple parents of the tree.

		Example:
			For instance, to introduce a NDF analysis on a *<simulation>* entry of the IDF file,
			we can do the following::
				
				#get the simulation parent of the IDF file
				simulation_entry = self.get_simulation(spectra_id=spectra_id, simulation_id = simulation_id)
				
				#create a parent tree on that parent
				data_entry = self.create_tree_on_parent(
									['ndf','fitresults','data', 'simpledata'],
									simulation_entry, 
									prefix = 'ndf:')
			
			Note the use of the ``prefix = 'ndf:'`` to indicate that we are introducing a another
			XML schema (i.e. the NDF one) into the IDF file. The above code will produce::
				
				<...>
					<simulation>
						<ndf:ndf>
							<ndf:fitresults>
								<ndf:data>
									<ndf:simpledata>
			
		
		Args:
			tree (list): List with the keywords of the parents forming the tree.
			parent (XML Element): Parent to which the tree is added
			prefix (str, optional): A prefix that is added to all of the parents keywords
		
		Returns:
			XML Element: The last element of the tree just created
		"""
		element_parent = parent

		if replace:
			try:
				self.remove_nodes(element_parent, tree[0])
			except:
				pass

		for key in tree:
			element = get_xml_section(element_parent, prefix + key)
			if element is None:
				self.create_element(element_parent, prefix + key)

			element_parent = get_xml_section(element_parent, prefix + key)[0]

		# returns the last element created
		return element_parent


	def get_section(self, parent, keyword, create_if_not_found = False):
		"""For internal use
		"""
		entry = parent.getElementsByTagName(keyword)
		if len(entry)==0:
			entry = None
		
		if entry == None:
			if create_if_not_found is False:
				return entry
			elif isinstance(create_if_not_found, list):
				entry = self.create_tree_on_parent(create_if_not_found, parent)
				return [entry]
		else:
			return entry

	def get_idf_text(self):
		xml_file = self.file.toprettyxml(indent='  ')
		xml_file = [s for s in xml_file.split('\n') if s.strip() !='']

		return xml_file


	def print_idf_file(self, mode = 'pretty'):
		"""Prints the XML contents of the IDF file.
		Used mostly to check/debug files.
		"""
		if mode == 'XML':
			xml_file = self.file.toprettyxml(indent='  ')

			xml_file = [s for s in xml_file.split('\n') if s.strip() !='']
			for l in xml_file:
				print(l)

		elif mode == 'pretty':
			nspectra = self.get_number_of_spectra()

			notes = self.get_notes()
			author = self.get_user()
			elements = self.get_elements()
			profile = self.get_profile()

			delH1 = ''.join(['=']*15)

			print('%s %s %s' %(delH1, self.name, delH1))
			print(self.file_path)
			print(author, '\n')
			print('------------------', ' Notes ', '------------------')
			for n in notes:
				print(n)

			print('\n------------------ Elements -----------------')
			if elements == None:
				print('No elements found')
			else:
				for k, param in elements.items():
					if k == 'nelements':
						print(k, '\t', param)
						continue

					print('\n - - - Element %i - - -' %k)

					for k2, param2 in param.items():
						if len(k2) < 6:
							fill = '\t\t'
						else:
							fill = ' \t'
						print(k2, fill,param2)

			print('\n------------------ Profile -----------------')
			if profile == None:
				print('Profile not found')
			else:
				for k, param in profile.items():
					if k in ['nlayers', 'names']:
						print(k, '\t\t', param)
						continue
					print('\n - - - Layer %i - - -' %k)

					for k2, param2 in param.items():
						if len(k2) < 10:
							fill = '\t\t'
						else:
							fill = ' \t'
						print(k2, fill,param2)


			print('\n\n')
			for n in range(0, nspectra):
				geo = self.get_geo_parameters(spectra_id = n)
				name = self.get_spectrum_file_name(spectra_id = n)
				technique = self.get_technique(spectra_id=n)
				reactions = self.get_reactions(spectra_id=n)
				if reactions is None:
					reactions = []
				try:
					geo.pop('mode')
				except Exception as e:
					pass

				geo.pop('window')
				if technique == 'ERDA':
					geo['detected ion'] = self.get_reactions(spectra_id=n)[0]['exitparticle']

				print('-------- Spectrum %i (%s) --------' %(n, name))
				print('Technique \t%s'%technique)
				for r in reactions:
					print('\t\t', r['code'])

				print('\n')
				for k, p in geo.items():
					if len(k) < 5:
						fill = '\t\t'
					else:
						fill = ' \t'
					print(k.replace('_', ' ').capitalize(), fill, p)


				xx, yy = self.get_dataxy(spectra_id = n)
				fig, ax = subplots(1,1)

				if technique in ['RBS', 'NRA', 'ERDA']:
					ax.plot(xx[2:], yy[2:])
					ax.set_xlabel('Energy (Channels)')
				elif technique == 'PIXE':
					ax.stem(xx, yy, basefmt = ' ')
			
					
					ax.set_xlabel('Element/Line')
					ax.set_ylabel('Line Area')
					ax.set_yscale('log')

				elif technique == 'SIMS':
					print('Plotting not supported for SIMS')

				fig.tight_layout()
				pltpause(0.1)
