from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'MEU PRIMEIRO PACOTE EM PYTHON'
LONG_DESCRIPTION = 'MEU PRIMEIRO PROJETO EM PYTHON COM UMA DESCRIÇÃO UM POUCO MAIS LONGA'

setup(
            nome = 'operatorsdavi',
            version = VERSION,
            author = 'davizetinha',
            author_email = 'davi512018@gmail.com',
            description = DESCRIPTION,
            long_description = LONG_DESCRIPTION,
            packages = ['operatorsdavi'],


            classifiers = [
                'Development Status :: 3 - Alpha',
                'Intended Audience :: Education',
                'Programming Language :: Python :: 3',
                'Operating System :: OS Independent'
            ]
)