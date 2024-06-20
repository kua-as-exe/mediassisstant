from src.models.ClassModel import ClassModel
from rich import print as rprint

from src.data.repositories.ClassRepository import *

class ClassService( ):

  def __init__(self, classRepository: ClassRepository) -> None:
    self.classRepository = classRepository
    pass

  def save(self, classModel: ClassModel):
    return self.classRepository.save(classModel)

  def getAll(self):
    return self.classRepository.getAll()

