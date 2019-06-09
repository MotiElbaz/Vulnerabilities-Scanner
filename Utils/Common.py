import urllib.request
import zipfile

def download(file_url_path, file_name):
    urllib.request.urlretrieve(file_url_path, file_name)


def unzip(file_name, folder_output_name):
    zipfile.ZipFile(file_name).extractall(folder_output_name)
