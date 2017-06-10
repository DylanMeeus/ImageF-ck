""" interpreter for Brainfuck """
import sys
import copy


class Interpreter:
    """ Interpret brainfuck code """

    def __init__(self, code):
        self.code = code

    def interpret(self):
        # initial memory estimate
        mem_estimate = self.code.count('>') if self.code.count('>') > 0 else 1

        # initialize memory slots
        self.memory = []
        for m in range(mem_estimate):
            self.memory.append(0)

        # run the actual code
        ptr = 0
        loop_stack = []
        index = 0
        while index < len(self.code):
            char = self.code[index]
            if char == '>':
                self.ensureCapacity(ptr)
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
                    ignore_loop_stack = ['[']
                    index += 1
                    while len(ignore_loop_stack) > 0: # need to find the MATCHING ], not just the first
                        if self.code[index] == ']':
                            ignore_loop_stack.pop()
                        elif self.code[index] == '[':
                            ignore_loop_stack.append('[')
                        index += 1
                    index -= 1      # we overjumped so we go one back now.

            elif char == ']':
                if len(loop_stack) > 0:
                    previndex = loop_stack[-1]
                    if self.memory[ptr] > 0:
                        index = previndex
                    else:
                        loop_stack.pop()

            elif char == '.':
                sys.stdout.write(chr(self.memory[ptr]))

            elif char == ',':
                firstbyte = input()[0]
                self.memory[ptr] = ord(firstbyte)

            index += 1


    def ensureCapacity(self,ptr):
        """ ensure the current pointer is in the memory limits """
        if ptr < len(self.memory)-1:
            return
        self.expandMemory()

    def expandMemory(self):
        oldsize = len(self.memory)
        newsize = (oldsize * 3) // 2 + 1

        while oldsize < newsize:
            self.memory.append(0)
