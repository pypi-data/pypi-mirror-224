from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.3'  # Update the version number
DESCRIPTION = 'PyChatVerse: Real-Time Chat Application for Python'
LONG_DESCRIPTION = '''
PyChatVerse is an innovative and user-friendly chat application package for Python, 
designed to provide a seamless real-time communication experience. 
With a focus on simplicity, interactivity, and versatility, PyChatVerse enables users 
to engage in both global and private chat rooms, making it an ideal solution 
for a wide range of communication needs.
'''

# Setting up
setup(
    name="PyChatVerse",
    version=VERSION,
    author="Dayanidi",
    author_email="<dayanidigv954@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests', 'pyrebase'],
    keywords=['python', 'chat', 'real-time', 'communication', 'messaging'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ]
)
