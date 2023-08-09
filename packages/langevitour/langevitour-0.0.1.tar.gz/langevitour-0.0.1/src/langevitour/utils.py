def as_factor(group: list):
    mapping = {}
    for item in group:
        mapping.setdefault(item, len(mapping))
    return [mapping[item] for item in group], list(mapping.keys())
