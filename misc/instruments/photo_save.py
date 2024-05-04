import os
from typing import NoReturn
from misc.instruments import request_session as session


class PhotoSave:

    def __init__(self) -> NoReturn:
        """
        Initializes the object with default values for the path and headers attributes.

        Parameters:
            self (object): The object being initialized.

        Returns:
            NoReturn: This function does not return anything.
        """
        self.__path = f'data-files/photos/'
        self.__headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'}

    def save_all(self, urls, uid):
        """
        Save all images from the given URLs to a directory based on the provided uid.

        Args:
            urls (list): A list of URLs to download images from.
            uid (str): A unique identifier used to create a directory for saving the images.

        Returns:
            bool: True if all images were successfully saved, False otherwise.
        """
        path = f'{self.__path}/{uid}'
        if not os.path.exists(path):
            os.makedirs(path)
        try:
            for i, url in enumerate(urls, start=1):
                img_data = session.get_session().get(url, headers=self.__headers).content
                with open(f'{path}/{i}.jpg', 'wb') as handler:
                    handler.write(img_data)
        except Exception:
            return False
        else:
            return True
