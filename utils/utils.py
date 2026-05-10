def to_list(obj):
    new = []
    for item in obj:
        v = list(item.values())
        """Remove password from list"""
        v.pop(3)
        new.append(v)
    return new