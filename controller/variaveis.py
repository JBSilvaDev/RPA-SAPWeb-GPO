from dotenv import load_dotenv
import os
import json


load_dotenv()

LOCAL_PROJETO = str(os.getenv('LOCAL_PROJETO'))
PERFIL_RPA_BROWSER = str(os.getenv('PERFIL_RPA_BROWSER'))
TEAMS_LINKS = json.loads(os.getenv('TEAMS_LINKS'))
LINK_FIREBASE = str(os.getenv('LINK_FIREBASE'))
LOCAL_DOWNLOAD = str(os.getenv('LOCAL_DOWNLOAD'))

