from abc import abstractmethod
from typing import Iterable, Iterator


class Slist:
    @abstractmethod
    def empty(self) -> bool:
        pass

    @abstractmethod
    def head(self):
        pass

    @abstractmethod
    def tail(self):
        pass

    def __iter__(self):
        return _Iter(self)

    @abstractmethod
    def __eq__(self, obj):
        pass

class _Nil(Slist):
    def empty(self) -> bool:
        return True

    def head(self):
        raise IndexError("head from empty list")

    def tail(self):
        raise IndexError("tail from empty list")

    def __eq__(self, obj):
        return isinstance(obj, _Nil)

# Global _Nil object
_nil = _Nil()

class _Node(Slist):
    def __init__(self, val, next: Slist):
        self.val = val
        self.next = next

    def empty(self) -> bool:
        return False

    def head(self):
        return self.val

    def tail(self):
        return self.next

    def __eq__(self, obj):
        return isinstance(obj, _Node) \
            and self.val == obj.val and self.next == obj.next
            # Note that the second `==` above calls __eq__() tail-recursively, and can
            # be implemented using `jump` instead of `call/ret`, depending on the Python
            # optimizer.

class _Iter:
    def __init__(self, p: Slist):
        self.p = p

    def __next__(self):
        if self.p.empty():
            raise StopIteration
        val = self.p.head()
        self.p = self.p.tail()
        return val

# Push at the front
def cons(val, sl: Slist) -> Slist:
    return _Node(val, sl)

# Construct Slist from an iterator in forward order
def _slist(it: Iterator) -> Slist:
    try:
        val = next(it)
    except StopIteration:
        return _nil
    return cons(val, _slist(it))

def slist(vals: Iterable =None, reverse: bool =False) -> Slist:
    if vals is None:
        return _nil

    if not reverse:
        return _slist(iter(vals))

    # If reverse is True,
    sl = _nil
    for val in vals:
        sl = _Node(val, sl)
    return sl


# Example 1
sl = slist([1, 2, 'a'])
print("Forward order:", end='')
for x in sl:
    print(f" {x}", end='')
print()

# Example 2
assert cons(1, cons(2, cons(3, slist()))) == slist([1, 2, 3])

# Example 3
sl = slist("abc")
assert sl.head() == 'a'
assert sl.tail().head() == 'b'
assert sl.tail().tail().head() == 'c'
try:
    sl.tail().tail().tail().head()
    assert False, "Exception should be raised"
except IndexError:
    pass

# Example 4
sl = slist([1, 2, 'a'], reverse=True)
l = list(sl)  # Convert it to an array
assert l == ['a', 2, 1]

# Example 5
sl = cons(1, cons(2, cons('a', slist())))
assert list(sl) == [1, 2, 'a']
