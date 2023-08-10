from re import search
from numpy import loadtxt, reshape, genfromtxt, array as nparray, arange
from fractions import Fraction


def get_xml_section(file, keyword):
	parent = file.getElementsByTagName(keyword)

	if len(parent)>0:
		return parent
	else:
		# print('%s entry missing' %keyword)
		return


def get_xml_entry(parent, keyword, attribute = ''):
	entry = parent.getElementsByTagName(keyword)

	if not entry: # check if list is empty
		# print('%s entry missing' %keyword)
		if attribute != '':
			return None, None
		return
	
	entry = entry[0]
	if entry is None or entry.firstChild is None:
		# print('%s entry missing' %keyword)
		if attribute != '':
			return None, None
		return



	if attribute!='':
		units = entry.getAttribute(attribute)
		return entry.firstChild.nodeValue, units
	else:
		return entry.firstChild.nodeValue




def load_spectrum_from_file(data_file, mode = 'channels vs yield'):
	if mode.lower() == 'channels vs yield':
		clean_lines = []
		with open(data_file, 'r') as file:
			for line in file.readlines():
				if line.strip()[0].isnumeric():
					clean_lines.append(line)					
					
		data_x, data_y = loadtxt(clean_lines, unpack=True)
		
		return data_x, data_y
		
	elif mode.lower() == '8 columns':
		# find footer
		nlinesfooter = 0
		nrows = 1
		ncolumns = 0

		with open(data_file, 'r') as file:
			ncolumns = len(file.readline().split())    
			for l in file.readlines():
				if l.split()[0].isnumeric():
					nrows += 1
				else:
					nlinesfooter += 1


		data_y = reshape(genfromtxt(data_file, skip_footer = nlinesfooter), nrows*ncolumns)
		
		data_x = range(0, len(data_y))
		
		return data_x, data_y

	elif mode.lower() == 'potku':
		with open(data_file, 'r') as file:
			text = file.readlines()
			data_start = text.index('[DATA]\n')
		
		data_y = nparray([int(float(n.replace('/', ''))) for n in text[data_start+1:]])
		data_x = arange(0, len(data_y))

		
		return data_x, data_y
		
		
	elif mode.lower() == 'ndf simulation':
		data = loadtxt(data_file, skiprows = 7)

		data_x = data[:,0]
		data_y = data[:,1]
		data_y_fit = data[:,2]
		
		return data_x, data_y, data_y_fit
		
	else:
		print('Choose mode = channels vs yield or mode = 8 columns')


def read_pixe_file(file_name, mode = 'GUPIX'):
	if mode == 'GUPIX':
		code_ini = 'Elmt  Lay   DF     Peak     2-FWHM       % Fit  % Stat. +1% Of     LOD'
		code_fin = '-------------------------------------------------------------------------------'

		data_lines = []
		save = False
		with open(file_name, 'r') as file:
			for line in file.readlines():
				if save and code_fin in line:
					save = False
					data_lines = data_lines[:-1]
					break

				if save:
					data_lines.append(line)
				if code_ini in line:
					save = True

		data_lines = [line.split() for line in data_lines]
		# xray_lines = [line[2] for line in data_lines][2:]
		xray_area = [line[7] for line in data_lines][2:]

		xray_lines = []
		for line in data_lines[2:]:
			xray = line[2]
			if len(xray) == 1:
				xray +=line[3][0]
			
			xray_lines.append(xray)

		return xray_lines, xray_area
	
	
	elif mode == 'NDF simulation':
		code_ini = 'element  data        error          fit'
		
		data_lines = []
		save = False
		with open(file_name, 'r') as file:
			for line in file.readlines():
				if save:
					data_lines.append(line)
				if code_ini in line:
					save = True
				   
		data_lines = [line.split() for line in data_lines]
		xray_lines = [''.join(line[0:2]).replace(':','') for line in data_lines]
		xray_area = [line[2] for line in data_lines]
		
		return xray_lines, xray_area
				
	
	else:
		print('Mode not recognised')

def load_SIMS_file(data_file):
	return loadtxt(data_file)




def capitalize_atom(atom):
	if atom is None:
		return

	m = search('[a-zA-Z]', atom);
	if m is not None:
		index = m.start()
		atom = atom[0:index] + atom[index].upper() + atom[index + 1:]

	return atom

def latex_atom(atom):
	m = search('[a-zA-Z]', atom);
	if m is not None:
		index = m.start()
		if index>0:
			atom = '$ ^{%s}$%s%s'%(atom[0:index], atom[index].upper(), atom[index + 1:])

	return atom


def simplify_atomic_formula(formula):
	formula = formula.replace('?=','')
	formula = formula.replace('.','')

	m = search('[a-zA-Z]', formula);
	formula_clean = formula[:m.start()]
	for i,c in enumerate(formula):
		if c.isnumeric() == False:
			formula_clean +=c
		elif formula_clean[-1]!=' ':
			formula_clean += ' '

	formula_clean = formula_clean.split()
	formula_clean = [capitalize_atom(n) for n in formula_clean]
	formula_clean = ''.join(formula_clean)
	
	return latex_atom(formula_clean)

def pretty_formula_ratio(name_ini):
	try:
		name = name_ini.split()

		name_clean = name
		numbers = [float(n) for n in name[1::2]]
		fracs = []
		for n in numbers:
			fracs.append(Fraction(n).limit_denominator(100))

		max_dom = max([f.denominator for f in fracs])
		
		if max_dom > 30:
			numbers = ['%0.2f'%n for n in numbers]
		else:        
			for i,f in enumerate(fracs):
				mult = int(max_dom/f.denominator)
				comm_f = f.numerator*mult
				
				numbers[i] = comm_f
				
				
		for i,n in enumerate(numbers):
			name[2*i + 1] = str(n) 
				
		# if max_dom < 30:
		#     name_recover = name*1
		#     total = sum(numbers)
		#     for i,n in enumerate(numbers):
		#         name_recover[2*i + 1] = '%0.5f' %(n/total)

		
		return ' '.join(name)
	except:
		return name_ini
	

def set_element_fit_symbol(formula):
	formula_clean = formula[0]

	for i in range(1, len(formula)):
		if (formula[i] == ' ') and (formula[i-1].isalpha()):
			formula_clean += ' ?='
		else:
			formula_clean += formula[i]

	return formula_clean



def uniformize_element_name(element):
	formula = element.replace('?=','')
	formula = formula.replace(' ', '')

	formula_clean = ''
	for i,c in enumerate(formula):
		if c.isnumeric():
			if (len(formula_clean) != 0) and (formula_clean[-1].isalpha()):                
				formula_clean += ' '
		elif i>0:
			if formula_clean[-1].isnumeric() and c != '.':
				formula_clean += ' '
		
		formula_clean += c
			

	formula_clean = formula_clean.split()
	formula_clean = [capitalize_atom(n) for n in formula_clean]
	formula_clean = ' '.join(formula_clean)
	
	return formula_clean



def normalize_list(list_original):
	list_original = [int(i) for i in list_original]
	list_sorted_index = sorted(range(len(list_original)), key=lambda k: list_original[k])
	list_sorted = nparray(sorted(list_original))
	list_sorted -= min(list_sorted) - 1

	for i in range(1, len(list_original)):
		dif = list_sorted[i] - list_sorted[i-1]

		if dif >0:
			list_sorted[i:] -= dif -1

	list_normalized = [0]*len(list_original)
	for i,e in enumerate(list_sorted_index):
		list_normalized[e] = list_sorted[i]

	return list_normalized


def check_its_number(number):
	# as per stackover flow, this is the fastest/versatil solution, as strange as it is
	# https://stackoverflow.com/questions/354038/how-do-i-check-if-a-string-is-a-number-float
	try:
		float(number)
		return True
	except:
		return False



