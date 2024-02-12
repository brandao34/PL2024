import re
import sys

#Ler o dataset, processá-lo e criar os seguintes resultados:
#   1.Lista ordenada alfabeticamente das modalidades desportivas;
#   2.Percentagens de atletas aptos e inaptos para a prática desportiva;
#   3.Distribuição de atletas por escalão etário (escalão = intervalo de 5 anos): ... [30-34], [35-39], ...



def querie(cvs_file):
    # regex para dar split de linhas csv
    pattern = re.compile(r',')
    # inicializar data structs para as queries
    modalidades = set()
    contador_atletas_aptos = 0
    contador_atletas_inaptos = 0
    contagem_por_escalao = {}

    #lidar com o ficheiro csv e processar os dados
    lines = cvs_file.split('\n')
    lines = lines[1:]

    # correr linha a linha, guardas as modalidades e contar os atletas aptos e inaptos e eliminar linhas vazias e o \n no fim 
    for line in lines:
        if not line.strip():
            continue
        
        line = line.rstrip('\n')
        data = pattern.split(line)

        modalidades.add(data[8])
        if re.match(r'^true$', data[12]):
                contador_atletas_aptos += 1
        elif re.match(r'^false$', data[12]):
                contador_atletas_inaptos += 1


        ## adicionar a distribuição de atletas por escalão etário (escalão = intervalo de 5 anos)
        idade = int(data[5])
        escalao = (idade // 5) * 5  # Criar intervalos de 5 anos
        contagem_por_escalao[escalao] = contagem_por_escalao.get(escalao, 0) + 1

                

    # ordenar a lista de modalidades
    modalidades = sorted(modalidades)
    print("1.Modalidades desportivas Ordenadas Alfabeticamente:\n")
    for i, modalidade in enumerate(modalidades, start=1):
        print(f"{i}. {modalidade}")
    

    # calcular as percentagens de atletas aptos e inaptos
    n_total_atletas = contador_atletas_aptos + contador_atletas_inaptos
    percentagem_aptos = (contador_atletas_aptos / n_total_atletas) * 100
    percentagem_inaptos = (contador_atletas_inaptos / n_total_atletas) * 100

    print("\n2.Percentagens de atletas aptos e inaptos para a prática desportiva:")
    print(f"Atletas aptos: {percentagem_aptos:.2f}%")
    print(f"Atletas inaptos: {percentagem_inaptos:.2f}%")

    # escalao 

    contagem_por_escalao = dict(sorted(contagem_por_escalao.items()))
    print("\n3.Distribuição por escalão etário:")
    for intervalo, contagem in contagem_por_escalao.items():
        percentagem = (contagem / n_total_atletas) * 100
        print(f"[{intervalo}-{intervalo+4}]: {percentagem:.2f}% dos atletas")

def main():
    if len(sys.argv) != 2:
        print("Uso correto: python3 fawkes.py arquivo.csv")
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        with open(file_path, 'r') as file:
            csv_data = file.read()
            querie(csv_data)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{file_path}' não foi encontrado.")
        sys.exit(1)


if __name__ == '__main__':
    main()
