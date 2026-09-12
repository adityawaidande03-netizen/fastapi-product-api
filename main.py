from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from database import engine, Base, get_db
import models
import crud
import schemas


# Create database tables
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Product Management API",
    description="APIs for managing products",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Product Management API is running"
    }


# 1. LIST PRODUCTS


@app.get("/product/list")
def list_products(
    page: int = Query(
        default=1,
        ge=1,
        description="Page number"
    ),
    db: Session = Depends(get_db)
):
    records_per_page = 10

    skip = (page - 1) * records_per_page

    products = crud.get_products(
        db,
        skip=skip,
        limit=records_per_page
    )

    return {
        "page": page,
        "records_per_page": records_per_page,
        "products": products
    }


# 2. PRODUCT INFORMATION


@app.get("/product/{pid}/info")
def product_info(
    pid: int,
    db: Session = Depends(get_db)
):
    product = crud.get_product(
        db,
        product_id=pid
    )

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product



# 3. ADD PRODUCT


@app.post("/product/add")
def add_product(
    product: schemas.ProductCreate,
    db: Session = Depends(get_db)
):
    # Check whether SKU already exists
    existing_product = (
        db.query(models.Product)
        .filter(models.Product.sku == product.sku)
        .first()
    )

    if existing_product:
        raise HTTPException(
            status_code=400,
            detail="SKU already exists"
        )

    new_product = crud.create_product(
        db,
        product
    )

    return {
        "message": "Product added successfully",
        "product": new_product
    }


# 4. UPDATE PRODUCT


@app.put("/product/{pid}/update")
def update_product(
    pid: int,
    product: schemas.ProductUpdate,
    db: Session = Depends(get_db)
):
    db_product = crud.get_product(
        db,
        product_id=pid
    )

    if db_product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    # Check whether another product already uses this SKU
    existing_product = (
        db.query(models.Product)
        .filter(
            models.Product.sku == product.sku,
            models.Product.product_id != pid
        )
        .first()
    )

    if existing_product:
        raise HTTPException(
            status_code=400,
            detail="SKU already exists"
        )

    updated_product = crud.update_product(
        db,
        db_product,
        product
    )

    return {
        "message": "Product updated successfully",
        "product": updated_product
    }