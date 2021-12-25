import subprocess as sp
from os.path import *

from vcpkg import *


def ls():
    sp.check_call(['ls', vcpkg_root])


def triplets():
    for parent, folders, files in os.walk(join(vcpkg_root, 'triplets')):
        for file in files:
            print(basename(join(parent, file)))


def port_count():
    a = sp.check_output(['ls', join(vcpkg_root, 'ports')])
    a = str(a, 'utf8')
    return len(a.split())


print('支持的port个数', port_count())
# triplets()
