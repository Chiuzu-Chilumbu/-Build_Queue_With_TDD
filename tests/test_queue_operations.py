"""unit tests to validate basic Queue operations"""

import pytest


def test_queue_is_initially_empty(new_queue):
    assert new_queue.size() == 0, "New queue should be empty."

def test_queue_enqueues_correctly(new_queue):
    new_queue.enqueue('item')
    assert new_queue.size() == 1, "Queue should have one item after enqueue."
    assert 'item' == new_queue.queue[0], "Enqueued item should be in the queue."

def test_queue_multiple_enqueues(new_queue):
    items = ['item1', 'item2', 'item3']
    for item in items:
        new_queue.enqueue(item)
    assert new_queue.size() == len(items), "Queue size should equal the number of enqueued items."
    for i, item in enumerate(items):
        assert item == new_queue.queue[i], f"Item {i} in the queue should be {item}."


def test_queue_is_not_empty_after_enqueue(new_queue):
    new_queue.enqueue(1)
    assert new_queue.isEmpty() is False, "Queue should not be empty after enqueue operation"


def test_queue_is_full(new_queue):
    # Fill the queue to its capacity
    for i in range(5):  
        new_queue.enqueue(i)
    assert new_queue.isFull() is True, "Queue should be full when enqueued to capacity"


def test_enqueue_on_full_queue_raises_exception(new_queue):
    for i in range(5):  # Fill the queue to its capacity
        new_queue.enqueue(i)
    with pytest.raises(Exception) as e:
        new_queue.enqueue(4)
    assert str(e.value) == "Queue is Full"

def test_dequeue_on_empty_queue_raises_exception(new_queue):
    with pytest.raises(Exception) as e:
        new_queue.dequeue()
    assert str(e.value) == "Queue is empty"


def test_queue_is_not_full_after_dequeue(new_queue):
    # Fill the queue to its capacity
    for i in range(5):
        new_queue.enqueue(i)
    new_queue.dequeue()  # Remove one item
    assert new_queue.isFull() is False, "Queue should not be full after dequeue operation"


def test_queue_becomes_empty_after_clearing(new_queue):
    for i in range(5):  # Fill the queue
        new_queue.enqueue(i)
    for _ in range(5):  # Empty the queue
        new_queue.dequeue()
    assert new_queue.isEmpty() is True, "Queue should be empty after removing all items"


def test_peek_operation(new_queue):
    new_queue.enqueue('peek_item')
    assert new_queue.peek() == 'peek_item', "Peek should return the first item without removing it."
    assert new_queue.size() == 1, "Queue size should not change after peek operation."