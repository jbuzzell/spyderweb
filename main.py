import random
import svgwrite
from aux import generate_hash_name
from aux import generate_lines

dwg = svgwrite.Drawing('img/' + generate_hash_name.generate_name() + '.svg', profile='full')
dwg.add(svgwrite.shapes.Rect((0, 0), (500, 500), fill="#000"))
seed = random.seed()


def create_line(start, end, rgb, stroke_width=1):

    dwg.add(dwg.line((start[0], start[1]),
                     (end[0], end[1]),
                     stroke=svgwrite.rgb(rgb[0], rgb[1], rgb[2]),
                     stroke_width=stroke_width))


def create_structure(num_points, pixel_range, color=(255, 0, 0)):

    lines = generate_lines.create_line_list(generate_lines.create_point_list(num_points, pixel_range))

    for i in lines:

        # todo: color modifier
        create_line(i[0], i[1], color)


create_structure(40, (0, 500))
dwg.save()
