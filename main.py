from flask import Flask

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "Simple Calculator App! Try /add/2/3"

# Addition
@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    return f"Result: {a + b}"

# Subtraction
@app.route('/sub/<int:a>/<int:b>')
def sub(a, b):
    return f"Result: {a - b}"

# Multiplication
@app.route('/mul/<int:a>/<int:b>')
def mul(a, b):
    return f"Result: {a * b}"

# Division
@app.route('/div/<int:a>/<int:b>')
def div(a, b):
    if b == 0:
        return "Error: Division by zero"
    return f"Result: {a / b}"

if __name__ == '__main__':
    app.run(debug=True)
