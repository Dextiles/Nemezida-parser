from datetime import datetime
from typing import NoReturn


class Logger:
    def __init__(self) -> NoReturn:
        """
        Initialize the class instance.
        """
        self.__counter = 0

    def to_log(self, process: str, status: str, url='') -> NoReturn:
        """
        Logs the given process and status information to the console.

        Args:
            process (str): The name of the process.
            status (str): The status of the process.
            url (str, optional): The URL associated with the process. Defaults to ''.

        Returns:
            None
        """
        self.__counter += 1
        time = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
        if url == '':
            print(f'{self.__counter}) {time} - Процесс: {process} - Статус: {status}')
        else:
            print(f'{self.__counter}) {time} - Процесс: {process} - URL: {url} - Статус: {status}')
