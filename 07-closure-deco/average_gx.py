
DEMO = """
>>> avg.__closure__
(<cell at 0x107a44f78: list object at 0x107a91a48>,)
"""

#閉包
def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)

    return averager
#类
class Averager():

    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total/len(self.series)

if __name__ == '__main__':
    avg = make_averager()
    # 10.0
    # 10.5
    print(avg(10))
    print(avg(11))

    # >> > avg.__code__.co_varnames
    # ('new_value', 'total')
    # >> > avg.__code__.co_freevars
    # ('series',)
    # >> > avg.__closure__  # doctest: +ELLIPSIS
    # (< cell at 0x...: list object at 0x...>,)
    # >> > avg.__closure__[0].cell_contents
    # avg= Averager()c
    # print(avg(10))
    # print(avg(11))

