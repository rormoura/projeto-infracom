from socket import * # importando todas as funções da biblioteca socket
nomeServidor = "localhost" # --------------------------------------------------------------> MUDAR PARA HOSTNAME DPS
portaServidor = 12000
socketCliente = socket(AF_INET, SOCK_DGRAM) # criando o socket do cliente
# AF_INET é uma constante definida em socket e representa as famílias de endereços e protocolos
# SOCK_DGRAM é outra constante definida em socket e representa o tipo de socket que utiliza o protocolo UDP
arquivo = open("TestePDF.pdf", "rb") # abrindo o arquivo
conteudo = arquivo.read() # salvando o conteúdo do arquivo
arquivo.close() # fechando o arquivo
# Como o tamanho do arquivo é maior do que o do buffer (WinError 10040), então tenho que quebrar esse arquivo em pedaços menores,
# os quais possuem 1024 bytes. 
# o arquivo TestePDF.pdf tem tamanho de 673080 bytes
for i in range(1, 658): # 673080/1024 ~ 657,3
    # enquanto houver pedaços inteiros de 1024 bytes
    socketCliente.sendto(conteudo[:1024],(nomeServidor, portaServidor))
    conteudo = conteudo[1024:]
socketCliente.sendto(conteudo,(nomeServidor, portaServidor)) #  para o último pedaço, que possui menos de 1024 bytes
                                                             #  através do socket UDP, o cliente manda pro servidor
                                                             #  vários bytes. O servidor é identificado
                                                             #  pelo IP (adquirido pelo nome) e pela porta.
arquivo = open("recebido_cliente.pdf", "ab") # criando o arquivo que recebe o conteúdo enviado do servidor
# pelo mesmos motivos que vemos acima, tenho que receber o arquivo em pedaços
for i in range(1, 658): # 673080/1024 ~ 657,3
    contrecebido, endServidor = socketCliente.recvfrom(1024)
    arquivo.write(contrecebido) # guardando o conteúdo enviado do servidor
contrecebido, endServidor = socketCliente.recvfrom(312)
arquivo.write(contrecebido) # para o último pedaço, que possui menos de 1024 bytes (673080 - 672768 = 312)
arquivo.close() # fechando o arquivo dps de guardar o conteúdo
e1, e2 = endServidor # e1 é o endereço IP do servidor e e2 a porta pela qual ele se comunica com o cliente
print("Endereço IP e porta do servidor:")
print(e1,e2)
socketCliente.close() # fechamos o socket do cliente