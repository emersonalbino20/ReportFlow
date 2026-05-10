def to_list(obj, type):
    new = []
    for item in obj:
        v = list(item.values())
        if type:
            """Remove password from list"""
            v.pop(3)
        new.append(v)
    return new