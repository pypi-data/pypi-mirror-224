from .classmodule import Image
from typing import List
from glob import glob

def parse_path(path: str, exiftool_path='exiftool') -> List[Image]:
	"""Convert path to Images."""
	file_paths = glob(path)
	images = []
	for file in file_paths:
		images.append(Image(path=file, exiftool_path=exiftool_path))
	return images
