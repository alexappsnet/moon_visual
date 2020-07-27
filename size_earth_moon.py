import vpython as vp

from cmn import prepare

vec1 = vp.vec(1, 1, 1)
earth_radius = 6370
moon_radius = 1737


def x(value):
    return vp.vec(value, 0, 0)


def main():
    prepare(5000)

    earth = vp.sphere(pos=x(-3000), size=earth_radius * vec1)
    earth.texture = {'file': vp.textures.earth}

    moon = vp.sphere(pos=x(4200), size=moon_radius * vec1)
    moon.texture = {'file': vp.textures.moon}


if __name__ == '__main__':
    main()
