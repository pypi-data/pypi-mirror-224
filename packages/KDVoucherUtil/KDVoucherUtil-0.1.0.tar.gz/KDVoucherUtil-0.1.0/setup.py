import codecs
import os
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()


VERSION = '0.1.0'
DESCRIPTION = '金蝶云平台凭证批量处理封装工具。因为依赖包古老，因此需要注意降级pip和setuptools版本，建议降级到pip-20.1.1, setuptools-57.5.0'

setup(
    name="KDVoucherUtil",
    version=VERSION,
    author="Arthur Yu",
    author_email="arthurzero@homtail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    license='MIT',
    install_requires=[
        "suds-jurko>=0.6",
    ],
    # keywords=['python', 'menu', 'dumb_menu','windows','mac','linux'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
