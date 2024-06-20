from data.utils.FileSystem import FileSystem
from domain.models.AssetModel import AssetModel
from domain.models.ItemModel import ItemModel
from data.entities.ItemEntity import ItemEntity
import os, json, glob
from os.path import join

class ItemRepository():
  repositorySlug = "items"
  __dataFileName = "data.json"
  __assetsDirName = "assets"

  def __init__(self, rootPath: str) -> None:
    self.rootPath = rootPath
    self.path = join(rootPath, self.repositorySlug)

    if not os.path.exists(self.path):
      os.mkdir(self.path)

    pass

  def __getClassPath(self, model: ItemModel):
    return join(self.path, model.id)

  def __createPathIfNotExists(self, model: ItemModel):
    dirs = [self.__getClassPath(model), self.__getAssetsPath(model)]
    for dir in dirs:
      FileSystem.createDirIfNotExists(dir )

  def __getDataFilePath(self, model: ItemModel):
    classPath = self.__getClassPath(model)
    return join(classPath, self.__dataFileName)
  
  def __getAssetsPath(self, model: ItemModel):
    classPath = self.__getClassPath(model)
    return join(classPath, self.__assetsDirName)

  def getAssets(self, model: ItemModel):
    assetsPath = self.__getAssetsPath(model)
    result = os.listdir(assetsPath)

    assets: list[AssetModel] = []
    for file in result:
      try:
        asset = AssetModel(
          basename= file,
          type= "" 
        ) 

        assets.append(asset)
      except:
        pass
        
    return assets
    
    
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

          assets = self.getAssets(model)
          for asset in assets:
            model.addAsset(asset)

          models.append(model)

      except Exception as e:
        print(e)
        pass
    
    return models

  def getByid(self, id: str) -> ItemModel:
    items = self.getAll()

    for item in items:
      if item.id == id:
        return item
    raise RuntimeError("Hola")

  def getBySlug(self, slug: str) -> ItemModel:
    pass

  def delete(self, theClass: ItemModel):
    pass