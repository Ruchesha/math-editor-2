from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/math-editor', methods=['GET', 'POST'])
def math_editor():
    result = None
    operation = None

    if request.method == 'POST':
        try:
            value1 = float(request.form['value1'])
            value2 = float(request.form['value2'])
            operation = request.form['operation']
            
            if operation == 'add':
                result = value1 + value2
            elif operation == 'subtract':
                result = value1 - value2
            elif operation == 'multiply':
                result = value1 * value2
            elif operation == 'divide':
                result = value1 / value2 if value2 != 0 else 'Error (division by zero)'
        except ValueError:
            result = 'Invalid input'

    return render_template('math_editor.html', result=result, operation=operation)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
