from typing import Dict, Type
from abc import ABC, abstractmethod
import json

from inventory_report.product import Product


class Importer(ABC):
    def __init__(self, path: str) -> None:
        self.path = path

    @abstractmethod
    def import_data(self) -> list[Product]:
        pass


class JsonImporter(Importer):
    def import_data(self) -> list[Product]:
        products = []

        with open(self.path) as file:
            data = json.load(file)

        for item in data:
            products.append(
                Product(
                    item["id"],
                    item["product_name"],
                    item["company_name"],
                    item["manufacturing_date"],
                    item["expiration_date"],
                    item["serial_number"],
                    item["storage_instructions"],
                )
            )

        return products


class CsvImporter:
    pass


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
