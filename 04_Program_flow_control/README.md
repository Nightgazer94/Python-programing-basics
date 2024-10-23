![Coders-Lab-1920px-no-background](https://user-images.githubusercontent.com/30623667/104709394-2cabee80-571f-11eb-9518-ea6a794e558e.png)


## Exercise 1 &ndash; Loop `while`

In `task.py`, display on the screen 10 times: `I am a Python programmer`.

> Use the `while` loop.


## Exercise 2 &ndash; Successive powers

In the file `task.py` write a program that calculates successive powers of the number 2 for an exponent between 0 and 10 inclusive.

Display the result in the following format:
```
2 to the power of 0 is 1
2 to the power of 1 is 2
2 to the power of 2 is 4
2 to the power of 3 is 8
2 to the power of 4 is 16
2 to the power of 5 is 32
2 to the power of 6 is 64
2 to the power of 7 is 128
2 to the power of 8 is 256
2 to the power of 9 is 512
2 to the power of 10 is 1024
```

> Use the `for` loop.


## Exercise 3 &ndash; Comparison of names

In the file `task.py` write a program that:

* displays the message `Enter your name: ` on the screen,
* retrieves a name from the keyboard and writes it to the variable `first_name`,
* displays `Enter your middle name: ` on the screen,
* retrieves the user's middle name from the keyboard and stores it in the variable `second_name`,
* display `Same` if the names are the same or `Different` if they are different.

> Hint: use the conditional statement `if`!


## Exercise 4 &ndash; Comparison of numbers

In `task.py`, write a program that takes the numbers `a` and `b` from the user.

Print out the information which of these is greater in the form:
```
a is greater!
```
or
```
b is greater!
```

> Hint: remember to convert numbers into numeric type (e.g. `float`)!
> Strings are compared in lexicographic order.


## Exercise 5 &ndash; Quadratic equations

In the file `task.py`, write a program to help high school students calculate the roots of quadratic equations. The program has to:

* display the message on the screen: `Equation a*x**2 + b*x + c == 0`,
* display on the screen the message: `Enter a`,
* get a value from the user and save it to the variable `a` (remember to convert to the correct type),
* display a message on the screen: `Enter b`,
* get a value from the user and save it to the variable `b` (remember to convert to the appropriate type),
* display a message on the screen: `Enter c`,
* get the value from the user and write it to the variable `c` (remember to convert to the appropriate type),
* calculate the delta,
* if delta > 0, count values of `x_1` and `x_2` according to the formulas:
```
x_1 = (-b - delta**0.5) / (2 * a)
x_2 = (-b + delta**0.5) / (2 * a)
```
and then display it as:
```
Primes of the quadratic equation:
x_1 = <value>
x_2 = <value>
```
* if delta = 0, count the values of `x_1` and `x_2` and then display it on the screen as:
```
Primes of the quadratic equation:
x_1 = x_2 = <value>

```
* if the delta is negative, print `no solution` on the screen.

**Note** Assume that the user correctly enters the numbers `a`, `b`, and `c`.


## Exercise 6 &ndash; Sum of numbers

In `task.py`, write a program that calculates the sum of all numbers from 0 to `n`. `n` is entered by the user.

Example:
```
Enter n: 4
10
```


## Exercise 7 &ndash; Mean

In file `task.py`, write a program that:
* creates a variable `numbers` and assigns an empty list to it,
* takes from the user the information about how many numbers they want to enter, and stores this information in the variable `n`,
* in a loop (which will be executed `n` times):
  * asks the user for a number
  * adds the number specified by the user to the end of the `numbers` list
* counts their sum and average (arithmetic mean),
* prints on the screen: these numbers and information if the sum is greater than the average:
```
Enter n: 4
Enter a number: 1
Enter a number: 2
Enter a number: -4
Enter a number: 5
Entered numbers: 1 2 -4 5
Sum: 4,
average: 1
The sum is greater!
```


## Exercise 8 &ndash; Defining a list of numbers

* Define a list consisting of the numbers from 1 to 8.
* List each of these numbers on a separate line, preceded by the word `number: `.

Example:
```
number: 1
number: 2
number: 3
number: 4
number: 5
number: 6
number: 7
number: 8
```


## Exercise 9 &ndash; Multiplication table

In the file `task.py`, write a program that takes a number `n` (from 1 to 10) from the user, and then generates operations with the results of multiplying the given `n` by numbers from 1 to 10.

##### Expected result:
```
Entered number: 3
1 * 3 = 3
2 * 3 = 6
3 * 3 = 9
4 * 3 = 12
5 * 3 = 15
6 * 3 = 18
7 * 3 = 21
8 * 3 = 24
9 * 3 = 27
10 * 3 = 30
```


## Exercise 10 &ndash; Fizzbuzz

In `task.py`, use the `for` loop to write the program FizzBuzz. In the loop that will be executed for numbers between 1 and 100 (inclusive):
* if the number is divisible by 3 and 5, output `FizzBuzz` (for example, for the number 15, **only** `FizzBuzz` should be displayed),
* if the number is divisible by 3, output `Fizz`,
* if the number is divisible by 5, output `Buzz`,
* otherwise, write the number on the screen.

```
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
...
```
