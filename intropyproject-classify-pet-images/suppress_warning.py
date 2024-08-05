import warnings

def suppress_typedstorage_warning():
    """
    Suppresses the specific UserWarning related to TypedStorage.
    This function filters out the warning message:
        "TypedStorage is deprecated" and ignores it.
    
    Parameters:
        None
    
    Returns:
        None
    """
    warnings.filterwarnings("ignore", message="TypedStorage is deprecated")