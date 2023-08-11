import os


def close_excel_instances() -> int:
    """
    Function will close all opened MS Excel instances.
    :return: None
    """
    os.system(f'taskkill /F /IM Excel.exe')