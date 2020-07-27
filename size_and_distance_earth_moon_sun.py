import vpython as vp

from cmn import prepare

earthR = 6.37
moonR = 1.737
sunR = 696
earth_moon_distance = 384
earth_sun_distance = 150000

vec1 = vp.vec(1, 1, 1)
green = vp.color.green
orange = vp.color.orange
gray = vp.color.gray(1)


def main():
    prepare(earth_sun_distance * 0.55)

    earth = vp.sphere(pos=vp.vec(-earth_sun_distance / 2, 0, 0), size=earthR * vec1, color=green)

    sun = vp.sphere(pos=earth.pos + vp.vec(earth_sun_distance, 0, 0), size=sunR * vec1, color=orange)

    moon = vp.sphere(pos=earth.pos + vp.vec(0, 0, earth_moon_distance), size=moonR * vec1, color=gray)

    sunArrow = vp.arrow(
        pos=sun.pos + vp.vec(0, 0.09 * earth_sun_distance, 0),
        axis=vp.vec(0, -0.09 * earth_sun_distance + 2 * sunR, 0),
        shaftwidth=1000,
        color=orange
    )

    earthArrow = vp.arrow(
        pos=earth.pos + vp.vec(0, 0.09 * earth_sun_distance, 0),
        axis=vp.vec(0, -0.09 * earth_sun_distance + 2 * earthR, 0),
        shaftwidth=1000,
        color=green
    )

    moonArrow = vp.arrow(
        pos=moon.pos - vp.vec(0, 0.09 * earth_sun_distance, 0),
        axis=vp.vec(0, 0.09 * earth_sun_distance - 2 * moonR, 0),
        shaftwidth=1000,
        color=gray
    )


if __name__ == '__main__':
    main()
