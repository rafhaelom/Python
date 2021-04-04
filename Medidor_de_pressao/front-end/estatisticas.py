# Importando Biblioteca
import PySimpleGUI as sg

# Função da janela inicial
def main():
    # Definição de conteudo da janela
    # Definição de conteudo da janela
    layout = [  [sg.Text('Estatísticas')],
                [sg.Button('Voltar ao Menu'), sg.Button('Sair')] ]
    
    # Criando a janela
    window = sg.Window('Cadastro de Pressão', layout)
    
    # Event Loop e interação com usuário
    while True:
        # Exibir e interagir com a janela
        event, values = window.read()
        
        #Verificando se usuário deseja sair ou a janela foi fechada
        if  event == sg.WIN_CLOSED or event == 'Sair':
            break
    # Terminando e removendo janela    
    window.close()

if __name__ == "__main__":
    main()