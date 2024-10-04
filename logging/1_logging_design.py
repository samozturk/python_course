import logging

import requests


logging.basicConfig(level='DEBUG')

logging.getLogger('urllib3').setLevel('ERROR')

logger = logging.getLogger()

# print(logger)
# print(logger.handlers)


def main(name):
    r = requests.get('https://google.com')
    logger.debug(f'Enter in the main() function, {name=}')



if __name__ == '__main__':
    main('John')