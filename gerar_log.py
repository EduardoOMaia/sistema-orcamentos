import random
from datetime import datetime, timedelta

niveis = ["INFO"] * 6 + ["WARNING"] * 2 + ["ERROR"] * 2
msgs = {
    "INFO": ["Login realizado", "Orçamento criado", "Orçamento consultado"],
    "WARNING": ["Resposta lenta do banco", "Senha incorreta"],
    "ERROR": ["Falha de conexão com o banco", "Erro ao calcular total", "Token expirado"]
}
inicio = datetime(2026, 10, 9, 8, 0)

with open("app.log", "w", encoding="utf-8") as f:
    for i in range(200):
        momento = inicio + timedelta(minutes=i * 3)
        nivel = random.choice(niveis)
    f.write(f"{momento:%Y-%m-%d %H:%M:%S} {nivel} {random.choice(msgs[nivel])}\n")