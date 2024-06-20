import os

class FileSystem():

  @staticmethod
  def createDirIfNotExists(path: str):
    if not os.path.exists(path):
      os.mkdir( path )