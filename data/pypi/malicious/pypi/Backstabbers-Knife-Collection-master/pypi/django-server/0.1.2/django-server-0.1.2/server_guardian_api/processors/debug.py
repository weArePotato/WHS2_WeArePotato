"""Some processors for debugging and testing."""

from ..constants import SERVER_STATUS


def exception_processor():  # pragma: no cover
    """This processor is only useful to test."""
    raise Exception('Something went wrong.')


def dummy_processor():  # pragma: no cover
    """Use this processor to test, that you've set up everything correct."""
    return {
        'label': 'Dummy',
        'status': SERVER_STATUS['OK'],
        'info': 'This is a dummy response.'
    }
