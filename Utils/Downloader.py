import Utils.Common as common
import Utils.File as file
import os


def download_definitions(target_directory, url_array):
    # Create folder for downloading into
    file.create_directory(target_directory)

    # Iterate through the url array downloading each zip file
    for url in url_array['urls']:
        print("Downloading from {}".format(url))
        # Split the url by the seperator
        url_split = url.split('/')
        # Get the last element in the url
        filename = url_split[-1]
        # Generate the output file name
        output_filepath = os.path.join(target_directory, filename)
        # Download the file
        common.download(url, output_filepath)
        # Unzip the file, to the same directory
        common.unzip(output_filepath, target_directory)
        # Remove the downloaded zip file
        os.remove(output_filepath)
