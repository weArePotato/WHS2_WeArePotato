import logging


def log(message, log='info'):
    """
    Logs a message to the console and file, if wish.
    """
    print(message)
    if log == 'error':
        logging.error(message)
    
    elif log == 'debug':
        logging.debug(message)
    
    elif log == 'warning':
        logging.warning(message)
        
    else:
        logging.info(message)


def print_dict(dictionary, logger=False):
    """
    Prints a dictionary in a pretty way.
    """
    for key, value in dictionary.items():
        if logger:
            log(f'{key}: {value}')
        else:
            print(f'{key}: {value}')
