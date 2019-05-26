import collections
import time
class GeoDistributedLRUCache:
    def __init__(self, capacity, expiration = 10):
        self.capacity = capacity
        self.expiration = expiration
        self.cache = collections.OrderedDict()
        self.accessTime = {}
        self.size = 0
    
    def get(self, key):
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            self.accessTime[key] = time.time()
            return value
        except KeyError as e:
            print('Key not in cache! ', e)

    def add(self, key, value):
        if(self.size >= self.capacity):
            self.clearExpired()
            while(self.size >= self.capacity):
                self.cache.popitem(last = False)
                self.size -= 1

        # After clearing cache, and popping least recently used, size should be less than capacity
        if(self.size < self.capacity):
            self.cache[key] = value
            self.accessTime[key] = time.time()
            self.size += 1

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

    def clear(self):
        while(self.size > 0):
            self.cache.popitem(last = False)
            self.size -= 1

    def toString(self):
        for key, value in self.cache.items():
            print(key, value)

geoCache = GeoDistributedLRUCache(capacity= 5, expiration = 2)
geoCache.add('key0','string0')
geoCache.add('key1','string1')
geoCache.add('key2','string2')
geoCache.add('key3','string3')
geoCache.add('key4','string4')
geoCache.toString()
print(geoCache.get('key0'))
print(geoCache.get('key1'))
geoCache.add('key5','string5')
geoCache.toString()

time.sleep(3)
geoCache.add('newKey','newVal')


geoCache.toString()





