from flask import Flask, render_template
from sampleData import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("/HTML/Clients/client1_portfolio_overview.html", people=people)

if __name__ == '__main__':
    app.run(debug=True)
