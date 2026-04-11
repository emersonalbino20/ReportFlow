def to_list(obj):
    new = []
    for item in obj:
        new.append(list(item.values()))
    return new