import collections
import collections.abc
import json


def mm_format(x):
    if isinstance(x, str):
        return json.dumps(x)
    elif isinstance(x, collections.UserString):
        return json.dumps(x.data)
    elif isinstance(x, complex):
        return str(x).replace('j', 'I', 1).replace('(', '', 1).replace(')', '', 1)
    elif isinstance(x, (list, tuple, range, set, frozenset, collections.deque, collections.abc.Sequence)):
        return ''.join(('{', ','.join(mm_format(y) for y in x), '}'))
    elif isinstance(x, (dict, collections.abc.Mapping)):
        return ''.join(('<|', ','.join(''.join((mm_format(k), '->', mm_format(v))) for k, v in x.items()), '|>'))
    else:
        return str(x)
