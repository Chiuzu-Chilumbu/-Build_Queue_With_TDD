# Queue ADT Built with TDD and BDD

This repository showcases the development of a Queue Abstract Data Type (ADT) employing Test-Driven Development (TDD) and Behavior-Driven Development (BDD) methodologies. Building upon the foundations of a previous Stack ADT project, this iteration advances the project's sophistication by integrating a Continuous Integration/Continuous Deployment (CI/CD) pipeline, leveraging additional pytest plugins for enhanced testing insights, and utilizing JUnit for the visualization of test results.

## Overview

The Queue ADT implemented in this project follows the First In, First Out (FIFO) principle. The development process was meticulously structured to emphasize code quality and functionality, ensuring the Queue operations are efficiently and correctly implemented.

## Development stages

- **Sage One**: Setup of the project structure with initial BDD scenarios. Incorporation of pytest-bdd fixtures and advanced assertions for robust BDD tests.
- **Stage Two**: Implementation of core Queue functionalities such as enqueue, dequeue, and checks for empty and full states, accompanied by comprehensive unit and BDD tests. Enhancement of the Queue with additional features and thorough testing to cover all possible use cases.
- **Stage Three**: Integration of a CI/CD pipeline to automate testing and deployment, adoption of pytest-cov for code coverage analysis, and JUnit for reporting test results.

## Features

The Queue supports several operations, providing a versatile data structure for various applications:

- **Enqueue**: Add an element to the end of the queue.
- **Dequeue**: Remove and return the element at the front of the queue.
- **Peek**: Return the front element without removing it.
- **isEmpty**: Determine if the queue is empty.
- **isFull**: Check if the queue has reached its capacity limit.
- **Size**: Obtain the current number of elements in the queue.

## Testing

A comprehensive test suite ensures the Queue ADT's reliability:

- **Unit Tests**: Execute `pytest tests/` to run unit tests that validate each Queue operation.
- **BDD Tests**: Utilize pytest-bdd for behavior-driven tests, closely aligning test scenarios with the expected behavior of the Queue.
- **Code Coverage**: Apply pytest-cov to measure test coverage, ensuring all code paths are verified.
- **Test Reporting**: Generate JUnit reports to visualize test execution results, enhancing the feedback loop for developers.

## CI/CD Pipeline

The project's CI/CD pipeline, implemented via GitHub Actions, automates the execution of tests, code coverage analysis, and deployment processes. This setup ensures that every commit and pull request is automatically tested, and code quality metrics are readily available for review.

## Linting

Code quality and consistency are maintained through pylint checks:

```bash
pylint queue_adt
```

## Acknowledgments

Inspiration for adopting TDD and BDD methodologies was drawn from various educational resources, including Test Automation Universtiy RealPython tutorials. Special thanks to the Python and testing communities for their invaluable resources and support.
