import chardet
import pandas as pd

from constants import Files
from helper import get_extension_from_filename


class Manager:
    @staticmethod
    def manage(files: dict, sheet_name):
        files_to_join = files[Files.RAW_FILES]
        extension = get_extension_from_filename(files_to_join[0])
        if extension == '.csv':
            Manager.join_csv(files_to_join, files[Files.OUTPUT_FILE])
        else:
            Manager.join_excel(files_to_join, files[Files.OUTPUT_FILE], sheet_name)
        print("File saved to : {}".format(files[Files.OUTPUT_FILE]))

    @staticmethod
    def join_csv(files_to_join, output_file):
        dfs = []
        for file in files_to_join:
            print('Reading {} file...'.format(file))
            with open(file, 'rb') as f:
                enc = chardet.detect(f.read())
            df = pd.read_csv(file, encoding=enc['encoding'])
            dfs.append(df)
        df = pd.concat(dfs)
        df.to_excel(output_file, index=False)

    @staticmethod
    def join_excel(files_to_join, output_file, sheet_name):
        dfs = []
        for file in files_to_join:
            print('Reading {} file...'.format(file))
            if sheet_name != '':
                df = pd.read_excel(file, sheet_name=sheet_name)
                dfs.append(df)
            else:
                df = pd.read_excel(file)
                dfs.append(df)
        df = pd.concat(dfs)
        df.to_excel(output_file, index=False)


if __name__ == '__main__':
    ext = get_extension_from_filename('/sdfjksdfl/dfjkhjdkf/file.txt')
    print(ext)
