#!/usr/bin/python

from gi.repository import Gtk, GObject, GdkPixbuf
import argparse
import glob
import time
import numpy as np
import cv2
import Image

#parser = argparse.ArgumentParser()
#parser.add_argument('-s','--sequence',dest='sequence',help='sequence d image')
#args = parser.parse_args()
my_files = glob.glob("Jupiter/jupiter_006*.bmp")
my_files.sort()

window = Gtk.Window()
image = Gtk.Image()
image.show()
window.add(image)
window.connect("delete-event", Gtk.main_quit)
window.show_all()

def consomme_fichier():
	global my_files
	try:
		f = my_files[0]
		img = cv2.imread(f)
		print img.shape
		[w, h, p] = img.shape
		print dir(img)
		img_pixbuf = GdkPixbuf.Pixbuf.new_from_bytes(img.tostring(), GdkPixbuf.Colorspace.RGB, False, 8, w, h,w*3)
		
		#image.new_from_pixbuf(img_pixbuf)
		print f
		my_files = my_files[1:]
		GObject.timeout_add(50,consomme_fichier)
	except IndexError:
		print "termine"

GObject.timeout_add(10,consomme_fichier)

Gtk.main()

