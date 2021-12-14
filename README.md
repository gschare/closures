# Closure examples in Python

[object_closure.py](object_closure.py): A bit silly, using object closures.
There's a big issue though: all public functions and variables are directly mutable. This can be "solved" using a wrapper function that adds the attributes (see [pointer_closure.py](pointer_closure.py) for an example of this) but all that really does is allow for a fallback to the dispatch function; the attributes themselves can still be changed at-will.

[pointer_closure.py](pointer_closure.py): exploits mutable data structures in
Python to mutate state of enclosed variables.

[nonlocal_closure.py](nonlocal_closure.py): uses Python's `nonlocal` keyword to
mutate state directly. This is most analogous to Scheme's `set!` procedure.

I'm still looking for a way to implement mutable state in closures in Python
without relying on any secondary languages features, i.e. just using the
basic scoping rules and the fact that functions are first-class objects.
