from setuptools import setup, find_packages

VERSION = '1.1.5'
DESCRIPTION = 'Meu primeiro pacote'
LONG_DESCRIPTION = 'Meu primeiro pacote completo longo'

#setting up
setup(
        #'name' deve corresponder ao nome da pasta 'PacoteTeste'
        name = "PacoteCalculoMat",
        version=VERSION,
        author="Milene Fialho",
        author_email="milefialho16@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        license='MIT',
        packages=find_packages(),
        install_requires=[],# adicione outros pacotes que precisem ser instalados com o seu pacote. EX: 'caer'
        
) 
    