from collections import deque

deq = deque()

deq.appendleft(4)
print("add_first(4) -> Deque:", deq)

deq.append(8)
print("add_last(8) -> Deque:", deq)

deq.append(9)
print("add_last(9) -> Deque:", deq)

deq.appendleft(5)
print("add_first(5) -> Deque:", deq)

back_value = deq[-1]
print("back() -> Returned value:", back_value)

deleted_first = deq.popleft()
print("delete_first() -> Deleted value:", deleted_first)
print("After delete_first() -> Deque:", deq)

deleted_last = deq.pop()
print("delete_last() -> Deleted value:", deleted_last)
print("After delete_last() -> Deque:", deq)

deq.append(7)
print("add_last(7) -> Deque:", deq)

first_value = deq[0]
print("first() -> Returned value:", first_value)

last_value = deq[-1]
print("last() -> Returned value:", last_value)

deq.append(6)
print("add_last(6) -> Deque:", deq)

deleted_first = deq.popleft()
print("delete_first() -> Deleted value:", deleted_first)
print("After delete_first() -> Deque:", deq)

deleted_first = deq.popleft()
print("delete_first() -> Deleted value:", deleted_first)
print("After delete_first() -> Deque:", deq)