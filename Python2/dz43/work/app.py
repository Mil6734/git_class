from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task.db'
db = SQLAlchemy(app)


class Shop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    content = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"<Task {self.id}>"


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Shop(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            return f"Не удалось добавить вашу задачу. {e}"

    else:
        tasks = Shop.query.order_by(Shop.content).all()
        return render_template('index.html', tasks=tasks)


@app.route('/content', methods=['POST', 'GET'])
def content():
    if request.method == 'POST':
        title = request.form['title']
        price = request.form['price']
        content = request.form['content']
        try:
            new_item = Shop(title=title, price=price, content=content)
            db.session.add(new_item)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            return f"Не удалось добавить товар. {e}"
    return render_template('content.html')


@app.route('/information')
def information():
    return render_template('information.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
