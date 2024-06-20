from domain.models.AssetModel import AssetModel
from .AudioModel import AudioModel
from dataclasses import dataclass

@dataclass
class ItemModel:
  id: str
  name: str
  slug: str
  __assets: list[AssetModel] = None

  def __str__(self) -> str:
    return f"ClassModel(id={self.id}, audioPath={self.audio.path})"

  def getAssets(self) -> list[AssetModel]:
    if self.__assets is None:
      return []
    return  self.__assets  
  
  def getAssetCount(self) -> int:
    return len(self.getAssets())
  
  def addAsset(self, asset: AssetModel):
    if self.__assets is None:
      self.__assets = []

    self.__assets.append(asset) 
    return asset
  