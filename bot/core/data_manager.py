import json
from threading import Lock

# fetches the data form the json file
class DataManager:
    def __init__(self, settings_file="settings/settings.json"):
        self.settings_file = settings_file
        self.lock = Lock()
        self.admin_ids = set()
        self.banned_words = set()
        self.load_data()

    def load_data(self):
        try:
            with open(self.settings_file, "r") as f:
                data = json.load(f)
                self.admin_ids = set(data.get("admin_ids", []))
                self.banned_words = set(data.get("banned_words", []))
        except FileNotFoundError:
            self.save_data()

    def save_data(self):
        with self.lock:
            with open(self.settings_file, "w") as f:
                json.dump(
                    {
                        "admin_ids": list(self.admin_ids),
                        "banned_words": list(self.banned_words),
                    },
                    f,
                    indent=4,
                )
