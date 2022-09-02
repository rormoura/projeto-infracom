from socket import * # importando todas as funções da biblioteca socket
nomeServidor = "localhost"
portaServidor = 12000
socketCliente = socket(AF_INET, SOCK_DGRAM) # criando o socket do cliente
# AF_INET é uma constante definida em socket e representa as famílias de endereços e protocolos
# SOCK_DGRAM é outra constante definida em socket e representa o tipo de socket que utiliza o protocolo UDP
arquivo = open("TesteTXT.txt", "rt") # abrindo o arquivo
conteudo = arquivo.read() # salvando o conteúdo do arquivo
arquivo.close() # fechando o arquivo

socketCliente.sendto(conteudo.encode(),(nomeServidor, portaServidor)) #  através do socket UDP, o cliente manda pro servidor
                                                                    #  uma string transformada em bytes. O servidor é identificado
                                                                    #  pelo IP (adquirido pelo nome) e pela porta.
contrecebido, endServidor = socketCliente.recvfrom(34)  # recebemos o conteúdo enviado pelo servidor
                                                        # o arquivo TesteTXT.txt tem tamanho de 34 bytes
e1, e2 = endServidor # e1 é o endereço IP do servidor e e2 a porta pela qual ele se comunica com o cliente
print("Endereço IP e porta do servidor:")
print(e1,e2)
print("Arquivo recebido do servidor: "+contrecebido.decode()) # printamos o conteúdo recebido em formato de string
arquivo = open("recebido_cliente.txt", "wt") # criando o arquivo que recebe o conteúdo enviado do servidor
arquivo.write(contrecebido.decode()) # guardando o conteúdo enviado do servidor
arquivo.close() # fechando o arquivo dps de guardar o conteúdo
socketCliente.close() # fechamos o socket do cliente