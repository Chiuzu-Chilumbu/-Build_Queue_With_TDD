"""unit tests to validate basic Queue operations"""

# test_queue.py
def test_queue_enqueues_correctly(new_queue):
    assert new_queue.size() == 0, "Initially, queue should be empty."
    new_queue.enqueue('item')
    assert new_queue.size() == 1, "Queue should have one item after enqueue."

