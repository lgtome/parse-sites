from os import path
from lib.pirate_bay import execute
import eel


eel.init(path.join(path.dirname(__file__), 'public'))


@eel.expose
def parse_sites(data):
    return execute(data)


eel.start('index.html')
# user_input = input()
# first_mirror_result = execute(user_input)


# if first_mirror_result:
#     for f_url in first_mirror_result:
# print(link(f_url), '\n')
