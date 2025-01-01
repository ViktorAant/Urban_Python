import tkinter as tk

def button_clicked():
    print("Кнопка была нажата!")

root = tk.Tk()
root.title("Проводник")
root.geometry("400x300+100+50")
root.resizable(False, False)
# Создаём метку с текстом
label = tk.Label(root, text="Привет, Tkinter!", font=("Arial", 20))
label.pack()
# Создаём кнопку с текстом и функцией, которая будет вызвана при нажатии
button = tk.Button(root, text="Выбрать файл", command=button_clicked)
button.pack()
# Создаём фрейм
frame = tk.Frame(root, borderwidth=2, relief="sunken")
frame.pack(padx=10, pady=10)

# Добавляем виджеты в фрейм
label = tk.Label(frame, text="Внутри фрейма")
label.pack(padx=10, pady=10)

button = tk.Button(frame, text="Кнопка")
button.pack(pady=5)


root.mainloop()