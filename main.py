import PySimpleGUI as sg
import csv

proper_csv_file = False

def read_csv(file_name):
    global proper_csv_file
    settlements = []
    try:
        with open(file_name, 'r') as fp:
            csv_file = csv.reader(fp)
            for l in csv_file:
                settlements.append(l)
        sg.popup('Poprawnie wczytano plik csv')
        proper_csv_file = True
        return settlements
    except:
        proper_csv_file = False
        sg.popup_error('Nie udało się wczytać pliku csv')

sg.theme('BrightColors')
layout = [  
            [sg.Image(r'img/hrappkabot_logo.png')],
            [sg.Text('Adres e-mail potrzebny do zalogowania: '), sg.InputText()],
            [sg.Text('Hasło potrzebne do zalogowania: '), sg.InputText(password_char='*')],
            [sg.Text('Plik zaimportowany z banku: '), sg.Input(), sg.FileBrowse(), sg.Button('Wczytaj plik')],
            [sg.Button('Zatwierdź'), sg.Button('Anuluj')] ]

window = sg.Window('Hrappka Bot', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Anuluj': # if user closes window or clicks cancel
        break
    if event == 'Wczytaj plik':
        file_name = values[3]
        settlements = read_csv(file_name)
    if event == 'Zatwierdź':
        if values[1] == '' or values[2] == '':
            sg.popup_error('Podaj email i hasło do hrappki głuptasie')
        elif proper_csv_file == False:
            sg.popup_error('Wczytaj plik csv aby zatwierdzić')
        else:
            sg.popup('Zatwierdziłeś, przechodzę do logowania')
            print(settlements)



window.close()
