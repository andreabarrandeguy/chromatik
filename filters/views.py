import os
from django.shortcuts import render
from PIL import Image
from django.core.files.storage import default_storage
import io
import base64

# Create your views here.
def index(request):
    if request.method == "POST":
        #Check for input file and save it
        input_file = request.FILES['input_file']
        if not input_file:
            return 'No file'
        imgSaved = default_storage.save('./filters/static/filters/input.jpg', input_file)

        # Get filter & image
        filter = request.POST["filter"]
        ogimg = Image.open('./filters/static/filters/input.jpg')
        #img = Image.open('./filters/static/filters/input.jpg')
        
        # Resize original image for process performance
        ogwidth, ogheight = ogimg.size
        newsize = (int((ogwidth/ogheight)*500), 500)
        img = ogimg.resize(newsize)
        width, height = img.size

        # Obtain RGB data for input file
        rgb_map = img.convert('RGB')
        new = Image.new("RGB", (width, height))
        
        # Apply filter - PURPLE
        if filter == "purple":
            for y in range(height):
                for x in range(width):
                    # Get pixel RGB data
                    [r,g,b] = rgb_map.getpixel((x, y))
                    og_red = r
                    og_green = g
                    og_blue = b

                    # Si el azul es mayoritario, Cambiar los azules a celestes
                    if ((og_blue >= og_green) and (og_blue >= og_red)):
                        b = og_green
                        g = og_blue

                    # Si el verde es mayoritario, Cambiar los verdes a purpuras/rosas
                    elif (og_green > og_blue) and (og_green > og_red):
                        r = og_green
                        g = og_blue
                        b = og_green

                    # Si el rojo es mayoritario (solo para marrones/verdes dudosos)
                    elif (og_red > og_blue) and (og_red >= og_green):
                        if (100 < og_red < 200) and (100 < og_green < 200):
                            r = og_green
                            g = og_blue
                            b = og_green
                        # El resto convertirlo a grises
                        else:
                            grey = int((og_red + og_green + og_blue) / 3)
                            r = grey
                            g = grey
                            b = grey

                    # Nuevo valor del pixel y lo guarda
                    value = (r,g,b)
                    new.putpixel((x, y), value)
        
        
        # Apply filter - TURQUOISE
        if filter == "turquoise":
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

                    # Nuevo valor del pixel y lo guarda
                    value = (r,g,b)
                    new.putpixel((x, y), value)


        # Apply filter - RED
        if filter == "red":
            for y in range(height):
                for x in range(width):
                    # Get pixel RGB data
                    [r,g,b] = rgb_map.getpixel((x, y))
                    og_red = r
                    og_green = g
                    og_blue = b

                    # Si el azul es mayoritario, desaturar
                    if ((og_blue > og_green) and (og_blue > og_red)) and (og_green > og_red):
                        r = og_green
                    if ((og_blue > og_green) and (og_blue > og_red)) and (og_red > og_green):
                        g = og_red
                    #if (og_blue > og_green) and (og_blue > og_red):
                    #    r = 150

                    # Si el verde es mayoritario, desaturar
                    if ((og_green > og_blue) and (og_green > og_red)) and (og_blue > og_red):
                        r = og_blue
                    if ((og_green > og_blue) and (og_green > og_red)) and (og_red > og_blue):
                        b = og_red

                    # Si el rojo es mayoritario, saturar
                    if (og_red > og_green) and (og_red > og_blue):
                        g = og_blue
                    

                    # Nuevo valor del pixel y lo guarda
                    value = (r,g,b)
                    new.putpixel((x, y), value)
        

        # Save output file & Delete input file
        bufferOutput = io.BytesIO()
        new.save(bufferOutput, 'PNG')
        PNG = bufferOutput.getvalue()
        output = base64.b64encode(PNG).decode("utf-8")
        os.remove('./filters/static/filters/input.jpg')

        if (width >= height):
            return render(request, "filters/outputh.html", {
                "output": output
            })
        if (height > width):
            return render(request, "filters/outputv.html", {
                "output": output
            })
    
    return render(request, "filters/index.html")

   

def about(request):
    return render(request, "filters/about.html")


def outputh(request):
    return render(request, "filters/outputh.html")

def outputv(request):
    return render(request, "filters/outputv.html")

def filters(request):
    return render(request, "filters/filters.html")
