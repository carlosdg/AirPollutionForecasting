from zipfile import ZipFile
import re
import sys
import os

# Regular expression to find the tag that contains the
# information about the zone
PLACE_INFO_REGEX_FINDER = re.compile(r'<Placemark>((.|\n)*)</Placemark>')

# Regular expression to get the XML coordinates
COORDINATES_REGEX_FINDER = re.compile(r'<coordinates>(.*)</coordinates>')

# Regular expression to get the zone name
PLACE_NAME_REGEX_FINDER = re.compile(r'<name>(.*)</name>')

# File extension for the XML inside the KMZ zip
XML_FILE_EXTENSION_IN_KMZ = '.kml'

def parse_kmz_file(kmz_file_path):
    """
        Opens the given kmz file path and parses the XML file to get the
        value in the 'coordinates' tag

        Args:
            kmz_file_path: kmz file path to parse
            
        Returns:
            A dictionary with the place information
    """
    with ZipFile(kmz_file_path, 'r') as compressed_file:
        # Get all KML files and check that there is only one to parse
        kml_files = [file_name for file_name in compressed_file.namelist() if file_name.endswith(XML_FILE_EXTENSION_IN_KMZ)]
        if len(kml_files) != 1:
            raise RuntimeError(f'Unexpected number of KML files inside KMZ: {len(kml_files)}, {kml_files}')

        # Read the KML file
        kml_file_to_parse = kml_files[0]
        xml_content = compressed_file.read(kml_file_to_parse).decode()
        file_info = { 'name': None, 'coords': None }

        # Parse the info
        try:
            place_info = PLACE_INFO_REGEX_FINDER.search(xml_content).group(1)

            name = PLACE_NAME_REGEX_FINDER.search(place_info)
            if name != None:
                file_info['name'] = name.group(1)
                
            coords = COORDINATES_REGEX_FINDER.search(place_info)
            if coords != None:
                file_info['coords'] = coords.group(1)
        finally:
            return file_info


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print('Usage: python parser.py <file_path> ...')
        exit()

    # Process each KMZ file
    for kmz_file_name in sys.argv[1:]:
        try:
            print(f'Parsing "{kmz_file_name}"...')
            place_info = parse_kmz_file(kmz_file_name)
            print(f'\t{place_info["name"]}: {place_info["coords"]}\n')
        except Exception as error:
            print(f'ERROR {str(error)}\n')