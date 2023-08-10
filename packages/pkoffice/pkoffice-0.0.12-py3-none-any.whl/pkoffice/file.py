import os
import re
import shutil


def files_delete_directory(directory_path: str) -> int:
    """
    Function to delete all files in indicated directory.
    :param directory_path: path to indicated folder
    :return: 1 - as success, 0 - as failure
    """
    try:
        with os.scandir(directory_path) as entries:
            for entry in entries:
                if entry.is_file():
                    os.unlink(entry.path)
        return 1
    except OSError:
        return 0


def files_copy_directory(path_source, path_destination, filter_re=None) -> int:
    """
    Function to copy all files from one directory to another.
    :param path_source: path to folder from files will be copied
    :param path_destination: path to folder where files will be copied
    :param filter_re: optional filter to indicate what files should be copied
    :return: 1 - as success, 0 - as failure
    """
    try:
        files = os.listdir(path_source)
        for fname in files:
            if re.search(filter_re, fname) or filter is None:
                shutil.copy2(os.path.join(path_source, fname), path_destination)
        return 1
    except OSError:
        return 0


def file_delete(path: str) -> None:
    """
    FUnction to delete proper file if it exists.
    :param path: path to proper file
    :return: None
    """
    if os.path.isfile(path):
        os.remove(path)