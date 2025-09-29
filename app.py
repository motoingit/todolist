from flask import Flask, render_template, request, redirect
from datetime import datetime
import pytz
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_

app = Flask(__name__)

# Configure instance path
app.config['INSTANCE_PATH'] = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'instance')
os.makedirs(app.config['INSTANCE_PATH'], exist_ok=True)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.config['INSTANCE_PATH'], 'todo.db')
app.config['SQLALCHEMY_BINDS'] = {
    'log': 'sqlite:///' + os.path.join(app.config['INSTANCE_PATH'], 'log.db')
}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

IST = pytz.timezone('Asia/Kolkata')

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=lambda: datetime.now(IST))

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

class Log(db.Model):
    __bind_key__ = 'log'
    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.String(50), nullable=False)
    message = db.Column(db.String(500), nullable=False)
    timestamp = db.Column(db.DateTime, default=lambda: datetime.now(IST))

    def __repr__(self):
        return f"[{self.timestamp}] [{self.level}] {self.message}"

def log_message(level, message):
    log = Log(level=level, message=message)
    db.session.add(log)
    db.session.commit()

@app.cli.command("init-db")
def init_db_command():
    """Initialize the database."""
    try:
        db.create_all()
        print("Initialized the database.")
    except Exception as e:
        print(f"Error initializing database: {e}")

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        if title: # Basic validation
            todo = Todo(title=title, desc=desc)
            db.session.add(todo)
            db.session.commit()
            log_message('INFO', f'Added new todo with title: {title}')
        return redirect('/')

    search_query = request.args.get('search')
    if search_query:
        log_message('INFO', f'Searched for: {search_query}')
        allTodo = Todo.query.filter(or_(Todo.title.contains(search_query), Todo.desc.contains(search_query))).all()
    else:
        allTodo = Todo.query.all()
    return render_template('index.html', allTodo=allTodo)

@app.route("/update/<int:sno>", methods=['GET', 'POST'])
def update(sno):
    todo = db.session.get(Todo, sno)
    if not todo:
        log_message('WARNING', f'Attempted to update non-existent todo with sno: {sno}')
        return redirect('/')

    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        if title: # Basic validation
            todo.title = title
            todo.desc = desc
            db.session.commit()
            log_message('INFO', f'Updated todo with sno: {sno}')
        return redirect('/')

    return render_template('update.html', todo=todo)

@app.route("/delete/<int:sno>")
def delete(sno):
    todo = db.session.get(Todo, sno)
    if todo:
        db.session.delete(todo)
        db.session.commit()
        log_message('INFO', f'Deleted todo with sno: {sno}')
    else:
        log_message('WARNING', f'Attempted to delete non-existent todo with sno: {sno}')
    return redirect('/')

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)