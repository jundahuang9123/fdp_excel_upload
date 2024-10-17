from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        df = pd.read_excel(file)
        # Run your Python script here
        result = process_data(df)
        return jsonify({'result': result})

def process_data(df):
    # Example processing function
    return df.describe().to_json()

if __name__ == '__main__':
    app.run(debug=True)
