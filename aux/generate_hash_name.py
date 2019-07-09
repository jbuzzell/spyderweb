import random

seed = random.seed()


def generate_name():

    name, char_set, num_set = "", (65, 90), (48, 57)

    for i in range(10):

        name_charset, rand = (), lambda: random.randint(0, 1) == 0

        if rand():
            name_charset = char_set
        else:
            name_charset = num_set

        name += chr(random.randint(name_charset[0], name_charset[1]))

    return name
