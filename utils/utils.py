import sys

def catch_error(base_fn):
    def enhaced_fn(*args):
        try:
            return base_fn(*args)
        except Exception as e:
            sys.stderr.write("Error: {}\n".format(e))
    return enhaced_fn

def to_list(obj, type):
    if obj is None:
        return []
    new = []
    for item in obj:
        v = list(item.values())
        if type:
            """Remove password from list"""
            v.pop(3)
        new.append(v)
    return new