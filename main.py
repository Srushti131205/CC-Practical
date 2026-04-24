from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML UI inside Python (simple way)
html_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Calculator</title>
</head>
<body>
    <h2>Simple Calculator</h2>
    
    <form method="post">
        <input type="number" name="num1" placeholder="Enter first number" required>
        <input type="number" name="num2" placeholder="Enter second number" required>
        
        <br><br>
        
        <button name="operation" value="add">Add</button>
        <button name="operation" value="sub">Subtract</button>
        <button name="operation" value="mul">Multiply</button>
        <button name="operation" value="div">Divide</button>
    </form>
    
    <h3>{{ result }}</h3>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = ""

    if request.method == 'POST':
        a = float(request.form['num1'])
        b = float(request.form['num2'])
        op = request.form['operation']

        if op == 'add':
            result = a + b
        elif op == 'sub':
            result = a - b
        elif op == 'mul':
            result = a * b
        elif op == 'div':
            if b == 0:
                result = "Error: Division by zero"
            else:
                result = a / b

    return render_template_string(html_page, result=result)

if __name__ == '__main__':
    app.run(debug=True)
