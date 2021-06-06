from PIL import Image

words = Image.open('word_matrix.png')
mask = Image.open('mask_file.png')

if words.size[0] > mask.size[0]:
    base_width = words.size[0]
else:
    base_width = mask.size[0]

if words.size[1] > mask.size[1]:
    base_height = words.size[1]
else:
    base_height = mask.size[1]

base_pixels = (base_width,base_height)

if words.size != base_pixels:
    words = words.resize(base_pixels)

if mask.size != base_pixels:
    mask = mask.resize(base_pixels)

mask.putalpha(230)
words.putalpha(240)
words.paste(mask,(0,0),mask)
words.show()
