#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:words>')
def print_string(words):
    print(words)
    return f'<h1>{words}</h1>'

@app.route('/count/<int:value>')
def count(value):
    numbers = range(1, value + 1)

    html = ''.join(f'<h1>{x}</h1>' for x in numbers)
    return html

    # for x in numbers:
    #     return f'<h2>{x}</h2>'
    
@app.route('/math/<int:num1><operation><int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Invalid operation'
    return f'<h1>{num1} {operation} {num2} = {result}</h1>'



if __name__ == '__main__':
    app.run(port=5555, debug=True)
