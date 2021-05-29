import collections

def main():
    queue = collections.deque(maxlen=3)
    queue.extend([1,2,3])
    queue.popleft()
    print(queue)

main()
