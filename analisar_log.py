contagem = {}
erros_por_mensagem = {}
erros_por_hora = {}

with open("app.log", encoding="utf-8") as f:
    for linha in f:
        partes = linha.strip().split(" ", 3)
        nivel = partes[2]
        contagem[nivel] = contagem.get(nivel, 0) + 1
        if nivel == "ERROR":
            mensagem = partes[3]
            erros_por_mensagem[mensagem] = erros_por_mensagem.get(mensagem, 0) + 1
            hora = partes[1][:2]
            erros_por_hora[hora] = erros_por_hora.get(hora, 0) + 1
print(contagem)
print(erros_por_mensagem)
print(erros_por_hora)
print("Erro mais frequente:", max(erros_por_mensagem, key=erros_por_mensagem.get))
print("Hora com mais erros:", max(erros_por_hora, key=erros_por_hora.get))