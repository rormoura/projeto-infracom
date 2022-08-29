from socket import * # importando todas as funções da biblioteca socket
portaServidor = 12000
socketServidor = socket(AF_INET, SOCK_DGRAM) # criando o socket do servidor
# AF_INET é uma constante definida em socket e representa as famílias de endereços e protocolos
# SOCK_DGRAM é outra constante definida em socket e representa o tipo de socket que utiliza o protocolo UDP
socketServidor.bind(("", portaServidor)) # aqui vinculamos ao socket do servidor a porta do servidor
print("O servidor está pronto.")
while (True): #servidor always on
    # Como o tamanho do arquivo é maior do que o do buffer (WinError 10040), então tenho que quebrar esse arquivo em pedaços menores,
    # os quais possuem 1024 bytes. 
    # o arquivo TestePDF.pdf tem tamanho de 673080 bytes
    arquivo = open("recebido_servidor.pdf", "ab") # criando o arquivo que recebe o conteúdo enviado do cliente
    for i in range(1, 658): # 673080/1024 ~ 657,3
        contrecebido, endCliente = socketServidor.recvfrom(1024)
        arquivo.write(contrecebido) # guardando o conteúdo enviado do cliente
    contrecebido, endCliente = socketServidor.recvfrom(312) # para o último pedaço, que possui menos de 1024 bytes (673080 - 672768 = 312)
    arquivo.write(contrecebido)
    arquivo.close() # fechando o arquivo dps de guardar o conteúdo
    e1, e2 = endCliente # e1 é o endereço IP do cliente e e2 a porta pela qual ele se comunica com o servidor
    print("Endereço IP e porta do cliente:")
    print(e1,e2)
    arquivo = open("recebido_servidor.pdf", "rb") # abrindo o arquivo dnv para pegar todo o conteúdo a ser enviado pro cliente
    contrecebido = arquivo.read() # contrecebido armazena agr todo o conteúdo de arquivo
    arquivo.close() # fechando o arquivo dps de utilizá-lo
    # pelo mesmos motivos que vemos acima, tenho que enviar o arquivo em pedaços
    for i in range(0, 658): # 673080/1024 ~ 657,3
    # enquanto houver pedaços inteiros de 1024 bytes
        socketServidor.sendto(contrecebido[:1024], endCliente)
        contrecebido = contrecebido[1024:]
    socketServidor.sendto(contrecebido, endCliente) #  para o último pedaço, que possui menos de 1024 bytes