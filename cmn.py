import vpython as vp
import sys


def prepare(range=None):
    if sys.platform == 'linux':
        vp.scene.width = 1900  # my linux box
        vp.scene.height = 1060
    else:
        vp.scene.width = 1420  # my macbook
        vp.scene.height = 700

    if range:
        vp.scene.range = range
