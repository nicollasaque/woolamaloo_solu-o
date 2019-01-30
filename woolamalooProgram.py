#! /usr/bn/python
from __future__ import print_function

arqSys = open('employees_system.txt', 'r')	#abrindo o arquivo de dados dos funcionarios
arqWeb = open('web_auth_data.txt', 'r')			#abrindo o c

sys = arqSys.readlines()		#fazendo um vetor com as linhas dos arquivos
web = arqWeb.readlines()						

del sys[0]									#deletando a linha de cabecalho dos arquivos
del web[0]

i = 0
for line in sys :						#dividindo as informacoes de cada linha em um vetor (fazendo um vetor de vetores) para o primeiro arquivo
		x = line.split(',')			#a divisao e feita a partir das virgulas das linhas
		sys[i] = x
		i += 1

j = 0
for line2 in web :					#agora para o segundo arquivo		
		y = line2.split(',')
		web[j] = y
		j += 1 

print ('Woolamaloo Synchronization Report\n---------------------------------\n')		#cabecalho do relatorio
print ('ID   Name                Status\n---- ------------------- ------------------------------------------------------------\n')

l = 0
while l < len(sys):			#o arquivo do sistema vai ser percorrido linha por linha (ID por ID)

	if sys[l][3] != '':		#se o campo de data de demissao conter alguma data, ela vai ser impressa e o proximo individuo vai ser analisado
		print('{:<25}'.format('{0} {1} '.format(sys[l][0], sys[l][1])), end='')
		print('Worked with the Woolamaloo from {0} until {1}.'.format(sys[l][2], sys[l][3]))	
	
	else:												#se o individuo nao foi demitido, seu ID vai ser comparado com os IDs do arquivo da web
		for k in web:							#a variavel 'k' vai conter o vetor do ID que esta sendo comparado
			local = web.index(k)		#a variavel 'local' vai conter o valor do indice do ID que esta sendo comparado do arquivo da web
			if k[1] == sys[l][0]:		#se encontrar o ID no arquivo da web:

				if k[4] != sys[l][4]: 	#vao ser comparados os campos 'position' e 'department', se estiverem incoerentes vao para o relatorio
					print('{:<25}'.format('{0} {1} '.format(sys[l][0], sys[l][1])), end='')
					print('Changed department, was {0}, now it is {1}.'.format(k[4], sys[l][4]))
	 
				if k[5] != sys[l][5]:
					print('{:<25}'.format('{0} {1} '.format(sys[l][0], sys[l][1])), end='')
					print('Changed position, was {0}, now it is {1}.'.format(k[5].rstrip(), sys[l][5].rstrip()))
				break

			else:										#se nao ser encontrado o ID no arquivo da web entao o funcionario e novo e deve-se ir para o relatorio		
				if local == len(web)-1:
					print('{:<25}'.format('{0} {1} '.format(sys[l][0], sys[l][1])), end='')
					print('New employee of Woolamaloo since {0}.'.format(sys[l][2]))
	l = l+1	

arqSys.close()					#fechando os arquivos
arqWeb.close()
