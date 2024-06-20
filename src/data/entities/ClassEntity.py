import jsons
from dataclasses import dataclass
from src.data.repositories.ClassRepository import ClassModel

@dataclass
class ClassEntity():
  id: str
  slug: str
  name: str
  
  def toJSON(self):
    return jsons.dumps(self)
  
  @staticmethod
  def fromJson(data: any):
    return ClassEntity(
      id= data['id'],
      slug= data['slug'],
      name= data['name'],
    )

  def toModel(self):
    model = ClassModel(
      id= self.id,
      slug= self.slug,
      name= self.name,
    )
    return model

  @staticmethod
  def fromModel(model: ClassModel):
    return ClassEntity(
      id= model.id,
      slug= model.name,
      name= model.name
    )