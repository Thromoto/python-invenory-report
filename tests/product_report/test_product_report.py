from inventory_report.product import Product


def test_product_report() -> None:
    produto = Product(
        "1",
        "curso",
        "trybe",
        "13/07/2023",
        "14/07/2023",
        "123456",
        "xxxxxx",
    )

    assert str(produto) == (
            f"The product {produto.id} - {produto.product_name} "
            f"with serial number {produto.serial_number} "
            f"manufactured on {produto.manufacturing_date} "
            f"by the company {produto.company_name} "
            f"valid until {produto.expiration_date} "
            "must be stored according to the following instructions: "
            f"{produto.storage_instructions}."
    )
