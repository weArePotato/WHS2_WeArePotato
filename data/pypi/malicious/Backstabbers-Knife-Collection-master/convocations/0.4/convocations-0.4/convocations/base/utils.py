from decimal import Decimal
from functools import wraps
from io import StringIO
from itertools import chain
import os
import sys
from typing import Any
import yaml
from termcolor import colored, cprint


def expand_template(local_path, context):
    from jinja2 import Environment, FileSystemLoader
    jenv = Environment(loader=FileSystemLoader(os.getcwd()), lstrip_blocks=True, trim_blocks=True)
    content = jenv.get_template(local_path).render(**context or {})
    return content


def create_owner_string(owner=None, group=None):
    if owner:
        if group:
            return f'{owner}:{group}'
        return f'{owner}:'
    if group:
        return f':{group}'
    return None


def flush_print(st, **kwargs):
    """
    prints a string to stdout and flushes the stdout buffer.
    This is useful where stdout buffering delays the output of certain messages
    :param st: the message to print
    :param kwargs: additional kwargs to pass to the `print` function
    """
    flush = kwargs.pop('flush', True)
    print(st, **kwargs, flush=flush)
    sys.stdout.flush()


g_which_dot = -1


def dot_leader(st, length=40):
    """
    creates a dot leader to suffix a message with so that we get
    nicely aligned output and an easy way to get from message to value
    :param st: the message we are suffixing with the dot leader
    :param length: the field length (i.e., dot leader + len(st) == legnth)
    :return: the suffixed string, including the message + dot leader
    """
    global g_which_dot
    dot_chars = [ '.' ]
    g_which_dot += 1
    g_which_dot %= len(dot_chars)
    dot_char = dot_chars[g_which_dot]
    while length <= len(st):
        length += 10
    dots = dot_char * (length - len(st))
    return f'{st}{dots}'


def notice(st, length=40, **kwargs):
    """
    provides a notification message to the user.  this function is used
    in conjunction with `notice_end` to notify the user that something is
    happening and to await the response.
    :param st: the message that will be noticed to theuser
    :param length: the expected maximum field length for dot leads
    :param kwargs: additional kwargs to provide to `termcolor.cprint`
    :return:
    """
    ending = kwargs.pop('end', None) or ''
    color = kwargs.pop('color', 'blue')
    attrs = kwargs.pop('attrs', None)
    if isinstance(attrs, str):
        attrs = [ attrs ]
    cprint(dot_leader(st, length), end=ending, color=color, attrs=attrs, **kwargs)


def notice_end(st=None, color=None, **kwargs):
    """
    ends the notice cycle.  this function is used
    in conjunction with `notice` to notify the user that something is
    happening and to await the response.
    :param st: the message that will be provided to the user
    :param color: the color of the notification
    :param kwargs: additional kwargs to provide to `termcolor.cprint`
    :return:
    """
    if st:
        cprint(st, color, **kwargs)
    else:
        flush_print('\u2714')


def to_string(value: Any) -> str:
    """
    used by the `print_table` function, this function converts
    a value to a string making sure to format decimal.Decimal and float values
    to 2 decimal places
    :param Any value: the message that will be provided to the user
    :return: the string representation of value
    :rtype: str
    """
    if isinstance(value, (float, Decimal)):
        return f'{value:,.2f}'
    return f'{value}'


def print_table(header, rows, color='cyan'):
    """
    prints a header and rows in a tabular format in the specified color.
    this function is useful for presenting summary information from aws
    commands in a tabular format
    :param list[str] header: a list of strings for the table header
    :param list[Iterable[Any]] rows: a list of list of values to present
    :param str color: the color in which we will print our table
    """
    max_lens = [ 0 ] * len(header)
    rows = [ [ to_string(x) for x in row ] for row in rows ]
    for row in chain([ header ], rows):
        for i, x in enumerate(row):
            max_lens[i] = max(max_lens[i], len(x))
    f_header = []
    for width, x in zip(max_lens, header):
        diff = len(x)
        x = colored(x, color)
        diff = len(x) - diff
        f = f'%-{width + diff}s'
        f = f % (x,)
        f_header.append(f)
    print(' | '.join(f_header))
    print(' | '.join([ colored('-' * width, color) for width in max_lens ]))
    for row in rows:
        f_row = []
        for n, (width, x) in enumerate(zip(max_lens, row)):
            diff = 0
            if n == 0:
                diff = len(x)
                x = colored(x, color)
                diff = len(x) - diff
            f = f'%-{width + diff}s'
            f = f % (x,)
            f_row.append(f)
        print(' | '.join(f_row))


def confirm(message: str) -> bool:
    """
    presents the user with a confirmation message to which the user should
    respond with a YES / NO response
    :param message: the confirmation prompt
    :rtype: bool
    :return: whether the user entered yes or not
    """
    cprint(message, color='red', attrs=['underline'])
    confirmation = input("Please enter 'YES' to confirm and continue: ")
    return confirmation.lower() == 'yes'


def noticed(initial, completion=None):
    def wrap(fn):
        @wraps
        def decorated(*args, **kwargs):
            notice(initial)
            fn(*args, **kwargs)
            notice_end(completion)
        return decorated
    return wrap


def load_yaml(filename: str) -> Any:
    """
    Loads the yaml from filename and returns the relevant object
    :param filename: the name of the file to load
    :return: the constructed yaml object
    """
    with open(filename, 'r') as f:
        return yaml.load(f, yaml.SafeLoader)


def yaml_serializer():
    from ruamel.yaml import YAML
    y = YAML()
    y.indent(sequence=4, mapping=2, offset=2)
    return y


def get_context_value(ctx, key):
    pieces = key.split('.')
    value = ctx
    for piece in pieces:
        try:
            value = getattr(value, piece, None)
        except AttributeError:
            return None
    return value


def dump_yaml(p, buff=None, quiet=True):
    """
    dumps an object as yaml to stdout
    """
    y = yaml_serializer()
    buff = buff or StringIO()
    y.dump(p, buff)
    buff.seek(0)
    if not quiet:
        print(buff.getvalue())
