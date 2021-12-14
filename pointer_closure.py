#!/bin/env python3

def _my_closure(msg='none'):
    MSG = 0
    DISPLAY = 1
    private = [msg, lambda: None]

    def update(m):
        private[MSG] = m
        private[DISPLAY] = lambda: print(private[MSG])

    def reset():
        update(msg)

    reset()

    def dispatch(m):
        if m == 'display':
            return private[DISPLAY]
        if m == 'update':
            return update
        if m == 'reset':
            return reset
        else:
            print("Error: unknown op:", m)
            return None

    return dispatch

def my_closure(msg='none'):
    closure = _my_closure(msg)
    closure.display = closure('display')
    closure.update = closure('update')
    closure.reset = closure('reset')
    return closure

def main():
    a = my_closure('a')
    b = my_closure('b')

    a.display()
    print()

    a.update('a: meet me at the docks tonight')
    b.display()
    print()

    b.update('b: the bird is in the nest')
    a.display()
    # This style still lets us mutate the attributes but because this is a wrapper, we can always fall back to the real versions:
    a.update = lambda _: print('c: I am c, I promise!')
    a('update')('a: No one can touch me!')
    a.display()
    a.update = a('update')
    print()

    a.update('a: this message will self destruct')
    a.display()
    print()

    a.reset()
    a.display()
    b.display()
    print()

    c = my_closure('c')
    c.display()
    c.update('c: no one bothered me this whole time')
    c.display()

main()
