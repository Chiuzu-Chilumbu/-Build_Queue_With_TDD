"""Unit test for individual components of the queue class"""

from queue import Queue


def test_should_create_a_stack_object_from_stack_class():
    """a class called Queue."""
    queue = Queue()
    assert queue is not None
    assert isinstance(queue, Queue)
