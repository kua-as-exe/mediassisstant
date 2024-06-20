import uuid
from rich import print as rprint
from os.path import join
from dataclasses import dataclass

from app.services.ItemService import *

@dataclass
class ItemNewClassDto():
   name: str
   slug: str

class ItemUseCases():

   def __init__(self, itemService: ItemService) -> None:
      self.itemService = itemService
      pass

   def registerClass(self, dto: ItemNewClassDto ):
      rprint(f"Creating [blue]{dto.name}[blue]")

      newClass = ItemModel(
         id= str(uuid.uuid4()),
         name=dto.name,
         slug=dto.slug,
      )

      self.itemService.save(newClass)
      rprint(f"[green]Class Saved {newClass.id}[blue]")
   
   def getAll(self):
      return self.itemService.getAll() 
   
   def getById(self, id: str):
      return self.itemService.getById(id)
