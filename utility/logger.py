import logging


def get_logger(name: str):
    logger = logging.getLogger(name)

    log_level = logging.INFO
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)

    logger.setLevel(log_level)
    logger.addHandler(console_handler)

    return logger