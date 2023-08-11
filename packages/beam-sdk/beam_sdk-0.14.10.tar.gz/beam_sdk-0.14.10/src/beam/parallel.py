import os
import inspect

from typing import Callable

"""

What do we have to do?
- 



"""


class Parallel:
    def _generate_func(self, f):
        return f

    def __init__(self, func: Callable, count: int):
        self.func = func
        self.count = count

    def __iter__(self):
        for idx in range(self.count):
            f = self._generate_func(self.func)
            yield f, idx
