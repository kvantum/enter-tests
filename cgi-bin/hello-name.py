#!/usr/bin/env python3

import cgi
import html

form = cgi.FieldStorage()
text1 = form.getfirst("User_name","noname")
text1 = html.escape(text1)

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Greeting</title>
            <style>
                h1, h2, h3, h4, h5 {text-align:center;}
                p {text-align:center;}
            </style>
        </head>
        <body>""")

print("<h2>Hello, {}!<h2>".format(text1))
print("""<br><a href="../index.html">Go to main page</a>
        </body>
        </html>""")
