# PCP-DeepDive-Python

Within the module Programming Concepts and Paradigms (PCP) at HSLU Thomas and Maurizio decided to have an 
extended look at Python. The programming language shall be analyzed and compared to other languages discussed in the
module. Furthermore, some previously solved exercise shall also be completed in Python to allow for further comparison.  

### Python Enhancement Proposals (PEPs)
In an analog manner to Java Enhancement Proposals (JEP), Python developers maintain a list of possible future 
enhancements to the Python Language named PEP.
Some features which we are going to discuss were such a Proposal once. They are going to be marked accordingly.

A Special guest here is [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/) which deserves some
special attention. PEP8 is a styleguide on how to write Python code. This leads (if you read warnings and follow the 
recommendations) to a more uniform look of the written programs in general.

If you write Python Code. It's a worth enabling automatic checks in your IDE of choice. But also to read through the 
styleguide. It's not a waste of time :-)

## DeepDive
Within this Project we are going to shed some light especially on the following topics

- Concurrency / Parallelism
- Duck-Typing 
- Indentation
- List Comprehension
- Yield
- Zen of Python

## Setup
This project is built and tested with Python version 3.9.
As for now no special libraries are used thus, the plain Python installation should suffice to run all the code.

## Concurrency / Parallelism
Python and Ruby (and probably some otters) use a Mechanism called **Global Interpreter Lock (GIL)**. 
This mechanism is used to synchronize the execution of threads so that there is only one thread (per process) active at 
a given time. Even if there are multiple CPU cores available only one thread will be active.

This is useful if a program has to deal with a lot of IO which is considered very slow and while a thread is waiting.
for IO to complete, another thread can to it's work. All threads share the same memory space.

On the other hand there is true parallelism by spawning multiple processes (instead of threads). These are not affected
by the GIL and will be running at the same time if the architecture allows it.
The downside is that Python needs to copy the whole memory space for each process. Depending on available resources
(RAM) this could lead to issues.


## Duck-Typing 
Why the name? :-)

## Indentation

## List Comprehension
PEP 202 – List Comprehensions was created on July, 13 2000 for Python 2.0. 
The idea was/is to allow conditional construction of list literals with if statements and loops.

```python
# Example before PEP202
my_list = []
for i in range(10):
    if i % 2 == 0:
        my_list.append(i)
        
# Example after PEP202
my_list = [i for i in range(10) if i % 2 == 0]
```

## Yield
## Zen of Python
[PEP 20 – The Zen of Python](https://peps.python.org/pep-0020/) was created in late August 2004. Tim Peters, a long 
time Pythoneer, wrote down 19 guiding principles on how to write Python programs.
Those principles remind us of [Clean Code](https://de.wikipedia.org/wiki/Clean_Code) by Robert C. Martin.

```Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```