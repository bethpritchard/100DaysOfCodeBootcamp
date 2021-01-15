import colorgram
import turtle as t
import random as rand

width = 600
height = 600
screen = t.Screen()
screen.setup(width,height)


t.colormode(255)
# # Get colour palette
# rgb_colors = []
# colors = colorgram.extract('damien-hirst-ethyl-laurate.jpg', 30)
# for color in colors:
#     r  = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_colour = (r,g,b)
#     rgb_colors.append(new_colour)
#
# print(rgb_colors)


colours = [(233, 236, 241), (157, 76, 55), (232, 238, 234), (129, 174, 195), (187, 157, 51), (197, 153, 119),
            (152, 51, 84), (234, 215, 90), (113, 35, 48), (62, 106, 136), (36, 42, 65), (173, 145, 168),
            (74, 105, 82), (38, 56, 97), (127, 163, 150), (64, 37, 45), (217, 174, 197), (98, 117, 177),
            (109, 45, 38), (100, 145, 105), (190, 91, 72), (181, 78, 129), (219, 180, 167), (189, 190, 202),
            (214, 203, 36), (176, 196, 205), (182, 198, 188), (85, 33, 31)]



paint = t.Turtle(visible=False)
paint.speed("fastest")
def get_colour():
    random_colour = rand.choice(colours)
    r = random_colour[0]
    g = random_colour[1]
    b = random_colour[2]
    return (r,g,b)

def draw_dot():
    colour = get_colour()
    paint.dot(30, colour)


rand_colour = get_colour()

gap = (width + 100)/10
paint.penup()
# paint.goto(int((-width+100)/2), int((-width+100)/2),)

def draw_painting():
    draw_dot()
    paint.forward(gap)

def draw_line():
    count = 0

    while count < 10:
        paint.goto(int((-width + 100) / 2) , int((-width + 100) / 2) + count*gap)

        for _ in range(9):
            draw_painting()
        count += 1

draw_line()


#
# r, g, b = get_colour()
# draw_dot(r,g,b)



screen.exitonclick()
