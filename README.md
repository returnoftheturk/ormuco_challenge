# ormuco_challenge

## Question 3 Documentation
The class LRUCache is a library I built to be used extensively
by Ormuco services.  
A new cache is initialized with parameters "capacity" and
"expiration".  Capacity is the total number of entries allowed into the cache. 
Expiration is the number of seconds until the cache entry expires and is deleted from the cache forever.  
```python
geoCache = GeoDistributedLRUCache(capacity = 100, expiration = 600)
```
The library has 7 public methods that are available to use: add, get, update, delete, clearExpired, clearCache, and toString.  Documentation for using functions are available above the function declarations in Q3.py

The library currently meets the following criteria:
1. Simplicity.  It is dead simple. Uses an ordered dictionary to account for LRU, and an extra dictionary to take into account time expiration.
2. Resilient to network failures and crashes (everything is local)
3. Not implemented
4. Not implemented, everything is local
5. Data is only stored local, so data is always available from closest region
6. Flexible schema
7. Cache can expire

In terms of Geolocation, the timestamps that take into account whether or not something has expired are saved as UTC time.  This is the same regardless of which geolocation you are, so consistency across geolocation for entry expiration is there. For feature 3 I am unsure how to build a library like this at the moment.  My guess would be that I would need to deploy this code somewhere online, and have a backend service running that stores the information in a real-time database.  Then calling these functions would perform the operations on objects stored on the database, which would mean real time replication across geolocation.  