#!/bin/env python3
from setuptools import setup, find_packages

setup(
  name="capys", version="0.0.1",
  url="https://github.com/duangsuse-valid-projects/Share",
  author="duangsuse", author_email="fedora-opensuse@outlook.com", license="MIT",
  description="Capybara, an object FFI/RPC tool like PyOdide, PyJnius, or Luajava with Jupyter/Qt UI&DevTools",
  packages=find_packages(),
  install_requires=["requests>=2.0.0", "retry>=0.8.0", "bs4>=0.0.1", "loger>=0.1.0"],
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
)
