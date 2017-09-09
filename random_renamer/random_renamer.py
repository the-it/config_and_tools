#!/usr/bin/env python3
import os
import random
import string
import sys


class RandomRenamer(object):
    def __init__(self, path):
        self.work_path = path
        if len(sys.argv) > 2:
            raise TypeError('No command line arguments allowed.')
        self.run()

    @staticmethod
    def _get_random_string():
        return ''.join(random.sample(string.ascii_lowercase, random.randint(5, 10)))

    def run(self):
        for root, directories, files in os.walk(self.work_path, topdown=False):
            print('root: {}'.format(root))
            print('dirs: {}'.format(directories))
            print('files: {}'.format(files))
            for file in files:
                if file in __file__:
                    continue
                file_split = file.split('.')
                file_split[0] = self._get_random_string()
                new_file = '.'.join(file_split)
                os.rename('/'.join((root, file)), '/'.join((root, new_file)))
            for directory in directories:
                os.rename('/'.join((root, directory)), '/'.join((root, self._get_random_string())))

if '__main__' == __name__:
    RandomRenamer(os.getcwd())
