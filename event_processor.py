import subprocess
import json
from collections import Counter

class EventProcessor:
    def __init__(self, consumer_command, max_events=10):
        self.process = subprocess.Popen(consumer_command, stdout=subprocess.PIPE)
        self.event_type_counts = Counter()
        self.word_appearances = Counter()
        self.max_events = max_events
        self.events_processed = 0

    def process_output(self, output):
        try:
            event_type, data = [x.split(': ')[1] for x in output.strip().split(', ')]
            self.event_type_counts[event_type] += 1

            words = data.split()
            self.word_appearances.update(words)

            self.events_processed += 1
        except Exception as e:
            print("Error processing event:", e)

    def count_events_by_type(self):
        while self.events_processed < self.max_events:
            output = self.process.stdout.readline().decode()
            if output == '' and self.process.poll() is not None:
                break
            if output.strip():
                self.process_output(output)

        # Output event type counts in JSON format
        return json.dumps(dict(self.event_type_counts), indent=2)

    def count_words_appearances(self):
        while self.events_processed < self.max_events:
            output = self.process.stdout.readline().decode()
            if output == '' and self.process.poll() is not None:
                break
            if output.strip():
                self.process_output(output)

        # Output word appearances in JSON format
        return json.dumps(dict(self.word_appearances), indent=2)





