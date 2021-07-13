import requests
import re 
import os
import sys
import time

r = requests.get('https://10minutemail.net/')
mail = re.findall(r'class="mailtext" value="(.*\@.+\.\w*)" />',r.content,re.I) 
print( "\033[1;31mYour email:\033[0m \033[3;33m"+email[0]+"\033[0m")
