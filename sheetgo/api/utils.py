import os


def validate_zero_file_size(stream):
    chunk = stream.read(1)
    stream.seek(0)
    if not len(chunk):
        return False
    return True


def file_loader(filename, binary=False):
    """Loads data from file"""
    read_option = 'r'
    if binary:
        read_option = 'rb'

    with open(filename, read_option) as f:
        data = f.read()

    return data


def split_filename(filename):
    return os.path.splitext(filename)[0], os.path.splitext(filename)[1]


def remove_dot(ext):
    return ext[1: len(ext)]
