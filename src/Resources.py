import pygame
import os
import Constants

# Memory
loadedResources = {}

def load_image(name, path=Constants.IMAGE_DIR, colorkey=None):
	fullname = os.path.join(path , name)

	image = loadedResources.get(fullname)
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

	loadedResources[fullname] = image
	return image


def load_music(name, path=Constants.MUSIC_DIR):
	fullname = os.path.join(path, name)

	music = loadedResources.get(fullname)

	if music:
		return music

	try:
		music = pygame.mixer.music.load(fullname)
	except pygame.error, message:
		print "Cannot load music: ", fullname
		raise SystemExit, message

	loadedResources[fullname] = music
	return music


def load_sound(name, path=Constants.SOUND_DIR):
	fullname = os.path.join(path, name)

	sound = loadedResources.get(fullname)

	if sound:
		return sound

	try:
		sound = pygame.mixer.Sound(fullname)
	except pygame.error, message:
		print "Cannot load sound: ", fullname
		raise SystemExit, message

	loadedResources[fullname] = sound
	return sound

def clearResources():
	loadedResources.clear()
