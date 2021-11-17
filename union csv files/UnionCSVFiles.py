import os
import glob
import pandas as pd

"""
    More options to get the "path":
    ----------------------------
    path = input("Enter here directory path:")
    OR
    path = "./"   --> run from current directory
    OR
    path = "..."
"""
"""
    More options to get the data type:
    ----------------------------
    data_type = input("Enter here type of data [Security Positions, Security Movements, Cash Positions or Cash Movements] :")
    OR
    data_type = "FILE_TYPE_1"
"""


def unionCsvs(path, data_type):
    os.chdir(path)

    # Define the pattern of files we want to connect
    extension = 'csv'

    # Save the list of all files with the extension defined above
    """
    from one folder only:
    --------------------
    all_filenames = [i for i in glob.glob('*' + data_type + '*.{}'.format(extension))]
    """
    all_filenames = [i for i in glob.glob(path + '/**/*' + data_type + '*.{}'.format(extension), recursive=True)]

    # combine all files in the list
    combined_csv = pd.concat([pd.read_csv(f, error_bad_lines=False) for f in all_filenames])

    # export to new csv file
    csv_file_name = path + "/combined-" + data_type + ".csv"
    combined_csv.to_csv(csv_file_name, index=False, encoding='utf-8-sig')
    print(data_type + " complete!")


def do_for_all():
    # Here we define the directory path of the CSV files.
    path = input("Enter directory path of data: ")

    # Here we define the desired type of data according to the file name.
    data_type = ("TYPE_1", "TYPE_2")

    [unionCsvs(path, t) for t in data_type]


if __name__ == '__main__':
    do_for_all()
