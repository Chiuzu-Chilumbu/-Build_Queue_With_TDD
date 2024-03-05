"""Behavioural test to validate basic Queue operations"""
import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from queue.queue_adt import Queue

# Load scenarios from the feature file
scenarios('features/queue_operations.feature')



# Given Steps
@given('a new created queue object', target_fixture='queue')
def a_new_created_queue_object(new_queue):
    """a new created queue object."""
    return new_queue

@given('a queue with data in it')
def queue_with_data(new_queue):
    new_queue.enqueue('test_data')  # Add test data to the queue
    return new_queue


@given('a queue containing data with a certain size')
def queue_with_certain_size(new_queue):
    # Enqueue a known number of items; adjust size as needed for tests
    for i in range(3):
        new_queue.enqueue(f'data_{i}')
    return new_queue


# When Steps
@when('data is enqueued onto the queue')
def data_is_enqueued_onto_the_queue(new_queue):
    """data is enqueued onto the queue."""
    new_queue.enqueue('test_data')



@when('data is dequeued from the queue')
def dequeue_data(new_queue):
    return new_queue.dequeue()


@when('the size of the queue is checked')
def check_size(new_queue):
    return new_queue.size()


# Then Steps
@then('the data should be added onto the queue')
def the_data_should_be_added_onto_the_queue(new_queue):
    """the data should be added onto the queue."""
    assert new_queue.size() == 1
    assert new_queue.dequeue() == 'test_data', "The enqueued data should be 'test_data'"


@then('the data should be removed from the queue')
def data_removed(new_queue):
    # Assuming 'test_data' was the only item; adjust assertion as needed
    assert new_queue.size() == 0, "Queue should be empty after dequeue."


@then('the queue should return the size of the queue which is equivalent to the number of data in the queue')
def size_returned(new_queue):
    # Here we directly assert in the When step; adjust based on actual When
    # step action
    assert new_queue.size() == 3, "Queue size should match the number of enqueued items."