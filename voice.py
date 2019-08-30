import time
import requests
from robodk import* 
from robolink import*
RDK = Robolink()
glist=[]
while 1:	
	r = requests.get("http://192.168.20.143:5001")
	r = r.text
	print(r)