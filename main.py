import random
import svgwrite
from aux import generate_hash_name

dwg = svgwrite.Drawing('img/' + generate_hash_name.generate_name() + '.svg', profile='full')
seed = random.seed()


def create_line(start, end, rgb):

    dwg.add(dwg.line((start[0], start[1]), (end[0], end[1]), stroke=svgwrite.rgb(rgb[0], rgb[1], rgb[2], '%')))


def create_structure(iterations, pixel_range, color=(255, 0, 0)):

    start = (random.randint(pixel_range[0], pixel_range[1]), random.randint(pixel_range[0], pixel_range[1]))
    end = (random.randint(pixel_range[0], pixel_range[1]), random.randint(pixel_range[0], pixel_range[1]))

    for i in range(iterations):
        create_line(start, end, color)

        start = end
        end = (random.randint(pixel_range[0], pixel_range[1]), random.randint(pixel_range[0], pixel_range[1]))


create_structure(45, (0, 500))
dwg.save()
