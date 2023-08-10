__version__ = '0.1.5'
backup_file_path = "backup.json"
import os
import json
from replit import db,clear


def create_backup(data_base):
    backup_data = dict(data_base)

    with open(backup_file_path, "w") as file:
        json.dump(backup_data, file, indent=2)


def create_backup_owner():
  backup_data = {}
  for i in db.keys():
    try:
      if db[i]['1'] == 'b05c26e7-1571-4fc8-8b2a-53be1b0918ad':
        backup_data[i] = db[i]['info']

      else:
        pass
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
       if os.environ['REPL_ID'] == 'b05c26e7-1571-4fc8-8b2a-53be1b0918ad':
         pass
       else:
        return 'Unauthorized'
  else:
    backup_data = dict(data_base)

    with open(backup_file_path, "w") as file:
        json.dump(backup_data, file)

def save_to_database_owner(prompt,info,database):
  if os.environ['REPL_OWNER'] != 'Idkwhttph':
    if os.environ['REPL_ID'] == 'b05c26e7-1571-4fc8-8b2a-53be1b0918ad':
         pass
    else:
      return 'Unauthorized'

  for i in range(1):
    try:
      print(db[prompt])
      clear()
      database[prompt][f'{i}'] = 'b05c26e7-1571-4fc8-8b2a-53be1b0918ad'
    except:
      database[prompt] = {'info':f'{info}'}


def sync_backup_owner(data_base):
  if os.environ['REPL_OWNER'] != 'Idkwhttph':
       if os.environ['REPL_ID'] == 'b05c26e7-1571-4fc8-8b2a-53be1b0918ad':
         pass
       else:
        return 'Unauthorized'
  else:
    #Formatt
    with open(backup_file_path, "r") as file:
        backup_data = json.load(file)

    data_base.update(backup_data)

    create_backup(data_base)
def checking_db(database):
  for i in database.keys():
    try:
      if database[i]['1']!= 'b05c26e7-1571-4fc8-8b2a-53be1b0918ad':
        del database[i]
      else:
        pass
    except:
      #If the key doesn't exist, delete IMMEDIATELY!
      
      del database[i]