[![checks](../../actions/workflows/checks.yml/badge.svg)](../../actions/workflows/checks.yml)
[![pylint Score](https://mperlet.github.io/pybadge/badges/10.0.svg)](./logs/pylint/)
[![Coverage score](https://img.shields.io/badge/coverage-100%25-dagreen.svg)](./logs/cov.out)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](./LICENSE)
***

## Table of contents

1. [Introduction](./README.md#introduction)
    1. [Objective](./README.md#objective)
    1. [Programming style](./README.md#programming-style)
    1. [Version control](./README.md#version-control)
    1. [Contribution guidelines](./.github/CONTRIBUTING.md)
    1. [Slack](https://join.slack.com/t/slack-alh8147/shared_invite/zt-xye4mwee-gSLttX5elyho4wrE0No8gg)
1. [Project documents](./docs)
    1. [Approach](./docs/Approach.pdf)
1. [Pull request guidelines](./.github/PULL_REQUEST_TEMPLATE.md)
1. [Initial setup](./README.md#initial-setup)
1. [Unit tests](./README.md#run-unit-tests-and-pylint-ratings)
1. [Important links](./README.md#important-links)
1. [License](./LICENSE)
***

## Introduction

#### Objective

The objective of this repository is to:

1. Create a scalable recommendation engine in a modular environment.

#### Programming style

It's good practice to follow accepted standards while coding in python:
1. [PEP 8 standards](https://www.python.org/dev/peps/pep-0008/): For code styles.
1. [PEP 257 standards](https://www.python.org/dev/peps/pep-0257/): For docstrings standards.
1. [PEP 484 standards](https://www.python.org/dev/peps/pep-0484/) For function annotations standards.

Also, it's a good idea to rate all our python scripts with [Pylint](https://www.pylint.org/). If we score anything less than 8/10, we should consider redesigning the code architecture.

A composite pylint ratings for all the codes are automatically computed when we [run the tests](./bin/run_tests.sh) and prepended on top of this file.

#### Version control

We use semantic versionning ([SemVer](https://semver.org/)) for version control. You can read about semantic versioning [here](https://semver.org/).

## Initial setup

```console
bash install.sh
```

#### Requirements

The python requirements can be found at
1. [Requirements](./requirements.txt)

***

## Run unit tests and pylint ratings

To run all unit tests and rate all python scripts, run the following in
**project** directory:

```console
./bin/run_tests.sh
```

Available options:

```console
-a default, runs both code rating and unit tests.
-u unit tests.
-r code rating.
```
The pylint ratings for each python script can be found at
[logs/pylint/](./logs/pylint/)
***

## Important links

#### Guidelines

- [Contribution guidelines](./.github/CONTRIBUTING.md)
- [Branching conventions](./docs/Branch.md)
- [Directory structure](./docs/Directory_structure.md)
***
