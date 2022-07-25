## Singly linked list in Python (under updating)

Python already has a data structure called `list`, which is more like `array` as occupying a contiguous memory and dereferenced by index. However, we can still implement the pure singly linked list using object binding in Python.

Source code is attached with simple example usages.

### Slist
`Slist` is the data type.

### Constructors
`slist(vals: Iterable =None, reverse: bool =False) -> Slist`
- `slist()` creates an empty list.
- Non-empty list can be created from an existing `Iterable`.  
  `slist([1, 2, 'a'])`  
  `slist("abc")`

`cons(val, sl: Slist) -> Slist`
- `cons` can create a new 

### Not mutable
Once created the `Slist` can not modify the value of its element, though this can be changed by providing a `setter` method and by 
