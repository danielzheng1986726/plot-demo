class Array(list):
    def __pow__(self, power):
        return Array([x ** power for x in self])

def linspace(start, stop, num):
    if num < 2:
        return Array([start])
    step = (stop - start) / (num - 1)
    return Array([start + step * i for i in range(num)])
