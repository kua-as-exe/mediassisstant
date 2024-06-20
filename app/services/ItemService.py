from rich import print as rprint

from data.repositories.ItemRepository import *

class ItemService( ):

  def __init__(self, classRepository: ItemRepository) -> None:
    self.classRepository = classRepository
    pass

  def save(self, classModel: ItemModel):
    return self.classRepository.save(classModel)

  def getAll(self):
    return self.classRepository.getAll()

