""" interpreter for Brainfuck """
import sys



class Interpreter:
    """ Interpret brainfuck code """

    def __init__(self, code):
        self.code = code

    def interpret(self):
        # count the > - < to determine memory locations
        mem = (self.code.count('>')) # + self.code.count('<')) - (self.code.count('<'))
        # initialize memory slots
        self.memory = []
        for m in range(mem+1000000):
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
                if self.memory[ptr] > 0:
                    loop_stack.append(index)
                else:
                    # ignore the rest of the statements until the next ] is found
                    while self.code[index] != ']':
                        print(self.code[index])
                        index += 1

            elif char == ']':
                if len(loop_stack) > 0:
                    previndex = loop_stack[-1]
                    if self.memory[ptr] > 0:
                        index = previndex
                    else:
                        loop_stack.pop()
            elif char == '.':
                sys.stdout.write(chr(self.memory[ptr]))
            index += 1
