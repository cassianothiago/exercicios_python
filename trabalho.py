
import sys
import termcolor

from termcolor import colored, cprint

#ttext = colored("Hello, World!", "red", attrs=["reverse", "blink"])
text = colored("Hello, World!")

print(text)
cprint("Hello, World!", "green", "on_red")

'''
cprint("Hello, World!", "green", "on_red")

print_red_on_cyan = lambda x: cprint(x, "red", "on_cyan")
print_red_on_cyan("Hello, World!")
print_red_on_cyan("Hello, Universe!")

for i in range(10):
    cprint(i, "magenta", end=" ")

cprint("Attention!", "red", attrs=["bold"], file=sys.stderr)'''