
import sys
from os.path import dirname, join as osjoin

path_pyIBA = osjoin(dirname(__file__), '').replace('pyIBA/codes/','')
sys.path.insert(0, path_pyIBA)
from pyIBA import IDF


def IDF2NDF(filename):
    try:
        ori = IDF(filename)
    except Exception as e:
        print('File not found')
        sys.exit()

    nspectra = ori.get_number_of_spectra()

    if nspectra == 1: 
        print('Opening %s (%s spectrum):\n' %(ori.name, nspectra))
    else:
        print('Opening %s (%s spectra):\n' %(ori.name, nspectra))

    print(ori.user + '\n')
    print('')

    for l in ori.description:
        print(l)


    for i in range(nspectra):
        print('\n\n ==============  Spectrum  %i ==============' %(i+1))

        ori.write_dataxy(spectra_id = i, path_dir = ori.path_dir)
        ori.write_geo(spectra_id = i, path_dir = ori.path_dir)


    print('\n\n ==============  General Files ==============')

    ori.write_str(path_dir = ori.path_dir)
    ori.write_prf(path_dir = ori.path_dir)
    ori.write_spc(path_dir = ori.path_dir)



if __name__ == '__main__':
    filename = sys.argv[1]

    IDF2NDF(filename)
