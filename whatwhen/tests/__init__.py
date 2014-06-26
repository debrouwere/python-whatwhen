import unittest
import whatwhen


def one():
    pass

one.provides = ['entertainment']

def two():
    pass

def three():
    pass

three.dependencies = ['one', 'two']
three.provides = ['good cheer']

def four():
    pass

four.needs = ['good cheer']

def five():
    pass

def six():
    pass

six.needs = ['entertainment']

fns = [one, two, three, four, five, six]


class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.order = whatwhen.sort(fns)
        self.names = [fn.__name__ for fn in self.order]

    def test_dependencies(self):
        print self.names
        self.assertTrue(self.names.index('one') < self.names.index('three'))
        self.assertTrue(self.names.index('two') < self.names.index('three'))

    def test_needs(self):
        self.assertTrue(self.names.index('three') < self.names.index('four'))
        self.assertTrue(self.names.index('one') < self.names.index('six'))