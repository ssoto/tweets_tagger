#!/usr/bin/env python
"""Package used on smyrooms pricing DAG."""
import os
from setuptools import setup, find_packages

try:
    from pip import main
except ImportError:
    from pip._internal import main

try:
    from pip import req
except ImportError:
    from pip._internal import req

HERE = os.path.abspath(os.path.dirname(__file__))


def get_requirements(reqfile):
    path = os.path.join(HERE, reqfile)
    deps = set()
    for dep in req.parse_requirements(path, session=False):
        try:
            # Pip 8.1.2 Compatible
            specs = ','.join(''.join(str(spec)) for spec in dep.req.specifier)
        except AttributeError:
            # Pip 1.5.4 Compatible
            specs = ','.join(''.join(spec) for spec in dep.req.specs)
        requirement = '{name}{extras}{specs}'.format(
            name=dep.name,
            extras=(
                '[{extras}]'.format(extras=','.join(dep.extras))
                if dep.extras else ''
            ),
            specs=specs,
        )

        deps.add(requirement)
    result = list(deps)
    return result


setup(
    name='tweet_tagger',
    version='1.0.0',
    setup_requires=['pip>=19.3.1, <20.0.1', 'versiontools', ],
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages(),
)
