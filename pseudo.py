import time

start_time = time.perf_counter()

fruits = ["apple", "banana", "mango"]
for i, fruit in enumerate(fruits):
    print(f"Index: {i}, Fruit: {fruit}")

fruits = ["apple", "banana", "mango"]
quantities = [5, 3, 4]
for fruit, quantity in zip(fruits, quantities):
    print(f"Fruit: {fruit}, Quantity: {quantity}")

print()

names = ["Alice", "Bob", "Charlie"]
favorite_food = ["Pizza", "Burger", "Sushi"]
for i, (name, food) in enumerate(zip(names, favorite_food)):
    print(f"Person {i+1} is {name} and their favorite food is {food}")

end_time = time.perf_counter()

print(f"Execution time: {end_time - start_time} seconds")

"""
The logging module in Python is used to track events that happen when some software runs. The software's developer adds logging calls to their code to indicate that certain events have occurred. An event is described by a descriptive message which can optionally contain variable data (i.e. data that is potentially different for each occurrence of the event). Events also have an importance which the developer ascribes to the event; the importance can also be used to filter out events.

An event's importance is ranked by the following levels:

- DEBUG: Detailed information, typically of interest only when diagnosing problems.
- INFO: Confirmation that things are working as expected.
- WARNING: An indication that something unexpected happened, or may happen in the future (e.g. ‘disk space low’). The software is still working as expected.
- ERROR: Due to a more serious problem, the software has not been able to perform some function.
- CRITICAL: A very serious error, indicating that the program itself may be unable to continue running.

The Logging functions are named after the level or severity of the events they are used to track. The standard levels and their applicability are described above.

Logging provides a set of convenience functions for simple logging usage. These are debug(), info(), warning(), error() and critical(). To determine when to use logging, see the notes on Debugging vs Logging.
"""

import logging

print()
# Create and configure logger
logging.basicConfig(level=logging.DEBUG)

# Creating an object
logger = logging.getLogger()

# Test messages
logger.debug("This is a debug message")
logger.info("This is an informational message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")

"""
"On the hour" is a phrase used to describe an event happening at the start of any given hour during the day. It's often used in relation to timekeeping and scheduling, particularly in public transportation and broadcasting. For example, if a train departs "on the hour" every hour, that means it leaves at times like 1:00, 2:00, 3:00, etc., rather than at times like 1:15, 2:35, or 3:42.
"""
