from setuptools import setup

with open("README.md","r") as fh:
	long_description = fh.read()
setup(

	name='fock_matrix',
	version= "0.0.1" ,
	description = 'fock matrix implementation' ,
	py_modules = ["fock_matrix"],
	package_dir = {'':'src'},
	readme = "README.md",
	classifiers = [
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.5",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    ],
    long_description = long_description,
    long_description_content_type="text/markdown",
    install_requires = [
    	"blessings ~= 1.7",
	],
	extras_require = {
		"dev": [
			"pytest >= 3.5",
			],

	},

	url = "https://github.com/Razer-07" , 
	author= "Rahul" ,
	author_email = "rajkrahul00@gmail.com",

    )