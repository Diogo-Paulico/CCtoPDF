from cc import ccPDFmake
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showinfo, showerror

front = None
back = None
save = None
def open_back():
    global back, back_txt
    back = askopenfilename(title="Costas CC", filetypes=[("Imagem", ".jpg, .jpeg, .png")])
    if back:
        back_txt.set("Escolhido")
    else:
        back_txt.set("Escolher Costas CC")


def open_front():
    global front, frente_txt
    front = askopenfilename(title="Frente CC", filetypes=[("Imagem", ".jpg, .jpeg, .png")])
    if front:
        frente_txt.set("Escolhido")
    else:
        frente_txt.set("Escolher Frente CC")


def save_pick():
    global save
    save = asksaveasfilename(defaultextension='.pdf', filetypes=[("pdf files", '*.pdf')])
    saveText()
    if save:
        generate()

def saveText():
    global text, txt_edit
    text = txt_edit.get()

def generate():
    global front, back, save, text
    if front and back and save:
        ccPDFmake(front, back, save, text)
        showinfo(title="Gerado!", message="PDF gerado com sucesso!")
        window.destroy()
    else:
        showerror(title="Erro!", message="Escolha ambas as faces do CC!")


window = tk.Tk()
window.title("CC para PDF")
window.rowconfigure(0, minsize=10, weight=1)
window.columnconfigure(1, minsize=10, weight=1)



frente_txt = tk.StringVar()
frente_txt.set("Escolher Frente CC")

back_txt = tk.StringVar()
back_txt.set("Escolher Costas CC")

txt_edit = tk.Entry(width=50)


front_open = tk.Button(window, textvariable = frente_txt, command=open_front)
back_open = tk.Button(window, textvariable = back_txt, command=open_back)
btn_save = tk.Button(window, text="Gerar", command=save_pick)
text_label = tk.Label(text = "Se desejar insira um texto para usar como marca de água")

front_open.grid(row=0, column=0, sticky="ew", padx=0.2, pady=5)
back_open.grid(row=1, column=0, sticky="ew", padx=0.2, pady=5)

text_label.grid(row=2, column=0)
txt_edit.grid(row=3, column=0, sticky="nsew", pady=5)

btn_save.grid(row=4, column=0, sticky="ew", padx=5)

window.mainloop()



