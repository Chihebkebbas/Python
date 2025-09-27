# tests/test_structures.py
import pytest
from src.stack import Stack
from src.queue import Queue

def test_stack_behavior():
    s = Stack()
    s.push(1); s.push(2)
    assert s.size() == 2
    assert s.peek() == 2
    assert s.pop() == 2
    assert s.pop() == 1
    with pytest.raises(IndexError):
        s.pop()

def test_queue_behavior():
    q = Queue()
    q.enqueue("a"); q.enqueue("b")
    assert q.size() == 2
    assert q.peek() == "a"
    assert q.dequeue() == "a"
    assert q.dequeue() == "b"
    with pytest.raises(IndexError):
        q.dequeue()
