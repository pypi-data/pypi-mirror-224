# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pytest_robotframework']

package_data = \
{'': ['*']}

install_requires = \
['robotframework>=6.1.1,<7.0.0']

entry_points = \
{'pytest11': ['robotframework = pytest_robotframework.pytest_robotframework']}

setup_kwargs = {
    'name': 'pytest-robotframework',
    'version': '1.0.0',
    'description': 'a pytest plugin to generate robotframework reports without having to write your tests in the robot langauge',
    'long_description': '# pytest-robotframework\n\na pytest plugin to generate robotframework reports without having to write your tests in the robot langauge\n\n![](https://github.com/DetachHead/pytest-robotframework/assets/57028336/9caabc2e-450e-4db6-bb63-e149a38d49a2)\n\n## install\n\n```\npoetry add pytest-robotframework --group=dev\n```\n\n## usage\n\npytest should automatically find and activate the plugin once you install it, so all you should have to do is write tests with pytest like you would normally:\n\n```py\n# you can use both robot and pytest features\nfrom robot.api import logger\nfrom pytest import Cache\n\nfrom pytest_robotframework import keyword\n\n@keyword  # make this function show as a keyword in the robot log\ndef foo():\n    ...\n\n\ndef test_foo(cache: Cache):\n    foo()\n```\n\n### robot command line arguments\n\nspecify robot CLI arguments with the `--robotargs` argument:\n\n```\npytest --robotargs="-d results --listener foo.Foo"\n```\n\nsome arguments such as `--extension` obviously won\'t work .\n\n### setup/teardown and other hooks\n\nto define a function that runs for each test at setup or teardown, create a `conftest.py` with a `pytest_runtest_setup` and/or `pytest_runtest_teardown` function:\n\n```py\n# ./tests/conftest.py\ndef pytest_runtest_setup():\n    log_in()\n```\n\n```py\n# ./tests/test_suite.py\ndef test_something():\n    """i am logged in now"""\n```\n\nthese hooks appear in the log the same way that the a `.robot` file\'s `Setup` and `Teardown` options in `*** Settings ***` would:\n\n![](https://github.com/DetachHead/pytest-robotframework/assets/57028336/d0b6ee6c-adcd-4f84-9880-9e602c2328f9)\n\nfor more information, see [writing hook functions](https://docs.pytest.org/en/7.1.x/how-to/writing_hook_functions.html). pretty much every pytest hook should work with this plugin\nbut i haven\'t tested them all. please raise an issue if you find one that\'s broken.\n\n### tags/markers\n\npytest markers are converted to tags in the robot log:\n\n```py\nfrom pytest import mark\n\n@mark.slow\ndef test_blazingly_fast_sorting_algorithm():\n    [1,2,3].sort()\n```\n\n![](https://github.com/DetachHead/pytest-robotframework/assets/57028336/f25ee4bd-2f10-42b4-bdef-18a22379bd0d)\n',
    'author': 'DetachHead',
    'author_email': 'detachhead@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/detachhead/pylint-module-boundaries',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
