
def validate_zero_file_size(stream):
    chunk = stream.read(1)
    stream.seek(0)
    if not len(chunk):
        return False
    return True
