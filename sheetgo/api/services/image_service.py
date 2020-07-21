import io

from PIL import Image


class ImageService:
    """
        The idea here is to create a service that could be used with injector.
        This has only two methods and no constructor because it only converts a simple image.
        In a real world application this service probably would have a bunch of other helpful methods.
    """
    @staticmethod
    def convert_from_jpeg_to_png(the_file):
        im = Image.open(the_file)
        rgb_im = im.convert('RGB')
        output = io.BytesIO()
        rgb_im.save(output, format='PNG')
        return output.getvalue()

    def convert_from_png_to_jpeg(self):
        pass
