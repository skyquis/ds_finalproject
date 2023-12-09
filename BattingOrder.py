from collections import deque
from QueueEmptyException import QueueEmptyException


class BattingOrderQueue:
    def __init__(self):
        self.size = 0
        self.queue = deque()

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise QueueEmptyException("Can't dequeue - Batting Order Queue is empty!")
        self.size -= 1
        deq_string = self.queue.popleft()
        return deq_string

    def peek(self):
        if self.is_empty():
            raise QueueEmptyException("Can't peek - Batting Order Queue is empty!")
        peek_string = self.queue[0]
        return peek_string

    def display(self):
        print("Batting order is as follows: ")
        for j in range(0, self.size):
            print(f"{self.queue[j]}")


if __name__ == "__main__":
    boq = BattingOrderQueue()
    boq.enqueue("A")
    boq.enqueue("B")
    boq.enqueue("C")

    boq.display()

    first_in_queue = boq.peek()
    print("First peek result: " + first_in_queue)

    first_in_queue = boq.dequeue()
    print("First dequeue result: " + first_in_queue)

    second_in_queue = boq.peek()
    print(second_in_queue, boq.size)

    # print out queue to show only 2 items in there
    boq.display()

    boq.enqueue(first_in_queue)
    print(boq.size)

    boq.display()
