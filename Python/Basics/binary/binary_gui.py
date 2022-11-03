# hello_world.py

import PySimpleGUI as sg
from translate_from_binary import translate
from Utils.cls import clear_console


def main():
    window = init_window()
    while True:
        event, values = window.read()
        print(event)
        if event == sg.WIN_CLOSED or event == '-EXIT-':
            break
        elif event == "-BtT-":
            binary = values["-BINARY-"]
            window["-TEXT-"].update(translate(binary))
        elif event == "-TtB-":
            pass
    window.close()
    clear_console()


def init_window():
    sg.theme('Reds')
    window_layout = init_layout()
    return sg.Window(title="Binary Converter", layout=window_layout)


def init_layout():

    layout_binary = [
        [sg.Frame('Enter Binary Code', [
            [sg.Multiline(
                "", key="-BINARY-", size=(None, 10))]
        ])]
    ]

    layout_text = [
        [sg.Frame('Text', [
            [sg.Multiline("", key="-TEXT-", size=(None, 10))]
        ])]]

    buttons_size = 10
    centered = [
        [sg.Frame('Options', [
            [
                sg.Button("To_Binary", size=(buttons_size, None), key='-BtT-'),
                sg.Exit('Exit', size=(buttons_size, None), key='-EXIT-'),
                sg.Button("To_Text", size=(buttons_size, None), key='-TtB-', disabled=True)
            ]
        ])]

    ]

    layout = [
        [layout_binary],
        [sg.VPush()],
        [sg.Push(), sg.Column(centered,
                              element_justification='c'), sg.Push()],
        [sg.VPush()],
        [layout_text]
    ]

    return layout


if __name__ == "__main__":
    main()
