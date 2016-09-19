from distutils.core import setup
import py2exe

setup(    
    name = "Not Ransomware...",
    version = '1.0',
    description = "Totally not bad.",
    author = "...",
    windows = [{'script': 'demo.py'}],
    zipfile = None,
    data_files=[],
    options = {
        'py2exe': {
            'optimize':2, 
            'bundle_files': 1, 
            'compressed': True, 
            'excludes':[],
            'dll_excludes':['w9xpopen.exe']
            }
        }
)