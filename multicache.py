#!/usr/bin/env python




def multi_cache(cache, get_key, get_values, items, *args, **kargs):

    if get_key is None:
        get_key = lambda item: item
    keys = [get_key(item, *args, **kargs) for item in items]

    def get_exists_and_value(key):
        try:
            return True, cache[key]
        except KeyError:
            return False, None
    
    exists, values = zip(*(get_exists_and_value(key) for key in enumerate(keys)))
    index_item_key_to_get = tuple(
        ((i, item, key)
        for i, (item, key, exist) in enumerate(zip(items, keys, exists))
        if not exist)
    )
    
    if index_item_key_to_get:
        items_to_get = tuple((item for i, item, key in index_item_key_to_get))
        gotten_values = get_func(items_to_get, *args, **kargs)
        for (i, item, key), value in zip(index_item_key_to_get, gotten_values):
            values[i] = value
            cache[key] = value

    return values
