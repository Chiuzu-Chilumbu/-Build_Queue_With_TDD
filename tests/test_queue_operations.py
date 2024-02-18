"""unit tests to validate basic Queue operations"""

import pytest
from queue import Queue


@pytest.fixture(scope='function')
def queue_object():
    return Queue()


def test_should_be_able_to_enqueue_data_onto_the_queue(queue_object):
    # Act
    new_queue = queue_object
    #  Arrange
    data = 'DATA'
    new_queue.enqueue(data)
    #  Assert
    assert new_queue.size() == 1
