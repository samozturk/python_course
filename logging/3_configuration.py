import logging
import logging.handlers
import logging.config

from settings import logger_config

logging.config.dictConfig(logger_config)


logger = logging.getLogger('app_logger')




# logger.setLevel('DEBUG')

# std_format = logging.Formatter(
#     # fmt='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
#     fmt='{asctime} - {levelname} - {name} - {message}',
#     style='{'
# )

# console_handler = logging.StreamHandler()
# logger.addHandler(console_handler)
# console_handler.setFormatter(std_format)

# file_handler = logging.handlers.RotatingFileHandler(
#     'debug.log',
#     maxBytes=100,
#     backupCount=5
# )
# logger.addHandler(file_handler)
# file_handler.setFormatter(std_format)





def main():
    logger.debug('Enter: main()')


if __name__ == '__main__':
    main()