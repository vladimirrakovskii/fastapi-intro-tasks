from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional


app = FastAPI()

# Временная база данных
product_list = []
product_id_counter = 1

# BEGIN (write your solution here)
class ProductSpecifications(BaseModel):
    size: str = Field(...)
    color: str = Field(...)
    material: str = Field(...)

class Product(BaseModel):
    name: str = Field(...)
    price: float = Field(..., gt=0)
    specifications: ProductSpecifications

class ProductResponse(BaseModel):
    id: int
    name: str
    price: float

class ProductDetailResponse(BaseModel):
    id: int
    name: str
    price: float
    specifications: ProductSpecifications

@app.post("/product")
async def create_product(product: Product):
    global product_id_counter, product_list
    product_data = product.model_dump()
    product_data['id'] = product_id_counter
    product_list.append(product_data)
    product_id_counter += 1
    return product_data

@app.get("/products", response_model=List[ProductResponse])
async def get_products():
    products_response = []
    for product in product_list:
        product_response = ProductResponse(id=product['id'], name=product['name'], price=product['price'])
        products_response.append(product_response)
    return products_response

@app.get("/product/{product_id}", response_model=ProductDetailResponse)
async def get_product(product_id: int):
    for product in product_list:
        if product['id'] == product_id:
            return ProductDetailResponse(**product)
    raise HTTPException(status_code=404, detail="Product not found")
# END
