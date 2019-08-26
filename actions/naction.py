import sys
import requests
import json

from st2common.runners.base_action import Action

class MyAction(Action):
        def run(self,id,title,description,page_count,excerpt,publish_date):
                try:
              		x={"ID": id,"Title": title,"Description": description,"PageCount": page_count,"Excerpt": excerpt,"PublishDate": publish_date}
                	y1=json.dumps(x)
			header_data={'content-type': 'application/json'}
			url='https://fakerestapi.azurewebsites.net/api/Books'
			response=requests.post(url,headers=header_data,data=y1)
			print(response)
			y2=response.json()
			print(y2)
			

	        except:
                    	sys.exit(0)

