from pydantic import BaseModel, Field, HttpUrl, ConfigDict
from typing import Optional, Literal


Category = Literal[
    "finished",
    "semi-finished",
    "raw"
]

UnitOfMeasure = Literal[
    "mtr",
    "mm",
    "ltr",
    "ml",
    "cm",
    "mg",
    "gm",
    "unit",
    "pack"
]


class ProductCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)

    category: Category

    description: Optional[str] = Field(
        default=None,
        max_length=250
    )

    product_image: Optional[HttpUrl] = None

    sku: str = Field(..., min_length=1, max_length=100)

    unit_of_measure: UnitOfMeasure

    lead_time: int = Field(..., ge=0, le=999)


class ProductUpdate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)

    category: Category

    description: Optional[str] = Field(
        default=None,
        max_length=250
    )

    product_image: Optional[HttpUrl] = None

    sku: str = Field(..., min_length=1, max_length=100)

    unit_of_measure: UnitOfMeasure

    lead_time: int = Field(..., ge=0, le=999)


class ProductResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    product_id: int
    name: str
    category: str
    description: Optional[str]
    product_image: Optional[str]
    sku: str
    unit_of_measure: str
    lead_time: int
    created_date: Optional[str]
    updated_date: Optional[str]