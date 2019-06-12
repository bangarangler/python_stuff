# Regular Expressions

---

Note to self: Jon, ppl are not weird like you. comment this if you use it in a group project *high five ... carry on*

## Special Characters

\ : Escape a Character

. : Match anything except line break

\d : digit 0-9

\w : letter, digit, or underscore

\s : whitespace character

\D : not a digit

\W : not a word character

\S : not a whitespace character

() : signifies a group

## Quantifiers

+ : One or more

{3} : Exactly x times. ex. 3 times

{3,5} : Three to five times

{4,} : Four or more times

* : Zero or more times

? : Once or none (optional)

## Logical OR

| (pipe) : Example "Mr|Mrs|Ms" will match any of them. (252) or 252 —> \(\d{3}\)|\d{3}

## Quick Tips

\d\d : double digit

^x\w+ : anything that starts with letter (where letter is x)... ex. a\w+ matches ally allergy angry 

\w{5} : match any 5 letters in a row... ex. matches frank molly lover

[aeiou] : match vowels

[a-z] : any lowercase letter

[A-Z] : any uppercase letter

[0-9] : any digit

[a-z0-9] : any lowercase letter any digits

[^k] : anything that is not the letter k

(\(\d{3}\)|\d{3}) \d{3} \d{4} : matches phone numbers like 222 222 2222 or like (222) 222 2222

## Anchors and Boundaries

^ : start of string or line

$ : end of string or line

\b : word boundary

# Use Cases

- Credit Card number validation
- Phone number validation
- find / replace in text
- Formatting text / output
- Syntax highlighting

## Validating Emails

Starts with 1 or more letter, number, +, _ , - , . then

A single @ sign then

1 or more letter, number, or - then

A single dot then

ends with 1 or more letter, number, - , or .

(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)