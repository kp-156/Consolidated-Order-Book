from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Load the merged and sorted data
merged_data = pd.read_csv('merged_data_with_profit.csv')

@app.route('/api/data', methods=['GET'])
def get_data():
    # Return the merged and sorted data as JSON
    data = merged_data.to_dict(orient='records')
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
