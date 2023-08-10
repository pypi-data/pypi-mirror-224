__version__ = '0.1.0'
backup_file_path = "backup.json"
import os
import json
from replit import db,clear


def create_backup(data_base):
    backup_data = dict(data_base)

    with open(backup_file_path, "w") as file:
        json.dump(backup_data, file, indent=2)


def create_backup_owner():
    if os.environ['REPL_OWNER'] != 'Idkwhttph':
       return 'Unauthorized'
    else:
      backup_data = {}
      for i in db.keys():
        try:
          print(db[i]['CHECKER7'])
          clear()
          backup_data[i] = db[i]['info']
        except:
          pass
        
    
        with open(backup_file_path, "w") as file:
            json.dump(backup_data, file, indent=2)





def load_backup_owner(data_base):
  if os.environ['REPL_OWNER'] != 'Idkwhttph':
       return 'Unauthorized'
  else:
    if os.path.exists(backup_file_path):
        with open(backup_file_path, "r") as file:
            backup_data = json.load(file)
            data_base.update(backup_data)







def save_backup_owner(data_base):
  if os.environ['REPL_OWNER'] != 'Idkwhttph':
       if os.environ['REPL_ID'] == '7ff791fa-3a09-49ae-a710-44e3b7ea42d9':
         pass
       else:
        return 'Unauthorized'
  else:
    backup_data = dict(data_base)

    with open(backup_file_path, "w") as file:
        json.dump(backup_data, file)

def save_to_database_owner(prompt,info):
  if os.environ['REPL_OWNER'] != 'Idkwhttph':
    if os.environ['REPL_ID'] == '7ff791fa-3a09-49ae-a710-44e3b7ea42d9':
         pass
    else:
      return 'Unauthorized'

  for i in range(12):
    try:
      print(db[prompt])
      clear()
      db[prompt][f'CHECKER{i}'] = '7ff791fa-3a09-49ae-a710-44e3b7ea42d9'
    except:
      db[prompt] = {'info':f'{info}'}


def sync_backup_owner(data_base):
  if os.environ['REPL_OWNER'] != 'Idkwhttph':
       if os.environ['REPL_ID'] == '7ff791fa-3a09-49ae-a710-44e3b7ea42d9':
         pass
       else:
        return 'Unauthorized'
  else:
    #Formatt
    with open(backup_file_path, "r") as file:
        backup_data = json.load(file)

    data_base.update(backup_data)

    create_backup(data_base)
