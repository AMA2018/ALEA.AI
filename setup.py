import asyncio

from setuptools import find_packages
from setuptools import setup
from distutils.command.install import install


# from alea_bot import PROJECT_NAME, VERSION
# todo figure out how not to import alea_bot.__init__.py here
PROJECT_NAME = "Alea-Bot"
VERSION = "1.0.0"  # major.minor.revision


def _post_install():
    import alea_bot.cli
    asyncio.run(alea_bot.cli.install_all_tentacles(True))


class InstallWithPostInstallAction(install):
    def run(self):
        install.run(self)
        self.execute(_post_install, (), msg="Installing Alea-Bot tentacles")


PACKAGES = find_packages(
    exclude=[
        "tests",
        "alea_bot.imports*",
        "alea_bot.user*",
    ]
)

# long description from README file
with open('README.md', encoding='utf-8') as f:
    DESCRIPTION = f.read()

REQUIRED = open('requirements.txt').readlines()
REQUIRES_PYTHON = '>=3.10'

setup(
    name=PROJECT_NAME,
    version=VERSION,
    url='https://github.com/AMA2018/ALEA.AI',
    license='MIT',
    author='AMA2018',
    author_email='contact@alea-ai.com',
    description='AI-driven crypto trading bot with advanced market intelligence',
    packages=PACKAGES,
    cmdclass={'install': InstallWithPostInstallAction},
    long_description=DESCRIPTION,
    long_description_content_type='text/markdown',
    tests_require=["pytest"],
    test_suite="tests",
    zip_safe=False,
    data_files=[],
    include_package_data=True,  # copy non python files on install
    install_requires=REQUIRED,
    python_requires=REQUIRES_PYTHON,
    entry_points={
        'console_scripts': [
            'alea = alea_bot.cli:main'
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Operating System :: OS Independent',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.10',
    ],
)
