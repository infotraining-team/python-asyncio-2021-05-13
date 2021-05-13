import time
from collections import deque

def task(n):
    while n > 0:
        time.sleep(0.3)
        yield n
        n -= 1

persons = deque(("Ola", "Ala", "Ela"))

def get_person(persons):
    yield from persons

def greet(gen):
    while True:
        try:
            person = next(gen)
            yield f"Hello {person}" ## await
        except StopIteration:
            break

tasks = deque( (task(5), get_person(persons), task(10), greet(get_person(persons))) )

def task_runner(queue: deque):
    while tasks:
        task = queue.popleft()
        try:
            x = next(task)
            print(x)
            queue.append(task)
        except StopIteration:
            print("task finished")

task_runner(tasks)