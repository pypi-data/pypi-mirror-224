import pytest

def parse_attrs(attrs):
    parsed = {}
    for attr in attrs:
        if '=' in attr:
            key, value = attr.split('=', 1)
            parsed[key] = value
        else:
            parsed[attr] = True
    return parsed

def has_matching_attrs(item, parsed_attrs):
    for key, value in parsed_attrs.items():
        if getattr(item.obj, key, None) != value:
            return False
    return True

def pytest_addoption(parser):

    group = parser.getgroup("general")

    group._addoption("-a", action="append", default=[],
                     dest="attr", metavar="ATTR",
                     help='Only run tests matching given attribute expression.'
                          'Example: -a "attr1=val1".')

def attr(*args, **kwargs):
    def wrap_ob(ob):
        for name in args:
            setattr(ob, name, True)
        for name, value in kwargs.items():
            setattr(ob, name, value)
        return ob
    return wrap_ob

def pytest_collection_modifyitems(config, items):
    attrs = parse_attrs(config.option.attr)

    selected = []
    deselected = []
    for item in items:
        if has_matching_attrs(item, attrs):
            selected.append(item)
        else:
            deselected.append(item)

    config.hook.pytest_deselected(items=deselected)
    items[:] = selected
