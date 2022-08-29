# Parte 1 - Projeto Infracom - CIn UFPE

## Grupo: 

- Jeferson Severino de Araujo (jsa2)

- Marcus Vinicius de Faria Santos (mvfs)

- Rodrigo Rocha Moura (rrm2)

- Victor Gabriel de Carvalho (vg3).

 ---

## Descrição da parte 1:

### Para cada uma das leituras, do arquivo TesteTXT.txt e do arquivo TestePDF.pdf, temos dois códigos em Python, um para o cliente e outro para o servidor.

- ### Descrição do cliente: No código do cliente: criamos um socket que utiliza o protocolo UDP -> abrimos o arquivo correspondente e salvamos seu conteúdo -> enviamos esse conteúdo pro servidor -> (imprimimos o conteúdo no caso do txt) -> recebemos do servidor o que ele enviou -> imprimimos o IP e a porta do servidor -> (imprimimos o conteúdo no caso do txt) -> salvamos em um novo arquivo o conteúdo recebido.

- ### Descrição do servidor: No código do servidor: criamos um socket que utiliza o protocolo UDP -> recebemos o conteúdo do cliente -> imprimimos o IP e a porta do cliente -> (imprimimos o que recebemos no caso do txt) -> salvamos o conteúdo recebido em um novo arquivo -> enviamos o conteúdo que recebemos de volta pro cliente.

---