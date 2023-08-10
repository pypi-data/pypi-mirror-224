import logging


def configure_logging():
    logging.basicConfig(filename='mi_log.txt', level=logging.ERROR,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    file_handler = logging.FileHandler('mi_log.txt')
    file_handler.setLevel(logging.ERROR)

    logger = logging.getLogger()
    logger.addHandler(file_handler)
