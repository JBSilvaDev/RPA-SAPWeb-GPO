from dotenv import load_dotenv
import os


load_dotenv()

"""
Crie as variaveis abaixo num arquivo .env na raiz do projeto, os nomes das variaveis estao explicitos, porem abairo esta a descrição de cada um deles

LOCAL_PROJETO: Link onde a pasta deste projeto esta incluindo o nome do projeto
PERFIL_RPA_BROWSER: Link do perfil Edger para manter historico e configurações ao abrir navegador (usado para manter whatsapp logado em cada execussão) acessar -> edge://version/ e obter "Caminho do perfil"
TEAMS_LINKS: Link para canal do teams onde sera enviado as informações
LINK_FIREBASE: Link do firebase onde contem os dados 
LOCAL_DOWNLOAD: Local onde os arquivos baixados sera armazenado
"""
LOCAL_PROJETO = str(os.getenv('LOCAL_PROJETO'))
PERFIL_RPA_BROWSER = str(os.getenv('PERFIL_RPA_BROWSER'))
TEAMS_LINKS = str(os.getenv('TEAMS_LINKS'))
LINK_FIREBASE = str(os.getenv('LINK_FIREBASE'))
LOCAL_DOWNLOAD = str(os.getenv('LOCAL_DOWNLOAD'))

