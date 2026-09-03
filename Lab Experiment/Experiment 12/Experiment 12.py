from PIL import Image
from PIL.ExifTags import TAGS

filename = "sample.jpg"

image = Image.open(filename)
exif = image.getexif()

if exif:
    print("\nEXIF Metadata")
    print("-" * 30)
    for tag_id, value in exif.items():
        tag = TAGS.get(tag_id, tag_id)
        print(f"{tag}: {value}")
else:
    print("No EXIF metadata found.")
