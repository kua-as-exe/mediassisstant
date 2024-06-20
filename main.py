import typer
from rich import print as rprint
import os

from src.app.usecases.ClassUseCases import *

app = typer.Typer()

dataPath = "./.data"

if not os.path.exists(dataPath):
  os.mkdir(dataPath)

classUseCases = ClassUseCases(
  classService= ClassService(
    classRepository= ClassRepository(
      rootPath= dataPath
    )
  )
)

@app.command("hi")
def sample_func():
    rprint("[red bold]Hi[/red bold] [yellow]World[yello]")

@app.command("create")
def create():
  name = typer.prompt("Session name")
  rprint(f"name: [blue bold]{name}[blue bold]")
  confirm = typer.confirm("Create new class?")

  slug = str(name).replace(" ", "-")

  if not confirm:
    print("Not deleting")
    raise typer.Abort()

  classUseCases.registerClass(
    dto= CreateNewClassDto(
      name = name,
      slug = slug
    )
  )

@app.command("ls")
def getAll():
  classes = classUseCases.getAll()
  rprint(f"Classes: ")
  for index, classModel in enumerate(classes):

    indexLabel = f"[[blue]{index + 1}[/blue]]"
    nameLabel = f"{classModel.name}"
    audioLabel = f"[green][AUDIO][/green]" if classModel.hasAudio() else "[red][NO AUDIO][/red]"
    
    rprint(f"  - {indexLabel} {nameLabel} {audioLabel}")

    
if __name__ == "__main__":
    app()    