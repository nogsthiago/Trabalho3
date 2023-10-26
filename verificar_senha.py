import hashlib
import sys

def encriptar_senha(senha):
    # Função para criptografar a senha
    s = b'salt_string_here'
    senha = senha.encode('utf-8')
    senha_hash = hashlib.pbkdf2_hmac('sha256', senha, s, 100000)
    return senha_hash

def checar_senha(senha_criptografada, usuario_senha):
    # Função para verificar se a senha fornecida pelo usuário coincide com a senha criptografada
    usuario_senha_hash = encriptar_senha(usuario_senha)
    return usuario_senha_hash == senha_criptografada

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python verificar_senha.py <senha_fornecida> <arquivo_senha>")
        sys.exit(1)

    with open(sys.argv[2], "rb") as f:
        senha_criptografada = f.read()
    
    usuario_senha = sys.argv[1]

    if checar_senha(senha_criptografada, usuario_senha):
        print("Senha correta.")
        sys.exit(0)
    else:
        print("Senha incorreta.")
        sys.exit(1)
