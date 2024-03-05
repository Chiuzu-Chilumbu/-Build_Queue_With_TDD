"""unit tests to validate basic Queue operations"""

# test_queue.py

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

