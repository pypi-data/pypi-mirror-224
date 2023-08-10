import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='serial_scanner',
    version='0.1',
    author='Jonathon Taufatofua',
    author_email='j.taufatofua@uq.edu.au',
    description='Serial port device scanner',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/jttaufa/serialport_scanner',
    # license='MIT',
    python_requires='>=3.8',
    packages=setuptools.find_packages(),
    install_requires=["pyserial"],
    classifiers=['Development Status :: 3 - Alpha',
               "Programming Language :: Python :: 3",
               "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
               "Operating System :: OS Independent",
               ],
    # zip_safe=False,
)
