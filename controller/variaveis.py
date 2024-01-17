from dotenv import load_dotenv
import os


load_dotenv()

LOCAL_PROJETO = str(os.getenv('LOCAL_PROJETO'))
PERFIL_RPA_BROWSER = str(os.getenv('PERFIL_RPA_BROWSER'))

print(PERFIL_RPA_BROWSER)
