from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Sample data to return
data = [
    {"id": 1, "name": "Alice", "age": 30},
    {"id": 2, "name": "Bob", "age": 25},
    {"id": 3, "name": "Charlie", "age": 35}
]

@app.route('/')
def index():
    # Serve the HTML file directly
    print("hello")
    return render_template('index.html')

@app.route('/testAPI')
def testAPI():
    # Serve the HTML file directly
    return render_template('testAPI.html')

@app.route('/Clients/client1_conversation_interface')
def client():
    return render_template("/Clients/client1_conversation_interface.html")

@app.route('/Clients/api/data', methods=['GET'])
def get_data():
    # Return data as JSON
    return jsonify(data)

@app.route('/Clients/client1_financial_roadmap')
def getfinancialR():
    return render_template("/Clients/client1_financial_roadmap.html")

@app.route('/Clients/client1_portfolio_overview')
def getPortOverview():
    return render_template("/Clients/client1_portfolio_overview.html")


if __name__ == '__main__':
    app.run(debug=True, port=5500)
