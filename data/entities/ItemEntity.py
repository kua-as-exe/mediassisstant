import jsons
from dataclasses import dataclass
from data.repositories.ItemRepository import ItemModel

@dataclass
class ItemEntity():
  id: str
  slug: str
  name: str
  
  def toJSON(self):
    return jsons.dumps(self)
  
  @staticmethod
  def fromJson(data: any):
    return ItemEntity(
      id= data['id'],
      slug= data['slug'],
      name= data['name'],
    )

  def toModel(self):
    model = ItemModel(
      id= self.id,
      slug= self.slug,
      name= self.name,
    )
    return model

  @staticmethod
  def fromModel(model: ItemModel):
    return ItemEntity(
      id= model.id,
      slug= model.name,
      name= model.name
    )