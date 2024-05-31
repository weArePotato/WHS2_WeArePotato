from raft.collection import Collection
from .codebuild import codebuild_collection
from .codebuild import global_collection as global_codebuild
from . import codebuild
from . import ec2
from . import elb
from . import iam
from . import ami_helpers
from . import open_id
from .keypairs import new_key_pair
from .cfn import import_instance
from .cfn import import_route_table
from .cfn import import_security_group
from .cfn import import_subnet
from .cfn import import_vpc
from .cfn import stack_commands
from . import mgn
from .ssm import runners as ssm_runners


ns = Collection()
ns.add_collection(codebuild_collection, 'codebuild')
ns.add_tasks(codebuild.build)
ns.add_tasks(ec2)
ns.add_tasks(elb)
ns.add_tasks(iam)
ns.add_tasks(import_instance)
ns.add_tasks(import_route_table)
ns.add_tasks(import_security_group)
ns.add_tasks(import_subnet)
ns.add_tasks(import_vpc)
ns.add_tasks(mgn)
ns.add_tasks(stack_commands)
ns.add_tasks(open_id)
ns.add_tasks(ami_helpers)
ns.add_task(new_key_pair)
ns.add_task(ssm_runners.run_posh)
