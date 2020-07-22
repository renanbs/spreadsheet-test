import io

import PIL
from PIL import Image


class ImageServiceException(Exception):
    pass


class ImageService:
    """
        The idea here is to create a service that could be used with injector.
        This has only two methods and no constructor because it only converts a simple image.
        In a real world application this service probably would have a bunch of other helpful methods.
    """
    @staticmethod
    def _convert_image(the_file, file_format):
        try:
            im = Image.open(the_file)
            rgb_im = im.convert('RGB')
            output = io.BytesIO()
            rgb_im.save(output, format=file_format)
            return output.getvalue()
        except (PIL.UnidentifiedImageError, ValueError, Exception):
            raise ImageServiceException('could not convert image')

    def convert_image(self, the_file, file_format):
        if file_format in ['png', 'PNG']:
            return self._convert_image(the_file, 'PNG')
        else:
            return self._convert_image(the_file, 'JPEG')
