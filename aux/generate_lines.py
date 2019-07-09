import random


def create_line_list(point_list):

    line_list = [(point_list[0], point_list[-1]), (point_list[-1], point_list[0])]

    for i in range(len(point_list)):

        if i > 0:
            line_list.append((point_list[i-1], point_list[i]))

    return line_list


def create_point_list(points, pixel_range):

    return [
        (random.randint(pixel_range[0], pixel_range[1]),
         random.randint(pixel_range[0], pixel_range[1]))
        for i in range(points)
    ]
