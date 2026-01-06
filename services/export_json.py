import json
from interface.export_interface import ExportInterface

class ExportJSON(ExportInterface):
    def export(self, data):
        return json.dumps(
            [
                {
                    "name": d.name,
                    "gender": d.gender,
                    "year": d.year
                }
                for d in data
            ],
            indent=3,
            ensure_ascii=False
        )
