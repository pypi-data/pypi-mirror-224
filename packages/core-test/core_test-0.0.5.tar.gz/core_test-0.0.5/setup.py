from setuptools import setup, find_packages

setup(
    name = "core_test",
    version = "0.0.5",
    license = "MIT",
    description = "descripcion del paquete.",
    author="autor",
    author_email="autor-email@gmail.com",
    packages=find_packages() # Para que pueda localizar los subpaquetes y el paquete como tal.
)