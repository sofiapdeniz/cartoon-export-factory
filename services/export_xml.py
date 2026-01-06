import xml.etree.ElementTree as et
from interface.export_interface import ExportInterface

class ExportXML(ExportInterface):
    def export(self, data):
        root = et.Element("cartoons")

        for d in data:
            cartoon = et.SubElement(root, "cartoon")

            et.SubElement(cartoon, "name").text = d.name
            et.SubElement(cartoon, "gender").text = d.gender
            et.SubElement(cartoon, "year").text = str(d.year)

        return et.tostring(root, encoding='unicode')
