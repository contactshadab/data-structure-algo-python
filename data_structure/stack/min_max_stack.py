class MinMaxStack:
    def __init__(self):
        self.stack = []
        self.min_max = []

    def peek(self):
        return self.stack[-1]

    def pop(self):
        self.min_max.pop()

        return self.stack.pop()

    def push(self, number):
        min_max = [number, number]
        if len(self.min_max) > 0:
            last_min_max = self.min_max[-1]
            min_max[0] = min(min_max[0], last_min_max[0])
            min_max[1] = max(min_max[1], last_min_max[1])

        self.min_max.append(min_max)
        self.stack.append(number)

    def getMin(self):
        return self.min_max[-1][0]

    def getMax(self):
        return self.min_max[-1][1]


if __name__ == "__main__":
    stack = MinMaxStack()
    stack.push(5)
    print(stack.getMin())
    print(stack.getMax())
    print(stack.peek())
    stack.push(7)
    print(stack.getMin())
    print(stack.getMax())
    print(stack.peek())
    stack.push(2)
    print(stack.getMin())
    print(stack.getMax())
    print(stack.peek())
    print(stack.pop())
    print(stack.pop())
    print(stack.getMin())
    print(stack.getMax())
    print(stack.peek())
