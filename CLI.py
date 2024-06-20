from PyInquirer import prompt, Separator
import typer
import os

class CLI():
  
  def askConfirm(self, message: str, default: bool = False) -> bool:
    results = prompt([
      {
          'type': 'confirm',
          'message': message,
          'name': 'continue',
          'default': default,
      },
    ])
    return bool(results["continue"])
  
  def askChoice(self, message: str, options: list[str]) -> str:
    key = "question"
    answers = prompt([
      {
        'type': 'list',
        'name': key,
        'message': message,
        'choices': options,
      },
    ])    
    return str(answers[key])
  
  
  def clear(self):
    os.system('cls' if os.name=='nt' else 'clear')
    