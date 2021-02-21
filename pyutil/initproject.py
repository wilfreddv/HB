import sys
import os
from pyutil.selector import selector



_PYTHON_MAIN = """\
def main():
    print("Hello world!")


if __name__ == '__main__':
    main()
"""

_C_MAIN = """\
#include <stdio.h>

int main()
{
    printf("Hello world!\n");
    return 0;
}
"""


_CPP_MAIN = """\
#include <iostream>

int main()
{
    std::cout << "Hello World!" << std::endl;
    return 0;
}
"""


LANGUAGES = {
    "Python": ["py", _PYTHON_MAIN],
    "C": ["c", _C_MAIN],
    "C++": ["cpp", _CPP_MAIN],
    "Other": ["", ""]
}


project = {
    "name": None,
    "language": None,
    "has_git": None,
    "license": None
}


def _create_project(project):
    name = project['name']
    language = project['language']

    print(f"Creating {language} project: {name}...")

    if os.path.exists(name):
        print("Path already exists.")
        return

    os.mkdir(name)
    os.chdir(name)

    os.mkdir("src")
    os.chdir("src")
    
    with open(f"{name}.{LANGUAGES[language][0]}", "w") as f:
        f.write(LANGUAGES[language][1])

    
    os.chdir('..') # base directory
    if project['has_git']: os.system("git init")


    with open("README.md", "w") as f:
        f.write(f"# {name}")

    if project['license']:
        with open("LICENSE", "w") as f:
            f.write("license goes here")


    os.chdir("..")


def main():
    language = selector("Select a language:", list(LANGUAGES.keys()))

    if not language:
        return


    project['language'] = language


    name = input("Enter a name: ").strip()
    while not len(name):
        name = input("Enter a name: ").strip()

    project['name'] = name


    use_git = input("Initialize a git repository? [y/N] ").lower()
    project['has_git'] = use_git in ["yes", "y"]


    print("Creating project using the following settings:")
    for k, v in project.items():
        print(f"{k}: {v}")


    if input("Do you want to continue? [Y/n] ").lower() in ["no", "n"]:
        return

    _create_project(project)



if __name__ == '__main__':
    main()