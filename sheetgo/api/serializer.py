from sheetgo.api.utils import validate_zero_file_size, split_filename, remove_dot


class FileSerializerException(Exception):
    pass


class FileSerializer:
    def __init__(self, the_file, ext: list, request_format=None):
        self.the_file = the_file
        self.ext = ext
        self.request_format = request_format

    def _has_file_in_request(self):
        if 'file' not in self.the_file:
            raise FileSerializerException('a file is required')

    def _has_a_valid_file(self):
        if self.the_file['file'].filename == '' or not validate_zero_file_size(self.the_file['file']):
            raise FileSerializerException('did you try to send a file?')

    def _is_filename_valid(self):
        filename, file_ext = split_filename(self.the_file['file'].filename)
        if remove_dot(file_ext) not in self.ext:
            raise FileSerializerException('unsupported file format')

    def _has_format(self):
        if 'format' not in self.request_format:
            raise FileSerializerException('a format is required')

    def _validate_request_format(self):
        if self.request_format['format'] not in self.ext:
            raise FileSerializerException('unsupported conversion format')

    def is_valid(self):
        self._has_file_in_request()
        self._has_a_valid_file()
        self._is_filename_valid()

        if self.request_format is not None:
            self._has_format()
            self._validate_request_format()
