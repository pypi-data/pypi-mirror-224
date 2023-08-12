# encoding: utf-8

import sys

if sys.version_info[0] < 3:
    text_type = unicode  # NOQA
else:
    text_type = str


# used by LDAPBase and db/mongo to calculate history
def diff_dict(olddict, newdict, skip_leading_underscore=False, utf8=False):
    """Compare newdict and olddict generating a dictionary of elements
    that need to be added to olddict to get newdict and a list of keys
    of olddict elements that are not in newdict at all
    """
    difference = {}
    removed = []
    for key, val in olddict.items():
        if skip_leading_underscore and key[0] == '_':
            continue
        try:
            # utf8 as mongodb maps values to utf-8
            if utf8 and isinstance(val, text_type):
                val = val.encode('utf-8')
            if key not in newdict or val != newdict[key]:
                difference[key] = val
        except UnicodeWarning:
            print(repr(key))
            print(repr(newdict))
            print('val', repr(val))
            raise
    for key in newdict.keys():
        if skip_leading_underscore and key[0] == '_':
            continue
        if key not in olddict:
            removed.append(key)
    return difference, removed


def revert_dict(latest, history, ts):
    """assume that latest is a tuple(dict, timestamp, author)
    history is a mapping from timestamps to
        tuple (oldvalues_dict, delete_list, author)
    and ts is the oldest timestamp
    ts must be comparable to the keys of history
    return: tuple (dictionary_state_at_ts, author,
                   latest_timestamp_older_equal_ts)
    """
    dictionary, timestamp, author = latest[0].copy(), latest[1], latest[2]
    timestamps = sorted(history.keys(), reverse=True)
    # older than oldest entry -> object did not exist
    if not history or ts < timestamps[-1]:
        return {}, None, None
    for timestamp in timestamps:
        values, del_list, author = history[timestamp]
        dictionary.update(values)
        for key in del_list:
            del dictionary[key]
        # after update, so that you get the last state before or on ts
        if timestamp <= ts:
            break
    return dictionary, timestamp, author
