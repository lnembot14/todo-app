from flask import Flask, render_template,request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable = True)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return f"<Task: {self.id}>"



@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = todo(content = task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return "There was an issue adding your test"

    else:
        tasks = todo.query.order_by(todo.date_created).all()
        return render_template('index.html', tasks = tasks)
    
@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = todo.query.get_or_404(id) #Attempt to get id, if ID can't be retrieved return 404

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return "Error"
    
@app.route('/update/<int:id>', methods = ['GET', 'POST'])
def update(id):
    task = todo.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']
        
        try:
            db.session.commit()
            return redirect('/')
        except:
            return "Error"
    else:
        return render_template('update.html', task = task)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)