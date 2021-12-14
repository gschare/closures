#!/bin/env python3

def my_closure(msg='none'):
    private = lambda: None
    private.msg = msg
    public = lambda: None

    def update(m):
        private.msg = m
        public.display = lambda: print(private.msg)

    def reset():
        update(msg)

    reset()

    public.update = update
    public.reset = reset

    return public

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
    # This style is dangerous because you can mutate methods themselves:
    a.update = lambda _: print('c: I am c, I promise!') # c hasn't even been declared yet!
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
