# Importando Biblioteca
import PySimpleGUI as sg

# Função da janela de cadastro
def main():
    # Definição de conteudo da janela
    layout = [  [sg.Text('Cadastro')],
                [sg.Text('Nome'), sg.Input()],
                [sg.Text('Pressão Arterial Sistólica'), sg.Input()],
                [sg.Text('Pressão Arterial Diastólica'), sg.Input()],
                [sg.Text('Pulsação'), sg.Input()],
                [sg.Button('Ok'), sg.Button('Cancelar')] ]
    
    # Criando a janela
    window = sg.Window('Cadastro de Pressão', layout)
    
    # Event Loop e interação com usuário
    while True:
        # Exibir e interagir com a janela
        event, values = window.read()
        
        #Verificando se usuário deseja sair ou a janela foi fechada
        if  event == sg.WIN_CLOSED or event == 'Cancelar':
            break
        print('Nome ', values[0])
        print('Pressão Arterial Sistólica ', values[1])
        print('Pressão Arterial Diastólica ', values[2])
        print('Pulsação', values[3])
    # Terminando e removendo janela    
    window.close()

if __name__ == "__main__":
    main()