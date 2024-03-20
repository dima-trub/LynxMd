import sys
from flask import Flask, jsonify
from event_processor import EventProcessor  # Assuming the EventProcessor class is in event_processor.py

app = Flask(__name__)

consumer_command = ['python', 'consumer.py']  # Update to use the consumer script
event_processor = EventProcessor(consumer_command)

@app.route('/events/countByEventType', methods=['GET'])
def event_stats():
    event_counts = event_processor.count_events_by_type()
    return jsonify(event_counts)

@app.route('/events/countWords', methods=['GET'])
def word_appearances():
    word_counts = event_processor.count_words_appearances()
    return jsonify(word_counts)

if __name__ == '__main__':
    app.run(debug=True)
