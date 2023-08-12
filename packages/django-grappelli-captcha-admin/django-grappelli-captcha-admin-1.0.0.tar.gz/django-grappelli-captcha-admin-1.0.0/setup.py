#!/usr/bin/env python
import codecs
from setuptools import setup, find_packages


def read_me(filename):
    return codecs.open(filename, encoding='utf-8').read()


setup(
    name='django-grappelli-captcha-admin',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    description=(
        'easy added captcha to login page of django grappelli admin'
    ),
    url='http://github.com/xcai/django-grappelli-captcha-admin',
    download_url='https://pypi.python.org/pypi/django-grappelli-captcha-admin/',
    author='xcai',
    author_email='xxiaocai@163.com',
    keywords="django captcha recaptcha recaptcha2 simple-captcha admin grappelli",
    license='MIT',
    platforms=['any'],
    python_requires='>=3',
    install_requires=[
        "django",
        "django-grappelli",
    ],
    long_description=read_me('README.md'),
    long_description_content_type='text/markdown',
    zip_safe=False,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
