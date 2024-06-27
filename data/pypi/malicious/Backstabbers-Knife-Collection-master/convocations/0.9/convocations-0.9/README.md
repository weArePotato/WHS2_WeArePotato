# convocations

a set of [`invoke`](https://pypi.org/project/invoke)-inspired, [`raft`](https://pypi.org/project/raft)-based convocations that we hope
can help make development and devops a little easier.  brought to you
by the m&a team at cscgh.


## pypi

useful utilities when working on projects intended to be published in a
python repository like pypi

### pypi.template

creates a template project that you can use to create packages / modules
that will be deployed to pypi or another python repository.  

## python

useful utilities to make life easier for those getting started with using
a repository.

### python.setup

creates a standard virtual environment for running the project

### python.build

builds the project using setup.py or pyproject.toml

### python.clean

cleans any builds

### python.test

runs test via pytest and prints out a coverage report

### python.bump_version

bumps the current version of the project via bumpversion

### python.upload

uploads any distribution via twine

### python.publish

a handy combination of clean, test, build, version, upload

## aws

### configuration keys

| name                       | description                                                                                                                                                                    |
|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| convocations.prefix        | a handy prefix used in output and the directory in which cfn templates / parameters can be found                                                                               |
| aws                        | object                                                                                                                                                                         |
| aws.profile                | the profile to use when creating boto3 sessions                                                                                                                                |
| aws.start_url              | the sso start url                                                                                                                                                              |
| aws.account_id             | the target account id for sso                                                                                                                                                  |
| aws.sso_account_id         | an alias for account_id                                                                                                                                                        |
| aws.sso_region             | the region in which sso is configured                                                                                                                                          |
| aws.sso_start_url          | an alias for start_url                                                                                                                                                         |
| aws.role                   | the role which we will assume after sso is completed, if unspecified, we will take the first role alphabetically                                                               |
| aws.sso_role_name          | an alias for role                                                                                                                                                              |
| aws.global_parameter_files | files that contain parameters that should be loaded by default when using cloudformation.  by convention the file at convocation.prefix/params/global.yml will also be loaded. |


## palo_alto

## todd

## fortigate

## checkpoint

## xkcd

