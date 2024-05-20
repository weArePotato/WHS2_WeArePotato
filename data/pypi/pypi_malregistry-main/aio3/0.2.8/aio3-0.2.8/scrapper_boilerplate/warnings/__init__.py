import sys
import warnings

def disable_warnings():
    """
    Disable all warnings
    
    Returns: None
    """
    if not sys.warnoptions:
        warnings.simplefilter("ignore")
