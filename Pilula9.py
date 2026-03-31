def calcular_media (prod, qual, pont):
    return (prod + qual + pont) / 3

def classificar(media):
    if media >= 8:
        return 'Excelente'
    elif media >= 6:
        return 'Bom'
    else: 
        return 'Crítico'
    
def avaliar_funcionarios():
    total = 0
    exc = 0
    bom = 0
    crit = 0
    melhorNome = ""
    melhorMedia = -1
    while True:
        nome = input("Nome: ")
        if nome == "fim":
            break
        prod = int(input("Produtividade: "))
        qualidade = int(input("Qualidade: "))
        pont = int(input("Pontualidade: "))
        
        media = calcular_media(prod, qualidade, pont)
        categoria = classificar (media)
        print (f"{nome}, media {media}, {categoria}")
        
        total += 1
        if categoria == "Excelente":
            exc += 1
        elif categoria == "Bom":
            bom += 1
        else:
            critico += 1
            
        if media > melhorMedia:
            melhorMedia = media
            melhorNome = nome
    if total == 0:
        print ('Nada para calcular')
        return
    
    print('-' * 50)
    print('Relatório')
    print('-' * 50)
    print(f'Total de funcionários: {total}')
    print(f'Excelente: {exc}')
    print(f'Bom: {bom}')
    print(f'Crítico {critico}')
    print(f'Melhor Funcionário: {melhorNome}')
    print(f'Melhor Funcionário Média: {melhorMedia}')
    
    avaliar_funcionarios()
        
            
            