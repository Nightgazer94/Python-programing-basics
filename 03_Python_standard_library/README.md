![Coders-Lab-1920px-no-background](https://user-images.githubusercontent.com/30623667/104709394-2cabee80-571f-11eb-9518-ea6a794e558e.png)


## Exercise 1 &ndash; Retrieving data from the user

In file `task.py` write a program that:

1. retrieves the user's name from the keyboard,
2. retrieves the user's surname from the keyboard,
3. displays the message "Name Surname is a Python programmer!"

**Example:**
```
Enter name: Guido
Enter surname: van Rossum
Guido van Rossum is a Python programmer!
```

**Hint:** write user input to variables.


## Exercise 2 &ndash; Joining a list

In the file `task.py`, define an array of letters from `a` to `e`. Then output these letters connected by a space character.

Use the `join` method to concatenate the letters together.

The result of your program should be:
```
a b c d e
```


## Exercise 3 &ndash; Modulo

In the file `task.py` create variables named `a` and `b` and assign arbitrary numbers to them. Calculate the remainder of the division of these numbers (modulo) and assign the result to the variable `result`.

Output the variable `result` in the console.

> If you do not fully understand the modulo operator, practice with other numbers.

Sample program result (for `a = 53` and `b = 17`):
```
2
```


## Exercise 4 &ndash; Increment and decrement

In the file `task.py`, find the variable `counter` with the value `145`. Then:
* output its value in the console
* increment the variable `counter` by 1,
* display it on the console,
* decrement the variable `counter` by 1,
* display it on the console.

###### Use the abbreviated notation!


## Exercise 5 &ndash; Comparing variables

In file `task.py`, create variables `a` and `b` storing arbitrary numbers. Check if the number `a` is **greater** than `b` using the appropriate operator. Store the result of the comparison in the variable `result`.

Output this variable in the console.

Example result (for `a = 7` and `b = 13`):
```
False
```


## Exercise 6 &ndash; Age difference

In the file `task.py` create a variable named `father` and assign the value `1974` to it, Create a second variable named `child` and assign `2007` to it.

Display a message on the console (instead of ###, insert the age difference between the father and the child):
```
The father is older than the child by ### years.
```

> ###### Hint: use `fstring` or method `format`.


## Exercise 7 &ndash; Division

In the file `task.py`, create the variable `result` and assign the result of dividing 11 by 7 to it.

Display the result as:

```
11 : 7 = (place result here)
```

Round the result to 2 decimal places.

> ###### Hint: use the function `round`.


## Exercise 8 &ndash; User's age

In file `task.py`, write a program that:

* displays the message `Enter your name: ` on the screen,
* retrieves the user's name entered on the keyboard, and writes it to the variable `name`,
* displays the message `Enter your year of birth: ` on the screen,
* retrieves the user's year of birth from the keyboard and stores it in the variable `year`,
* converts the user's year of birth into a number,
* calculates the user's current age and write it to the variable `age`,
* displays a message on the console with the user's name and current age:
```
User: <name> is <age> years old
```

**NOTE:** assume that the user will enter a correct number as their birth year!
