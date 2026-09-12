from sqlalchemy.orm import Session

from models import Product
from schemas import ProductCreate, ProductUpdate


def get_products(
    db: Session,
    skip: int = 0,
    limit: int = 10
):
    return (
        db.query(Product)
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_product(
    db: Session,
    product_id: int
):
    return (
        db.query(Product)
        .filter(Product.product_id == product_id)
        .first()
    )


def create_product(
    db: Session,
    product: ProductCreate
):
    db_product = Product(
        name=product.name,
        category=product.category,
        description=product.description,
        product_image=(
            str(product.product_image)
            if product.product_image
            else None
        ),
        sku=product.sku,
        unit_of_measure=product.unit_of_measure,
        lead_time=product.lead_time
    )

    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product


def update_product(
    db: Session,
    db_product: Product,
    product: ProductUpdate
):
    db_product.name = product.name
    db_product.category = product.category
    db_product.description = product.description

    db_product.product_image = (
        str(product.product_image)
        if product.product_image
        else None
    )

    db_product.sku = product.sku
    db_product.unit_of_measure = product.unit_of_measure
    db_product.lead_time = product.lead_time

    db.commit()
    db.refresh(db_product)

    return db_product