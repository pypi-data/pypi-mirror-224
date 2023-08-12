from h2lib.dll_wrapper import DLLWrapper
import os


class H2Lib(DLLWrapper):
    def __init__(self, filename=None):
        if filename is None:
            if os.name == 'nt':
                filename = os.path.dirname(__file__) + '/TestLib.dll'
            else:
                filename = os.path.dirname(__file__) + '/TestLib.so'
            
        DLLWrapper.__init__(self, filename, cdecl=True)
