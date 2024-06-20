from src.models.ClassModel import ClassModel
from src.data.entities.ClassEntity import ClassEntity
import os, json, glob
from os.path import join

class ClassRepository():
  repositorySlug = "classes"
  __dataFileName = "data.json"
  __audioFileName = "audio.mp3"

  def __init__(self, rootPath: str) -> None:
    self.rootPath = rootPath
    self.path = join(rootPath, self.repositorySlug)

    if not os.path.exists(self.path):
      os.mkdir(self.path)

    pass

  def __getClassPath(self, model: ClassModel):
    return join(self.path, model.id)

  def __createPathIfNotExists(self, model: ClassModel):
    classPath = self.__getClassPath(model)
    if not os.path.exists(classPath):
      os.mkdir( classPath )

  def __getDataFilePath(self, model: ClassModel):
    classPath = self.__getClassPath(model)
    return join(classPath, self.__dataFileName)
  
  def __getAudioFilePath(self, model: ClassModel):
    classPath = self.__getClassPath(model)
    return join(classPath, self.__audioFileName)
    
  
  def save(self, model: ClassModel):
    self.__createPathIfNotExists(model)

    dataPath = self.__getDataFilePath(model)
    entity = ClassEntity.fromModel(model)

    with open(dataPath, "w") as dataFile:
      dataFile.write(entity.toJSON()) 
    
    pass

  def getAll(self) -> list[ClassModel]:
    globQuery = join(self.path, "*", self.__dataFileName)
    result = glob.glob(  globQuery )

    models: list[ClassModel] = []
    for file in result:
      try:
        with open(file, "r") as file:
          jsonData = json.load(file)
          entity = ClassEntity.fromJson(jsonData)
          model = entity.toModel()

          audioPath = self.__getAudioFilePath(model)
          if os.path.exists(audioPath):
            model.setAudio(audioPath)
          
          models.append(model)
      except Exception as e:
        print(e)
        pass
    
    return models

  def getByid(self, id: str) -> ClassModel:
    pass

  def getBySlug(self, slug: str) -> ClassModel:
    pass

  def delete(self, theClass: ClassModel):
    pass