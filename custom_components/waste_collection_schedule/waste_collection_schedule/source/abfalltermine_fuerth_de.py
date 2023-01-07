import requests
from waste_collection_schedule import Collection
from waste_collection_schedule.service.ICS import ICS

TITLE = "Abfalltermine Fürth"
DESCRIPTION = "Source for Stadt Fürth"
URL = "https://abfallwirtschaft.fuerth.eu/"
TEST_CASES = {
    "Flößaustraße": {"id": 88852001},
}

API_URL = "https://www.abfallwirtschaft.fuerth.eu/"

ICON_MAP = {
    "Restabfall": "mdi:trash-can",
    "Bioabfall": "mdi:leaf",
    "Gelber Sack": "mdi:recycle",
    "Altpapier": "mdi:package-variant",
}

class Source:
    def __init__(self, id):
        self._id = id
        self._ics = ICS()

    def fetch(self):
        # fetch the ical
        r = requests.get(f"{API_URL}/termine.php?icalexport={self._id}")
        r.raise_for_status()

        dates = self._ics.convert(r.text)

        entries = []

        for d in dates:
            entries.append(Collection(date=d[0], t=d[1], icon=ICON_MAP.get(d[1])))

        return entries
