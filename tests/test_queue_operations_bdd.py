"""Behavioural test to validate basic Queue operations"""

from queue import Queue
from pytest_bdd import scenario, given, when, then


@scenario('features/queue_operations.feature',
          'The queue class should be able to enqueue data onto the created deque')
def test_enqueue():
    pass


@given('a new created queue object')
def created_queue():
    return Queue()


@when('data is enqueued onto the queue')
def enqueue_data_onto_queue(created_queue):
    data = 'new_data'
    queue = created_queue
    queue.enqueue(data)
    return queue


@then('the data shoud be added onto the queue')
def test_data_should_be_in_queue(enque_data_onto_queue):
    queue = enque_data_onto_queue
    assert len(queue) == 1