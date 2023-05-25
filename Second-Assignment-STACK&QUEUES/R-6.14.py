from collections import deque

D = deque([1, 2, 3, 4, 5, 6, 7, 8])
S = []

for _ in range(3):
    S.append(D.popleft())

D.append(D.popleft())

while S:
    D.append(S.pop())

print("Final order of elements in D:", list(D))
