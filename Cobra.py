# Nome do Projeto: COBRA (Congo-Brasil)
# Áreas de estudo: Processamento de Sinais (Imagens), Tratamento de Materias (Metalurgia)
# Tipo de Projeto: OpenSource com foco CEFET-RJ (Maracanã)
# Repositório do Projeto: https://github.com/james988/Cobra_EstudoDeMateriais
# Ingenheiros Fundadores do Projeto: Carlos Eduardo Guedes Catunda e Jacques Ben Bilombe 

from Analyzer import processing

def main():
    # Ask the user if He/She wants extract a ROI or to analyze the entire Image.
    ROI_NOT = input('Escolha a processo de análise: Y/y para imagem inteira ou N/n para selecionar uma parte: ')

    processing(ROI_NOT)


if __name__ == '__main__':
    print('Start the analyze\n')
    main()
