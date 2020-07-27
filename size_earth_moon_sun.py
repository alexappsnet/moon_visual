from vpython import *

from cmn import prepare

vec1 = vec(1, 1, 1)
earth_radius = 6370
moon_radius = 1737
sun_radius = 696000


def x(value):
    return vector(value, 0, 0)


def main():
    prepare(500000)

    earth = sphere(pos=x(-200000), size=earth_radius * vec1)
    earth.shininess = 0
    earth.texture = {'file': textures.earth}

    moon = sphere(pos=x(-140000), size=moon_radius * vec1)
    moon.shininess = 0
    moon.texture = {'file': textures.moon}

    sun = sphere(pos=x(300000), size=sun_radius * vec1)
    sun.shininess = 0
    sun.texture = {'file': textures.sun}


if __name__ == '__main__':
    main()
