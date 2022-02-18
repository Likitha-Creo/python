from collections import deque
queue = deque([1, 2, 3, 4])
print(queue)
queue.append(5)
print(queue)
queue.append(6)
print(queue)
print(queue.popleft())
print(queue)
print(queue.popleft())
print(queue)

