from verificar_senha import checar_senha

def teste_checar_senha():
    senha_encriptada = b'\x08k2}\xba\xc3\x99\xc3G\x03\xe1\xd4e\x85\x1d\xa3\xab\x9b6W~\x0a\x87\x7f\x8cVb\xa0\x1b\x06\xbb\xce\x0e'
    assert checar_senha(senha_encriptada, "senha_correta") == True
    assert checar_senha(senha_encriptada, "senha_incorreta") == False
