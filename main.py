from flask import Flask, render_template

app = Flask(__name__)


items = [
    {'image': 'https://i.ibb.co/9tJdPbB/flag-ua.png', 'name': 'Ukraine', 'age': 2, 'breed': 'Oleg',
     'origin': 'Moscow', 'id': 1},
    # Додайте більше об'єктів за необхідності...
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

