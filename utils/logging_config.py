import logging


def log_message(level, message):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    if level == 'info':
        logger.info(message)
    elif level == 'error':
        logger.error(message)
    elif level == 'warning':
        logger.warning(message)