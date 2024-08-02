import os
from django.shortcuts import render
from PIL import Image, ExifTags
from django.core.files.storage import default_storage
import io
import base64
from .filters import apply_purple_filter, apply_turquoise_filter, apply_red_filter

# Create your views here.
def correct_image_orientation(image):
    try:
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == 'Orientation':
                break

        exif = image._getexif()

        if exif is not None:
            orientation = exif.get(orientation)

            if orientation == 3:
                image = image.rotate(180, expand=True)
            elif orientation == 6:
                image = image.rotate(270, expand=True)
            elif orientation == 8:
                image = image.rotate(90, expand=True)

    except (AttributeError, KeyError, IndexError):
        # cases: image don't have getexif
        pass

    return image

def index(request):
    if request.method == "POST":
        input_file = request.FILES.get('input_file')
        if not input_file:
            return 'No file'

        imgSaved = default_storage.save('./filters/static/filters/input.jpg', input_file)

        filter_type = request.POST.get("filter")
        ogimg = Image.open('./filters/static/filters/input.jpg')

        # Correct the orientation
        ogimg = correct_image_orientation(ogimg)
        
        # Resize original image for process performance
        ogwidth, ogheight = ogimg.size
        newsize = (int((ogwidth / ogheight) * 750), 750)
        img = ogimg.resize(newsize)

        # Apply the appropriate filter
        if filter_type == "purple":
            new_img = apply_purple_filter(img)
        elif filter_type == "turquoise":
            new_img = apply_turquoise_filter(img)
        elif filter_type == "red":
            new_img = apply_red_filter(img)
        else:
            new_img = img  # Default to the original image if filter is unknown

        # Save output file & Delete input file
        bufferOutput = io.BytesIO()
        new_img.save(bufferOutput, 'PNG')
        PNG = bufferOutput.getvalue()
        output = base64.b64encode(PNG).decode("utf-8")
        os.remove(imgSaved)

        if img.width >= img.height:
            return render(request, "filters/outputh.html", {"output": output})
        else:
            return render(request, "filters/outputv.html", {"output": output})

    return render(request, "filters/index.html")

   

def about(request):
    return render(request, "filters/about.html")


def outputh(request):
    return render(request, "filters/outputh.html")

def outputv(request):
    return render(request, "filters/outputv.html")

def filters(request):
    return render(request, "filters/filters.html")
