from setuptools import setup
import setuptools

DESCRIPTION = 'PyChatVerse: Real-Time Chat Application for Python'
LONG_DESCRIPTION = '''
PyChatVerse is an innovative and user-friendly chat application package for Python, 
designed to provide a seamless real-time communication experience. 
With a focus on simplicity, interactivity, and versatility, PyChatVerse enables users 
to engage in both global and private chat rooms, making it an ideal solution 
for a wide range of communication needs.
'''

setup(
    name="PyChatVerse",
    version="0.0.6",
    description=DESCRIPTION,
    author="Dayanidi Vadivel",
    keywords=['python', 'chat', 'real-time', 'communication', 'messaging', 'Firebase', 'PyChatVerse' ,'pychatverse'  ,'python chat Application'  ,'Real time chat application'  ,'Global Chat'  ,'Private Chat'],
    long_description=open("README.md", "r", encoding="utf8").read(),
    long_description_content_type='text/markdown',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    py_modules=["PyChatVerse"],
    packages=setuptools.find_packages("PyChatVerse"),
    package_dir={"":"PyChatVerse"},
    requires=[
        "requests",
        "pyrebase"
    ],
    url="https://dayanidigv.github.io/PyChatVerse/",
    license="MIT",
    author_email="<dayanidigv954@gmail.com>",

)



