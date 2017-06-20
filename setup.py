from setuptools import setup, find_packages

setup(
    name="textprocessor",
    version="0.2.0",
    author="Fabien Schwob",
    license="BSD",
    url="http://github.com/jibaku/django-textprocessor",
    description="""
    Templatetags and filter to process text (string) to enhance link (add
    link, check typography rules, etc.)
    """.strip(),
    packages=find_packages(exclude=[]),
    include_package_data=True,
    install_requires=[
        'markdown',
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ]
)
