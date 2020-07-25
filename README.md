# Bot da toca da coruja
Bot do telegram criado para auxiliar o Grupo de leitura do entocados.

## Biblioteca utilizada
- [telepot](https://telepot.readthedocs.io/en/latest/)

## Uso
Para utilizar o bot e realizar modificações basta dar um fork nesse repositório e alterar o token e as mensagens de resposta no arquivo common.py.
Após as modificação basta utilizar o comando :
```
python coruja.py
```
## Funcionamento
O bot detecta a entrada e saída de novos membros no grupo do Telegram e envia uma mensagem de boas vindas ou uma mensagem dizendo que está triste com a saída do membro.
Além disso, a coruja responde a dois comandos :
- /livrodomes
- /cronograma

Ao ser chamada pelos comandos acima, a coruja envia uma imagem com a capa do livro e/ou o cronograma de leitura do mês.