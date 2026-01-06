from services.cartoon import Cartoon
from factory.export_factory import export_factory
from common.enum.export_format import ExportFormat

cartoons = [
    Cartoon('hora de aventura', 'humor', 2010),
    Cartoon('apenas um show', 'humor', 2010)
]

print("=== JSON ===")
exporter_json = export_factory(ExportFormat.JSON)
print(exporter_json.export(cartoons))

print("\n=== XML ===")
exporter_xml = export_factory(ExportFormat.XML)
print(exporter_xml.export(cartoons))
