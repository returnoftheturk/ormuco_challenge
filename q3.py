import collections
import time
class GeoDistributedLRUCache:
    def __init__(self, capacity, expiration = 10):
        self.capacity = capacity
        self.expiration = expiration
        self.cache = collections.OrderedDict()
        self.accessTime = {}
        self.size = 0
    
    '''
    Finds a key in the cache and returns in
    First pops the key and adds it back into 
    cache to renew access time, and to put 
    into beginning of the line (most recently used
    to should be last popped)
    '''
    def get(self, key):
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            self.accessTime[key] = time.time()
            return value
        except KeyError as e:
            print('Key not in cache! ', e)

    '''
    First clears expired cache entries.
    While size > capacity, pops items from cache
    in Least Recently Used manner.
    '''
    def add(self, key, value):
        self.clearExpired()

        while(self.size >= self.capacity):
            self.cache.popitem(last = False)
            self.size -= 1

        # After clearing cache, and popping least recently used, size should be less than capacity
        if(self.size < self.capacity):
            self.cache[key] = value
            self.accessTime[key] = time.time()
            self.size += 1
    
    '''
    Updates cache entry if it finds the key value pair,
    if not catches error and logs to user
    '''
    def update(self, key, value):
        try:
            self.cache.pop(key)
            self.cache[key] = value
            self.accessTime[key] = time.time()
            return value
        except KeyError as e:
            print('Key not in cache! ', e)

    '''
    Deletes a key value pair from the cache 
    if it finds it, else reports error back to user
    '''
    def delete(self, key):
        try: 
            self.cache.pop(key)
            del self.accessTime[key]
            self.size -= 1
        except KeyError as e:
            print('Key not in cache! ', e)

    '''
    Checks each entry in the cache to see 
    if suffifient time has passed for the 
    cache entry to expire, if it has then
    the cache entry is deleted
    '''
    def clearExpired(self):
        curTime = time.time()
        deleted = []
        for key, value in self.accessTime.items():
            if( curTime - value > self.expiration):
                if key in self.cache:
                    del self.cache[key]
                    deleted.append(key)
                    self.size -= 1
                    print('deleted ', key)
        for key in deleted:
            del self.accessTime[key]

    '''
    Clears the cache completely.  Deletes 
    all entries 
    '''
    def clearCache(self):
        self.accessTime.clear()
        self.cache.clear()
        self.size = 0

    '''
    Prints key value pairs from the cache
    '''
    def toString(self):
        for key, value in self.cache.items():
            print(key, value)

geoCache = GeoDistributedLRUCache(capacity= 5, expiration = 2)
geoCache.add('key0','string0')
geoCache.add('key1','string1')
geoCache.add('key2','string2')
geoCache.add('key3','string3')
geoCache.add('key4','string4')
print(geoCache.get('key0'))
print(geoCache.get('key1'))
geoCache.add('key5','string5')
geoCache.update('key2','string2updated')

# time.sleep(3)
geoCache.add('newKey','newVal')


geoCache.toString()
geoCache.clearCache()
geoCache.toString()





