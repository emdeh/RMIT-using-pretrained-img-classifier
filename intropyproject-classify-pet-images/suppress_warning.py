import warnings

def suppress_typedstorage_warning():
    # Suppress the specific UserWarning related to TypedStorage
    warnings.filterwarnings("ignore", message="TypedStorage is deprecated")