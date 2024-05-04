from misc import parser_body
from misc.instruments.get_links import LinksParser


start_endpoints = [
    'https://nemez1da.ru/voennoplennye/',
    'https://nemez1da.ru/voennye-prestupniki/',
    'https://nemez1da.ru/naczistskie-podrazdeleniya/',
    'https://nemez1da.ru/posobniki/',
    'https://nemez1da.ru/inostrannye-posobniki-i-naemniki/',
    'https://nemez1da.ru/posobniki/network-terrorists/'
]

if __name__ == '__main__':
    links = list()
    for endpoint in start_endpoints:
        links.extend(LinksParser(endpoint).get_all_links())
    parser = parser_body.Parser(links)
    parser.parse()
