import pandas as pd
from datetime import datetime
import openpyxl
import os
from typing import NoReturn


class FilesSaver:

    def __init__(self, data_frame: pd.DataFrame, data_folder_name='data-files') -> NoReturn:
        """
        Initializes the object with the given data frame and data folder name.
        If the data folder does not exist, it is created.
        Sets the path for the Excel file based on the current date.
        Saves an empty Excel file at the specified path.
        Sets the data frame for the object.
        """
        if not os.path.exists(data_folder_name):
            os.makedirs(data_folder_name)
        self.__path = f'{data_folder_name}/{datetime.now().strftime("%d.%m.%Y")}.xlsx'
        openpyxl.Workbook().save(self.__path)
        self.__data_frame = data_frame

    def save(self) -> bool:
        """
        Save the data frame to an Excel file at the specified path and return True if successful, otherwise return False.
        """
        try:
            self.__data_frame.to_excel(self.__path, index=False)
        except Exception:
            return False
        else:
            return True
