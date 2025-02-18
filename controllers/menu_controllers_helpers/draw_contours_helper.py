from processing.image.methods.contours import contours_method
import turtle
from PIL import Image
import logging

def perform_turtle(image_file_path, retrieve_option, chain_option):
    try:
        turtle.bye()
    except:
        pass
    turtle.TurtleScreen._RUNNING = True

    contours, hierarchy = contours_method(image_file_path, retrieve_option, chain_option)

    hierarchy = hierarchy[0]

    image = Image.open(image_file_path)

    width, height = image.size

    try:

        screen = turtle.Screen()
        screen.setup(width=width, height=height)
        t = turtle.Turtle()
        t.speed(0)
        t.penup()

        scale = 1

        def draw_contour(contour):
            t.penup()
            for point in contour:
                x, y = point[0]
                t.goto(x * scale - (width * scale) / 2, -y * scale + (height * scale) / 2)
                t.pendown()
            t.penup()

        def draw_contours_recursive(index):
            if index == -1:
                return

            draw_contour(contours[index])

            child_index = hierarchy[index][2]
            if child_index != -1:
                draw_contours_recursive(child_index)

            next_index = hierarchy[index][0]
            if next_index != -1:
                draw_contours_recursive(next_index)

        draw_contours_recursive(0)

        t.hideturtle()
        turtle.done()
    except turtle.Terminator:
        logging.info("Turtle window was closed! Application continues running.")