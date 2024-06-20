from models.ItemModel import ItemModel
from data.entities.ItemEntity import ItemEntity
import os, json, glob
from os.path import join

class ItemRepository():
  repositorySlug = "classes"
  __dataFileName = "data.json"
  __audioFileName = "audio.mp3"

  def __init__(self, rootPath: str) -> None:
    self.rootPath = rootPath
    self.path = join(rootPath, self.repositorySlug)

    if not os.path.exists(self.path):
      os.mkdir(self.path)

    pass

  def __getClassPath(self, model: ItemModel):
    return join(self.path, model.id)

  def __createPathIfNotExists(self, model: ItemModel):
    classPath = self.__getClassPath(model)
    if not os.path.exists(classPath):
      os.mkdir( classPath )

  def __getDataFilePath(self, model: ItemModel):
    classPath = self.__getClassPath(model)
    return join(classPath, self.__dataFileName)
  
  def __getAudioFilePath(self, model: ItemModel):
    classPath = self.__getClassPath(model)
    return join(classPath, self.__audioFileName)
    
  
  def save(self, model: ItemModel):
    self.__createPathIfNotExists(model)

    dataPath = self.__getDataFilePath(model)
    entity = ItemEntity.fromModel(model)

    with open(dataPath, "w") as dataFile:
      dataFile.write(entity.toJSON()) 
    
    pass

  def getAll(self) -> list[ItemModel]:
    globQuery = join(self.path, "*", self.__dataFileName)
    result = glob.glob(  globQuery )

    models: list[ItemModel] = []
    for file in result:
      try:
        with open(file, "r") as file:
          jsonData = json.load(file)
          entity = ItemEntity.fromJson(jsonData)
          model = entity.toModel()

          audioPath = self.__getAudioFilePath(model)
          if os.path.exists(audioPath):
            model.setAudio(audioPath)
          
          models.append(model)
      except Exception as e:
        print(e)
        pass
    
    return models

  def getByid(self, id: str) -> ItemModel:
    pass

  def getBySlug(self, slug: str) -> ItemModel:
    pass

  def delete(self, theClass: ItemModel):
    pass