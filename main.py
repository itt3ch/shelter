from flask import Flask, render_template

app = Flask(__name__)


items = [
    {'name': 'Item 1', 'price': 10},
    {'name': 'Item 2', 'price': 20},
    {'name': 'Item 3', 'price': 15},
    # Add more items as needed...
]


@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/catalog')
def catalog():
    return render_template('catalog.html', items=items)


if __name__ == '__main__':
    app.run(debug=True)

