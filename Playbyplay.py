class PlayByPlayStack:
    def __init__(self):
        self.plays = []

    # A boolean return of whether the stack is empty
    def is_empty(self):
        return len(self.plays) == 0

    # This will add a play to end (top) of stack
    def push(self, play):
        self.plays.append(play)

    # This will pop the top element (if there is one)
    # Maybe use else in here to say "New inning start" or "Game over" or something like that
    def pop(self):
        if not self.is_empty():
            return self.plays.pop()
        else:
            raise IndexError("pop from an empty stack")

    # This will return the top element (if there is one)
    def peek(self):
        if not self.is_empty():
            return self.plays[-1]
        else:
            raise IndexError("peek from an empty stack")

    # This will empty the stack (performed every half-inning)
    def empty(self):
        while not self.is_empty():
            self.plays.pop()

    # This will return size of the stack
    def size(self):
        return len(self.plays)


if __name__ == "__main__":

    # Testing out usage:
    stack = PlayByPlayStack()

    print("Is the stack empty? ", stack.is_empty())  # Output: True

    stack.push("Marquis with a single")
    stack.push("McMullen with an out")
    stack.push("Mathew with a double")

    print("Top of the stack:", stack.peek())  # Output: 3
    print("Size of the stack:", stack.size())  # Output: 3

    popped_item = stack.pop()
    print("Popped item:", popped_item)  # Output: 3

    print("Is the stack empty? ", stack.is_empty())  # Output: False

    stack.empty()
    print("Is the stack empty? ", stack.is_empty())  # Output: True
