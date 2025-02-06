from flask import Flask, request, jsonify
from digital_twin import DigitalTwin

app = Flask(__name__)
dt = DigitalTwin("worker123")

@app.route('/query', methods=['GET'])
def query_api():
    keyword = request.args.get('keyword')
    if not keyword:
        return jsonify({"error": "Keyword is required"}), 400
    results = dt.query_corpus(keyword)
    return jsonify(results)

@app.route('/schedule', methods=['POST'])
def schedule_meeting():
    data = request.get_json()
    date_time = data.get("date_time")
    location = data.get("location")
    topic = data.get("topic")
    if not all([date_time, location, topic]):
        return jsonify({"error": "Missing required fields"}), 400
    meeting = dt.schedule_meeting(date_time, location, topic)
    return jsonify(meeting)

if __name__ == '__main__':
    app.run(debug=True)
