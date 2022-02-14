"""The RecentDict class works just like a dict, except that it contains a
userdefined number of key-value pairs, which are determined when the instance is
created.

In a RecentDict(5), only the five most recent key-value pairs are kept;
if there are more than five pairs, then the oldest key is removed, along with its
value.

Note: your implementation could take into account the fact that modern
dicts store their key-value pairs in chronological order"""