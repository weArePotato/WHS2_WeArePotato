from os.path import abspath, dirname, join

from raft.collection import Collection
from convocations.base.utils import load_yaml


ns = Collection()

filename = dirname(dirname(abspath(__file__)))
filename = join(filename, 'conf', 'convocations.yml')
conf = load_yaml(filename)
ns.configure(conf)
