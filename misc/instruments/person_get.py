from bs4 import BeautifulSoup
import uuid
from typing import NoReturn
from misc.instruments import request_session as session


class GetPerson:
    def __init__(self) -> NoReturn:
        """
        Initialize the object with default headers.
        """
        self.__headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'}

    def get_person_data(self, url: str) -> tuple or bool:
        """
        A function to retrieve person data from a given URL.

        Parameters:
            self (object): The instance of the class.
            url (str): The URL to fetch the person data from.

        Returns:
            tuple: A tuple containing the person data dictionary, list of links, and a unique identifier.
                   If an exception occurs during the process, it returns False.
        """
        data_frame, links, uid = dict(), list(), str(uuid.uuid4())
        try:
            soup_object = BeautifulSoup(session.get_session().get(url, headers=self.__headers).text, 'lxml')
            data_frame['ФИО'] = [soup_object.title.text.split(" - ")[0]]
            for elem in soup_object.find_all('div' and 'b'):
                key, value = elem.parent.find('b').text, elem.parent.text
                data_frame[key] = [value.replace(key, '').strip()]
            data_frame['фото id'] = [uid]
            data_frame['На сайте'] = [url]
            for link in soup_object.find_all('a'):
                actual = link.get('href')
                if str(actual).endswith('.jpg'):
                    links.append(str(actual))
        except Exception:
            return False
        else:
            return data_frame, links, uid

