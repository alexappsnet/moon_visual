import vpython as vp

from cmn import prepare

vec1 = vp.vec(1, 1, 1)
earth_radius = 6370
moon_radius = 1737
distance_earth_moon = 384000


def main():
    prepare(distance_earth_moon * 0.3)

    earth = vp.sphere(pos=vp.vec(-distance_earth_moon / 2, 0, 0), size=earth_radius * vec1)
    earth.texture = {'file': vp.textures.earth}

    moon = vp.sphere(pos=earth.pos + vp.vec(distance_earth_moon, 0, 0), size=moon_radius * vec1)
    moon.texture = {'file': vp.textures.moon}


if __name__ == '__main__':
    main()
