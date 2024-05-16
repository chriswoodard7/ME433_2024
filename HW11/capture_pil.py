from io import BytesIO
from time import sleep
from picamera import PiCamera
from PIL import Image

### Create the in-memory stream

stream = BytesIO()
camera = PiCamera()
camera.start_preview()
sleep(2)

# capture
camera.capture(stream, format='jpeg')

### Rewind stream to beginning to read content
stream.seek(0)
image = Image.open(stream)

# save image
image = image.save("test_pil.jpg")
