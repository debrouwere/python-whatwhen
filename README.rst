Whatwhen
========

``whatwhen`` is a higher-level topological sort, a useful algorithm to
resolve dependencies and calculate a workable execution order for
functions and other things.

Basic topological sorting:

::

    tasks = [
        {
            'name: 'drive', 
            'dependencies': ['car'], 
        }, {
            'name': 'car', 
            'dependencies': ['wheels', 'gas'], 
        }, {
            'name': 'wheels', 
            'dependencies': 'rubber', 
        }, {
            'name': 'gas', 
        }, {
            'name': 'rubber', 
        }, 
    ]

    whatwhen.sort(items)

Topological sorting using contracts (needs and provisions):

::

    tasks = [
        {
            'name': 'drive', 
            'needs': ['car', 'gas'], 
        }, {
            'name': 'fill tank', 
            'provides': ['gas'], 
        }, {
            'name': 'rent a car', 
            'provides': ['car'], 
            'dependencies': ['money'],
        }, {
            'name': 'money'
        }
    ]

    whatwhen.sort(items)

Needs and provisions are useful when you don't know exactly what
function (or system or module or whatever) is going to provide the
necessary data or preconditions, but you do know what that data or those
preconditions are. This might happen in large systems or systems over
which you don't have full control.

In addition to dictionaries, the metadata on tasks can also be added to
functions:

::

    def one():
        pass

    def two():
        pass

    one.dependencies = ['two']

    whatwhen.sort([one, two])

Whatwhen will return the original functions (or dictionaries) in sorted
order, rather than just a sorted list of node names, so it's slightly
easier to work with than a raw topological sort.

Whatwhen lets the `tarjan <https://github.com/bwesterb/py-tarjan>`__
module do most of the heavy lifting, so there's really only about 40
lines of wrapper code to this module. It's up to you to decide whether
you'd rather build on top of WhatWhen or plain Tarjan.
