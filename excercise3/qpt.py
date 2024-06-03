def shared_keys(d1, d2, d3):
    return set(d1.keys()) & set(d2.keys()) & set(d3.keys())

def non_shared_keys(d1, d2, d3):
    all_keys = set(d1.keys()) | set(d2.keys()) | set(d3.keys())
    shared = shared_keys(d1, d2, d3)
    return all_keys - shared

def key_count_in_dicts(key, dicts):
    return sum(1 for d in dicts if key in d)

def add_shared_keys(shared, dicts, result):
    if not shared:
        return result
    
    key = shared.pop()
    values = []
    for d in dicts:
        if key in d and d[key] not in values:
            values.append(d[key])
    result[key] = tuple(values)
    
    return add_shared_keys(shared, dicts, result)

def add_non_shared_keys(non_shared, dicts, result):
    if not non_shared:
        return result
    
    key = non_shared.pop()
    for d in dicts:
        if key in d:
            if key in result:
                if isinstance(result[key], tuple):
                    if d[key] not in result[key]:
                        result[key] += (d[key],)
                else:
                    result[key] = (result[key], d[key]) if result[key] != d[key] else result[key]
            else:
                result[key] = d[key]
    
    return add_non_shared_keys(non_shared, dicts, result)

def add2dicts(d1, d2, d3):
    shared = list(shared_keys(d1, d2, d3))
    non_shared = list(non_shared_keys(d1, d2, d3))
    dicts = [d1, d2, d3]

    all_keys = shared + non_shared
    all_keys.sort(key=lambda k: -key_count_in_dicts(k, dicts))
    
    shared.sort(key=lambda k: -key_count_in_dicts(k, dicts))
    non_shared.sort(key=lambda k: -key_count_in_dicts(k, dicts))

    result = add_shared_keys(shared, dicts, {})
    result = add_non_shared_keys(non_shared, dicts, result)
    
    return result

# Example usage
d1 = dict([(1, 'a'), (3, 'd'), (5, 'e')])
d2 = dict([(1, 'b'), (3, (11, 22)), (7, 'f'), (4, 'q')])
d3 = dict([(2, 'c'), (3, 'x'), (4, 't'), (8, 'g')])

print(add2dicts(d1, d2, d3))
