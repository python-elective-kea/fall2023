# range_mimic.py

# 1. Create a "clone" of the build in range() function.

class range:

    def __init__(self, *args):
        if len(args) == 1:
            self.start = 0
            self.end = args[0]
            self.step = 1
        elif len(args) == 2:
            self.start = args[0]
            self.end = args[1]
            self.step = 1
        elif len(args) == 3:
            self.start = args[0]
            self.end = args[1]
            self.step = args[2]

    def __iter__(self):
        self.i = self.start
        return self

    def __next__(self):
        try:
            if self.end > self.i:
                self.tmp = self.i
                self.i += self.step
                return self.tmp
            else:
                raise StopIteration
        except AttributeError:
            raise TypeError('range method is not itterable')


x = range(2, 12, 2)
for i in x:
    print(i)

# or just:
for i in range(2, 12, 2):
    print(i)

# 2. Now do the same, but use a generator function instead.
def range(*args):
    
    if len(args) == 1:
        start = 0
        end = args[0]
        step = 1
    elif len(args) == 2:
        start = args[0]
        end = args[1]
        step = 1
    elif len(args) == 3:
        start = args[0]
        end = args[1]
        step = args[2]
    
    count = start 
    while count < end:
        yield count
        count += step




