# vector-field-generator
To run:
cd into the directory and run:
```
python vector_field.py
```
A simple python program to generate a vector field in tkinter
Functions are inputted in a strange way. For example, to add x and 1, you do (+(x)_(1)). Operator -> term 1 in parentheses -> underscore -> term 2 in parentheses. 
As a general rule of thumb more parentheses are always better. Functions currently included are basic operations (+, -, *, /) and basic trig (sin, cos, tan). No exponentiation at the moment.
Trig works pretty similarly to normal, only exception is that like others you have to surround everything in parentheses. To compute sine of x you would do (sin(x)).
The two valid variables are x and y. Its a vector field generator.
Example of a more complex function: Taking the negative sine of the sum of x and tangent y: (*(-1)_(sin(+(x)_(tan(y)))))
