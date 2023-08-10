from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Pacote em python'
LONG_DESCRIPTION = 'Pacote de calculos'

#setting up
setup(
        #'name' deve corresponder ao nome da pasta 'PacoteTeste'
        name = "CalculosPacotes",
        version=VERSION,
        author="Millena Lira",
        author_email="millena.mp2@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        license='MIT',
        packages=find_packages(),
        install_requires=[],# adicione outros pacotes que precisem ser instalados com o seu pacote. EX: 'caer'
        
) 
    