def calcular_fila(lavagens):
    tempos = {"S": 10, "M": 20, "G": 30}
    total = 0
    for tipo in lavagens:
        if tipo in tempos:
            total += tempos[tipo]
    
    multa = 0
    if total > 50:
        multa = 5
    
    horario_saida = 14 + total // 60
    minutos_saida = total % 60
    
    pode_sair = horario_saida < 18 or (horario_saida == 18 and minutos_saida == 0)
    
    print(f"Tempo total: {total} min | Multa: {multa} min | Sai antes das 18h: {pode_sair}")

entradas = ["S", "G", "M"]
calcular_fila(entradas)