#!/usr/bin/env python3
# Copyright (C) 2015 Sebastian Pipping <sebastian@pipping.org>
# Licensed under GPL v2 or later

from setuptools import find_packages, setup

from grub2_theme_preview.version import VERSION_STR


setup(
    name='grub2-theme-preview',
    description='Preview a GRUB 2.x theme using KVM/QEMU',
    license='GPL v2 or later',
    version=VERSION_STR,
    url='https://github.com/hartwork/grub2-theme-preview',
    download_url='https://github.com/hartwork/grub2-theme-preview/archive/%s.tar.gz' % VERSION_STR,
    author='Sebastian Pipping',
    author_email='sebastian@pipping.org',
    python_requires='>=3.6',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'grub2-theme-preview = grub2_theme_preview.__main__:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: System :: Boot',
        'Topic :: Utilities',
    ],
)
