cache_size, city = 3,   ["Jeju", 'Pangyo', "Seoul", "NewYork", "LA", "Jeju", "Pangyo", \
                        "Seoul", "NewYork", "LA"]
cache_old = [ 6, 4, 9 ]


ind = cache_old.index(min(cache_old))

cache_old.pop(ind)
print(cache_old)
