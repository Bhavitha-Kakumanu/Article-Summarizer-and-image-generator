from wand.image import Image
import requests

image_url = 'https://cdn.arstechnica.net/wp-content/uploads/2018/04/shiny_merlin_edited-760x380.jpg'
image_blob = requests.get(image_url)
with Image(blob=image_blob.content) as img:
    print(img.size)

dims = (1080, 1920)
ideal_width = dims[0]
ideal_height = dims[1]
ideal_aspect = ideal_width / ideal_height

# Get the size of the downloaded image
with Image(blob=image_blob.content) as img:
   size = img.size
width = size[0]
height = size[1]
aspect = width/height

if aspect > ideal_aspect:
 # Then crop the left and right edges:
 new_width = int(ideal_aspect * height)
 offset = (width - new_width) / 2
 resize = (
   (0, 0, int(new_width), int(height)),
   (int(width-new_width), 0, int(width), int(height))
  )
else:
 # ... crop the top and bottom:
   new_height = int(width / ideal_aspect)
   offset = (height - new_height) / 2
   resize = (
    (0, 0, int(width), int(new_height)),
    (0, int(height-new_height), int(width), int(height))
   )

with Image(blob=image_blob.content) as img:
   img.crop(*resize[0])
   img.save(filename='cropped_1.jpg')

with Image(blob=image_blob.content) as img:

  img.crop(*resize[1])
  img.save(filename='cropped_2.jpg')