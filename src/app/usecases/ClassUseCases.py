import uuid
from rich import print as rprint
from os.path import join
from dataclasses import dataclass

from src.app.services.ClassService import *

@dataclass
class CreateNewClassDto():
   name: str
   slug: str

class ClassUseCases():

   def __init__(self, classService: ClassService) -> None:
      self.classService = classService
      pass

   def registerClass(self, dto: CreateNewClassDto ):
      rprint(f"Creating [blue]{dto.name}[blue]")

      newClass = ClassModel(
         id= str(uuid.uuid4()),
         name=dto.name,
         slug=dto.slug,
      )

      self.classService.save(newClass)
      rprint(f"[green]Class Saved {newClass.id}[blue]")
   
   def getAll(self):
      return self.classService.getAll() 
