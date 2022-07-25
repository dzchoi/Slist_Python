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
            and self.head() == obj.head() and self.tail() == obj.tail()

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
xs = slist([1, 2, 'a'])
print("Forward order:", end='')
for x in xs:
    print(f" {x}", end='')
print()

# Example 2
assert cons(1, cons(2, cons(3, slist()))) == slist([1, 2, 3])

# Example 3
xs = slist("abc")
print(f"car: {xs.head()}")                  # 'a'
print(f"cadr: {xs.tail().head()}")          # 'b'
print(f"caddr: {xs.tail().tail().head()}")  # 'c'
try:
    print(f"cadddr: {xs.tail().tail().tail().head()}")
except IndexError as e:
    print(e)

# Example 4
xs = slist([1, 2, 'a'], reverse=True)
l = list(xs)  # Convert it to an array
print(f"Reverse order: {l}")

# Example 5
xs = cons(1, cons(2, cons('a', slist())))
l = list(xs)
print(f"{l}")
