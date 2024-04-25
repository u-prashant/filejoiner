import os
from datetime import datetime


def get_file_location(directory, prefix):
    current_time = datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
    return os.path.join(directory, '{}_{}.xlsx'.format(prefix, current_time))


def get_extension_from_filename(file):
    _, extension = os.path.splitext(file)
    return extension
