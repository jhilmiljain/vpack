import sys
import requests
import json

from st2common.runners.base_action import Action

class MyAction(Action):
      
      def run(self,id):
            try:
                  x={"ID"=id}
                  y1=json.dumps(x)
                  url='https://fakerestapi.azurewebsites.net/api/books/1'
                  headers={'content-type':'application/json'}
                  response=requests.post(url,headers=headers,data=y1)
                  print(response)
                  y2=response.json()
                  print(y2)
            except:
                  sys.exit(0)
             
                  
                  
                  
                  
          
