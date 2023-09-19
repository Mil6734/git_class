from flask import Flask, render_template, url_for

app = Flask(__name__)

info = [
    {'name': 'Главная', 'url': 'index41'},
    {'name': 'Персонал', 'url': 'staff'}
]


@app.route('/index41')
@app.route('/')
def index():
    print(url_for('index'))
    return render_template('index41.html', title='Главная страница', info=info)


@app.route('/staff')
def staff():
    print(url_for('staff'))
    return render_template('staff.html', title='Персонал', info=info)


if __name__ == '__main__':
    app.run(debug=True)
