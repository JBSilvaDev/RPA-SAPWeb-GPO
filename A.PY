from dotenv import load_dotenv
import os
import json



load_dotenv()

a = str(os.getenv('LOCAL_DOWNLOAD'))
print(a)