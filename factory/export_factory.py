from services.export_json import ExportJSON
from services.export_xml import ExportXML
from common.enum.export_format import ExportFormat

def export_factory(format: ExportFormat):
    export_types = {
        ExportFormat.JSON: ExportJSON,
        ExportFormat.XML: ExportXML
    }

    try:
        return export_types[format]()
    except KeyError:
        raise ValueError("invalid export format.")
