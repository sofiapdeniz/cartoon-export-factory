from abc import ABC, abstractmethod

class ExportInterface(ABC):

    @abstractmethod
    def export(self, data):
        pass
