''' 
A tuple is a fixed-length, immutable sequence of Python objects

In[1]:tup=4,5,6 
In [2]: tup
Out[2]: (4, 5, 6)

creating a tuple of tuples:
In [3]: nested_tup = (4, 5, 6), (7, 8)
In [4]: nested_tup
Out[4]: ((4, 5, 6), (7, 8))

You can convert any sequence or iterator to a tuple by invoking tuple:
In [5]: tuple([4, 0, 2])
Out[5]: (4, 0, 2)
In [6]: tup = tuple('string')
In [7]: tup
Out[7]: ('s', 't', 'r', 'i', 'n', 'g')


once the tuple is cre‐ ated it’s not possible to modify which object is stored in each slot:
In [9]: tup = tuple(['foo', [1, 2], True])
In [10]: tup[2] = False 
--------------------------------------------------------------------------- 
TypeError Traceback (most recent call last) <ipython-input-10-c7308343b841> in <module>()
----> 1 tup[2] = False
TypeError: 'tuple' object does not support item assignment

If an object inside a tuple is mutable, such as a list, you can modify it in-place:
In [11]: tup[1].append(3)
In [12]: tup
Out[12]: ('foo', [1, 2, 3], True)

