def print_alter(person):
    """
    >>> print_alter(dict(alter=25))
    25
    >>> print_alter(dict(alter=17))
    17
    """
    # FIXME: Hier kommt dein Code.



person = {
    "name": "Satoshi",
    "alter": 19,
}
print_alter(person)


def increment_alter(person):
    """
    >>> person =  dict(alter=25)
    >>> increment_alter(person)
    >>> person
    {'alter': 26}
    """
    # FIXME: Hier kommt dein Code.



increment_alter(person)
print(person)

import doctest
#print(doctest.testmod(report=False))
