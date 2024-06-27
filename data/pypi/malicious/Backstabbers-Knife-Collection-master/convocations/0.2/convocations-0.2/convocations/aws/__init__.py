from raft.collection import Collection
from .codebuild import codebuild_collection
from .codebuild import global_collection as global_codebuild
from . import codebuild, rds
from . import codedeploy
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
from .cfn import import_ecs_service
from .cfn import import_code_pipeline
from .cfn import stack_commands
from . import mgn
from . import transit_gateway
from . import ram
from .ssm import runners as ssm_runners
from . import s3
from . import organizations
from . import route53
from . import vpc_peering
from .route53 import zone_parser
from . import reservations
from .ec2 import routing
from .ec2 import ssh


ns = Collection()
ns.add_collection(codebuild_collection, 'codebuild')
ns.add_tasks(codebuild.build)
ns.add_tasks(codedeploy)
ns.add_tasks(ec2)
ns.add_tasks(elb)
ns.add_tasks(iam)
ns.add_tasks(import_instance)
ns.add_tasks(import_route_table)
ns.add_tasks(import_security_group)
ns.add_tasks(import_subnet)
ns.add_tasks(import_vpc)
ns.add_tasks(import_ecs_service)
ns.add_tasks(mgn)
ns.add_tasks(stack_commands)
ns.add_tasks(transit_gateway)
ns.add_tasks(open_id)
ns.add_tasks(ami_helpers)
ns.add_task(new_key_pair)
ns.add_task(ssm_runners.run_posh)
ns.add_tasks(ram)
ns.add_tasks(s3)
ns.add_tasks(organizations)
ns.add_tasks(route53)
ns.add_tasks(zone_parser)
ns.add_tasks(vpc_peering)
ns.add_tasks(import_code_pipeline)
ns.add_tasks(rds)
ns.add_tasks(reservations)
ns.add_tasks(routing)
ns.add_tasks(ssh)
