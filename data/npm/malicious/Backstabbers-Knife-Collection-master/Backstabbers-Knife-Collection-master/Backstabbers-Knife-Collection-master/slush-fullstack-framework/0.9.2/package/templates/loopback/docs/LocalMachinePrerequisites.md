# Local Machine Prerequiites

## Mininum version of prerequisites

| Software | Mininum version |
| --- | --- |
| Mac OSX | 10.12 |
| git | 2.14.1 |
| git-flow | 0.4.1 |
| docker | 1.30 |
| docker-compose | 1.14 |
| nvm | 6.11.0 |
| rbenv | 1.1.1 |
| ruby | 2.4.1 |
| cucumber | 2.4.0 |

## Mac OSX

It is expected developer will use This framework in Mac OSX 10.12 or above.

## Git

Please make sure you have git client tool ver 2.14.1 or above installed.

You can check your git version as follow:

```shell
$ git --version
git version 2.14.1
```

If you cannot find git installed in your local machine, please use brew to install latest git.

```shell
$ brew install git
```

## Git Flow

You can install git-flow using homebrew:

```shell
$ brew install git-flow
```
## Docker

To adapt DevOps practice, this framework use docker and docker-compose tools to streamline local devleopment environment and future continuous deployment.

The following command is used to check docker and docker-compose version.

```shell
$ docker version
Client:
 Version:      17.06.1-ce
 API version:  1.30
 Go version:   go1.8.3
 Git commit:   874a737
 Built:        Thu Aug 17 22:53:38 2017
 OS/Arch:      darwin/amd64

Server:
 Version:      17.06.1-ce
 API version:  1.30 (minimum version 1.12)
 Go version:   go1.8.3
 Git commit:   874a737
 Built:        Thu Aug 17 22:54:55 2017
 OS/Arch:      linux/amd64
 Experimental: true

$ docker-compose version
docker-compose version 1.14.0, build c7bdf9e
docker-py version: 2.3.0
CPython version: 2.7.12
OpenSSL version: OpenSSL 1.0.2j  26 Sep 2016
```

If any error found in the above step, please download Docker Community Edition for Mac at [Docker Store](https://store.docker.com/editions/community/docker-ce-desktop-mac).

## NVM

```shell
$ curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.2/install.sh | bash
```

Add the following code segment in .bash_profile

```bash
export NVM_DIR="$HOME/.nvm"
export PATH=$NVM_DIR:$PATH
source $NVM_DIR/nvm.sh
```

Use nvm to install latest NodeJS

```shell
$ nvm install 8
$ nvm use 8
```

## Cucumber

With BDD practice, each user story and acceptance criteria should be documented before coding.  Cucumber feature file can be used to document each user story.  Afterward, the team should document each scenario and Given, WHen, Then statement to describe whole user journey using Gherkin language.

### Ruby

Even Cucumber can support Javascript and Java, this framework uses Ruby version in order to leverage pre-defined steps bundled with plugins like cucumber-api, selenium-cucumber, Calaba.sh, etc.

The following steps are used to install ruby in your local machine.

```shell
$ brew install rbenv ruby-build
$ rbenv install 2.4.1
$ rbenv global 2.4.1
$ ruby -v
```

Add the following code segment in .bash_profile.

```bash
if which rbenv > /dev/null
then
  eval "$(rbenv init -)";
fi
```

### Install Cucumber

The following steps are used to install cucumber.

```shell
$ rbenv global 2.4.1
$ gem install cucumber
```

### Install Cucumber API plugin for pre-defined steps

The following steps are used to install cucumber-api plugin.

```shell
$ rbenv global 2.4.1
$ gem install cucumber-api
```

### Install Cucumber Selenium plugin for pre-definied steps

The following steps are used to install selenium-cucumber plugin.

```shell
$ rbenv global 2.4.1
$ gem install selenium-cucumber
```

### Install Calabash on top of Cucumber (if mobile UI test is required)

The following steps are used to install Calaba.sh.

```shell
$ rbenv global 2.4.1
$ curl -sSL https://raw.githubusercontent.com/calabash/install/master/install-osx.sh | bash
```

## Loopback.io Client

```shell
$ npm install -g loopback-cli
```
