from dataclasses import dataclass
from typing import List

from raft import task


@dataclass
class Recordset:
    hosted_zone_name: str = None
    type_: str = None
    name: str = None
    ttl: str = None
    resource_records: List[str] = None

    @property
    def normalized_name(self):
        name = self.name
        if not name.endswith('.'):
            name = f'{name}.'
        return name

    @property
    def normalized_hosted_zone_name(self):
        name = self.hosted_zone_name
        if not name.endswith('.'):
            name = f'{name}.'
        return name

    @property
    def logical_name(self):
        name = self.normalized_name
        pieces = name.split('.')[:-3]
        if pieces:
            pieces = [ x.replace('_', 'underscore').title() for x in pieces ]
            rg = []
            for x in pieces:
                x = ''.join([ lx.title() for lx in x.split('-') ])
                rg.append(x)
            pieces = rg
            lname = ''.join(pieces)
        else:
            type_ = self.type_.title()
            lname = f'Apex{type_}'
        return lname

    @property
    def logical_name_with_type(self):
        name = self.normalized_name
        pieces = name.split('.')[:-3]
        if pieces:
            pieces = [ x.replace('_', 'underscore').title() for x in pieces ]
            rg = []
            for x in pieces:
                x = ''.join([ lx.title() for lx in x.split('-') ])
                rg.append(x)
            pieces = rg
            pieces.append(self.type_.title())
            lname = ''.join(pieces)
        else:
            type_ = self.type_.title()
            lname = f'Apex{type_}'
        return lname

    def cfn(self):
        properties = dict(
            HostedZoneName=self.normalized_hosted_zone_name,
            Name=self.normalized_name,
            TTL=self.ttl,
            Type=self.type_,
            ResourceRecords=self.resource_records,
        )
        data = {
            self.logical_name: {
                'Type': 'AWS::Route53::RecordSet',
                'Properties': properties,
            },
        }
        return data


def parse_zone_line(st):
    pieces = st.split(' ', 4)
    name = pieces[0]
    if not name.endswith('.'):
        name = f'{name}.'
    hosted_zone_name = name.split('.')[-3:]
    hosted_zone_name = '.'.join(hosted_zone_name)
    if '"' in pieces[-1]:
        values = pieces[-1].split('"')[1::2]
        values = [ f'"{x}"' for x in values ]
    else:
        values = [ pieces[-1] ]
    return Recordset(
        hosted_zone_name=hosted_zone_name,
        name=name,
        ttl=pieces[1],
        type_=pieces[3],
        resource_records=values,
    )


@task
def parse_zone_file(ctx, filename):
    """
    parses a zone file and reformats as a cloudformation template
    """
    from convocations.base.utils import dump_yaml
    with open(filename, 'r') as f:
        raw_lines = f.readlines()
    lines = [ x.strip() for x in raw_lines if not x.startswith(';') ]
    resources = {}
    recordsets = {}
    for x in lines:
        recordset = parse_zone_line(x)
        names = [ recordset.logical_name, recordset.logical_name_with_type ]
        for logical_name in names:
            if logical_name not in recordsets:
                recordsets[logical_name] = recordset
                break
            r = recordsets[logical_name]
            if r.type_ == recordset.type_:
                r.resource_records += recordset.resource_records
                break

    for x in recordsets.values():
        cfn = x.cfn()
        resources.update(cfn)
    cfn = dict(AWSTemplateFormatVersion='2010-09-09', Resources=resources)
    dump_yaml(cfn)

