import os

from flask import render_template

def purple(img):
        # Obtain RGB data for input file
        width, height = img.size
        rgb_map = img.convert('RGB')

        # Apply filter
        for y in range(height):
            for x in range(width):
                # Get pixel RGB data
                [r,g,b] = rgb_map.getpixel((x, y))
                og_red = r
                og_green = g
                og_blue = b

                # Si el azul es mayoritario
                if ((og_blue > og_green) and (og_blue > og_red)) or (og_blue+50 > og_green):
                     # Cambiar los azules a naranjas
                     b = og_green
                     g = og_blue

                # Si el verde es mayoritario
                elif (og_green > og_blue) and (og_green > og_red):
                     # Cambiar los verdes a azules
                     r = og_green
                     g = og_red

                # Si el rojo es mayoritario
                #elif (og_red > og_blue) and (og_red > og_green):
                     # Cambiar los rojos a azules
                #     b = og_red
                #     r = og_blue

                value = (r,g,b)
                rgb_map.putpixel((x, y), value)

        # Save output file & Delete input file
        rgb_map.save('./static/output.jpg')
        os.remove('./temp_images/input.jpg')

        return render_template("output.html")


def turquoise(img):
        # Obtain RGB data for input file
        width, height = img.size
        rgb_map = img.convert('RGB')

        # Apply filter
        for y in range(height):
            for x in range(width):
                # Get pixel RGB data
                [r,g,b] = rgb_map.getpixel((x, y))
                og_red = r
                og_green = g
                og_blue = b

                # Si el azul es mayoritario
                if ((og_blue > og_green) and (og_blue > og_red)) or (og_blue+50 > og_green):
                     # Cambiar los azules a naranjas
                     b = og_red
                     r = og_blue

                # Si el verde es mayoritario
                elif (og_green > og_blue) and (og_green > og_red):
                     # Cambiar los verdes a azules
                     b = og_green
                     g = og_blue

                # Si el rojo es mayoritario
                elif (og_red > og_blue) and (og_red > og_green):
                     # Cambiar los rojos a azules
                     b = og_red
                     r = og_blue

                value = (r,g,b)
                rgb_map.putpixel((x, y), value)

        # Save output file & Delete input file
        rgb_map.save('./static/output.jpg')
        os.remove('./temp_images/input.jpg')

        return render_template("output.html")
