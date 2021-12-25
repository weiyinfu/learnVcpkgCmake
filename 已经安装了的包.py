"""
如果$VCPKG_ROOT/installed/vcpkg/status文件中的依赖发生损坏，则vcpkg将报错：data corrupted，数据乱了。
"""

from os.path import *

from vcpkg import *


def parse(s):
    a = s.splitlines()
    b = {}
    for i in a:
        ind = i.index(':')
        left = i[:ind]
        right = i[ind + 1:]
        left = left.strip()
        right = right.strip()
        b[left] = right

    b['Depends'] = [i.strip() for i in b.get('Depends', '').split(',') if i.strip()]
    return b


def get():
    a = open(join(vcpkg_root, 'installed/vcpkg/status')).read()
    a = a.split('\n\n')
    print(f'一共安装了{len(a)}个包')
    return [parse(i) for i in a if i.strip()]


all_installed = get()
name2package = {f"{i['Package']}:{i['Architecture']}": i for i in all_installed}


# print(name2package)


def check_health():
    # 检查没有安装的包
    for k, v in name2package.items():
        for d in v['Depends']:
            if ':' not in d:
                d = f"{d}:{v['Architecture']}"
            if d not in name2package:
                print(f"{k}:{v['Architecture']} depends on {d}(not found)")


# print(all_installed)
check_health()
