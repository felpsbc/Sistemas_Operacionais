MEMORIA_TOTAL = 1000  
NUM_PARTICOES = 10    

class Processo:
    def __init__(self, id, tamanho, alocado=False):
        self.id = id
        self.tamanho = tamanho
        self.alocado = alocado

memoria = [0] * MEMORIA_TOTAL

def inicializar_memoria():
    global memoria
    memoria = [0] * MEMORIA_TOTAL

def exibir_memoria():
    print(' '.join(map(str, memoria)))

def alocar_particoes_fixas(processo):
    particao_tamanho = MEMORIA_TOTAL // NUM_PARTICOES
    for i in range(NUM_PARTICOES):
        espaco_encontrado = True
        for j in range(i * particao_tamanho, (i + 1) * particao_tamanho):
            if memoria[j] != 0:
                espaco_encontrado = False
                break
        if espaco_encontrado:
            for j in range(i * particao_tamanho, (i + 1) * particao_tamanho):
                memoria[j] = processo.id
            print(f"Processo {processo.id} alocado na particao {i}")
            return True
    return False

def alocar_particoes_dinamicas(processo):
    espaco_continuo = 0
    for i in range(MEMORIA_TOTAL):
        if memoria[i] == 0:
            espaco_continuo += 1
            if espaco_continuo == processo.tamanho:
                for j in range(i - espaco_continuo + 1, i + 1):
                    memoria[j] = processo.id
                print(f"Processo {processo.id} alocado dinamicamente na memoria.")
                return True
        else:
            espaco_continuo = 0
    return False

def alocar_paginacao(processo, tamanho_pagina):
    num_paginas = (processo.tamanho + tamanho_pagina - 1) // tamanho_pagina
    paginas_alocadas = 0
    for i in range(0, MEMORIA_TOTAL, tamanho_pagina):
        espaco_disponivel = True
        for j in range(i, i + tamanho_pagina):
            if memoria[j] != 0:
                espaco_disponivel = False
                break
        if espaco_disponivel:
            for j in range(i, i + tamanho_pagina):
                memoria[j] = processo.id
            paginas_alocadas += 1
            if paginas_alocadas == num_paginas:
                print(f"Processo {processo.id} alocado com paginacao.")
                return True
    return False

def desalocar(processo):
    for i in range(MEMORIA_TOTAL):
        if memoria[i] == processo.id:
            memoria[i] = 0
    print(f"Processo {processo.id} desalocado.")

def main():
    inicializar_memoria()
    
    p1 = Processo(1, 75)
    p2 = Processo(2, 140)
    p3 = Processo(3, 50)
    
    if not alocar_particoes_fixas(p1):
        print(f"Falha ao alocar processo {p1.id} nas particoes fixas.")
    
    if not alocar_particoes_dinamicas(p2):
        print(f"Falha ao alocar processo {p2.id} nas particoes dinâmicas.")
    
    tamanho_pagina = 10
    if not alocar_paginacao(p3, tamanho_pagina):
        print(f"Falha ao alocar processo {p3.id} usando paginacao.")

    exibir_memoria()

    desalocar(p1)
    desalocar(p2)
    desalocar(p3)
    
    exibir_memoria()

if __name__ == "__main__":
    main()

# Parte 4
# Particionamento fixo: Memória dividida em blocos de tamanho fixo.
# Particionamento dinâmico: Memória dividida em blocos de tamanhos variáveis.

# Memória é dividida em páginas (memória virtual) e quadros de páginas (memória física).
# O processo é alocado em qualquer quadro disponível, sem precisar de contiguidade.
# Usa uma tabela de páginas para mapear a memória virtual à memória física.

# Fragmentação interna: Ocorre quando há desperdício de espaço dentro de um bloco devido ao tamanho fixo das unidades de alocação.
# Fragmentação externa: Ocorre quando o espaço livre na memória é insuficiente para alocar novos processos, embora a soma total de memória livre seja suficiente.

# Parte 5
# 1- Ao implementar o gerenciamento de memória, os principais desafios incluem garantir uma alocação eficiente de memória, controlar a fragmentação interna e externa, e gerenciar o espaço livre de forma eficaz. Além disso, a troca de dados entre memória física e virtual pode impactar o desempenho, exigindo estratégias para otimizar o uso de memória e minimizar a latência.
# 2- O gerenciamento de memória impacta diretamente o desempenho do sistema, pois uma alocação ineficiente pode causar lentidão devido ao uso excessivo de memória virtual ou trocas frequentes de página. Um bom gerenciamento garante melhor utilização dos recursos, permitindo que mais processos sejam executados sem sobrecarregar o sistema, melhorando a velocidade e a eficiência das aplicações.
# 3- A fragmentação interna ocorre quando há desperdício de memória dentro de uma unidade de alocação, enquanto a fragmentação externa ocorre quando pequenos espaços livres na memória não são suficientes para novos processos. 
