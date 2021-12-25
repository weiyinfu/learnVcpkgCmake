import os
from os.path import *


class Node:
    def __init__(self, name, src):
        self.name = name
        self.src = src
        self.children = {}


def submit(fpath: str, ans: Node):
    p = fpath.split('/')
    now = ans
    for i in p[1:]:
        if i not in now.children:
            now.children[i] = Node(i, '')
        now = now.children[i]
    now.src = fpath


def handle(folder: str, root: str, gen: str):
    ans = Node("vcpkg-doc", '')
    for parent, folders, files in os.walk(folder):
        for f in files:
            if not f.endswith('.md'):
                continue
            fpath = join(parent, f)
            fpath = relpath(fpath, root)
            submit(fpath, ans)

    def rewrite_name(name):
        if name.endswith('.md'):
            return name[:-3]
        return name

    ind = 1

    def tos(x: Node, depth: int):
        nonlocal ind
        children_str = ''
        for k, v in x.children.items():
            children_str += tos(v, depth + 1) + "\n"
        if not x.src:
            fpath = join(gen, f"{ind}.md")
            catelog = ''
            for k, v in x.children.items():
                catelog += tos(v, 0)
            open(fpath, 'w').write(catelog)
            x.src = relpath(fpath, root)
            ind += 1

        s = f"{'  ' * depth}* [{rewrite_name(x.name)}]({x.src})\n"
        s += children_str
        return s

    return tos(ans, 0)


def main():
    if not exists('./src/gen'):
        os.mkdir('./src/gen')
    s = handle('./src/vcpkg-doc', './src', './src/gen')
    print(s)


main()
