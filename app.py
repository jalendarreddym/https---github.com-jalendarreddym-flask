from flask import Flask, render_template, request, jsonify
import pandas as pd
import ml_model
import chatbot

app = Flask(__name__)

# Load sample data
data = pd.read_csv('data/sample_data.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/view/<int:application_id>')
def view(application_id):
    application = data[data['application_id'] == application_id].to_dict('records')[0]
    prediction = ml_model.predict(application)
    return render_template('view.html', application=application, prediction=prediction)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['message']
    response = chatbot.get_response(user_message, data)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
