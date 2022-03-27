from exception.NullElementException import NullElementException
from exception.EmptyStackException import EmptyStackException
class Stack:

    def __init__(self):
        self.data = []

    def size(self):
        '''Returns an integer representing the total number of items in the stack.'''
        return len(self.data)

    def push(self, element):
        '''
        Pushes the element onto the top of the stack.
        Throws a custom NullElementException if the supplied element is null
        '''
        if element is None:
            raise NullElementException()
        self.data.append(element)

    def pop(self):
        '''
        Removes the top element from the stack and returns its value.
        Throws a custom EmptyStackException if the stack is empty when this method is called
        '''
        if self.empty():
            raise EmptyStackException()
        return self.data.pop()
    
    def peek(self):
        '''
        Retrieves the top element from the stack without removing it, and returns its value.
        Throws a custom EmptyStackException if the stack is empty when this method is called.
        '''
        if self.empty():
            raise EmptyStackException()
        return self.data[-1]

    def empty(self):
        '''Tests whether the stack is empty.'''
        return len(self.data) == 0
