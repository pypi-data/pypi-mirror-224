# coding: utf-8

"""
routines to help database instances to log (or not), without double line testing

    if self.verbose > 0:
        print(.......)

the first parameter is the verbosity level
"""


def no_log(*args, **kw):
    pass


class debug:
    def __init__(self, verbose=0):
        self.verbose = verbose

    def __call__(self, *args, **kw):
        # print('call', args[0], self.verbose)
        try:
            lvl = int(args[0])
            args = args[1:]
        except ValueError:
            lvl = 0
        # print('lvl', lvl)
        if self.verbose >= lvl:
            print(*args, **kw)

