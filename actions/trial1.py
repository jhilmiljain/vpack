import sys
import requests
import json

from st2common.runners.base_action import Action

class MyAction(Action):
      
      def run(self,id):
            try:
                  id1=str(id)
                  url='https://fakerestapi.azurewebsites.net/api/books/'+id1
                  headers={'content-type':'application/json'}
                  response=requests.get(url,headers=headers)
                  y2=response.json()
                  print(y2)
            except:
                  sys.exit(0)
             
                  
                  
                  
                  
          
