# PCP-Vertiefung-Python

Im Rahmen des Modules Programming Concepts and Paradigms (PCP) an der HSLU haben sich Thomas und Maurizio entschieden, 
Python als Sprache vertieft anzuschauen.

Die Programmiersprache wird dabei generell betrachet. Es werden Hauptparadigmen identifiziert und Spezialitäten der 
Sprache hervorgehoben.


### Python Enhancement Proposals (PEPs)
In an analog manner to Java Enhancement Proposals (JEP), Python developers maintain a list of possible future 
enhancements to the Language named PEP.
Some features which we are going to discuss were a PEP once and are marked accordingly.

A Special guest here is [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/) which deserves some
special attention. PEP8 is a styleguide on how to write Python code. This leads (if you read warnings and follow the 
recommendations) to a uniform look of the written Programms in general.

If you start writing Python Code. It's a worth enabling automatic checks in your IDE of choice. But also to read 
through the styleguide. :-)  

## Vertiefung
Auf folgende Punkte wird im Rahmen der Arbeit genauer eingegangen.

- Concurrency / Parallelism
- Duck-Typing 
- Indentation
- List Comprehension
- Yield
- Zen of Python




## Setup


## Concurrency / Parallelism
Python and Ruby (and probably some otters) use a Mechanism called **Global Interpreter Lock (GIL)**. 
This mechanism is used to synchronize the execution of threads so that there is only one thread (per process) active at 
a given time. Even if there are multiple CPU cores available only one thread will be active.

This is still very useful if a program has to deal with a lot of IO which is considered very slow.
The beneficial part is that all the threads share the same memory space.

On the other hand there is true parallelism by spawning multiple processes (instead of threads). These are not affected
by the GIL and will be running at the same time if the architecture allows it.
The downside is that Python needs to copy the whole memory for each process. Depending on available resources (Memory)
this could lead to issues.



## Duck-Typing 
Why the name? :-)

## Indentation

## List Comprehension
PEP 202 – List Comprehensions was created on July, 13 2000 for Python 2.0. 
The idea was/is to allow conditional construction of list literals with if statements and for loops.

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