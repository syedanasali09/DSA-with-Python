from collections import deque

D = deque([1, 2, 3, 4, 5, 6, 7, 8])
Q = deque()

for _ in range(3):
    Q.append(D.popleft())

D.append(D.popleft())

while Q:
    D.append(Q.popleft())

print("Final order of elements in D:", list(D))
