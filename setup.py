from setuptools import setup

setup(name='keras_squeezenet',
      version='0.3',
      description='Squeezenet implementation with Keras framework',
      url='https://github.com/rcmalli/keras-squeezenet',
      author='Refik Can MALLI',
      author_email = "mallir@itu.edu.tr",
      license='MIT',
      packages=['keras_squeezenet'],
      zip_safe=False,
      install_requires=['keras','tensorflow','pillow','numpy'])
