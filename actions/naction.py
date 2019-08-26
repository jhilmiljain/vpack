import sys	
import json	
import requests	

from st2common.runners.base_action import Action	


class MyVAction(Action):	
         def run(self,id,title,description,page_count,excerpt,publish_date)	
               try:	
                     x={"ID":id,"Title":title,"Description":description,	
                        "PageCount":page_count,"excerpt":excerpt,	
                        "PublishDate":publish_date}	
                     y1=json.dumps(x)	
                     header_data={'content-type':'application/json'}	
                     url='https://fakerestapi.azurewebsites.net/api/Books'	
                     response=requests.post(url,headers=header_data,x=y1)	
                     print(response)	
                     y2=response.json()	
                     print(y2)	

               except: requests.exceptions.MissingSchema:	
                      print("wrong URL")	
                      sys.exit(0)	

