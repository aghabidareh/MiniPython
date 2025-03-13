# sum of 1 to 100 without "for" loop and another things, only numpy.

import numpy as np
from colorama import Fore

numbers = np.arange(1, 100 + 1)
s = np.sum(numbers)

print(Fore.GREEN)

print(f'the sum of 1 to 100 is {s}.')

print(Fore.WHITE)
