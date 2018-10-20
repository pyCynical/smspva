from setuptools import setup,find_packages

setup(
    name='smspva',
    version='0.0.1',
    description='An API wrapper for the website smspva',
    license='GNU',
    install_requires=["requests"],
    author='pyCynical',
    author_email='enxfusion@gmail.com',
    keywords=['smspva','sms'],
    url='https://github.com/pyCynical/smspva',
    packages = find_packages(exclude=["docs","tests"])

)
