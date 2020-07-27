from functools import partial
from vpython import sphere, color, vec, scene, local_light, textures, rate
from math import pi, cos, sin
from bunch import Bunch
from cmn import prepare

phase_names = 'https://graceintorah.files.wordpress.com/2015/02/moon-phases.jpg'

earth_radius = 6.37
earth_tilt = pi/10
moon_radius = 1.737
moon_day = 27.3
distance = 10


def control_by_key(context, evt):
    print(evt.__dict__)
    if evt.key == ' ':
        context.live = not context.live
    if evt.key == 'right':
        context.live = False
        context.time += 0.8
    if evt.key == 'left':
        context.live = False
        context.time += -0.8
    if evt.key == 'up':
        context.live = True
        context.life_time_step *= 1.25
    if evt.key == 'down':
        context.live = True
        context.life_time_step /= 1.25
    if evt.key == 'l':
        context.lights_on = not context.lights_on
        for light in context.original_lights:
            light.visible = context.lights_on


def main():
    prepare(3 * distance)

    context = Bunch(
        time=3/4*moon_day,
        life_time_step=0.01,
        live=False,
        lights_on=True,
        original_lights=scene.lights[:]
    )

    earth = sphere(pos=vec(0, 0, 0), size=earth_radius * vec(1, 1, 1))
    earth.shininess = 0
    earth.texture = {'file': textures.earth}
    earth.rotate(earth_tilt, axis=vec(0, 0, 1))

    moon = sphere(pos=vec(0, 0, 0), size=moon_radius * vec(1, 1, 1))
    moon.shininess = 1
    moon.texture = {'file': textures.moon}

    sun_x = 40
    sun = sphere(pos=vec(sun_x, 0, 0), size=5 * vec(1, 1, 1), emissive=True)
    sun.texture = {'file': textures.sun}

    local_light(pos=sun.pos, color=color.red)
    local_light(pos=sun.pos + vec(-10, 0, 0), color=color.white)

    scene.bind('keydown', partial(control_by_key, context))

    earth_rotate = 0
    moon_rotate = 0

    while True:
        rate(50)

        if context.live:
            context.time += context.life_time_step

        earth.rotate(-earth_tilt, axis=vec(0, 0, 1))
        earth.rotate(-earth_rotate, axis=vec(0, 1, 0))
        earth_rotate = 2 * pi * context.time
        earth.rotate(earth_rotate, axis=vec(0, 1, 0))
        earth.rotate(earth_tilt, axis=vec(0, 0, 1))

        moon.rotate(-moon_rotate, axis=vec(0, 1, 0))
        moon_angle = -2 * pi * context.time / moon_day
        moon.pos = vec(distance * cos(moon_angle), 0, distance * sin(moon_angle))
        moon_rotate = -pi/2 + 2*pi * context.time / moon_day
        moon.rotate(moon_rotate, axis=vec(0, 1, 0))


if __name__ == '__main__':
    main()
