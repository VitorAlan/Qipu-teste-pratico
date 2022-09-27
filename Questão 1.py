from num2words import num2words

while(True):
    try:
        print("Para encerrar o programa, escreva 'fim'")
        entrada = str(input("Digite o número desejado com um máximo de 9 dígitos e até 2 casas decimais"+
                               " (qualquer valor com mais casas decimais será arredondado para duas casas decimais)\nEX:R$9999,15\nR$"))
        if(entrada == 'fim'):
            print("Finalizando!")
            break
        entrada_numerica = round(float(entrada.replace(",",".")),2)
        if(entrada_numerica>=1000000000):
            raise "erro"
        real = entrada_numerica//1
        centavo = int(str(entrada).split(",")[1])
        reais_ptbr = num2words(real, lang='pt-br')
        centavos_ptbr = num2words(centavo, lang='pt-br')
        string_real = " real"
        string_centavo = " centavo"
        conector = " e "
        saida = ""
        if(real > 0):
            if(real > 1):
                string_real = " reais"
            saida += reais_ptbr+string_real
        if(real>0 and centavo>0):
            saida += " e "
        if(centavo>0):
            if(centavo > 0.01):
                string_centavos = " centavos"
            saida += centavos_ptbr + string_centavos
        print(saida+"\n\n")
    except:
        print("\nValor informado inválido, por favor informe o valor novamente!\n O valor deve estar no formato R$XX,XX\n")
