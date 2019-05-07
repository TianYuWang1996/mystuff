try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    "description": "ex47:自动化测试",
    "author": "TianYuWang1996",
    "url": "URL to get it at.",
    "download": "Where to download it.",
    "author_email": "17809299217@163.com",
    "version": "0.1",
    "install_requires": ["nose"],
    "packages": ["ex47"],
    "scripts": [],
    "name": "ex47"
}

setup(**config)