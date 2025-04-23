import os
from PIL import Image


def verify_folders():
	if not os.path.exists(old_directory):
		os.mkdir(old_directory)
	if not os.path.exists(new_directory):
		os.mkdir(new_directory)


def save_updated(img_name: str, image_format: str, rotate: float = 0, resize: tuple[int, int] = (0, 0)):
	with Image.open(img_name) as image:
		new_file_name = ""
		try:
			dot_index = img_name.rindex(".")
			new_file_name = img_name[len(old_directory)+1:dot_index]
		except ValueError:
			new_file_name = img_name[len(old_directory)+1:]
		finally:
			width = resize[0] if resize[0] > 0 else image.size[0]
			height = resize[1] if resize[1] > 0 else image.size[1]
			new_file_name = f"{new_file_name}_rot{rotate:03}_{width:04}x{height:04}"
			image.rotate(rotate).resize((width, height)).save(f"{new_directory}/{new_file_name}.{image_format}")


old_directory = "./originals"
new_directory = "./updated"

verify_folders()
files = [f for f in os.listdir(old_directory) if os.path.isfile(f"{old_directory}/{f}")]
for f in files:
	save_updated(f"{old_directory}/{f}", "jpeg", 90, (128, 128))
