import os


def iterate_directory(rootdir, filter = None):
    file_list = []
    if filter is None:
        filter = '*'
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            filepath = subdir + os.sep + file
            if filepath.endswith(filter):
                file_list.append(filepath)

    return file_list


def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
