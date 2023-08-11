from setuptools import setup, find_packages
from pathlib import Path

current_directory = Path(__file__).parent
VERSION = "1.5"
DESC = "A python tool to edit image geolocation data."
LONG_DESC = (current_directory/'README.md').read_text()

setup(
	name="P.E.T-build",
	version="1.5",
	description=DESC,
	long_description=LONG_DESC,
	long_description_content_type='text/markdown',
	packages=find_packages(),
	install_requires=["requests", "typer", "rich", 'pyexiftool', 'pyfzf'],
	entry_points={
		"console_scripts": [
			"pet = pet.__main__:main"
		]
	},
	keywords=['python', 'photo', 'edit', 'metadata', 'exif', 'gps'],
	classifiers=[
		'Development Status :: 5 - Production/Stable',
		'Programming Language :: Python :: 3',
		'Environment :: Console',

	]
)
