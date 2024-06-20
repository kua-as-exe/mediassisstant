import typer
from rich import print as rprint
import os
from typing import Optional
from PyInquirer import prompt, Separator


import typer
from typing_extensions import Annotated


from CLI import CLI
from app.usecases.ItemUseCases import *

app = typer.Typer()

dataPath = "./.data"

FileSystem.createDirIfNotExists(dataPath)

cli = CLI()

classUseCases = ItemUseCases(
  itemService= ItemService(
    itemRepository= ItemRepository(
      rootPath= dataPath
    )
  )
)

def handleTranscribeAsset(item: ItemModel, asset: AssetModel):

  if not cli.askConfirm(f" Transcribe file \"{asset.basename}\""):
    return
  
  choice = cli.askChoice("Select Whisper model", [
    "base", "normal", "large"
  ])
  print(choice)
  cli.askConfirm("Start speeck recognition now?")



def selectAsset( item: ItemModel, asset: AssetModel ):

  cli.clear()
  rprint(f" [green bold]{item.name}[/green bold] - [red]{asset.basename}[/red]")

  answers = prompt([
    {
        'type': 'expand',
        'message': 'Actions:',
        'name': 'action',
        'choices': [
              {
                  'key': 't',
                  'name': 'Transcribe',
                  'value': 'transcribe'
              },
              Separator(),
              {
                  'key': 'q',
                  'name': 'Abort',
                  'value': 'abort'
              }
          ]
      }
  ])

  if answers['action'] == "transcribe":
    handleTranscribeAsset( item, asset )
    
  cli.confirm("")

def selectItem( item: ItemModel ):

  while True:
    item = classUseCases.getById( item.id )
    
    nameLabel = f"[green bold]{item.name}[/green bold]"

    assets = item.getAssets()
  
    cli.clear() 
    rprint(f" {nameLabel}")
    for index, asset in enumerate(assets):
      rprint(f"  - [{index+1}] {asset.basename}")
    rprint("")

    indexInput = typer.prompt(f"[{item.name}]")

    if indexInput == "q":
      break
    
    try:
      index = int(indexInput)
      if index < 1 or index > len(assets):
        continue
    except Exception as e:
      print("Select a numeric index")
      print(e)
      cli.askConfirm("Ok?")

    asset = assets[index - 1]
    try:
      selectAsset(item, asset)      
    except Exception as e:
      print("Error")
      print(e)
      cli.askConfirm("Ok?")
  

@app.command("create")
def create():
  name = typer.prompt("Session name")
  rprint(f"name: [blue bold]{name}[blue bold]")
  confirm = cli.askConfirm("Create new class?")

  slug = str(name).replace(" ", "-")

  if not confirm:
    print("Not deleting")
    raise typer.Abort()

  classUseCases.registerClass(
    dto= ItemNewClassDto(
      name = name,
      slug = slug
    )
  )

@app.command("start")
def main():

  while True:
    items = classUseCases.getAll()

    cli.clear()
    rprint("")
    rprint(f"Items: ")
    for index, item in enumerate(items):
      indexLabel = f"[[blue]{index + 1}[/blue]]"
      nameLabel = f"[green bold]{item.name}[/green bold]"
      assetsLabel = f" Assets: {item.getAssetCount()}"
      rprint(f"  - {indexLabel} {nameLabel} - {assetsLabel}")

    rprint("")
    indexInput = typer.prompt("item")

    if indexInput == "q":
      break
    
    try:
      index = int(indexInput)
      if index < 1 or index > len(items):
        continue

      item = items[index -1 ]
      selectItem(item)
    except Exception as e:
      print("Select a numeric index")
      print(e)

    
if __name__ == "__main__":
    app()    