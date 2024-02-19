# Feature file with description of queue operations

Feature: Created Queue class must be able to perform the basic operations

  Scenario: The queue class should be able to enqueue data onto the created deque
    Given a new created queue object
    When data is enqueued onto the queue
    Then the data should be added onto the queue
