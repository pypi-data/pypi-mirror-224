from numpy import array as nparray
from numpy import savetxt, pi, loadtxt, genfromtxt, reshape
from collections import OrderedDict
from re import search


from pyIBA.main_idf import main_idf
from pyIBA.auxiliar import *

class NDF():
	"""Class focusing the NDF part of the IDF.
	"""

	def set_simulation_group(self, simulation_group, shared_charge = False, spectra_id = 0, simulation_id = 0):
		simulation_entry = self.get_simulation(spectra_id=spectra_id, simulation_id = simulation_id)
		
		ndf_entry = self.get_section(simulation_entry, 'ndf:ndf', create_if_not_found=['ndf:ndf'])[0]
		
		self.change_node_value(simulation_group, ndf_entry, 'ndf:simulationgroup')
		self.change_node_value(shared_charge, ndf_entry, 'ndf:sharedcharge')

	def get_nspectra_in_simulation_group(self, simulation_group):
		nspectra = 0
		for i in range(self.get_number_of_spectra()):
			sim_group = self.get_simulation_group(spectra_id = i)[0]
			if sim_group == simulation_group:
				nspectra += 1

		return nspectra
		
	def get_simulation_group(self, spectra_id = 0, simulation_id = 0):
		simulation_entry = self.get_simulation(spectra_id=spectra_id, simulation_id = simulation_id)
		
		sim_group, file_id = get_xml_entry(simulation_entry, 'ndf:simulationgroup', attribute = 'id')
		shared_charge = get_xml_entry(simulation_entry, 'ndf:sharedcharge')

		
		if sim_group is None:
			return 1, '0101', False
		else:
			### The code below is not acutally needed. The IDF2NDF saves the IDs into the 
			### IDF file. Make sure you reload the file after run NDF.
			# sim_group = int(sim_group)
			# if spectra_id <10: head_spectra_0 = '0'
			# else: head_spectra_0 = ''
			# if sim_group <10: head_sim_0 = '0' 
			# else: head_sim_0 = ''

			# file_id = '%s%i%s%i' %(head_spectra_0, sim_group + 1, head_sim_0, spectra_id + 1)
			if shared_charge is not None:
				if shared_charge.lower() == 'true':
					shared_charge = True
				else:
					shared_charge = False
			else:
				shared_charge = True
	
			return sim_group, file_id, shared_charge


## Methods to set resultant spectra

	def set_PIXE_data_fit_result(self, xray_lines, xray_area, spectra_id = 0):
		spectrum_entry= self.get_spectrum(spectra_id=spectra_id)

		simulation_entry = self.create_tree_on_parent(['process','simulations', 'simulation'], spectrum_entry)
		data_entry = self.create_tree_on_parent(['ndf','fitresults','data', 'linedata'], simulation_entry, prefix = 'ndf:')

		xaxis_entry = self.create_tree_on_parent(['xaxis'], data_entry, prefix = 'ndf:')
		yaxis_entry = self.create_tree_on_parent(['yaxis'], data_entry, prefix = 'ndf:')
		self.change_node_value('xrayline', xaxis_entry, 'ndf:axisname')
		self.change_node_value('', xaxis_entry, 'ndf:axisunit')
		self.change_node_value('yield', yaxis_entry, 'ndf:axisname')
		self.change_node_value('counts', yaxis_entry, 'ndf:axisunit')
				
		self.change_node_value(' '.join(xray_lines), data_entry, 'ndf:line')
		self.change_node_value(' '.join(xray_area), data_entry, 'ndf:y')


	def set_SIMS_data_fit(self, data_list, spectra_id = 0):       
		spectrum_entry= self.get_spectrum(spectra_id=spectra_id)
		
		simulation_entry = self.create_tree_on_parent(['process','simulations', 'simulation'], spectrum_entry)
		
		try:
			data_node = self.get_section(spectrum_entry, 'ndf:data')[0]
			self.remove_nodes(data_node, 'ndf:multipledata')
		except Exception as e:
			pass
		
		data_entry = self.create_tree_on_parent(['ndf','fitresults','data', 'multipledata'], simulation_entry, 
												prefix = 'ndf:')

		xaxis_entry = self.create_element(data_entry, 'xaxis')
		self.change_node_value('depth', xaxis_entry, 'axisname')
		self.change_node_value('umr', xaxis_entry, 'axisunit')
		
				
		multipledata_entry = self.create_element(data_entry, 'ndf:multipledataentries')
		
		for line in data_list:
			line2write = [str(e) for e in line]
			line2write = '\t'.join(line2write)
			self.change_node_value(line2write, multipledata_entry, 'ndf:multipledataentry', append=True)
		

	def get_SIMS_data_fit(self, spectra_id = 0, simulation_id = 0):
		simulation_entry = self.get_simulation(spectra_id=spectra_id, simulation_id = simulation_id)
		if simulation_entry is None:
			return [None, None]

		particles = self.get_SIMS_particles(spectra_id = spectra_id)

		data_entry = get_xml_section(simulation_entry, 'ndf:multipledataentries')
		if data_entry is None:
			return [None, None]
		else:
			data_entry = data_entry[0]

		depth_lines_entry = get_xml_section(data_entry, 'ndf:multipledataentry')

		depth_lines = [d.firstChild.nodeValue.split() for d in depth_lines_entry]

		depth = [float(d[0]) for d in depth_lines]

		sims_data = {}
		for i,p in enumerate(particles):
			sims_data[p] = [float(d[i+1]) for d in depth_lines]


		return depth, sims_data	



	####################### Methods to set the spectra results  ##############################

	def set_spectrum_data_fit_result(self, data_x, data_y, spectra_id = 0, simulation_id = 0):
		simulation_entry = self.get_simulation(spectra_id=spectra_id, simulation_id = simulation_id)
		data_entry = self.create_tree_on_parent(['ndf','fitresults','data', 'simpledata'], simulation_entry, prefix = 'ndf:')

		xaxis_entry = self.create_tree_on_parent(['xaxis'], data_entry, prefix = 'ndf:')
		yaxis_entry = self.create_tree_on_parent(['yaxis'], data_entry, prefix = 'ndf:')
		self.change_node_value('energy', xaxis_entry	, 'ndf:axisname')
		self.change_node_value('channel', xaxis_entry	, 'ndf:axisunit')
		self.change_node_value('yield', yaxis_entry	    , 'ndf:axisname')
		self.change_node_value('counts', yaxis_entry	, 'ndf:axisunit')

		# data_entry = self.create_tree_on_parent(['ndf','fitresults','data', 'simpledata'], spectrum_entry, prefix = 'ndf:')
		
		data_x = [str(s) for s in data_x]
		data_y = [str(s) for s in data_y]
			
		x_string = ' '.join(data_x)
		y_string = ' '.join(data_y)

		self.change_node_value(x_string, data_entry, 'ndf:x')
		self.change_node_value(y_string, data_entry, 'ndf:y')

	def set_elemental_spectrum_data_fit_result(self, data, spectra_id = 0, simulation_id = 0):
		simulation_entry = self.get_simulation(spectra_id=spectra_id, simulation_id = simulation_id)
		data_entry = self.create_tree_on_parent(['ndf','fitresults','data', 'elementaldata'], simulation_entry, prefix = 'ndf:')

		# x axis will always be shared between the elemental spectra
		xaxis_entry = self.create_tree_on_parent(['xaxis'], data_entry, prefix = 'ndf:')
		self.change_node_value('energy' , xaxis_entry, 'ndf:axisname')
		self.change_node_value('channel', xaxis_entry, 'ndf:axisunit')

		if data == None:
			try:
				self.remove_nodes(data_entry, 'ndf:x')
				self.remove_nodes(data_entry, 'ndf:element')
			except:
				pass
			return

		data_x = [str(s) for s in data['x']]
		x_string = ' '.join(data_x)
		self.change_node_value(x_string, data_entry, 'ndf:x')

		for k, yelement in data.items():
			if k == 'x':
				continue
			try:
				self.remove_nodes(data_entry, 'ndf:element')
			except:
				pass

		for k, yelement in data.items():
			if k == 'x':
				continue

			element_entry = self.create_element(data_entry, 'ndf:element')
			self.change_node_value(k, element_entry, 'ndf:elementname')
			yaxis_entry = self.create_tree_on_parent(['yaxis'], element_entry, prefix = 'ndf:')
			self.change_node_value('yield' , yaxis_entry	, 'ndf:axisname')
			self.change_node_value('counts', yaxis_entry	, 'ndf:axisunit')

			# data_entry = self.create_tree_on_parent(['ndf','fitresults','data', 'simpledata'], spectrum_entry, prefix = 'ndf:')
			
			data_y = [str(s) for s in yelement]
			
			y_string = ' '.join(data_y)

			self.change_node_value(y_string, yaxis_entry, 'ndf:y')


	def get_dataxy_fit(self, spectra_id = 0, simulation_id = 0):
		technique = self.get_technique(spectra_id=spectra_id)
		if technique in ['RBS', 'NRA', 'ERDA', None]:
			type_data = 'ndf:simpledata'
			x_tag = 'ndf:x'
			y_tag = 'ndf:y'
		elif technique == 'PIXE':
			type_data = 'ndf:linedata'
			x_tag = 'ndf:line'
			y_tag = 'ndf:y'
		elif technique == 'SIMS':
			return self.get_SIMS_data_fit(spectra_id=spectra_id, simulation_id = simulation_id)
		else:
			return [0], [0]

		simulation_entry = self.get_simulation(spectra_id = spectra_id, simulation_id=simulation_id)
		if simulation_entry is None:
			return [0], [0]

		total_fit_entry = get_xml_section(simulation_entry, type_data)
		if total_fit_entry is None: 
			return [0], [0]
		else:
			total_fit_entry = total_fit_entry[0]

		xx = get_xml_section(total_fit_entry, x_tag)
		yy = get_xml_section(total_fit_entry, y_tag)
		
		if xx is None or yy is None: return None, None
		
		xx = xx[0].firstChild.nodeValue.split()
		yy = yy[0].firstChild.nodeValue.split()

		if x_tag != 'ndf:line':
			xx = nparray(xx).astype('float')
		yy = nparray(yy).astype('float')

		return xx, yy


	def get_elemental_dataxy_fit(self, spectra_id = 0, simulation_id = 0):
		technique = self.get_technique(spectra_id=spectra_id)
		if technique in ['RBS', 'NRA', 'ERDA', None]:
			type_data = 'ndf:elementaldata'
			x_tag = 'ndf:x'
			y_tag = 'ndf:y'
		else:
			return [0], [0]


		simulation_entry = self.get_simulation(spectra_id = spectra_id, simulation_id=simulation_id)
		elements_fit_entry = get_xml_section(simulation_entry, type_data)

		if elements_fit_entry is None: 
			return {'x':[]}
		else:
			elements_fit_entry = elements_fit_entry[0]


		# if xx is None or yy is None: return None, None

		xx = get_xml_section(elements_fit_entry, x_tag)
		xx = xx[0].firstChild.nodeValue.split()
		xx = nparray(xx).astype('float')

		data = {'x': xx}

		element_entry = get_xml_section(elements_fit_entry, 'ndf:element')
		for ele_fit in element_entry:
			name = get_xml_section(ele_fit, 'ndf:elementname')[0].firstChild.nodeValue
			yy = get_xml_section(ele_fit, y_tag)		
			yy = yy[0].firstChild.nodeValue.split()
			yy = nparray(yy).astype('float')

			data[name] = yy

		return data



	####################### Methods for profile results   ##################################

	def set_profile_fit_result(self, profile_dic, spectra_id = 0, simulation_id = 0):
		simulation_entry = self.get_simulation(spectra_id=spectra_id, simulation_id=simulation_id)

		layers_entry = self.create_tree_on_parent(['ndf','fitresults','structure', 'layeredstructure'],
													 simulation_entry, prefix = 'ndf:')
		
		
		self.change_node_value(profile_dic['nlayers'], layers_entry, 'ndf:nlayers')
		
		try:
			self.remove_nodes(layers_entry, 'ndf:layers')
		except Exception as e:
			pass
			#print(e)
			
		layer_entries = self.create_element(layers_entry, 'ndf:layers')
		
		
		
		for key, ele in profile_dic.items():
			if key in ['nlayers', 'names']:
				continue
				
			layer_entry = self.create_element(layer_entries, 'ndf:layer')
			self.change_node_value(ele['thickness'], layer_entry, 'ndf:layerthickness', 
								   attributes={'units':'1e15at/cm2'})
			
			layerelements_entry = self.create_element(layer_entry, 'ndf:layerelements')
			
			# loop elements
			for i,c in enumerate(ele['concentrations']):
			   # if c != 0:
				element_entry = self.create_element(layerelements_entry, 'ndf:layerelement')

				name = profile_dic['names'][i]
				self.change_node_value(name, element_entry, 'ndf:name')
				self.change_node_value(c, element_entry, 'ndf:concentration', attributes={'units':'fraction'})
			
	
	def get_profile_fit_result(self, spectra_id = 0, simulation_id = 0):
		ndf_results = self.get_fit_results_entry(spectra_id = spectra_id, simulation_id = simulation_id)
		if ndf_results is None:
			return	

		params = {}        
		
		params['nlayers'] = get_xml_entry(ndf_results, 'ndf:nlayers')
		layer_entries = get_xml_section(ndf_results, 'ndf:layer')
		if layer_entries == None:
			return params
		
		for i,layer in enumerate(layer_entries):
			elements_entry = get_xml_section(layer, 'ndf:layerelement')
			
			concentrations = []
			names = [] 
			# although all the names are the same and hence this will be repeated for nlayers, 
			#I leave it like this  to remove the elements with concentration 0 from the IDF
			
			for element in elements_entry:
				concentrations.append(get_xml_entry(element, 'ndf:concentration'))
				names.append(get_xml_entry(element, 'ndf:name'))
				
			
			params[i] = {
				'thickness' : get_xml_entry(layer,'ndf:layerthickness'),
				'concentrations' : concentrations
			}

		params['names'] = names
		
		return params


	def set_data_from_prf_file(self, prf_file, spectra_id = 0, simulation_id = None):
		profile_dic = read_prf_file(prf_file)
		if simulation_id != None:
			self.set_profile_fit_result(profile_dic, spectra_id = spectra_id, simulation_id = simulation_id)
		else:
			self.set_profile(profile_dic)


	####################### Methods for elements results  ##################################

	
	def set_elements_fit_result(self, elements_dic, spectra_id = 0, simulation_id = 0):
		simulation_entry = self.get_simulation(spectra_id=spectra_id, simulation_id=simulation_id)

		molecules_entry = self.create_tree_on_parent(['ndf','fitresults','elementsandmolecules', 'molecules'],
													 simulation_entry, prefix = 'ndf:')

		self.change_node_value(elements_dic['nelements'], molecules_entry, 'ndf:nmolecules')
		
		
		try:
			self.remove_nodes(molecules_entry, 'ndf:molecule')
		except:
			pass
		
		for i, values in elements_dic.items():
			if i == 'nelements':
				continue
			name = values['name']
			
			molecule_entry = self.create_element(molecules_entry, 'ndf:molecule')
			self.change_node_value(name, molecule_entry, 'ndf:name')

			
	def get_elements_fit_result(self, spectra_id = 0, simulation_id = 0):
		ndf_results = self.get_fit_results_entry(spectra_id = spectra_id, simulation_id = simulation_id)
		if ndf_results is None:
			return
		
		params = {}
		
		params['nelements'] = get_xml_entry(ndf_results, 'ndf:nmolecules')
		
		molecule_entries = get_xml_section(ndf_results, 'ndf:molecule')
		if molecule_entries is not None:
			for i,mol in enumerate(molecule_entries):
				params[i] = get_xml_entry(mol, 'ndf:name')
					   

		return params


	def set_data_from_str_file(self, str_file, spectra_id = 0, simulation_id = 0, type = 'result'):
		params = read_str_file(str_file)
		
		if type == 'result':
			self.set_elements_fit_result(params, spectra_id = spectra_id, simulation_id =simulation_id) 
		else:
			self.set_elements(params)


	



	####################### Methods for geometry results  ################################

	
		
	def set_beam_energy_fit_result(self, energy, spectra_id = 0, simulation_id = 0):
		simulation_entry = self.get_simulation(spectra_id=spectra_id, simulation_id = simulation_id)
		if simulation_entry is None:
			spectrum_entry= self.get_spectrum(spectra_id=spectra_id)
			simulation_entry = self.create_tree_on_parent(['process','simulations', 'simulation'], spectrum_entry)

		beam_entry = self.create_tree_on_parent(['ndf','fitresults','beam'], simulation_entry, prefix = 'ndf:')

		attributes = {'units': 'keV'}
		self.change_node_value(energy, beam_entry, 'ndf:beamenergy', attributes=attributes)
		
	def get_beam_energy_fit_result(self, spectra_id = 0, simulation_id = 0):
		ndf_results = self.get_fit_results_entry(spectra_id = spectra_id, simulation_id = simulation_id)      

		if ndf_results is None:
			return

		energy_value, energy_units = get_xml_entry(ndf_results, 'ndf:beamenergy', attribute='units')
		
		return energy_value
	
	
	
	def set_beam_energy_spread_fit_result(self, FWHM, spectra_id = 0, simulation_id = 0):
		simulation_entry = self.get_simulation(spectra_id=spectra_id, simulation_id = simulation_id)
		if simulation_entry is None:
			spectrum_entry= self.get_spectrum(spectra_id=spectra_id)
			simulation_entry = self.create_tree_on_parent(['process','simulations', 'simulation'], spectrum_entry)

		beam_entry = self.create_tree_on_parent(['ndf','fitresults','beam'], simulation_entry, prefix = 'ndf:')

		attributes = {'units': 'keV', 'mode':'FWHM'}
		self.change_node_value(FWHM, beam_entry, 'ndf:beamenergyspread', attributes=attributes)
		
	def get_beam_energy_spread_fit_result(self, spectra_id = 0, simulation_id = 0):
		ndf_results = self.get_fit_results_entry(spectra_id = spectra_id, simulation_id = simulation_id)      
		if ndf_results is None:
			return

		energy_value, energy_units = get_xml_entry(ndf_results, 'ndf:beamenergyspread', attribute='units')
		
		return energy_value
		
		
	
	def set_incident_angle_fit_result(self, angle, spectra_id = 0, simulation_id = 0):
		simulation_entry = self.get_simulation(spectra_id=spectra_id, simulation_id = simulation_id)
		if simulation_entry is None:
			spectrum_entry= self.get_spectrum(spectra_id=spectra_id)
			simulation_entry = self.create_tree_on_parent(['process','simulations', 'simulation'], spectrum_entry)

		geo_entry = self.create_tree_on_parent(['ndf','fitresults','geometry'], simulation_entry, prefix = 'ndf:')
		attributes = {'units': 'degree'}
		self.change_node_value(angle, geo_entry, 'ndf:incidenceangle', attributes=attributes)
		
	def get_incident_angle_fit_result(self, spectra_id = 0, simulation_id = 0):
		ndf_results = self.get_fit_results_entry(spectra_id = spectra_id, simulation_id = simulation_id)
		if ndf_results is None:
			return
		
		angle = get_xml_entry(ndf_results, 'ndf:incidenceangle')
		
		return angle
	
	
		
	def set_scattering_angle_fit_result(self, angle, spectra_id = 0, simulation_id = 0):
		simulation_entry = self.get_simulation(spectra_id=spectra_id, simulation_id = simulation_id)
		if simulation_entry is None:
			spectrum_entry= self.get_spectrum(spectra_id=spectra_id)
			simulation_entry = self.create_tree_on_parent(['process','simulations', 'simulation'], spectrum_entry)

		geo_entry = self.create_tree_on_parent(['ndf','fitresults','geometry'], simulation_entry, prefix = 'ndf:')
		attributes = {'units': 'degree'}
		self.change_node_value(angle, geo_entry, 'ndf:scatteringangle', attributes=attributes)
		
	def get_scattering_angle_fit_result(self, spectra_id = 0, simulation_id = 0):
		ndf_results = self.get_fit_results_entry(spectra_id = spectra_id, simulation_id = simulation_id)      
		if ndf_results is None:
			return
		
		angle = get_xml_entry(ndf_results, 'ndf:scatteringangle')
		
		return angle
		
	
	def set_charge_fit_result(self, charge, spectra_id = 0):
		spectrum_entry= self.get_spectrum(spectra_id=spectra_id)
		simulation_entry = self.create_tree_on_parent(['process','simulations', 'simulation'], spectrum_entry)

		beam_entry = self.create_tree_on_parent(['ndf','fitresults','beam'], simulation_entry, prefix = 'ndf:')
		
		self.change_node_value(charge, beam_entry, 'ndf:charge')

	def get_charge_fit_result(self, spectra_id = 0, simulation_id = 0):
		ndf_results = self.get_fit_results_entry(spectra_id = spectra_id, simulation_id = simulation_id)      
		if ndf_results is None:
			return
		
		charge = get_xml_entry(ndf_results, 'ndf:charge')
		
		return charge



	# to be removed since detector solid angle is not fitted

	def set_detector_solid_angle_fit_result(self, angle, spectra_id = 0, simulation_id = 0):
		simulation_entry = self.get_simulation(spectra_id=spectra_id, simulation_id = simulation_id)
		if simulation_entry is None:
			spectrum_entry= self.get_spectrum(spectra_id=spectra_id)
			simulation_entry = self.create_tree_on_parent(['process','simulations', 'simulation'], spectrum_entry)

		detector_entry = self.create_tree_on_parent(['ndf','fitresults','detection', 'detector'], simulation_entry, prefix = 'ndf:')
		attributes = {'units': 'msr'}
		self.change_node_value(angle, detector_entry, 'ndf:solidangle', attributes=attributes)
		
	def get_detector_solid_angle_fit_result(self, spectra_id = 0, simulation_id = 0):
		ndf_results = self.get_fit_results_entry(spectra_id = spectra_id, simulation_id = simulation_id)
		if ndf_results is None:
			return
		
		angle = get_xml_entry(ndf_results, 'ndf:solidangle')
		
		return angle
	
	
		
	def set_energy_calibration_fit_result(self, m, b, spectra_id = 0, simulation_id = 0):
		simulation_entry = self.get_simulation(spectra_id=spectra_id, simulation_id = simulation_id)
		if simulation_entry is None:
			spectrum_entry= self.get_spectrum(spectra_id=spectra_id)
			simulation_entry = self.create_tree_on_parent(['process','simulations', 'simulation'], spectrum_entry)
			
		calib_entry = self.create_tree_on_parent(['ndf','fitresults','calibrations', 'energycalibrations', 'energycalibration', 'calibrationparameters'], 
			simulation_entry, prefix = 'ndf:')

		#remove old ones:
		try:
			self.remove_nodes(calib_entry, 'ndf:calibrationparameter')
		except:
			pass

		attributes = {
			'units': 'keV'
		}
		self.change_node_value(b, calib_entry, 'ndf:calibrationparameter', attributes = attributes)


		attributes = {
			'units': 'keV/channel'
		}
		self.change_node_value(m, calib_entry, 'ndf:calibrationparameter', attributes = attributes,
							  append = True)

		
	def get_energy_calibration_fit_result(self, spectra_id = 0, simulation_id = 0):
		ndf_results = self.get_fit_results_entry(spectra_id = spectra_id, simulation_id = simulation_id)
		if ndf_results is None:
			return
		

		param = get_xml_section(ndf_results, 'ndf:calibrationparameter')

		if param is None:
			return [None, None]
		if None in [p.firstChild for p in param]:
			return [None, None]

		if param[0].getAttribute('units') == 'keV':
			param_b = float(param[0].firstChild.nodeValue)
			param_m = float(param[1].firstChild.nodeValue)
		else:
			param_m = float(param[0].firstChild.nodeValue)
			param_b = float(param[1].firstChild.nodeValue)


		return [param_m, param_b]



## Methods to load the parameters directly from the NDF files

	def set_data_from_geo_file(self, geo_file, type_data = 'experimental', add_models = True, spectra_id = 0, simulation_id = 0):
		params = read_geo_file(geo_file)
		

		if type_data == 'experimental':
			self.set_beam_particles(params['reactions']['incidentparticle'], spectra_id=spectra_id)
			self.set_beam_energy(params['energy'], spectra_id=spectra_id)
			self.set_beam_energy_spread(params['FWHM'], spectra_id=spectra_id)
			self.set_geometry_type(params['geometry_type'], spectra_id=spectra_id)
			self.set_incident_angle(params['angles'][0], spectra_id=spectra_id)
			self.set_scattering_angle(params['angles'][1], spectra_id=spectra_id)
			self.set_detector_solid_angle(params['solidangle'], spectra_id=spectra_id)
			self.set_energy_calibration(*params['calibration'], spectra_id=spectra_id)
			
			
			if '.eff' in params['calibration'][0]:
				path = '/'.join(geo_file.split('/')[:-1]) + '/' + params['calibration'][0]
				self.set_energy_calibration_file(path, spectra_id=spectra_id)

			reactions = params['reactions']
			
			if reactions['initialtargetparticle'] == '':
				if reactions['incidentparticle'] == reactions['exitparticle']:
					technique = 'RBS'
				elif reactions['exitparticle'].lower() == 'x':
					technique = 'PIXE'
				else:
					technique = 'ERDA'
			else:
				technique = 'NRA'
			
			self.set_technique(technique, spectra_id=spectra_id)
			self.set_reactions(params['reactions'], append=False, spectra_id=spectra_id, linked_calibrations = False)
			
			if add_models:
				self.set_models_from_geo_file(geo_file, spectra_id=spectra_id)

			
			
		elif type_data == 'result':
			self.set_beam_energy_fit_result(params['energy'], spectra_id = spectra_id, simulation_id = simulation_id)
			self.set_beam_energy_spread_fit_result(params['FWHM'], spectra_id = spectra_id, simulation_id = simulation_id)
			self.set_incident_angle_fit_result(params['angles'][0], spectra_id = spectra_id, simulation_id = simulation_id)
			self.set_scattering_angle_fit_result(params['angles'][1], spectra_id = spectra_id, simulation_id = simulation_id)
			if isinstance(params['solidangle'], list):
				self.set_detector_solid_angle_fit_result(params['solidangle'], spectra_id = spectra_id, simulation_id = simulation_id)
			self.set_energy_calibration_fit_result(*params['calibration'], spectra_id = spectra_id, simulation_id = simulation_id)


	def set_models_from_geo_file(self, geo_file, spectra_id=0, simulation_id = 0):
		params = read_geo_file(geo_file)

		self.set_window_min(params['window'][0], spectra_id=spectra_id, simulation_id = simulation_id)
		self.set_window_max(params['window'][1], spectra_id=spectra_id, simulation_id = simulation_id)

		param_methods = {
				'energy_fitparam': self.set_beam_energy_fitparam,
				'energy_spread_fitparam': self.set_beam_energy_spread_fitparam,
				'incident_angle_fitparam': self.set_incident_angle_fitparam,
				'scattering_angle_fitparam': self.set_scattering_angle_fitparam,
				'double_scattering_model': self.set_model_doublescatter,
				'straggling_model': self.set_model_straggling,
				'stoploss_model': self.set_model_energyloss,
				'pileup_model': self.set_model_pileup,
			}
		
		for p, method in param_methods.items():
			if p in params.keys():
				value = params[p]
				
				if isinstance(value, dict):
					method(value['model'], value['parameter'], spectra_id=spectra_id, simulation_id = simulation_id)                        
				else:
					method(value, spectra_id=spectra_id, simulation_id = simulation_id)


	def set_data_from_spc_file(self, spc_file):
		params_spc = read_spc_file(spc_file)

		self.set_charge_fit_result(params_spc['charge'])	





####################### General Methods to work with results ############################

	def remove_results_from_IDF(self, spectra_id = 0):
		spectrum_entry= self.get_spectrum(spectra_id=spectra_id)
		ndf_entry = get_xml_section(spectrum_entry, 'ndf:ndf')
		if ndf_entry is None:
			return None
		else:
			ndf_entry = ndf_entry[0]

		try:
			self.remove_nodes(ndf_entry, 'ndf:fitresults')
		except Exception as e:
			pass
			#print(e)


	#######################  Methods to set window limits  ###################################

	def set_window_min(self, window_min, spectra_id = 0, simulation_id=0):
		spectrum_entry= self.get_spectrum(spectra_id=spectra_id)
		# simulation_entry = self.create_tree_on_parent(['process','simulations', 'simulation'], spectrum_entry)
		simulation_entry = self.get_simulation(spectra_id=spectra_id, simulation_id = simulation_id)

		
		window_entry = self.create_tree_on_parent(['ndf','fitparameters','window'], simulation_entry, prefix = 'ndf:')
		attributes = {'units': 'channel'}
		self.change_node_value(window_min, window_entry, 'ndf:windowmin', attributes=attributes)


	def set_window_max(self, window_max, spectra_id = 0, simulation_id=0):
		spectrum_entry= self.get_spectrum(spectra_id=spectra_id)
		simulation_entry = self.get_simulation(spectra_id=spectra_id, simulation_id = simulation_id)

		
		window_entry = self.create_tree_on_parent(['ndf','fitparameters','window'], simulation_entry, prefix = 'ndf:')
		attributes = {'units': 'channel'}
		self.change_node_value(window_max, window_entry, 'ndf:windowmax', attributes=attributes)


						
	#######################  Methods to set beam fits  #######################################


	def set_beam_energy_fitparam(self, energy_change, spectra_id = 0, simulation_id = 0):
		if energy_change == 0:
			energy_change = ''

		spectrum_entry= self.get_spectrum(spectra_id=spectra_id)
		simulation_entry = self.get_simulation(spectra_id=spectra_id, simulation_id = simulation_id)
		# simulation_entry = self.create_tree_on_parent(['process','simulations', 'simulation'], spectrum_entry)
		
		beam_entry = self.create_tree_on_parent(['ndf','fitparameters','beam'], simulation_entry, prefix = 'ndf:')
		attributes = {'units': 'keV'}
		self.change_node_value(energy_change, beam_entry, 'ndf:beamenergy', attributes=attributes)
	
	def set_beam_energy_spread_fitparam(self, fwhm_change, spectra_id = 0, simulation_id = 0):
		spectrum_entry= self.get_spectrum(spectra_id=spectra_id)
		simulation_entry = self.get_simulation(spectra_id=spectra_id, simulation_id = simulation_id)

		
		beam_entry = self.create_tree_on_parent(['ndf','fitparameters','beam'], simulation_entry, prefix = 'ndf:')
		attributes = {'units': 'keV'}
		self.change_node_value(fwhm_change, beam_entry, 'ndf:beamenergyspread', attributes=attributes)


	def set_charge_fitparam(self, charge, spectra_id = 0, simulation_id=0):
		spectrum_entry= self.get_spectrum(spectra_id=spectra_id)
		simulation_entry = self.get_simulation(spectra_id=spectra_id, simulation_id = simulation_id)
		
		beam_entry = self.create_tree_on_parent(['ndf','fitparameters','beam'], simulation_entry, prefix = 'ndf:')
		
		self.change_node_value(charge, beam_entry, 'ndf:charge')

		
	#######################  Methods to set angles fits  #######################################    
		
	def set_incident_angle_fitparam(self, angle_change, spectra_id = 0, simulation_id = 0):
		spectrum_entry= self.get_spectrum(spectra_id=spectra_id)
		simulation_entry = self.get_simulation(spectra_id=spectra_id, simulation_id = simulation_id)
		
		geo_entry = self.create_tree_on_parent(['ndf','fitparameters','geometry'], simulation_entry, prefix = 'ndf:')
		attributes = {'units': 'degree'}
		self.change_node_value(angle_change, geo_entry, 'ndf:incidenceangle', attributes=attributes)
		
	def set_scattering_angle_fitparam(self, angle_change, spectra_id = 0, simulation_id = 0):
		spectrum_entry= self.get_spectrum(spectra_id=spectra_id)
		simulation_entry = self.get_simulation(spectra_id=spectra_id, simulation_id = simulation_id)
		
		geo_entry = self.create_tree_on_parent(['ndf','fitparameters','geometry'], simulation_entry, prefix = 'ndf:')
		attributes = {'units': 'degree'}
		self.change_node_value(angle_change, geo_entry, 'ndf:scatteringangle', attributes=attributes)
	 
	def set_exit_angle_fitparam(self, angle_change, spectra_id = 0, simulation_id = 0):
		spectrum_entry= self.get_spectrum(spectra_id=spectra_id)
		simulation_entry = self.get_simulation(spectra_id=spectra_id, simulation_id = simulation_id)
		
		geo_entry = self.create_tree_on_parent(['ndf','fitparameters','geometry'], simulation_entry, prefix = 'ndf:')
		attributes = {'units': 'degree'}
		self.change_node_value(angle_change, geo_entry, 'ndf:exitangle', attributes=attributes)
		
		
	#######################  Methods to set calibration fits  #######################################    
		
	
	
	def set_energy_calibration_fitparam(self, m_change, b_change, spectra_id = 0, simulation_id = 0):
		spectrum_entry= self.get_spectrum(spectra_id=spectra_id)
		simulation_entry = self.get_simulation(spectra_id=spectra_id, simulation_id = simulation_id)
		
		calib_entry = self.create_tree_on_parent(['ndf','fitparameters','calibrationparameters'], simulation_entry, prefix = 'ndf:')

		
		#remove old ones:
		try:
			self.remove_nodes(calib_entry, 'ndf:calibrationparameter')
		except:
			pass
		

		attributes = {
			'units': 'keV'
		}
		self.change_node_value(b_change, calib_entry, 'ndf:calibrationparameter', attributes = attributes)


		attributes = {
			'units': 'keV/channel'
		}
		self.change_node_value(m_change, calib_entry, 'ndf:calibrationparameter', attributes = attributes,
							  append = True)
		

	
	#######################  Methods to set solid angle fits  #######################################
	
	
	
	def set_detector_solid_angle_fitparam(self, angle_change, spectra_id = 0, simulation_id = 0):
		spectrum_entry= self.get_spectrum(spectra_id=spectra_id)
		simulation_entry = self.get_simulation(spectra_id=spectra_id, simulation_id = simulation_id)
		
		detector_entry = self.create_tree_on_parent(['ndf','fitparameters','detection','detector'], simulation_entry, prefix = 'ndf:')
		
		attributes = {
			'units': 'msr'
		}
		self.change_node_value(angle_change, detector_entry, 'ndf:solidangle', attributes = attributes)

	def set_detector_foil(self, material, thickness, spectra_id = 0, simulation_id = 0):
		spectrum_entry= self.get_spectrum(spectra_id=spectra_id)
		simulation_entry = self.get_simulation(spectra_id=spectra_id, simulation_id = simulation_id)
		
		foil_entry = self.create_tree_on_parent(['ndf','fitparameters','detection','detector', 'foil'], simulation_entry, prefix = 'ndf:')
		self.change_node_value(material, foil_entry, 'ndf:material')
		self.change_node_value(thickness, foil_entry, 'ndf:thickness')

	
	########################### To get parameters

	def get_window_min(self, spectra_id = 0, simulation_id = 0):
		spec = self.get_spectrum(spectra_id=spectra_id)  
		simulation_entry = self.get_simulation(spectra_id=spectra_id, simulation_id = simulation_id)    
		ndf_entry = get_xml_section(simulation_entry, 'ndf:ndf')
		if ndf_entry is None:
			return 100
		else:
			ndf_entry = ndf_entry[0]

		value, units = get_xml_entry(ndf_entry, 'ndf:windowmin', attribute='units')

		# if value is None:
		# 	return 1500

		return value or 100

	def get_window_max(self, spectra_id = 0, simulation_id = 0):
		spec = self.get_spectrum(spectra_id=spectra_id)        
		simulation_entry = self.get_simulation(spectra_id=spectra_id, simulation_id = simulation_id)    
		ndf_entry = get_xml_section(simulation_entry, 'ndf:ndf')

		if ndf_entry is None:
			return 1500
		else:
			ndf_entry = ndf_entry[0]

		value, units = get_xml_entry(ndf_entry, 'ndf:windowmax', attribute='units')

		# if value is None:
		# 	return 1500

		return value or 1500


	def get_beam_energy_fitparam(self, spectra_id = 0, simulation_id = 0):
		spec = self.get_spectrum(spectra_id=spectra_id)        
		simulation_entry = self.get_simulation(spectra_id=spectra_id, simulation_id = simulation_id)    
		ndf_entry = get_xml_section(simulation_entry, 'ndf:ndf')

		if ndf_entry is None:
			return None
		else:
			ndf_entry = ndf_entry[0]


		energy_value, energy_units = get_xml_entry(ndf_entry, 'ndf:beamenergy', attribute='units')

		if energy_value in ['', '0']: energy_value = None

		if energy_value != None:
			energy_value = float(energy_value)

			if energy_units == 'MeV':
				energy_value *= 1e3
			elif energy_units == 'meV':
				energy_value *= 1e-3
			elif energy_units == 'GeV':
				energy_value *= 1e6
		
		return energy_value
	
	def get_beam_energy_spread_fitparam(self, spectra_id = 0, simulation_id = 0):
		spec = self.get_spectrum(spectra_id=spectra_id)        
		simulation_entry = self.get_simulation(spectra_id=spectra_id, simulation_id = simulation_id)    
		ndf_entry = get_xml_section(simulation_entry, 'ndf:ndf')

		if ndf_entry is None:
			return None
		else:
			ndf_entry = ndf_entry[0]

		energy_value, energy_units = get_xml_entry(ndf_entry, 'ndf:beamenergyspread', attribute='units')
		
		if energy_value == '': energy_value = None

		if energy_value != None:
			energy_value = float(energy_value)

			if energy_units == 'MeV':
				energy_value *= 1e3
			elif energy_units == 'meV':
				energy_value *= 1e-3
			elif energy_units == 'GeV':
				energy_value *= 1e6
		
		return energy_value
	
	def get_incident_angle_fitparam(self, spectra_id=0, simulation_id = 0):
		spec = self.get_spectrum(spectra_id=spectra_id)        
		simulation_entry = self.get_simulation(spectra_id=spectra_id, simulation_id = simulation_id)    
		ndf_entry = get_xml_section(simulation_entry, 'ndf:ndf')

		if ndf_entry is None:
			return None
		else:
			ndf_entry = ndf_entry[0]
		
		value, units = get_xml_entry(ndf_entry, 'ndf:incidenceangle', attribute='units')
		

		return value

	def get_scattering_angle_fitparam(self, spectra_id=0, simulation_id = 0):
		spec = self.get_spectrum(spectra_id=spectra_id)        
		simulation_entry = self.get_simulation(spectra_id=spectra_id, simulation_id = simulation_id)    
		ndf_entry = get_xml_section(simulation_entry, 'ndf:ndf')

		if ndf_entry is None:
			return None
		else:
			ndf_entry = ndf_entry[0]
		
		value, units = get_xml_entry(ndf_entry, 'ndf:scatteringangle', attribute='units')
		

		return value

	def get_exit_angle_fitparam(self, spectra_id=0, simulation_id = 0):
		spec = self.get_spectrum(spectra_id=spectra_id)        
		simulation_entry = self.get_simulation(spectra_id=spectra_id, simulation_id = simulation_id)    
		ndf_entry = get_xml_section(simulation_entry, 'ndf:ndf')

		if ndf_entry is None:
			return None
		else:
			ndf_entry = ndf_entry[0]
		
		value, units = get_xml_entry(ndf_entry, 'ndf:exitangle', attribute='units')
		

		return value

	def get_angles_fitparam(self, spectra_id=0, simulation_id = 0):
		return [self.get_incident_angle_fitparam(spectra_id=spectra_id, simulation_id = simulation_id), self.get_scattering_angle_fitparam(spectra_id=spectra_id, simulation_id = simulation_id)] #, self.get_exit_angle_fitparam
	
	def get_charge_fitparam(self, spectra_id = 0, simulation_id = 0):
		spec = self.get_spectrum(spectra_id=spectra_id)        
		simulation_entry = self.get_simulation(spectra_id=spectra_id, simulation_id = simulation_id)    
		ndf_entry = get_xml_section(simulation_entry, 'ndf:ndf')

		if ndf_entry is None:
			return None
		else:
			ndf_entry = ndf_entry[0]
		
		value, units = get_xml_entry(ndf_entry, 'ndf:charge', attribute='units')
		
		return value

	def get_detector_solid_angle_fitparam(self, spectra_id = 0, simulation_id = 0):
		spec = self.get_spectrum(spectra_id=spectra_id)        
		simulation_entry = self.get_simulation(spectra_id=spectra_id, simulation_id = simulation_id)    
		ndf_entry = get_xml_section(simulation_entry, 'ndf:ndf')

		if ndf_entry is None:
			return None
		else:
			ndf_entry = ndf_entry[0]
		
		value, units = get_xml_entry(ndf_entry, 'ndf:solidangle', attribute='units')
		
		return value

	def get_detector_foil(self, spectra_id = 0, simulation_id = 0):
		spec = self.get_spectrum(spectra_id=spectra_id)        
		simulation_entry = self.get_simulation(spectra_id=spectra_id, simulation_id = simulation_id)    
		ndf_entry = get_xml_section(simulation_entry, 'ndf:ndf')

		if ndf_entry is None:
			return [None, None]
		else:
			ndf_entry = ndf_entry[0]
		
		foil_entry = get_xml_section(ndf_entry, 'ndf:foil')
		if foil_entry is None : return [None, None]
		else: foil_entry = foil_entry[0]

		value = get_xml_entry(foil_entry, 'ndf:material')
		thickness = get_xml_entry(foil_entry, 'ndf:thickness')

		if value == '': value = None
		if thickness == '': thickness = None
		
		return [value, thickness]


	
	def get_energy_calibration_fitparam(self, spectra_id = 0, simulation_id = 0):
		spec = self.get_spectrum(spectra_id=spectra_id)        
		simulation_entry = self.get_simulation(spectra_id=spectra_id, simulation_id = simulation_id)    
		ndf_entry = get_xml_section(simulation_entry, 'ndf:ndf')

		if ndf_entry is None:
			return [None, None]
		else:
			ndf_entry = ndf_entry[0]
		
		fit_param = get_xml_section(ndf_entry, 'ndf:fitparameters')
		if fit_param is None:
			return [True, True]
		else:
			fit_param = fit_param[0]

		param = get_xml_section(fit_param, 'ndf:calibrationparameter')

		if param is None:
			return [True, True]

		if None in [p.firstChild for p in param]:
			return [True, True]

		return [param[0].firstChild.nodeValue, param[1].firstChild.nodeValue]

		
		
		# if param[0].getAttribute('units') == 'keV':
		# 	param_b = float(param[0].firstChild.nodeValue)
		# 	param_m = float(param[1].firstChild.nodeValue)
		# else:
		# 	param_m = float(param[0].firstChild.nodeValue)
		# 	param_b = float(param[1].firstChild.nodeValue)


		# return [param_m, param_b]



	####################  Methods to set and get fitting/sim models  ####################################

	def set_model_pileup(self, model, parameters, spectra_id = 0, simulation_id = 0):
		spectrum_entry= self.get_spectrum(spectra_id=spectra_id)        
		simulation_entry = self.get_simulation(spectra_id=spectra_id, simulation_id = simulation_id)
		

		models_entry = self.create_tree_on_parent(['ndf','fitparameters','models'], simulation_entry, prefix = 'ndf:')
		
		attributes = {'parameter': str(parameters)}
		self.change_node_value(model, models_entry, 'ndf:pileup', attributes = attributes)

	def get_model_pileup(self, spectra_id = 0, simulation_id = 0):
		spec = self.get_spectrum(spectra_id=spectra_id)    
		simulation_entry = self.get_simulation(spectra_id=spectra_id, simulation_id = simulation_id)    
		ndf_entry = get_xml_section(simulation_entry, 'ndf:ndf')

		if ndf_entry is None:
			return [None, None, None]
		else:
			ndf_entry = ndf_entry[0]

		model, parameter = get_xml_entry(ndf_entry, 'ndf:pileup', attribute='parameter')
		
		if (model is None) or (model ==''):
			code = None
		else:
			code = model.split('(')[-1]
			code = 'pile ' + code[:2]
		

		return code, parameter, model


	def set_model_doublescatter(self, model, parameters, spectra_id = 0, simulation_id = 0):
		spectrum_entry= self.get_spectrum(spectra_id=spectra_id)
		simulation_entry = self.get_simulation(spectra_id=spectra_id, simulation_id = simulation_id)

		models_entry = self.create_tree_on_parent(['ndf','fitparameters','models'], simulation_entry, prefix = 'ndf:')
		
		attributes = {'parameter': str(parameters)}
		self.change_node_value(model, models_entry, 'ndf:doublescatter', attributes = attributes)

	def get_model_doublescatter(self, spectra_id = 0, simulation_id = 0):
		spec = self.get_spectrum(spectra_id=spectra_id)        
		simulation_entry = self.get_simulation(spectra_id=spectra_id, simulation_id = simulation_id)    
		ndf_entry = get_xml_section(simulation_entry, 'ndf:ndf')

		if ndf_entry is None:
			return [None, None, None]
		else:
			ndf_entry = ndf_entry[0]

		model, parameter = get_xml_entry(ndf_entry, 'ndf:doublescatter', attribute='parameter')
		
		if (model is None) or (model == ''):
			code = None
		else:
			code = 'ds ' + model
		

		return code, parameter, model
	
	
	def set_model_straggling(self, model, parameters, spectra_id = 0, simulation_id = 0):
		spectrum_entry= self.get_spectrum(spectra_id=spectra_id)
		simulation_entry = self.get_simulation(spectra_id=spectra_id, simulation_id = simulation_id)

		models_entry = self.create_tree_on_parent(['ndf','fitparameters','models'], simulation_entry, prefix = 'ndf:')
		
		attributes = {'parameter': str(parameters)}
		self.change_node_value(model, models_entry, 'ndf:straggling', attributes = attributes)

	
	def get_model_straggling(self, spectra_id = 0, simulation_id = 0):
		spec = self.get_spectrum(spectra_id=spectra_id)        
		simulation_entry = self.get_simulation(spectra_id=spectra_id, simulation_id = simulation_id)    
		ndf_entry = get_xml_section(simulation_entry, 'ndf:ndf')

		if ndf_entry is None:
			return [None, None, None]
		else:
			ndf_entry = ndf_entry[0]

		model, parameter = get_xml_entry(ndf_entry, 'ndf:straggling', attribute='parameter')
		
		if (model is None) or (model ==''):
			code = None
		else:
			code = model.split('(')[-1]
			code = model.split(' ')[0]



		return code, parameter, model


	def set_model_energyloss(self, model, spectra_id = 0, simulation_id = 0):
		spectrum_entry= self.get_spectrum(spectra_id=spectra_id)
		simulation_entry = self.get_simulation(spectra_id=spectra_id, simulation_id = simulation_id)

		models_entry = self.create_tree_on_parent(['ndf','fitparameters','models'], simulation_entry, prefix = 'ndf:')
		
		# attributes = {'parameter': parameters}
		self.change_node_value(model, models_entry, 'ndf:energyloss')

	
	def get_model_energyloss(self, spectra_id = 0, simulation_id = 0):
		spec = self.get_spectrum(spectra_id=spectra_id)        
		simulation_entry = self.get_simulation(spectra_id=spectra_id, simulation_id = simulation_id)    
		ndf_entry = get_xml_section(simulation_entry, 'ndf:ndf')

		if ndf_entry is None:
			return [None, None, None]
		else:
			ndf_entry = ndf_entry[0]

		model = get_xml_entry(ndf_entry, 'ndf:energyloss')

		if (model is None) or (model == ''):
			code = None
		else:
			code = model.replace('(','').replace(')','').split(' ')[-1]
		parameter = ''



		return code, parameter, model


	def set_model_adhoc_correction(self, element, parameters, spectra_id = 0, simulation_id = 0):
		# spectrum_entry= self.get_spectrum(spectra_id=spectra_id)
		simulation_entry = self.get_simulation(spectra_id=spectra_id, simulation_id = simulation_id)

		models_entry = self.create_tree_on_parent(['ndf','fitparameters','models'], simulation_entry, prefix = 'ndf:')
		
		attributes = {'parameter': str(parameters)}
		self.change_node_value(element, models_entry, 'ndf:adhoc-correction', attributes = attributes)

	
	def get_model_adhoc_correction(self, spectra_id = 0, simulation_id = 0):
		# spec = self.get_spectrum(spectra_id=spectra_id)        
		simulation_entry = self.get_simulation(spectra_id=spectra_id, simulation_id = simulation_id)    
		ndf_entry = get_xml_section(simulation_entry, 'ndf:ndf')

		if ndf_entry is None:
			return [None, None, None]
		else:
			ndf_entry = ndf_entry[0]

		# model is in fact the element
		model, parameter = get_xml_entry(ndf_entry, 'ndf:adhoc-correction', attribute='parameter')
		
		if (model is None) or (model == ''):
			code = None
		else:
			code = model

		return code, parameter, model

	def set_rutherford_cross(self, rutherford_bol, ebsfile_path, spectra_id = 0, simulation_id = 0):
		simulation_entry = self.get_simulation(spectra_id=spectra_id, simulation_id = simulation_id)

		cross_section = self.create_tree_on_parent(['ndf','fitparameters','models', 'crossection'], simulation_entry, prefix = 'ndf:')
		cross_section_file_entry = self.create_tree_on_parent(['crossectionfile'], cross_section, prefix = 'ndf:')
		
		self.change_node_value(rutherford_bol, cross_section, 'ndf:Rutherford')
		self.change_node_value(ebsfile_path, cross_section_file_entry, 'ndf:filename')
		self.change_node_value(ebsfile_path.split('/')[-1].split('.')[-1], cross_section_file_entry, 'ndf:fileformat')
		


	def get_rutherford_cross(self, spectra_id = 0, simulation_id = 0):
		simulation_entry = self.get_simulation(spectra_id=spectra_id, simulation_id = simulation_id)    
		ndf_entry = get_xml_section(simulation_entry, 'ndf:ndf')

		if ndf_entry is None:
			return [None, None, None]
		else:
			ndf_entry = ndf_entry[0]

		cross_entry = get_xml_section(ndf_entry, 'ndf:crossection')
		if cross_entry is None : return [None, None]
		else: cross_entry = cross_entry[0]

		rutherford_bol = get_xml_entry(cross_entry, 'ndf:Rutherford')
		ebsfile_path = get_xml_entry(cross_entry, 'ndf:filename')

		if rutherford_bol == '': rutherford_bol = True
		if ebsfile_path == '': ebsfile_path = None
		
		return [rutherford_bol == 'True', ebsfile_path]

	####################  Methods for the NDF flags  ############################################

	def set_NDF_run_option(self, option_name, option, spectra_id = 0, simulation_id = 0):
		spectrum_entry= self.get_spectrum(spectra_id=spectra_id) 
		simulation_entry = self.get_simulation(spectra_id=spectra_id, simulation_id = simulation_id)

		runoptions_entry = self.create_tree_on_parent(['ndf','fitparameters','runoptions'], simulation_entry, prefix = 'ndf:')
		
		self.change_node_value(option, runoptions_entry, 'ndf:' + option_name)

	def get_NDF_run_option(self, option_name, spectra_id = 0, simulation_id = 0):
		spec = self.get_spectrum(spectra_id=spectra_id)        
		simulation_entry = self.get_simulation(spectra_id=spectra_id, simulation_id = simulation_id)    
		ndf_entry = get_xml_section(simulation_entry, 'ndf:ndf')

		if ndf_entry is None:
			return [None, None]
		else:
			ndf_entry = ndf_entry[0]

		
		options_entry = get_xml_section(ndf_entry, 'ndf:runoptions')
		if options_entry is None: return [None, None]

		option = get_xml_entry(ndf_entry, 'ndf:' + option_name)

		if option is None:
			code = [None, None]
		else:
			code = option.split()[0]

		return code, option




	def get_fit_results_entry(self, spectra_id = 0, simulation_id = 0):
		# spectrum_entry = self.get_spectrum(spectra_id=spectra_id)
		simulation_entry = self.get_simulation(spectra_id=spectra_id, simulation_id=simulation_id)
		if simulation_entry is None: return None

		ndf_entry = get_xml_section(simulation_entry, 'ndf:ndf')
		if ndf_entry is None: return None
		else: ndf_entry = ndf_entry[0]

		ndf_results = get_xml_section(simulation_entry, 'ndf:fitresults')

		if ndf_results is None: return None
		else: ndf_results = ndf_results[0]
		
		return ndf_results

	
	def set_spectra_result(self, spectra_id = 0):
		for i in range(len(self.get_reactions(spectra_id = spectra_id))):
			sim_group, file_id, _ = self.get_simulation_group(spectra_id = spectra_id, simulation_id = i)
			if sim_group == -1:
				return

			# load total fit
			res_filename = '%sf%s.dat' %(self.file_name[:3], file_id)
			data_x, data_y_given, data_y_fit = read_spectra_fit_file(self.path_dir + res_filename)

			self.set_spectrum_data_fit_result(data_x, data_y_fit, spectra_id = spectra_id, simulation_id = i)


			# load elemental fits
			try:
				rese_filename = '%sx%s.dat' %(self.file_name[:3], file_id)
				data_ele = read_elemental_spectra_fit_file(self.path_dir + rese_filename)
			except Exception as e:
				data_ele = None

			self.set_elemental_spectrum_data_fit_result(data_ele, spectra_id = spectra_id, simulation_id = i)
			


	def set_geometry_result(self, spectra_id = 0):
		for i in range(len(self.get_reactions(spectra_id = spectra_id))):
			sim_group, file_id, _ = self.get_simulation_group(spectra_id = spectra_id, simulation_id = i)
			if sim_group == -1:
				return

			res_filename = '%sg%s.geo' %(self.file_name[:3], file_id)
			res_filename = self.path_dir + res_filename

			with open(res_filename, 'r') as file:
				data = file.readlines()
			

			self.set_data_from_geo_file(res_filename, type_data = 'result', spectra_id = spectra_id, simulation_id = i)

		spc_file = self.file_name.split('.')[0] + '.spx'
		self.set_data_from_spc_file(self.path_dir + spc_file)

	def set_elements_result(self, spectra_id = 0):
		sim_group, file_id, _ = self.get_simulation_group(spectra_id = spectra_id)
		if sim_group == -1:
			return

		res_filename = '%ss%s.str' %(self.file_name[:3], file_id[:2])

		res_filename = self.path_dir + res_filename

		with open(res_filename, 'r') as file:
			data = file.readlines()
		
		self.set_data_from_str_file(res_filename, spectra_id = spectra_id)


	def set_profile_result(self, spectra_id = 0):
		sim_group, file_id, _ = self.get_simulation_group(spectra_id = spectra_id)
		if sim_group == -1:
			return

		res_filename = '%s%s.prf' %(self.file_name[:3], file_id[:2])
		res_filename = self.path_dir + res_filename
		
		self.set_data_from_prf_file(res_filename, spectra_id = spectra_id, simulation_id  = 0)


	
## Methods to write input files
	
	def write_dataxy(self, name = '', mode = 19, spectra_id = 0, simulation_id = 0, path_dir = ''):
		# modes correspond to the NDF file format index, 19 is double column with channels vs counts
		if name == '':
			name = '%s%i.dat' %(self.name, spectra_id+1)
		else:
			name = name

		technique = self.get_technique(spectra_id=spectra_id)
		if technique in ['RBS', 'NRA', 'ERDA', None]:
			xx, yy = self.get_dataxy(spectra_id=spectra_id)

			data = nparray([xx, yy])
			data = data.T

			savetxt(path_dir + name, data, delimiter='  ', fmt=' %i   %f')
		elif technique == 'PIXE':
			data = self.get_PIXE_file(spectra_id=spectra_id)
			with open(path_dir + name, 'w') as file:
				file.write(data)

		print('\n----------- ' + name + ' -----------')
		print(data)
		

		#save file name to input in spc file
		self.dataxy_files.append(name)

		#save the simulation group to input in spc file
		group, _, charge = self.get_simulation_group(spectra_id = spectra_id, simulation_id=simulation_id)
		self.simulation_group.append(group)
		self.shared_charge.append(charge)

		
	def write_geo(self, spectra_id = 0, path_dir = ''):
		# list of parameters fixed for each spectrum (i.e. constant to all reactions)
		pairs_fitparam = {
			'beam_energy': self.get_beam_energy_fitparam,
			'beam_FWHM': self.get_beam_energy_spread_fitparam,
			'angles': self.get_angles_fitparam,
			'dect_solid': self.get_detector_solid_angle_fitparam,
		}

		params = self.get_geo_parameters(spectra_id = spectra_id)

		#save some of the parameters to recover in the future
		beam_energy = params['beam_energy']
		beam_FWHM = params['beam_FWHM']
		angles = params['angles']
		dect_solid = params['dect_solid']
		
		reactions = self.get_reactions(spectra_id = spectra_id)
		technique = self.get_technique(spectra_id = spectra_id)
		
		names = []
		for i,r in enumerate(reactions):
			params['energy_calib'] = self.get_energy_calibration(spectra_id = spectra_id, reaction_id = i)
			params['window'] = [self.get_window_min(spectra_id = spectra_id, simulation_id = i), self.get_window_max(spectra_id = spectra_id, simulation_id = i)]
			foil_params = self.get_detector_foil(spectra_id = spectra_id, simulation_id = i)
			if None not in foil_params:
				params['foil'] = 'foil ' + foil_params[1] + '\n' + foil_params[0].split('-')[1].strip()

			rutherford_params = self.get_rutherford_cross(spectra_id = spectra_id, simulation_id = i)
			if None not in rutherford_params:
				if not rutherford_params[0]:
					params['rutherford'] = 'ebsfiles ' + rutherford_params[1]




			params['beam_energy'] = beam_energy
			params['beam_FWHM'] = beam_FWHM
			params['angles'] = angles
			params['dect_solid'] = dect_solid

			if technique == 'NRA' and r['initialtargetparticle'] is not None:
				params['projectile'] = [r['initialtargetparticle'] + ' ' + r['incidentparticle'] + ' ' + r['finaltargetparticle'] + ' ' + r['exitparticle'] + ' ' + r['reactionQ'],
										r['exitparticle']]
			elif technique == 'PIXE':
				params['projectile'] = [r['incidentparticle'], 'X']
				params['mode'] = 28
				
				# write calibration file
				with open(path_dir + params['energy_calib'][0], 'w') as file:
					file.write(''.join(params['energy_calib'][1]))
				params['energy_calib'] = params['energy_calib'][0]                     
			else:
				params['projectile'] = [r['incidentparticle'], r['exitparticle']]
			
			
			for k,p in pairs_fitparam.items():
				value = p(spectra_id = spectra_id, simulation_id = i)
					
				if isinstance(value, list):
					if None not in value:
						params[k] = '%s %s %s %s' %(params[k][0], params[k][1], value[0], value[1])
				elif value is not None:
					if k == 'beam_FWHM':
						# add zeros for so that the FWHM is linear (pag. 29 of manual)
						params[k] = '%s 0 %s 0' %(params[k], value)
					else:
						params[k] = '%s %s' %(params[k], value)
				


			pairs_model = {
				'pileup':self.get_model_pileup,
				'double_scatter': self.get_model_doublescatter,
				'straggling': self.get_model_straggling,
				'energy_loss': self.get_model_energyloss,
				'adhoc-correction': self.get_model_adhoc_correction
			}

			for k,m in pairs_model.items():
				code,param,_ = m(spectra_id = spectra_id, simulation_id = i)

				if (code is None):
					continue


				if k != 'adhoc-correction':
					params[k] =  '%s %s' %(code, param)
				else:
					params[k] =  '%s\n%s' %(code, param)


			calibration = self.get_energy_calibration_fitparam(spectra_id = spectra_id, simulation_id = i)
			charge = self.get_charge_fitparam(spectra_id = spectra_id, simulation_id = i)

			params['energy_calib_m'] = 'flagvar_conv on'
			params['energy_calib_b'] = 'flagvar_offset on'
			params['charge'] = 'flagvar_charge on'

			if calibration[0] == 'False':
				params['energy_calib_m'] = 'flagvar_conv off'
			if calibration[1] == 'False':
				params['energy_calib_b'] = 'flagvar_offset off'
			if charge == 'False':
				params['charge'] = 'flagvar_charge off'


			name = '%s_spec%i-%i_%s.geo' %(self.name, spectra_id+1, i, r['exitparticle'])
			with open(path_dir + name, 'w') as file:
				print('\n----------- ' + name + ' -----------')
				for key, param in params.items():
					if isinstance(param, list):
						param = [str(p) for p in param]
						file.write(' '.join(param) + '\n')
						print(' '.join(param) + '\t\t\t ' + key)
					else:
						file.write(str(param) + '\n')
						print(str(param) + '\t\t\t ' + key)

			#save file name to input in spc file
			names.append(name)
		
		self.geo_files.append(names)
			

		return name


		
	def write_str(self, path_dir = ''):        
		params = {
			'min_max_thick' : 0, #[Min, Max] 1e15 at/cm2
			'n_elements': None,
			'elements':{                
				#name, dentsity 1e22 at/cm2
				#depth range 1e15 at/cm2
				#concentration range 0 to 1				
			}            
		}
		
		max_thickness = self.get_max_thickness()
		if max_thickness == '0' or max_thickness is None:
			params['min_max_thick'] = self.get_min_thickness()
		else:
			params['min_max_thick'] = [self.get_min_thickness(), self.get_max_thickness()]
		params['n_elements'] = self.get_nelements()
		params['elements'] = self.get_elements()
		
		#transform elements dic into string
		string_ele = ''
		for key, param in params['elements'].items():
			if key == 'nelements':
				continue
			 # print(key, param)
			string_ele += param['name'] + ' ' + str(param['density']) + '\n'
			
			p = [str(p1) for p1 in param['depth']]
			string_ele += ' '.join(p) + '\n'
			p = [str(p1) for p1 in param['concentration']]
			string_ele += ' '.join(p) + '\n'
			
			
		
		params['elements'] = string_ele
		
		name = '%s.str' %(self.name)
		with open(path_dir + name, 'w') as file:
			print('\n----------- ' + name + ' -----------')
			for key, param in params.items():
				if isinstance(param, list):
					param = [str(p) for p in param]
					file.write(' '.join(param) + '\n')
					print(' '.join(param) + '\t\t ' + key)
				else:
					file.write(str(param) + '\n')
					print(str(param) + '\t\t ' + key)

		#save file name to input in spc file
		self.str_files.append(name)

		return name


		
		
	def write_prf(self, path_dir = ''):        
		params = {
			'n_layers' : 1,
			'layers':{}
		}
		
		
		# get number of layers
		params['n_layers'] = self.get_nlayers()#get_xml_entry(layers_entry, 'nlayers')
		
		# get layers
		params['layers'] = self.get_profile()
		
		if params['layers'] is None:
			print('Layer definition missing from file, prf file not written')
			self.prf_files.append(None)
			return None
		
		# name = '%s.prf' %(self.name)
		name = 'ndf.prf'
		with open(path_dir + name, 'w') as file:
			file.write(str(params['n_layers']) + '\n')
			for key, param in params['layers'].items():
				if key in ['nlayers', 'names']:
					continue
				string_ele = param['thickness'] + ' '
				conce_string = [str(p) for p in param['concentrations']]
				string_ele += ' '.join(conce_string) + '\n'

				file.write(string_ele)
		
		# print out file to verify
		with open(path_dir + name, 'r') as file:         
			print('\n----------- ' + name + ' -----------')
			for l in file.readlines():
				print(l, end='')
		 
		#save file name to input in spc file
		self.prf_files.append(name)

		return name
		
	def write_spc(self, path_dir = ''):
		name = '%s.spc' %(self.name)
		print('\n----------- ' + name + ' -----------')

		# sort data / simulation group
		simulation_group_sorted = sorted(range(len(self.simulation_group)), key=lambda k: self.simulation_group[k])
		simulation_group_normalized = normalize_list(self.simulation_group)

		charge = self.get_charge()
		with open(path_dir + name, 'w') as file:
			group_before = -1
			nspectra_group = 0
			line = 0
			main_file_line = 0
			
			for i in simulation_group_sorted:
				if self.simulation_group[i] == -1:
					continue
					
				d = self.dataxy_files[i]
				
				for j in range(len(self.get_reactions(spectra_id = i))):
					line += 1
					if self.simulation_group[i] != group_before:
						strf = self.str_files[0].split('.')[0]
						line = 1
						if j == 0:
							main_file_line = line
					elif j == 0:
						if self.shared_charge[i]:
							strf = '[1]'
						else:
							strf = ''
						main_file_line = line
					else:
						strf = '(%i)'%main_file_line

					g = self.geo_files[i][j]
					geo = g.split('.')[0]
					# strf = self.str_files[0].split('.')[0] 
					file.write('%s %s %s %s\n' %(d, charge, geo, strf))
					print('%s %s %s %s\n' %(d, charge, geo, strf))


					# save file id for reading NDF outputs afterwards
					id = ''
					if simulation_group_normalized[i] < 10:
						id = '0'
					id += '%i'%simulation_group_normalized[i]
					if line < 10:
						id += '0'
					id += '%i'%(line)

					simulation_entry = self.get_simulation(spectra_id=i, simulation_id = j)		
					ndf_entry = self.get_section(simulation_entry, 'ndf:ndf', create_if_not_found=['ndf:ndf'])[0]
					attributes = {'id': id}
					self.change_node_value(self.simulation_group[i], ndf_entry, 'ndf:simulationgroup', attributes = attributes)


					group_before = self.simulation_group[i]


		self.spc_files.append(name)

		# save idf file to save the NDF files ids
		self.save_idf(path_dir + self.file_name)

		return name


	def export_ndf_inputs(self, path_dir = ''):
		self.dataxy_files = []
		self.geo_files = []
		self.str_files = []
		self.prf_files = []
		self.spc_files = []
		self.simulation_group = []
		self.shared_charge = []

		
		nspectra = self.get_number_of_spectra()

		if nspectra == 1: 
			print('Opening %s (%s spectrum):\n' %(self.name, nspectra))
		else:
			print('Opening %s (%s spectra):\n' %(self.name, nspectra))

		print(self.user + '\n')
		print('')

		for l in self.description:
			print(l)


		for i in range(self.get_number_of_spectra()):
			print('\n\n ==============  Spectrum  %i ==============' %(i+1))

			self.write_dataxy(path_dir = path_dir, spectra_id = i)
			self.write_geo(path_dir = path_dir, spectra_id = i)
	
		print('\n\n ==============  General Files ==============')

		self.write_str(path_dir = path_dir)
		self.write_prf(path_dir = path_dir)
		self.write_spc(path_dir = path_dir)

		return {
			'dataxy_files' : self.dataxy_files,
			'geo_files' : self.geo_files,
			'str_files' : self.str_files,
			'prf_files' : self.prf_files,
			'spc_files' : self.spc_files
		}




def read_spectra_fit_file(spectra_file):
	data = loadtxt(spectra_file, skiprows = 7)

	data_x = data[:,0]
	data_y_given = data[:,1]
	data_y_fit = data[:,2]
	
	return data_x, data_y_given, data_y_fit

def read_elemental_spectra_fit_file(spectra_file):
	"""
	Returns:
		A dictionary of the form:
		data = {'x': array([]),
				'element1': array([]),
				'element2': array([]),
				'...'     : array([]),
				'extra'   : array([])}
	"""

	with open(spectra_file, 'r') as file:
		for _ in range(5):
			file.readline()
		
		names = file.readline().split()
	names.append('extra')    
	
	data_raw = genfromtxt(spectra_file, skip_header=7, skip_footer=1)
	data_raw = data_raw.T
	
	data = {'x':data_raw[0]}
	   
	for n,y in zip(names, data_raw[1:]):
		data[n] = y

	return data


def read_geo_file(geo_file):
	params = {}
	with open(geo_file, 'r') as file:
		lines = file.readlines()
		
		energy_params = lines[3].split()
		FWHM_params = lines[4].split()
		angles_params = lines[6].split()
		solidangle_params = lines[7].split()
		
		params['energy'] = energy_params[0]
		params['FWHM'] = FWHM_params[0]
		params['geometry_type'] = lines[5].split()[0]
		params['angles'] = angles_params[0:2]
		params['solidangle'] = solidangle_params[0]
		params['calibration'] = lines[8].split()[0:2]

		params['window'] = lines[1].split()[-2:]
		if len(energy_params)>1:
			params['energy_fitparam'] = energy_params[1]
		if len(FWHM_params)>1:
			params['energy_spread_fitparam'] = FWHM_params[1]
		if len(angles_params)>2:
			params['incident_angle_fitparam'] = angles_params[2]
			params['scattering_angle_fitparam'] = angles_params[3]
		if len(solidangle_params)>1:
			params['solid_angle_fitparam'] = solidangle_params[1]
			
		
			
		for l in lines:
			p = l.split()
			p = [i.lower() for i in p]
			
			if len(p) == 0:
				continue
				
			code = p[0]
			if code == 'pile':
				if p[1] == 'mg':
					model = 'Molodstov and Gurbich (MG - slow)'
				elif p[1] == 'wg':
					model = 'Wielopolski and Gardner (WG - slow)'
				elif p[1] == 'cj':
					model = 'Pure Autocorrelation Algorithm (CJ - fast)'
				elif p[1] == 'ga':
					model = 'Amsel (GA - fast)'
					
				params['pileup_model'] = {'model': model, 'parameter': p[2]}
				continue
				
			if code == 'ds':
				model = p[1]
				if len(p) ==2:
					parameter = '1'
				else:
					parameter = p[2]
					
				params['double_scattering_model'] = {'model': model, 'parameter': parameter}
				continue
			
			if code in ['chu', 'borh']:
				model = code
				parameter = p[1]
				
				params['straggling_model'] = {'model': model, 'parameter': parameter}
				continue
				
			if code in ['zbl00', 'zbl90', 'mstar', 'sr03']:
				if code == 'zbl00':
					model = 'ZBL2000 (ZBL00)'
				elif code == 'zbl90':
					model = 'ZBL1990 (ZBL90)'
				elif code == 'mstar':
					model = 'MSTAR (MSTAR)'
				elif code == 'sr03':
					model = 'SRIM 2003 (SR03)'
				 
				params['stoploss_model'] = model
				continue
				
				
		
		
		reaction_line = lines[2].split()
		reaction_line = [capitalize_atom(r) for r in reaction_line]
		
		if len(reaction_line) == 2:
				
			reactions_dic = {
				'initialtargetparticle': '',
				'incidentparticle': reaction_line[0],
				'exitparticle': reaction_line[1],
				'finaltargetparticle': '',
				'reactionQ' : ''
			}
			params['reactions'] = reactions_dic
			
		elif len(reaction_line) == 6:
			reactions_dic = {
				'initialtargetparticle': reaction_line[0],
				'incidentparticle': reaction_line[1],
				'exitparticle': reaction_line[3],
				'finaltargetparticle': reaction_line[2],
				'reactionQ' : reaction_line[4]
			}
			params['reactions'] = reactions_dic
		else:
			print('Reaction not recognized in geo file')

	return params


def read_prf_file(prf_file):
	params = {}
	# params_elements = self.get_elements_fit_result()
		# params_elements.pop('nelements')
	
	is_elements_lines = False
	names = []
	with open(prf_file, 'r') as file:
		lines = file.readlines()
		params['nlayers'] = lines[0].rstrip().lstrip()
		
		for i in range(int(params['nlayers'])):
			values = lines[1 + i].rstrip().lstrip().split()
			concentrations = [round(float(c), 3) for c in values[1:]]
			thickness = round(float(values[0]), 3)
			
			params[i] = {
				'thickness':thickness,
				'concentrations':concentrations
			}

		for line in lines:
			if 'NDF' in line:
				break

			if is_elements_lines:
				name = line.split()[1].replace('?=', '')
				name = uniformize_element_name(name)
				names.append(name)

			if 'molecules ' in line:
				is_elements_lines = True
					


				
	params['names'] = names
	return params



def read_spc_file(spc_file, spectra_id = 0):
	params = {}
	with open(spc_file, 'r') as file:
		lines = file.readlines()
		line = lines[spectra_id].split()
		params['initial data'] = line[0]
		params['charge'] = line[1]
		params['fit data'] = line[2]
		params['fit geo'] = line[3]

	return params


def read_str_file(str_file):
	params = {}

		
	with open(str_file, 'r') as file:
		lines = file.readlines()
		params['nelements'] = lines[1].rstrip().lstrip().replace('?=', '')

		for i in range(int(params['nelements'])):
			name = lines[2 + 3*i].rstrip().lstrip().replace('?=', '').split()
			depths = lines[3 + 3*i].split()
			concentrations = lines[4 + 3*i].split()


			
			if (len(name) == 2) and check_its_number(name[-1]):# and name[-1].isnumeric():
				density = name[-1]
				name = name[:-1]
			elif check_its_number(name[-1]) and check_its_number(name[-2]):
				density = name[-1]
				name = name[:-1]
			else:
				density = ''
		
			
			if 's' in concentrations:
				concentrations.append('')
				

			params[i] = {'name': uniformize_element_name(' '.join(name)),
						 'density':density,
						 'concentration': [concentrations[0], concentrations[1]],
						 'depth': [depths[0], depths[1]]
						}
			
			
	return params


 # added ad-hoc, should be implemented on its on class!

from subprocess import Popen
from os import getcwd
from platform import platform
from time import sleep


def run_ndf(idf_file, close_window = False):
	print('Opening NDF...')

	# self.save()

	OSname = platform()
	if 'Linux' in OSname:
		run_ndf_linux(idf_file, close_window = close_window)
	elif 'Windows' in OSname:
		run_ndf_windows(idf_file, close_window = close_window)


def run_ndf_windows(idf_file, close_window = False):
	shell = 'start cmd.exe /c'
	ndf_path = '\\codes\\NDF_11_MS\\NDF.exe'

	# get flags:
	options = ['fitmethod','channelcompreesion','convolute','distribution','smooth','normalisation']
	code = []					
	for o in options:			
		code.append(idf_file.get_NDF_run_option(o)[0])

	ndf_flags = ' '.join(code)

	path = idf_file.path_dir
	file = idf_file.file_name

	cwd = idf_file.executable_dir
	cmd = cwd + ndf_path + ' ' + file + ' ' + ndf_flags
	path_bat = path + 'ndf.bat'

	with open(path_bat,'w') as file:
		file.write('@echo off \n')
		file.write('cd ' + path + '\n')
		file.write('echo \'Run started...\' > run_status.res \n')
		file.write(cmd + '\n\n\n')
		file.write('echo \'Finished\' > run_status.res \n')
		file.write('echo \n')
		file.write('echo Press enter to close:\n')
		if close_window == False:
			file.write('pause >null')

	run = Popen(shell + ' ' + path_bat, shell = True)#, text=True) #
	
def run_ndf_linux(idf_file, close_window = False):
	shell = 'gnome-terminal'
	wine = 'wine'
	ndf_path = 'codes/NDF_11_MS/NDF.exe'

	# get flags:
	options = ['fitmethod','channelcompreesion','convolute','distribution','smooth','normalisation']
	code = []					
	for o in options:
		op = idf_file.get_NDF_run_option(o)[0]	
		if op == None:
			print('%s no set, default used (0)' %o)
			op = '0'
		code.append(op)

	if None in code:
		print('No NDF run options set')
		return
	else:
		ndf_flags = ' '.join(code)


	path = idf_file.path_dir	
	file = idf_file.file_name

	if path in ['/', '']:
		path = '.'

	cwd = idf_file.executable_dir
	cmd = wine + ' ' + cwd + ndf_path + ' ' + file + ' ' + ndf_flags
	path_bat = path + 'ndf.bat'
	
	with open(path_bat,'w') as file:
		file.write('cd ' + path + '\n')
		file.write('echo \'Run started...\' > run_status.res \n')
		file.write(cmd + '\n')
		file.write('echo \'Finished\' > run_status.res \n')
		file.write('echo \'\n\nPress enter to close:\'\n')
		if close_window == False:
			file.write('read line')

	run = Popen(shell + ' -- bash ' + path_bat, shell = True)#, text=True) #


def check_simulations_running(idf_file, block = False):
	while True:
		sleep(1)	
		try:
			with open(idf_file.path_dir + 'run_status.res') as file:
				status = file.readline()
				running_state = 'Run' in status
		except:
			running_state = False

		if not block or not running_state:
			print('Finished')
			break
		else:
			print('.', end = '')


	return running_state