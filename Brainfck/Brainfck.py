""" interpreter for Brainfuck """
import sys



class Interpreter:
    """ Interpret brainfuck code """

    def __init__(self, code):
        self.code = code

    def interpret(self):
        # count the > - < to determine memory locations
        mem = (self.code.count('>') + self.code.count('<')) - (self.code.count('<'))
        # initialize memory slots
        self.memory = []
        for m in range(mem+1):
            self.memory.append(0)

        # run the actual code
        ptr = 0
        loop_stack = []
        index = 0
        while index < len(self.code):
            char = self.code[index]
            if char == '>':
                ptr += 1
            elif char == '<':
                ptr -= 1
            elif char == '+':
                self.memory[ptr] += 1
            elif char == '-':
                self.memory[ptr] -= 1
            elif char == '[':
                loop_stack.append(index)
            elif char == ']':
                previndex = loop_stack[-1]
                if self.memory[ptr] > 0:
                    index = previndex
                    continue    # next loop
                # delete from stack
                loop_stack.pop()
            elif char == '.':
                sys.stdout.write(chr(self.memory[ptr]))
            index += 1
