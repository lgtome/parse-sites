import re
from bs4 import BeautifulSoup
import requests
from helpers import whitespace_regex, convert_to_tuple, space_transforme, link

mirrors = {'mirror_1': {'url': 'https://thepiratebay.party/search/{}', 'separator': '%20'},
           'mirror_2': {'url': 'https://www1.thepiratebay3.to/s/?q={}', 'separator': '+'}}


def split_string(string: str):
    regex = "(.* > .+)|('')|('\w{0,8}')"
    try:
        re.search(regex, string).group()
        return None
    except:
        if len(string) > 10:
            return string
    # if len(array_of_string) % 2 == 0:
    #     return array_of_string[1]
    # else:
    #     return array_of_string[2]


def find_urls(node):
    obj = {}
    result = []
    result_urls = {}
    try:
        for td_node in node.find('table').find_all('td'):
            if td_node.find('a'):
                name = split_string(td_node.find('a').text)
                link = td_node.find('a')['href']
                if name:
                    obj.update({name: link})

        for torrent in obj:
            if re.search('/torrent/', obj[torrent]):
                result_urls.update({torrent: obj[torrent]})
        return result_urls
    except:
        print('No results found :(')


def get_node_from_response(search, url: str):
    respons = requests.post(url.format(search)).text
    return BeautifulSoup(respons, features='html.parser')


def execute(searched_string: str):
    res = {}
    splitted_search = convert_to_tuple(
        re.split(whitespace_regex, searched_string.strip()))
    for mirror in mirrors:
        url_search = space_transforme(
            splitted_search, symbol=mirrors[mirror]['separator'])
        urls = find_urls(get_node_from_response(
            url_search, mirrors[mirror]['url']))
        if urls:
            res.update(urls)

    return res
