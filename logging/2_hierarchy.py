import logging


# root_logger = logging.getLogger()
# print(root_logger)
# print(type(root_logger))


# root.app_logger.utils
logging.basicConfig()

app_logger = logging.getLogger('app_logger')


f = logging.Formatter(
    fmt='%(levelname)s - %(name)s - %(message)s'
)

console_handler = logging.StreamHandler()
console_handler.setFormatter(f)
app_logger.addHandler(console_handler)


utils_logger = logging.getLogger('app_logger.utils')
utils_logger.setLevel('DEBUG')

app_logger.propagate = False


def main():
    utils_logger.debug('Hello world')


if __name__ == '__main__':
    main()
