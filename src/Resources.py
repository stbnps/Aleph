
import pygame
import os
import Constants

# Memory
loadedImages = {}

def load_image(name, path=Constants.IMAGE_DIR, colorkey=None):
	fullname = os.path.join(path , name)

	image = loadedImages.get(fullname)
	if image:
		return image

	try:
		image = pygame.image.load(fullname)
	except pygame.error, message:
		print 'Cannot load image:', fullname
		raise SystemExit, message

	if colorkey is not None:
		image = image.convert()
		if colorkey is -1:
			colorkey = image.get_at((0, 0))
		image.set_colorkey(colorkey, pygame.RLEACCEL)
	else:
		image = image.convert_alpha()

	loadedImages[fullname] = image
	return image


def clearResources():
	loadedImages.clear()