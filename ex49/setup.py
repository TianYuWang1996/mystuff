try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    "description": "ex49:创建句子",
    "author": "TianYuWang1996",
    "url": "URL to get it at.",
    "download": "Where to download it.",
    "author_email": "17809299217@163.com",
    "version": "0.1",
    "install_requires": ["nose"],
    "packages": ["ex49"],
    "scripts": [],
    "name": "ex49"
}

setup(**config)