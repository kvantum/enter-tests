#!/usr/bin/env python3

import cgi
import html
import cgitb

cgitb.enable()

form = cgi.FieldStorage()
number1 = form.getfirst("number1")
number2 = form.getfirst("number2")
operation = form.getvalue("operation") #get value from the radiobutton

def add(operand1, operand2):
    """ Adds two numbers """
    return operand1 + operand2

def subtract(operand1, operand2):
    """ Subtraction of the given numbers """
    return operand1 - operand2

def mult(operand1, operand2):
    """ Returns the product of two operands """
    return operand1 * operand2

def divide(operand1, operand2):
    """ Returns the result of division operand1 by operand2 """
    try:
        return operand1 / operand2
    except ZeroDivisionError:
        print("<h3>You cannot divide by zero! </h3> <p><a href='../calculator.html'>Try again, please.</a></p>")

operator = {
    "add": add,
    "sub": subtract,
    "mul": mult,
    "div": divide
}

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Simple calculator</title>
            <style>
                h1, h2, h3, h4, h5 {text-align:center;}
                p {text-align:center;}
            </style>
        </head>
        <body>""")

print("<br>")

try:
    print('<p>The result is: {0}</p>'.format(operator[operation](float(number1), float(number2))))
except ZeroDivisionError:
    print("<h4>You cannot divide by zero! </h4><a href='../calculator.html'>Try again, please.</a>")
except:
    print("<p>Enter two numbers, please. <a href='../calculator.html'>Try again</a></p>")

print("""<br><a href="../index.html">Go to main page</a>
        </body>
        </html>""")
