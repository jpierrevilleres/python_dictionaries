# python_dictionaries
Demonstration of Dictionaries in Python

Requirements:

* Write a function called `has_duplicates` that takes a string parameter and returns True if the string has any
repeated characters. Otherwise, it should return False.
Implement `has_duplicates` by creating a histogram using the below histogram function. Implementation should
use the counts in the histogram to decide if there are any duplicates.

```
def histogram(s):
d = dict()
for c in s:
if c not in d:
d[c] = 1
else:
d[c] += 1
return d
```

* Write a loop over the strings in the provided `test_dups` list. Print each string in the list and whether or not it has
any duplicates based on the return value of has_duplicates for that string. 
* Write a function called `missing_letters` that takes a string parameter and returns a new string with all the
letters of the alphabet that are not in the argument string. The letters in the returned string should be in
alphabetical order.
* It should also use the global variable alphabet. It should use this global variable directly, not through an argument or a local copy. It should loop over the letters in alphabet to determine which are missing from the input parameter.
The function `missing_letters` should combine the list of missing letters into a string and return that string.
* Write a loop over the strings in list test_miss and call missing_letters with each string. Print a line for each
string listing the missing letters.
* If the string has all the letters in alphabet, the output should say it uses all the letters.
