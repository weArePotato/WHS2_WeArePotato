""" requests_viewer; able to show how requests look like """

__project__ = "requests_viewer"
__version__ = "0.1.0"

from requests_viewer.main import main
from requests_viewer.main import view

try:
    from requests_viewer.web import get_tree
    from requests_viewer.web import view_tree
    from requests_viewer.web import view_html
    from requests_viewer.web import view_node
    import lxml.html

    lxml.html.HtmlElement.view = view_tree
except ImportError:
    print("Cannot import `lxml`, limited functionality.")
