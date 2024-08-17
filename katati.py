import tkinter as tk
from tkinter import Canvas

class DrawingApp:
    def __init__(self, master):
        self.master = master
        master.title("図形描画アプリ")

        # ボタンで図形を選択
        self.btn_draw_circle = tk.Button(master, text="円を描画", command=self.draw_circle)
        self.btn_draw_circle.pack()

        self.btn_draw_rectangle = tk.Button(master, text="長方形を描画", command=self.draw_rectangle)
        self.btn_draw_rectangle.pack()

        # 描画エリア
        self.canvas = Canvas(master, width=400, height=400)
        self.canvas.pack()

    def draw_circle(self):
        self.canvas.delete("all")  # 既存の図形をクリア
        self.canvas.create_oval(50, 50, 150, 150, fill="red")

    def draw_rectangle(self):
        self.canvas.delete("all")  # 既存の図形をクリア
        self.canvas.create_rectangle(200, 50, 300, 150, fill="blue")

def main():
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()