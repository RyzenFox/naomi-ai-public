"""
Demo conceitual simplificada do fluxo da Naomi AI.

Este arquivo NÃO contém a implementação real da Naomi.
Serve apenas para demonstrar a ideia geral do fluxo.
"""

def ouvir_usuario():
    return "Naomi, exemplo de comando"

def processar_comando(texto):
    if "Naomi" in texto:
        return "Comando recebido e processado de forma conceitual."
    return "Wake word não detectada."

def responder(texto):
    print(f"Naomi: {texto}")

if __name__ == "__main__":
    entrada = ouvir_usuario()
    resposta = processar_comando(entrada)
    responder(resposta)
