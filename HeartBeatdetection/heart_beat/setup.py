"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
    
"""

from setuptools import setup

APP = ['get_pulse.py']
DATA_FILES = ['cascades/haarcascade_frontalface_alt.xml']
OPTIONS = {'argv_emulation': True}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
