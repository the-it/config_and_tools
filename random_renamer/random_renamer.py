#!/usr/bin/env python3
import os, sys
import random
import string

print(sys.path)
print(os.getcwd())

class RandomRenamer(object):
    def __init__(self):
        if len(sys.argv) == 2:
            self.work_dir = sys.argv[1]
        else:
            self.work_dir = os.getcwd()
        if len(sys.argv) > 2:
            raise TypeError('To much command line arguments.')

    @staticmethod
    def _get_random_string():
        return ''.join(random.sample(string.ascii_lowercase, random.randint(5,10)))

    def run(self):
        for root, dirs, files in os.walk(self.work_dir, topdown=False):
            print('root: {}'.format(root))
            print('dirs: {}'.format(dirs))
            print('files: {}'.format(files))
            for file in files:
                if file in __file__:
                    continue
                file_split = file.split('.')
                file_split[0] = self._get_random_string()
                new_file = '.'.join(file_split)
                os.rename('/'.join((root, file)), '/'.join((root, new_file)))
            for dir in dirs:
                os.rename('/'.join((root, dir)), '/'.join((root, self._get_random_string())))

if '__main__' == __name__:
    RandomRenamer().run()