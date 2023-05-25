def _resize(self, cap):  
    old = self._data
    self._data = [None] * cap
    walk = self._front
    for k in range(self._size): 
        self._data[k] = old[k]
        walk = (1 + walk) % len(old)
    self._front = 0
    