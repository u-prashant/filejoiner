class APP:
    NAME = 'File Joiner'
    SOURCE_STATIC_LABEL = 'Files To Join'
    TARGET_STATIC_LABEL = 'Destination Folder'
    SELECT_RAW_FILES = 'Select Files'
    SELECT_DESTINATION_FOLDER = 'Select Destination Folder'
    NO_FILES_SELECTED = 'No Files Selected'
    NO_DIR_SELECTED = 'No Directory Selected'
    BROWSE = 'Browse'
    EXIT = 'Exit'
    JOIN_FILES = 'Join Files'
    SHEET_NAME_LABEL = 'Enter Sheet Name (if multiple sheets)'
    PREFIX_LABEL = 'Enter Prefix for the generated file'


class Files:
    RAW_FILES = 'raw_files_path'
    OUTPUT_FILE = 'output_file_path'
    CONFIG_FILE = 'config_file_path'


class Colors:
    AZURE3 = 'azure3'
    AZURE4 = 'azure4'
    BLUE = 'blue'
    WHITE = 'white'
    GRAY25 = 'gray25'


class Errors(Exception):
    RawFileNotProvided = 'Raw File Path not provided'
    OutputFileNotProvided = 'Output File Path not provided'
    ConfigurationFileNotFound = 'Config File not provided'

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
