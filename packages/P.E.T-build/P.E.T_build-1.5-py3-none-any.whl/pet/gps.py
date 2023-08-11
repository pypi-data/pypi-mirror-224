"""Manage GPS data"""
import typer
from .funcmodule import parse_path
from .classmodule import API, Image
from rich import print_json, print
from rich.progress import track

app = typer.Typer()

@app.callback()
def callback():
	"""Change GPS data using named locations and addresses"""

@app.command('add')
def add_location(path: str,
					fzf_path: str = typer.Option(help='Path for fzf executable', default='fzf'),
					exiftool_path: str = typer.Option(help='Path for exiftool executable', default='exiftool')):
	"""Add location to images."""
	images = parse_path(path=path, exiftool_path=exiftool_path)
	image: Image
	for image in images:
		if image.gps_coords is False:
			print(f'[blue]{image.path}[/blue] has no location.')
		else:
			print(f'Current location for [blue]{image.path}[/blue]: {image.gps_coords["lat"]}, {image.gps_coords["long"]}')

	addr = typer.prompt('Address')
	api = API(fzf=fzf_path)
	location = api.geocode(addr)
	print_json(data=location)

	image: Image
	for image in track(images, description='Processing...'):
		print(f'Setting {image.path} location to {location["lat"]}, {location["long"]}')
		image.add_location(lat=location['lat'], long=location['long'])
		print(f'Set {image.path} location to {image.gps_coords["lat"]}, {image.gps_coords["long"]}')

@app.command('rm')
def remove_location(path: str, exiftool_path: str = typer.Option(help='Path for exiftool executable', default='exiftool')):
	"""Remove location from images."""
	images = parse_path(path)
	image: Image
	for image in images:
		if image.gps_coords is False:
			print(f'[blue]{image.path}[/blue] has no location.')
		else:
			print(f'Current location for [blue]{image.path}[/blue]: {image.gps_coords["lat"]}, {image.gps_coords["long"]}')
		
	delete = typer.confirm('Are you sure you want to delete GPS data? (this cannot be undone!)', abort=True)
	if delete:
		image: Image
		for image in track(images, description='Processing...'):
			print(f'Deleting location from {image.path}')
			image.rm_location()
