from PIL import Image

def apply_purple_filter(img):
    width, height = img.size
    rgb_map = img.convert('RGB')
    new = Image.new("RGB", (width, height))

    for y in range(height):
        for x in range(width):
            [r, g, b] = rgb_map.getpixel((x, y))
            og_red, og_green, og_blue = r, g, b

            if (og_blue >= og_green) and (og_blue >= og_red):
                b = og_green
                g = og_blue
            elif (og_green > og_blue) and (og_green > og_red):
                r = og_green
                g = og_blue
                b = og_green
            elif (og_red > og_blue) and (og_red >= og_green):
                if (100 < og_red < 200) and (100 < og_green < 200):
                    r = og_green
                    g = og_blue
                    b = og_green
                else:
                    grey = int((og_red + og_green + og_blue) / 3)
                    r, g, b = grey, grey, grey

            new.putpixel((x, y), (r, g, b))
    
    return new

def apply_turquoise_filter(img):
    width, height = img.size
    rgb_map = img.convert('RGB')
    new = Image.new("RGB", (width, height))

    for y in range(height):
        for x in range(width):
            [r, g, b] = rgb_map.getpixel((x, y))
            og_red, og_green, og_blue = r, g, b

            if (og_blue > og_green) and (og_blue > og_red) or (og_blue + 50 > og_green):
                b = og_red
                r = og_blue
            elif (og_green > og_blue) and (og_green > og_red):
                b = og_green
                g = og_blue
            elif (og_red > og_blue) and (og_red > og_green):
                b = og_red
                r = og_blue

            new.putpixel((x, y), (r, g, b))

    return new

def apply_red_filter(img):
    width, height = img.size
    rgb_map = img.convert('RGB')
    new = Image.new("RGB", (width, height))

    for y in range(height):
        for x in range(width):
            [r, g, b] = rgb_map.getpixel((x, y))
            og_red, og_green, og_blue = r, g, b

            if (og_blue > og_green) and (og_blue > og_red) and (og_green > og_red):
                r = og_green
            if (og_blue > og_green) and (og_blue > og_red) and (og_red > og_green):
                g = og_red
            if (og_green > og_blue) and (og_green > og_red) and (og_blue > og_red):
                r = og_blue
            if (og_green > og_blue) and (og_green > og_red) and (og_red > og_blue):
                b = og_red
            if og_red > og_green and og_red > og_blue:
                g = og_blue

            new.putpixel((x, y), (r, g, b))

    return new
