# Importando Biblioteca
import PySimpleGUI as sg

# Função da janela inicial
def main():
    # Definição de conteudo da janela
    # Definição de conteudo da janela
    layout = [  [sg.Text('Visualização')],
                [sg.Text('Total de dias cadastrados')],
                [sg.Text('Total de Usuários:')],
                [sg.Button('Voltar ao Menu')] ]
    
    # Criando a janela
    window = sg.Window('Cadastro de Pressão', layout)
    
    # Event Loop e interação com usuário
    while True:
        # Exibir e interagir com a janela
        event, values = window.read()
        
        #Verificando se usuário deseja sair ou a janela foi fechada
        if  event == sg.WIN_CLOSED:
            break
    # Terminando e removendo janela    
    window.close()

if __name__ == "__main__":
    main()