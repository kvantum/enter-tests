#!/usr/bin/env python3

import cgi
import html

form = cgi.FieldStorage()
text_form = form.getfirst("ticket_number","none")
ticket_number = html.escape(text_form)

def lucky(num):
    """ Checks if the ticket is lucky.
    The ticket is lucky if the sum of the first three digits equals the last \
    three digits.
    """
    digits = [] #digits list
    st = str(num)
    try:
        for i in range(len(st)):
            digits.append(int(st[i]))
    except:
        print("<p>An error occurs! It's not an integer number!</p>")
    if len(digits) != 6:
        print("<p>Hey, you should enter a 6-digit number!</p>")
    elif (sum(digits[0:3]) == sum(digits[3:6])):
        print('<p>The number of your ticket is {}.</p>'.format(st))
        print('<h4>Congratulations! Your ticket is lucky.</h4>')
    else:
        print('<h4>Sorry, the ticket number {} is not lucky.</h4>'.format(st))

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Lucky ticket</title>
            <style>
                h1, h2, h3, h4, h5 {text-align:center;}
                p {text-align:center;}
            </style>
        </head>
        <body>""")

print("<br>")

lucky(ticket_number)

print("""<br><a href="../index.html">Go to main page</a>
        </body>
        </html>""")
