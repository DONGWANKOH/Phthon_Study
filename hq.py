from heapq import *

heap = []

heappush(heap, 4)
heappush(heap, 1)
heappush(heap, 7)
heappush(heap, 3)
print(heap)

print(heappop(heap))
print(heappop(heap))
print(heappop(heap))
print(heappop(heap))
print(heap)