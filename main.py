import pandas as pd
import PySimpleGUI as sg

def Add_good(arr):
    a = []
    for i in arr:
        a.append(str(arr[i]))
    goods.loc[len(goods)] = a
    goods.drop(goods.columns[[0]], axis = 1)
    print(goods.head())

def Add_user(arr):
    a = []
    for i in arr:
        a.append(str(arr[i]))
    users.loc[len(users)] = a
    users.drop(users.columns[[0]], axis = 1)
    print(users.head())

def Add_station(arr):
    a = []
    print(station.head())
    for i in arr:
        a.append(str(arr[i]))
    station.loc[len(station)] = a
    station.drop(station.columns[[0]], axis = 1)
    print(station.head())


goods = pd.read_excel("Goods.xlsx", sheet_name="Sheet1")
users = pd.read_excel("Users.xlsx", sheet_name="Sheet1")
station = pd.read_excel("Station.xlsx", sheet_name="Sheet1")

def End_session():
    goods.to_excel("Goods.xlsx", index=False)
    users.to_excel("Users.xlsx", index=False)
    station.to_excel("Station.xlsx", index=False)

#[sg.Output(size=(88, 20))],

sg.theme('DarkAmber')
win_add = [
    [
        sg.Text("Добавьте новый товар")
    ],
    [
        sg.Text("Дата:")
    ],
    [
        sg.InputText()
    ],
[
        sg.Text("Номер:")
    ],
    [
        sg.InputText()
    ],
[
        sg.Text("Артикул:")
    ],
    [
        sg.InputText()
    ],
[
        sg.Text("Наименование:")
    ],
    [
        sg.InputText()
    ],
[
        sg.Text("Тип номенклатуры:")
    ],
    [
        sg.InputText()
    ],
    [
        sg.Button("Done")
    ],
]
win_reg = [
    [
        sg.Text("Необхадима регистрация")
    ],
    [
        sg.Text("Логин:")
    ],
    [
        sg.InputText()
    ],
    [
        sg.Button("Вход")
    ]
]
window_add = sg.Window('Data_work', win_add)
def Window_add_good():
    print("New window start")
    win_add = [
        [
            sg.Text("Добавьте новый товар")
        ],
        [
            sg.Text("Артикул:")
        ],
        [
            sg.InputText()
        ],
        [
            sg.Text("Номер:")
        ],
        [
            sg.InputText()
        ],
        [
            sg.Text("Наименование:")
        ],
        [
            sg.InputText()
        ],
        [
            sg.Text("Тип номенклатуры:")
        ],
        [
            sg.InputText()
        ],
        [
            sg.Text("Дата:")
        ],
        [
            sg.InputText()
        ],
        [
            sg.Button("Добавить")
        ],
    ]
    window_local = sg.Window('Data_work', win_add, modal=True)
    while True:
        print("Start Loop")
        event, values = window_local.read()
        if event in (None, 'Добавить'):
            Add_good(values)
            window_local.close()
            return 0


def Window_add_user():
    win_user = [
        [
            sg.Text("Фамилия")
        ],
        [
            sg.InputText()
        ],
        [
            sg.Text("Имя")
        ],
        [
            sg.InputText()
        ],
        [
            sg.Text("Отчество")
        ],
        [
            sg.InputText()
        ],
        [
            sg.Text("Телефон")
        ],
        [
            sg.InputText()
        ],
        [
            sg.Text("Эл. почта")
        ],
        [
            sg.InputText()
        ],
        [
            sg.Text("Дата рождения")
        ],
        [
            sg.InputText()
        ],
        [
            sg.Text("Статус")
        ],
        [
            sg.InputText()
        ],
        [
            sg.Button("Добавить")
        ]
    ]
    window_local = sg.Window('Data_work', win_user, modal=True)
    while True:
        print("Start Loop")
        event, values = window_local.read()
        if event in (None, 'Добавить'):
            Add_user(values)
            window_local.close()
            return 0

def Window_add_station():
    win_stat = [
        [
            sg.Text("Номер")
        ],
        [
            sg.InputText()
        ],
        [
            sg.Text("Наименование")
        ],
        [
            sg.InputText()
        ],
        [
            sg.Text("Адрес")
        ],
        [
            sg.InputText()
        ],
        [
            sg.Text("Индекс")
        ],
        [
            sg.InputText()
        ],
        [
            sg.Text("Координата широта")
        ],
        [
            sg.InputText()
        ],
        [
            sg.Text("Координата долгота")
        ],
        [
            sg.InputText()
        ],
        [
            sg.Button("Добавить")
        ]
    ]
    window_local = sg.Window('Data_work', win_stat, modal=True)
    while True:
        print("Start Loop")
        event, values = window_local.read()
        if event in (None, 'Добавить'):
            Add_station(values)
            window_local.close()
            return 0

def Window_main():
    win_start = [
        [
            sg.Text("Добро пожаловать в программу для ведения учета товаров")
        ],
        [
            sg.Button("Добавить товар")
        ],
        [
            sg.Button("Добавить пользователя")
        ],
        [
            sg.Button("Добавить станцию")
        ],
        [
            sg.Button("Готово")
        ]
    ]
    window_local = sg.Window('Data_work', win_start, modal=True)
    while True:
        event, values = window_local.read()
        if event in (None, 'Добавить товар'):
            print("Open Add Window")
            Window_add_good()
        if event in (None, 'Добавить пользователя'):
            print('Open Users Win')
            Window_add_user()
        if event in (None, 'Добавить станцию'):
            print('Open Station Win')
            Window_add_station()
        if event in (None, 'Готово', 'Cancel'):
            End_session()
            break


window = sg.Window('Data_work', win_reg)

while True:                             # The Event Loop
    event, values = window.read()
    # print(event, values) #debug
    if event in (None, 'Вход'):
        if str(values[0]) in ['АрсеньевЛВ', 'СветлаковаИФ']:
            window.close()
            Window_main()
            break

print("End Session")
