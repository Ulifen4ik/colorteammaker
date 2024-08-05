import tkinter as tk
import customtkinter as ctk

from color_frame import ColorFrame

# Светлая тема
ctk.set_appearance_mode('light')
class App(ctk.CTk):
    def __init__(self):
        super().__init__()


        self.title('Color Theme Maker')

        self.configure(padx=10, pady=10)
        self.resizable(0, 0)

        # Создаем список виджетов
        self.color_frames = []
        
        for i in range(4):
            print(i)
            cf =  ColorFrame(self)
            cf.grid(column=i,row=0,padx=10,pady=10)
            self.color_frames.append(cf)

        # self.color_frames[1].set_color("#ff00ff")

        # Меню
        self.menu = tk.Menu(self)
        self.configure(menu=self.menu)
        self.configure(menu=self.menu)
        self.menu.add_command(label="Сохранить",command=self.save_colors)
        self.menu.add_command(label="Вернуть цвета",command=self.load_colors)

        self.load_colors()
        
        self.protocol("WM_DELETE_WINDOW", self.on_closing)


    def save_colors(self):
        # Ввыдем цвета в терминал
        

        # Сохраняем цвета в файл
        with open("mycolors.txt","w", encoding="utf-8") as file:
            for cf in self.color_frames:
                file.write(cf.get_color() + "\n") 

    def load_colors(self):
        # Получаем цвета из файлов
        try:
            with open('mycolors.txt','r', encoding="utf-8") as file:
                mycolors_list = []
                for line in file:
                    mycolors_list.append(line.strip())
            column=0
            for cf in self.color_frames:
                cf.set_color(mycolors_list[column])
                column+=1
        except FileNotFoundError:
            print("Файл с цветовой темой не найден")
    
    def on_closing(self):
        # По закрытию окна
        # Сохраняем цвета
        self.save_colors()
        # Закрываем окно программы
        self.destroy()


# Запуск программы
if __name__ == "__main__":
    app = App()
    app.mainloop()
