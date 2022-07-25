## Singly linked list in Python

Python already has a data structure called `list`, which is more like `array` as occupying a contiguous memory and dereferenced by index. However, we can still implement the pure singly linked list using object binding in Python.

Source code is attached with simple example usages.

### Slist
`Slist` is the data type.

### Constructors
`slist(vals: Iterable =None, reverse: bool =False) -> Slist`
- `slist()` creates an empty list.
- Can also create a list from an `Iterable`.  
  ```Python
  slist([1, 2, 'a'])` 
  slist("abc")
  ```

`cons(val, sl: Slist) -> Slist`
- `cons` can create a new list by appending a new head element to the existing list.
  ```Python
  cons(1, cons(2, cons(3, slist()))) == slist([1, 2, 3])
  ```

### `.empty()` method
`.empty() -> bool`
- An empty list is different from `None` and represented by a separate internal class. The `.empty()` returns `True` if the list is empty.

### `.head()` and `.tail()` methods
`.head() -> Any`  
`.tail() -> Slist`
- `.head()` returns the head element of the list and `.tail()` returns the remainingg list, just like `car()` and `cdr()` in Lisp. They will cause `IndexError` exception on an empty list.
  ```Python
  slist("abc").tail().tail().head() == 'c'
  ```

### Iterable
`Slist` is an Iterable object.
```Python
sl = slist([1, 2, 'a'])

for val in sl:
  print(f"{val}")

l = list(sl)
print(f"{l}")
```

### Not mutable!
Once created the `Slist` cannot modify the value of its elements, although this can be changed by providing a setter method and by providing a custom `copy` which is needed to save the contents before modifying.

However, by having it immutable, we can safely reuse the memory of old lists without having to worry about a list being changed unnoticedly.
