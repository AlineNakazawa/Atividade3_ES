def anagrama(string1, string2):
    """
    Verifica se duas strings são anagramas, ignorando espaços e maiúsculas/minúsculas.
    """

    string1_limpa = string1.replace(" ", "").lower()
    string2_limpa = string2.replace(" ", "").lower()

    if len(string1_limpa) != len(string2_limpa):
        return False
        
    return sorted(string1_limpa) == sorted(string2_limpa)

def cifra_cesar(texto, deslocamento):
    # TODO
    pass

def valida_cpf(cpf):
    # TODO
    pass