from setuptools import setup, find_packages
from os import path


setup(name='baekjoon-scraper', # 패키지 명

version='1.0.2',

description='A fork of smartwe\'s baekjoon api with optional argument fields for avoiding scraping detection' ,

long_description='An unofficial API for Baekjoon Online Judge that retrieves the data by scraping. This is a fork of smartwe\'s baekjoon package with additional parameters to the APIs in order to help bypass Baekjoon\'s bot detection while scraping. Read more at https://github.com/RoelYoon/baekjoon-scraper-api.git to learn how to use this package.',

author='RoelYoon',

author_email='roelyoon2@gmail.com',

url='https://github.com/RoelYoon/baekjoon-scraper-api.git',

license='MIT', # MIT에서 정한 표준 라이센스 따른다

py_modules=[''], # 패키지에 포함되는 모듈

python_requires='>=3',

install_requires=['bs4','requests'], # 패키지 사용을 위해 필요한 추가 설치 패키지

packages=['baekjoon'], # 패키지가 들어있는 폴더들

)