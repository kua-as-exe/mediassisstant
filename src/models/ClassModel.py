from .AudioModel import AudioModel
from dataclasses import dataclass

@dataclass
class ClassModel:
  id: str
  name: str
  slug: str
  audio: AudioModel = None

  def __str__(self) -> str:
    return f"ClassModel(id={self.id}, audioPath={self.audio.path})"
  
  def setAudio(self, path: str ):
    self.audio = AudioModel(
      path=path
    )
  
  def hasAudio(self):
    return self.audio != None