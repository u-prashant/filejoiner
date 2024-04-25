import os
import pickle
from constants import Errors


class Config:
    def __init__(self, config_file):
        self.config_file = config_file
        self.source_dir = '/'
        self.target_dir = '/'
        self.prefix = ''
        self.sheet_name = ''
        self.read()

    def read(self):
        try:
            with open(self.config_file, 'rb') as f:
                self.source_dir, self.target_dir, self.prefix, self.sheet_name = pickle.load(f)
        except:
            print(Errors.ConfigurationFileNotFound)

    def write(self):
        with open(self.config_file, 'wb') as f:
            pickle.dump([self.source_dir, self.target_dir, self.prefix, self.sheet_name], f)

    def set_source_dir(self, path):
        self.source_dir = self.get_directory(path)

    def set_target_dir(self, directory):
        self.target_dir = directory

    def set_prefix(self, prefix):
        self.prefix = prefix

    def set_sheet_name(self, sheet_name):
        self.sheet_name = sheet_name

    @staticmethod
    def get_directory(text):
        paths = text.split('\n')
        if not os.path.exists(paths[0]):
            return '/'
        return os.path.split(paths[0])[0]
