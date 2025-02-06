import json
import os

class MeetingScheduler:
    def __init__(self, data_dir="../data"):
        self.data_dir = data_dir
        os.makedirs(self.data_dir, exist_ok=True)

    def schedule(self, date_time, location, topic, talking_points):
        meeting_details = {
            "date_time": date_time,
            "location": location,
            "topic": topic,
            "talking_points": talking_points
        }
        with open(os.path.join(self.data_dir, "meetings.json"), "w", encoding='utf-8') as file:
            json.dump(meeting_details, file, indent=4)
        return meeting_details
