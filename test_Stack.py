#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
from Stack import Stack
from exception.NullElementException import NullElementException
from exception.EmptyStackException import EmptyStackException

class TestStack(unittest.TestCase):

    def test_size(self):
        stack = Stack()
        self.assertEqual(stack.size(), 0)
        self.assertEqual(stack.empty(), True)

    def test_push(self):
        stack = Stack()
        stack.push('a')
        stack.push('b')
        self.assertEqual(stack.size(), 2)
        self.assertEqual(stack.empty(), False)

    def test_push_none(self):
        stack = Stack()
        with self.assertRaises(NullElementException):
            stack.push(None)

    def test_pop(self):
        stack = Stack()
        stack.push('a')
        self.assertEqual(stack.pop(), 'a')
    
    def test_pop_empty_stack(self):
        stack = Stack()
        with self.assertRaises(EmptyStackException):
            stack.pop()

    def test_pop(self):
        stack = Stack()
        stack.push('a')
        self.assertEqual(stack.peek(), 'a')
    
    def test_pop_empty_stack(self):
        stack = Stack()
        with self.assertRaises(EmptyStackException):
            stack.peek()

    def test_empty(self):
        stack = Stack()
        self.assertEqual(stack.empty(), True)


if __name__ == '__main__':
    unittest.main()