# from genericpath import isdir
import os

class Path:
    def __init__(self, path):
        self.path = path
    def exists(self):
        return True if os.path.isdir(self.path) else False