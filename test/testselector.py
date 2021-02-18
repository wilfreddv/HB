import sys
sys.path.append('../')

from pyutil import selector

options = ["Python",
           "Java",
           "C",
           "PHP",
           "Swift",
           "Kotlin",
           "Perl",
           "Ruby",
           "C++",
           "C#",
           "OCaml",
           "Haskell"
          ]

selection = selector.selector("Enter a value:", options)

print(f"You chose: {selection}")
