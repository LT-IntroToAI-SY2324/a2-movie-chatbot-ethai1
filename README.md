---
title: 'Assignment 2: Movie Chatbot'
author: |
  | The original version of this assignment is taken from the textbook Concrete Abstractions:
  | An Introduction to Computer Science Using Scheme, by Max Hailperin, Barbara Kaiser,
  | and Karl Knight, Copyright (c) 1998 by the authors. Full text is available for free [here](http://www.gustavus.edu/+max/concrete-abstractions.html).
  | Assignment evolved at Pomona College through several instructors' offerings,
  | with changes by Nathan Shelly and Sara Sood, Northwestern University.
geometry: margin=1in
urlcolor: cyan
---

In this assignment, we begin to construct a natural language query system. We will create a program that will participate in dialogs like the following.

```text
Welcome to the movie database!

Your query? What movies were made in 1974?
Amarcord
Chinatown

Your query? Who acted in The Dresser?
Albert Finney
Tom Courtenay
Edward Fox
Zena Walker

Your query? What movies were directed by Federico Fellini?
Amarcord

Your query? Bye

So long!
```

In the example dialogue above, any text following the `Your query?` is a user input and everything else is stated by the system.

There are several parts to the program, and it is convenient (essential, even!) to consider them separately. In this assignment, we consider the textual patterns and how we can match them to real user input. In class, we will look at ways to create functions to attach to the patterns that we recognize. Finally, we will complete the program in Assignment 3.

Consider the questions below. There is a fixed pattern except for the year.

```text
What movies were made in 1974?
What movies were made in 1946?
What movies were made in 2001?
```

Or consider the questions

```text
Who acted in the movie Jaws?
Who directed the movie Citizen Kane?
```

These patterns are a little more complicated. The differences are that there are two parts in each question that can differ, "acted in" and "directed" as well as "Jaws" and "Citizen Kane." Also, the thing that differs *may* be more than one word.

Let us call a question like the ones above a `source`. A `pattern` is a string like one of these:

```text
what movies were made in _
who % the movie %
```

The idea is that we match words in the `source` with words in the `pattern`. The symbol `_` (an underscore) can match any single word, and the symbol `%` (a percent sign) can match a sequence of zero or more words.

The goal of this assignment is to write a function called `match`, that takes a `pattern` and a `source` as arguments (in that order, each as lists of strings) and returns either:

```text
* None (the NoneType) if the source does not match the pattern OR
* a list of substitutions (strings from the source that correspond to each _
and % in the pattern) if the source does match the pattern.
```
Note: The sequence of words that match a % in a pattern must all be condensed into one element of the returned list. There should be one space between each word in the sequence, but not at the beginning or end of the sequence. 

For example,

```python
match(['what', 'movies', 'were', 'made', 'in', '_'],
      ['what', 'movies', 'were', 'made', 'in', '1974'])
```
should return `['1974']`


```python
match(['who', '%', 'the', 'movie', '%'],
      ['who', 'acted', 'in', 'the', 'movie', 'jaws'])
```
should return `['acted in', 'jaws']`


```python
match(['who', '%', 'the', 'movie', '%'],
      ['what', 'movies', 'were', 'made', 'in', '1974'])
```
should return `None`

For simplicity, we do not allow our pattern to contain the sequence `['%', '%']` or `['%', '_']` because that would make the `match` function much more complicated.

You may assume that both the `pattern` and `source` lists of words are all lowercase.

You are welcome to come up with your own design for the match function and implement it. If you'd like more guidance we'll provide an outline below. Regardless of whether you use our outline or your own, we strongly recommend writing your logic out in English first before moving to python.

The structure of the my match will be as follows, using indices into the two lists.

```python
def match(pattern, source):
      sind = 0                # current index we are looking at in source list
      pind = 0                # current index we are looking at in pattern list
      result: List[str] = []  # store the substitutions that matched

      while "FILL IN CONDITION HERE":
            # do stuff here
```

The work is done in the body of the while loop. On each iteration, the function will take one step through the lists - at least one of the indices, and perhaps both, will be incremented by one. For example, `source[sind]` and `pattern[pind]` are equal it will simply increment the two indices. If `source[sind]` and `pattern[pind]` are not equal (and `pattern[pind]` is not a `%` or `_`), it will immediately return `None` because they do not match.

The body of the loop will be a sequence of cases using the structure `if ...elif ...elif ...else`. There will be several cases, and the order matters. You will need to consider what happens when the indices reach the end of the lists simultaneously and when one reaches the end before the other. (And notice that the pattern may end with `%`, in which case the source list may be longer than the pattern.)

Think carefully about all the cases before you begin to write any code. When you have written some code and find a problem, stop and analyze the difficulty. Go back and look at your overall plan before writing any more code. You should be in control of the code and not vice versa.

Remember that match takes two lists of strings and it returns a list of strings or `None`. The length of the result list is the same as the number of appearances of `_` and `%` in the pattern. Note also the different meanings between `[]` and `['']` and `None`.

The `assert` statements provided in `a2.py` show examples of correct results for the match function. If implemented correctly, your code should pass all of these asserts.

Write your match function in `a2.py`, once complete, push to github.
