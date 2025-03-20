from flask import Flask, render_template
from models import Person

app = Flask(__name__)

# Sample data
people = [
    Person("Alice", 300000),
    Person("Bob", 250000),
    Person("Charlie", 10000)
]

@app.route('/')
def index():
    return render_template("index.html", people=people)

if __name__ == '__main__':
    app.run(debug=True)
