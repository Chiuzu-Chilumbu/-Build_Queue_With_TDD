"""Test steps for testing the Queue class with BDD"""

from queue import Queue
from pytest_bdd import scenario, given, when, then


@scenario('features/create_queue.feature',
          'A queue object should be created from the queue class')
def instantiate_a_queue_object_from_queue_class():
    """A queue object should be created from the queue class."""
    pass


@given('a class called Queue')
def should_contain_a_queue_class():
    """a class called Queue."""
    pass


@when('an object is instantiated from the Queue class')
def test_object_should_be_created_from_queue_class():
    """an object is instantiated from the Queue class."""
    queue = Queue()
    assert queue is not None


@then('The object should be an instance of the queue class')
def test_created_object_should_be_instance_of_queue_class():
    """The object should be an instance of the queue class."""
    queue = Queue()
    assert isinstance(queue, Queue)
