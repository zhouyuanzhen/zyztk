"""
Yuanzhen Zhou 's Python Toolkit
"""

from setuptools import setup, find_packages

LONG_DESC = """
Python Toolkit of Yuanzhen Zhou.
"""

setup(
    name='zyz',
    version='0.2.0',
    license='Apache License 2.0',
    keywords='zyz, zyztk, zhouyuanzhen',
    maintainer='Yuanzhen Zhou',
    maintainer_email='szrednick@gmail.com',
    packages=find_packages(include=['zyz', 'zyz.*']),
    zip_safe=False,
    include_package_data=True,
    url='https://github.com/zhouyuanzhen/zyztk',
    author='Yuanzhen Zhou',
    author_email='szrednick@gmail.com',
    description='Python Toolkit of Yuanzhen Zhou',
    long_description=LONG_DESC,
    python_requires='>=3.5, <4',
    install_requires=[],
    extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
    },
)
