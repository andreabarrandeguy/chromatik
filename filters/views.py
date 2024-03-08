import os
from django.shortcuts import render
from PIL import Image
from django.core.files.storage import default_storage
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import io


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
        img = Image.open('./filters/static/filters/input.jpg')
                    
        # Obtain RGB data for input file
        width, height = img.size
        rgb_map = img.convert('RGB')
        new = Image.new("RGB", (width, height))
        
        # Apply filter
        if filter == "purple":
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
                    new.putpixel((x, y), value)
        
        if filter == "turquoise":
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
                    new.putpixel((x, y), value)
        
        # Save output file & Delete input file
        # output = default_storage.save('./filters/static/filters/output.jpg', new)
        new.save('./filters/static/filters/output.jpg')
        os.remove('./filters/static/filters/input.jpg')
        return render(request, "filters/output.html")
    
    return render(request, "filters/index.html")

   

def about(request):
    return render(request, "filters/about.html")

def output(request):
    return render(request, "filters/output.html")