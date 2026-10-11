# Sistema de Orçamentos

Projeto de estudo para praticar Python, SQL, logs e investigação de incidentes, simulando o dia a dia de uma equipe de sustentação.

## Scripts

- `gerar_log.py`: gera um arquivo `app.log` com 200 linhas de exemplo (INFO, WARNING e ERROR).

- `analisar_log.py`: lê o log e conta as ocorrências por nível, os erros por mensagem e os erros por hora.

## Análise do log

- Total de 200 linhas: 129 INFO, 35 WARNING e 26 ERROR.
- O erro mais frequente é **Falha de conexão com o banco**, com 17 dos 36 erros (quase metade).
- O horário com mais erros é **14**, com 10 ocorrências, o dobro das horas seguintes (08h e 12h, com 5).
- Hipótese: possível instabilidade ou sobrecarga no banco de dados por volta das 14h.
- Próximo passo de investigação: olhar os logs do banco nesse horário e verificar se há algum processo pesado rodando.

## O que aprendi

- Ler arquivos linha por linha e separar campos com `split`.
- Contar ocorrências com dicionários.
- Recuo (indentação) define o que fica dentro do `for` no Python.
- Ler a mensagem de erro para achar o problema (aspas, maiúsculas, nomes de parâmetros).

