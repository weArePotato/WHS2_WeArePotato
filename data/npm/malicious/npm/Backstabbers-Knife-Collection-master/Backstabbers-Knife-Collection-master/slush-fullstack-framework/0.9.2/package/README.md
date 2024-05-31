# Slush Fullstack Framework Generator

This slush generator is helping developers to quickly start hackathon project using loopback.io, redux and react framework. So it saves time to install individual framework during hackathon kick-start.

## Quick Start

Step 1 - Install Slush and this generator in your desktop

```bash
$ npm install -g slush
$ npm install -g slush-fullstack-framework
```

Step 2 - Create your backend project based on loopback.io  

```bash
$ mkdir sample-project
$ cd sample-project
$ slush fullstack-framework
$ npm install
```

Step 3 - Create your own git repository for your backend project

```bash
$ cd sample-project
$ git init
$ git add .
$ git commit
```

Step 4 - Create your front-end app based on Redux and React

```bash
$ mkdir sample-app
$ cd sample-app
$ slush fullstack-framework:redux-react
$ npm install
$ npm run webpack
```

Step 5 - Create your own git repository for your front-end app

```bash
$ cd sample-project
$ git init
$ git add .
$ git commit
```

Step 6 - Import your front-end app git repo as submodule 'client' in your backend project git repo

```bash
$ cd sample-project
$ git submodule add <frontend-app git url> client
$ git add .
$ git commit
```

## Optional Grommet app skeleton

If you want to use Redux with Grommet UI in your front-end app, you can replace Step 4 with the following steps:

```bash
$ mkdir sample-app
$ cd sample-app
$ slush fullstack-framework:redux-grommet
$ npm install
$ npm run webpack
```