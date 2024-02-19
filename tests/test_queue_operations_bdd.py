"""Behavioural test to validate basic Queue operations"""

import pytest
from pytest_bdd import scenario, given, when, then
from queue.queue_adt import Queue

@scenario('features/queue_operations.feature',
          'The queue class should be able to enqueue data onto the created deque')


# Fixtures
@pytest.fixture
def new_queue():
    """Return a fresh instance of Queue."""
    return Queue()

# Given Steps
@given('a new created queue object', target_fixture='queue')
def a_new_created_queue_object(new_queue):
    """a new created queue object."""
    return new_queue

# When Steps
@when('data is enqueued onto the queue')
def data_is_enqueued_onto_the_queue(queue):
    """data is enqueued onto the queue."""
    queue.enqueue('test_data')

# Then Steps
@then('the data should be added onto the queue')
def the_data_should_be_added_onto_the_queue(queue):
    """the data should be added onto the queue."""
    assert len(queue) == 1
    assert queue.dequeue() == 'test_data', "The enqueued data should be 'test_data'"
