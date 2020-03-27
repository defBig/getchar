from setuptools import setup

setup(name='getch',
      version='1.0',
      description='Função para ler o próximo char de stdin independente do sistema operacional.',
      url='https://github.com/defBig/ssaa',
      author='Louis',
      author_email='https://stackoverflow.com/users/1906307/louis',
      license='None',
      packages=['getch'],
      install_requires=[
          'unidecode',
      ],
      zip_safe=False)
