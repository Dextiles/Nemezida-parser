import pandas as pd
from typing import NoReturn


class DataFrameCombiner:
    def __init__(self) -> NoReturn:
        """
        Initializes the class instance with an empty pandas DataFrame.
        """
        self.__data_frame = pd.DataFrame()

    @property
    def data_frame(self) -> pd.DataFrame:
        """
        A property that returns the data frame associated with this object.
        Returns:
            pd.DataFrame: The data frame associated with this object.
        """
        return self.__data_frame

    def add(self, data_frame: pd.DataFrame) -> NoReturn:
        """
        Adds a DataFrame to the existing DataFrame.

        Parameters:
            data_frame (pd.DataFrame): The DataFrame to be added.

        Returns:
            None
        """
        self.__data_frame = pd.concat([self.__data_frame, pd.DataFrame(data_frame)], ignore_index=True, axis=0)
