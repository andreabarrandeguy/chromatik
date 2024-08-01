document
.getElementById("upload")
.addEventListener("change", function (event) {
  const file = event.target.files[0];
  if (!file) return;

  const reader = new FileReader();
  reader.onload = function (e) {
    const img = new Image();
    img.onload = function () {
      // Canvases and contexts
      const canvasPurple = document.getElementById("canvas-purple");
      const ctxPurple = canvasPurple.getContext("2d");

      const canvasTurquoise = document.getElementById("canvas-turquoise");
      const ctxTurquoise = canvasTurquoise.getContext("2d");

      const canvasRed = document.getElementById("canvas-red");
      const ctxRed = canvasRed.getContext("2d");

      // Resize image for performance
      const MAX_WIDTH = 500;
      const MAX_HEIGHT = 500;
      let width = img.width;
      let height = img.height;

      if (width > height) {
        if (width > MAX_WIDTH) {
          height *= MAX_WIDTH / width;
          width = MAX_WIDTH;
        }
      } else {
        if (height > MAX_HEIGHT) {
          width *= MAX_HEIGHT / height;
          height = MAX_HEIGHT;
        }
      }

      // Set canvas dimensions
      canvasPurple.width = canvasTurquoise.width = canvasRed.width = width;
      canvasPurple.height =
        canvasTurquoise.height =
        canvasRed.height =
          height;
      ctxPurple.drawImage(img, 0, 0, width, height);
      ctxTurquoise.drawImage(img, 0, 0, width, height);
      ctxRed.drawImage(img, 0, 0, width, height);

      // Get image data
      const imageDataPurple = ctxPurple.getImageData(0, 0, width, height);
      const dataPurple = imageDataPurple.data;

      const imageDataTurquoise = ctxTurquoise.getImageData(
        0,
        0,
        width,
        height
      );
      const dataTurquoise = imageDataTurquoise.data;

      const imageDataRed = ctxRed.getImageData(0, 0, width, height);
      const dataRed = imageDataRed.data;

      // Apply Purple filter
      for (let i = 0; i < dataPurple.length; i += 4) {
        const og_red = dataPurple[i];
        const og_green = dataPurple[i + 1];
        const og_blue = dataPurple[i + 2];

        let r = og_red;
        let g = og_green;
        let b = og_blue;

        if (og_blue >= og_green && og_blue >= og_red) {
          b = og_green;
          g = og_blue;
        } else if (og_green > og_blue && og_green > og_red) {
          r = og_green;
          g = og_blue;
          b = og_green;
        } else if (og_red > og_blue && og_red >= og_green) {
          if (
            100 < og_red &&
            og_red < 200 &&
            100 < og_green &&
            og_green < 200
          ) {
            r = og_green;
            g = og_blue;
            b = og_green;
          } else {
            const grey = (og_red + og_green + og_blue) / 3;
            r = grey;
            g = grey;
            b = grey;
          }
        }

        dataPurple[i] = r;
        dataPurple[i + 1] = g;
        dataPurple[i + 2] = b;
      }

      // Apply Turquoise filter
      for (let i = 0; i < dataTurquoise.length; i += 4) {
        const og_red = dataTurquoise[i];
        const og_green = dataTurquoise[i + 1];
        const og_blue = dataTurquoise[i + 2];

        let r = og_red;
        let g = og_green;
        let b = og_blue;

        if (
          (og_blue > og_green && og_blue > og_red) ||
          og_blue + 50 > og_green
        ) {
          b = og_red;
          r = og_blue;
        } else if (og_green > og_blue && og_green > og_red) {
          b = og_green;
          g = og_blue;
        } else if (og_red > og_blue && og_red > og_green) {
          b = og_red;
          r = og_blue;
        }

        dataTurquoise[i] = r;
        dataTurquoise[i + 1] = g;
        dataTurquoise[i + 2] = b;
      }

      // Apply Red filter
      for (let i = 0; i < dataRed.length; i += 4) {
        const og_red = dataRed[i];
        const og_green = dataRed[i + 1];
        const og_blue = dataRed[i + 2];

        let r = og_red;
        let g = og_green;
        let b = og_blue;

        if (og_blue > og_green && og_blue > og_red && og_green > og_red) {
          r = og_green;
        }
        if (og_blue > og_green && og_blue > og_red && og_red > og_green) {
          g = og_red;
        }

        if (og_green > og_blue && og_green > og_red && og_blue > og_red) {
          r = og_blue;
        }
        if (og_green > og_blue && og_green > og_red && og_red > og_blue) {
          b = og_red;
        }

        if (og_red > og_green && og_red > og_blue) {
          g = og_blue;
        }

        dataRed[i] = r;
        dataRed[i + 1] = g;
        dataRed[i + 2] = b;
      }

      // Put modified data back to canvas
      ctxPurple.putImageData(imageDataPurple, 0, 0);
      ctxTurquoise.putImageData(imageDataTurquoise, 0, 0);
      ctxRed.putImageData(imageDataRed, 0, 0);

      // Convert canvas to image and display
      const filteredImagePurple = document.getElementById(
        "filteredImagePurple"
      );
      filteredImagePurple.src = canvasPurple.toDataURL();
      filteredImagePurple.style.display = "block";

      const filteredImageTurquoise = document.getElementById(
        "filteredImageTurquoise"
      );
      filteredImageTurquoise.src = canvasTurquoise.toDataURL();
      filteredImageTurquoise.style.display = "block";

      const filteredImageRed = document.getElementById("filteredImageRed");
      filteredImageRed.src = canvasRed.toDataURL();
      filteredImageRed.style.display = "block";
    };
    img.src = e.target.result;
  };
  reader.readAsDataURL(file);
});

function applyFilter(filter) {
document.getElementById("filter").value = filter;
document.getElementById("filterForm").submit();
}