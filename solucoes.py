def anagrama(string1, string2):
    # TODO
    pass

def cifra_de_cesar(texto, deslocamento):
    """
    Aplica a Cifra de César ao texto, preservando minúsculas/maiúsculas e caracteres não-letras.
    """
    resultado = ""
    deslocamento = deslocamento % 26 

    for char in texto:
        if 'a' <= char <= 'z':
            inicio_alfabeto = ord('a')
            posicao_original = ord(char) - inicio_alfabeto
            nova_posicao = (posicao_original + deslocamento) % 26
            novo_char = chr(inicio_alfabeto + nova_posicao)
            resultado += novo_char
            
        elif 'A' <= char <= 'Z':
            inicio_alfabeto = ord('A')
            posicao_original = ord(char) - inicio_alfabeto
            nova_posicao = (posicao_original + deslocamento) % 26
            novo_char = chr(inicio_alfabeto + nova_posicao)
            resultado += novo_char
            
        else:
            resultado += char
            
    return resultado

def valida_cpf(cpf):
    # TODO
    pass