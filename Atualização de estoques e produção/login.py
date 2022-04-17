from pathlib import Path

localLogin = Path('./LoginSAP/Login.txt').absolute()

arquivoLogin = open(localLogin, 'r')

localSenha = Path('./LoginSAP/Senha.txt').absolute()

arquivoSenha = open(localSenha, 'r')

loginSAP = arquivoLogin.read()
senhaSAP = arquivoSenha.read()

print("Login e senha SAP, encontrados!")

