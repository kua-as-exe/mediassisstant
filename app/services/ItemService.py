from rich import print as rprint

from data.repositories.ItemRepository import *

class ItemService( ):

  def __init__(self, itemRepository: ItemRepository) -> None:
    self.classRepository = itemRepository
    pass

  def save(self, itemModel: ItemModel):
    return self.classRepository.save(itemModel)

  def getAll(self):
    return self.classRepository.getAll()

  def getById(self, id: str):
    return self.classRepository.getByid(id)

  def getAssetsPathById(self, id: str):
    return self.classRepository.getAssetsPathById(id)

