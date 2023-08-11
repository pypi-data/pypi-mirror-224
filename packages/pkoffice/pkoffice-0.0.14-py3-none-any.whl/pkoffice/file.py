import os
import re
import time
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
    Function to delete proper file if it exists.
    :param path: path to proper file
    :return: None
    """
    if os.path.isfile(path):
        os.remove(path)


def files_download_wait(directory: str, file_name: str, timeout_seconds: int,
                        nfiles: int = None):
    """
    Function to wait for files which are downloading.
    :param directory: path to folder where file will be downloaded
    :param file_name: name of the downloading file
    :param timeout_seconds: time computer will be wait if something go wrong
    :param nfiles: number of files
    :return: None
    """
    seconds = 0
    dl_wait = True
    while dl_wait and seconds < timeout_seconds:
        time.sleep(1)
        dl_wait = False
        files = os.listdir(directory)
        if nfiles and len(files) != nfiles:
            dl_wait = True
        if file_name not in files:
            dl_wait = True
        for fname in files:
            if fname.endswith('.crdownload'):
                dl_wait = True
        seconds += 1
    return seconds