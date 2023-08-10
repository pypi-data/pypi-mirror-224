from setuptools import setup

setup(
    name='pyIBA',
    version='1.0',    
    description='A Python library aimed at simplifying the life of Ion Beam Scientists',
    url='https://github.com/m-sequeira/pyIBA',
    author='Miguel Sequeira',
    author_email='miguel.sequeira@tecnico.ulisboa.pt',
    # license='BSD 2-clause',
    packages=['pyIBA',
              'pyIBA.codes'],
    install_requires=['numpy', 
                      'matplotlib>2'],
    package_data={'': ['pyIBA/aux_files/*'],
                  '': ['pyIBA/codes/NDF_11_MS/*']},

    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        # 'License :: OSI Approved :: BSD License',  
        # 'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.10',        
    ],
)
