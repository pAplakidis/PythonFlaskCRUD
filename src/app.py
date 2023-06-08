#!/usr/bin/env python3
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Person(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  content = db.Column(db.String(200), nullable=False)
  date_added = db.Column(db.DateTime, default=datetime.utcnow)

  def __repr__(self):
    return '<Person %r>' % self.id


@app.route("/", methods=['POST', 'GET'])
def index():
  if request.method == 'POST':
    person_content = None
    search_content = None
    if 'content' in request.form:
      person_content = request.form['content']
    elif 'search' in request.form:
      search_content = request.form['search']

    if person_content:
      new_person = Person(content=person_content)

      try:
        db.session.add(new_person)
        db.session.commit()
        return redirect('/')
      except:
        return "Error adding person!"
    elif search_content:
      people = []
      for person in Person.query.all():
        if search_content in person.content:
          people.append(person)
      return render_template('index.html', people=people)
    else:
      people = Person.query.order_by(Person.date_added).all()
      return render_template('index.html', people=people)
  else:
    people = Person.query.order_by(Person.date_added).all()
    return render_template('index.html', people=people)

@app.route("/delete/<int:id>")
def delete(id):
  person_to_delete = Person.query.get_or_404(id)

  try:
    db.session.delete(person_to_delete)
    db.session.commit()
    return redirect('/')
  except:
    return "Error deleting person!"

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
  person = Person.query.get_or_404(id)

  if request.method == "POST":
    person.content = request.form['content']

    try:
      db.session.commit()
      return redirect("/")
    except:
      return "Error updating person!"
  else:
    return render_template("update.html", person=person)


if __name__ == '__main__':
  app.run(debug=True)
