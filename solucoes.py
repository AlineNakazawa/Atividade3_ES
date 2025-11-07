def anagrama(string1, string2):
    """
    Verifica se duas strings são anagramas, ignorando espaços e maiúsculas/minúsculas.
    """

    string1_limpa = string1.replace(" ", "").lower()
    string2_limpa = string2.replace(" ", "").lower()

    if len(string1_limpa) != len(string2_limpa):
        return False
        
    return sorted(string1_limpa) == sorted(string2_limpa)

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

# Casos de teste - Anagramas
print(f'("amor", "roma"): {anagrama("amor", "roma")}')  # Esperado: True
print(f'("A gentleman", "Elegant man"): {anagrama("A gentleman", "Elegant man")}') # Esperado: True
print(f'("gato", "cabra"): {anagrama("gato", "cabra")}') # Esperado: False

# Casos de teste - Cifra de César
print(f'("abc", 2): {cifra_de_cesar("abc", 2)}')  # Esperado: "cde"
print(f'("xyz", 3): {cifra_de_cesar("xyz", 3)}')  # Esperado: "abc"
print(f'("Ataque ao Amanhecer!", 5): {cifra_de_cesar("Ataque ao Amanhecer!", 5)}') # Esperado: "Fyfvzj ft Frfsmjhmjw!"