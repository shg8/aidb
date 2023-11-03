import time

import pandas as pd


def command_line_utility(engine):
  welcome = '''
      _    ___ ____  ____  
     / \  |_ _|  _ \| __ ) 
    / _ \  | || | | |  _ \ 
   / ___ \ | || |_| | |_) |
  /_/   \_\___|____/|____/ 
                           
  '''
  print(welcome)
  print("Query AIDB using SQL....\n")
  while True:
    query = input(">>>")
    if query.strip() == "exit":
      return
    else:
      while query.strip()[-1] != ';':
        q = input("")
        query += f" {q.strip()}"
      print("Running...")
      start_time = time.time()
      results = engine.execute(query)
      end_time = time.time()
      print(f"Query Execution Time = {int((end_time - start_time)*100)/100} seconds")
      print("Query Result")
      print(pd.DataFrame(results))