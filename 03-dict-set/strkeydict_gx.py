import collections
class StrKeyDict(collections.UserDict):
    def __missing__(self, key):
        if isinstance(key,str):
            raise KeyError(key)
        return self[str(key)]
    def __contains__(self, key):
        return str(key) in self.data
    def __setitem__(self, key, item):
        #__setitem__ 会把所有的键都转换成字符串。由于把具体的实现委托给了self.data 属性，这个方法写起来也不难。
        self.data[str(key)] = item #

d = StrKeyDict([(2, 'two'), ('4', 'four')])
print(sorted(d.keys()))
print(d['2'])