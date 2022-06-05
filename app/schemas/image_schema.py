from pydantic import BaseModel
from app.schemas.base_schema import SchemaBase

class ImageBaseSchema(SchemaBase):
    id: int
    image_path: str
    name: str
    
class ImageCreate(BaseModel):
    image_path: str
    name: str