from flask import Flask, render_template, request, redirect # , render template with return
from datetime import datetime, timezone
##################3
# SQLAlchemy != SQLALchemy#
from flask_sqlalchemy import SQLAlchemy # for the classes of database and func for time

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db" #"sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # BASICALLY ITS FOR SIGNAL EMMITING / and even if it is not written it just sets implicity

db = SQLAlchemy(app)
##################3

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200), nullable = False) # should not null
    desc = db.Column(db.String(500), nullable = False)
    date_created = db.Column(db.DateTime, default = lambda: datetime.now(timezone.utc)) # lambda: is new here
                                                               # datetime.utcnow    nowdepricated ?
    def __repr__(self) -> str: #print karnekeliye
         return f"{self.sno} - {self.title}"

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        if title: # Basic validation
            todo = Todo(title=title, desc=desc)
            db.session.add(todo)
            db.session.commit()
        return redirect('/')

    allTodo = Todo.query.all()
    return render_template('index.html', allTodo=allTodo)


@app.route("/update/<int:sno>", methods=['GET', 'POST'])
def update(sno):
    todo = db.session.get(Todo, sno)
    if not todo:
        return redirect('/')

    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        if title: # Basic validation
            todo.title = title
            todo.desc = desc
            db.session.commit()
        return redirect('/')

    return render_template('update.html', todo=todo)


@app.route("/delete/<int:sno>")
def delete(sno):
    todo = db.session.get(Todo, sno)
    if todo:
        db.session.delete(todo)
        db.session.commit()
    return redirect('/')


@app.route("/about")
def about():
    return render_template('about.html')

# @app.route("/show")
# def show():
#     allTodo = Todo.query.all()
#     result = []
#     for todo in allTodo:
#         result.append({
#             'sno': todo.sno,
#             'title': todo.title,
#             'desc': todo.desc,
#             'date_created': todo.date_created.strftime('%Y-%m-%d %H:%M:%S')
#         })
#     return result  # Flask automatically converts to JSON

@app.cli.command("init-db")
def init_db_command():
    """Clears the existing data and creates new tables."""
    db.create_all()
    print("Initialized the database.")

if __name__ == "__main__":
    # The app.run() call is not needed here if you use `flask run`
    # The `if __name__` block is kept for users who might still run `python app.py`
    # However, the recommended way is to use the Flask CLI.
    app.run(debug=True) #in times of devlopment it should True