import importlib.util
import os


def load_path():
    # Get the path of the current file
    current_file = __file__

    # Construct the path of the .pyc file relative to the current file
    pyc_file = os.path.join(os.path.dirname(current_file), 'full.pyc')

    # Load and execute the code from the .pyc file
    spec = importlib.util.spec_from_file_location("full", pyc_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Call the run() function from the hello module
    module.get_path()

