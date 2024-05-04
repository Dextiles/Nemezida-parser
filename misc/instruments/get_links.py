from bs4 import BeautifulSoup
from typing import NoReturn
from misc.instruments import request_session as session


class LinksParser:
    def __init__(self, url: str) -> NoReturn:
        """
        Initialize the WebCrawler object with the provided URL.

        Parameters:
            url (str): The URL to start crawling from.

        Returns:
            None
        """
        self.__headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'}
        self.links_on_pages = list()
        self.__url = url
        self.__all_links = list()
        self.__exit_recursion = False

    def __get_links_from_page(self, page_link: str) -> NoReturn:
        """
        Get links from a given page and store them in the class instance.

        Args:
            page_link (str): The link to the page from which to extract links.

        Returns:
            NoReturn: This function does not return anything.
        """
        self.links_on_pages.append(page_link)
        for i, link in enumerate(self.links_on_pages):
            soup_object = BeautifulSoup(session.get_session().get(link, headers=self.__headers).text, 'lxml')
            person_links = soup_object.find_all('h3', {'class': 'simple-grid-grid-post-title'})
            self.__all_links.extend([elem.find('a').get('href') for elem in person_links])

    def __get_pages_links(self, url: str):
        """
        Given a URL, this function retrieves the HTML content of the page
        using the provided headers and parses it using BeautifulSoup.
        It then finds the 'next' page link and appends it to the list of links on pages.
        If the 'next' link is not found, the recursion is stopped.
        The function does not take any parameters and does not return anything.
        """
        soup_object = BeautifulSoup(session.get_session().get(url, headers=self.__headers).text, 'lxml')
        try:
            next_page = soup_object.find('a', {'class': 'next page-numbers'}).get('href')
        except AttributeError:
            self.__exit_recursion = True
            return
        else:
            self.links_on_pages.append(next_page)
            self.__get_pages_links(next_page)
            if self.__exit_recursion:
                return

    def get_all_links(self) -> NoReturn:
        """
        Retrieves all links from the specified URL and its pages. Returns a list of links.
        """
        print(f'Парсинг ссылок со страниц раздела {self.__url}. Это может занять некоторое время.')
        self.__get_pages_links(self.__url)
        self.__get_links_from_page(self.__url)
        return self.__all_links
