from pdf2docx import parse, Converter
from tkinter.filedialog import askopenfilename
from tkinter import * 

window = Tk() 
window.title("pdf-docx") 
window.geometry("220x280+10+10")

def convert(filename):
	pdf_file = filename
	out_name = str(my_entry.get())
	print(pdf_file, out_name)
	if out_name[-4:] == 'docx':
		word_file = out_name
	else:
		word_file = out_name + '.docx'

	try:
		parse(pdf_file, word_file, start=0, end=None)
		status_name.set("Concluído!")

	except:
		cv = Converter(pdf_file)
		cv.convert(word_file, start=0, end=None)
		cv.close()
		status_name.set("Concluído!")

def open_file():
	global filename
	filename = askopenfilename()
	for line in filename.split('/'):
		file = line
	file_name.set(file)
	status_name.set("Em processo...")
	#print('2- ',filename)

def on_click(event):
    my_entry.configure(state=NORMAL)
    my_entry.delete(0, END)

    # make the callback only work once
    my_entry.unbind('<Button-1>', on_click_id)


file_name = StringVar()
status_name = StringVar()
status_name.set("Aguardando o arquivo")
bt_Open = Button(window, text="Abrir arquivo", command=open_file).grid(row=1, column=0, padx=5, pady=5, sticky="w")
lb0 = Label(window, text="Arquivo: ").grid(row=2, column=0, padx=5, sticky="w")
lb1 = Label(window, textvariable=file_name).grid(row=2, column=0, padx=55, sticky="w")
lb2 = Label(window, text="Insira o nome do arquivo de saída").grid(row=3, column=0, padx=15, sticky="w")

my_entry = Entry(window, width=34)
my_entry.grid(row=4, column=0, padx=5, sticky="w")
my_entry.insert(0, ".docx")
my_entry.configure(state=DISABLED)
on_click_id = my_entry.bind('<Button-1>', on_click)
btStart = Button(window, text="Iniciar", command= lambda:convert(filename)).grid(row=5, column=0, padx=85, pady=5, sticky="w")
lb_l = Label(window, text="Status:").grid(row=6, column=0, pady=5, padx=5, sticky="w")
lb_load = Label(window, textvariable=status_name).grid(row=6, column=0, padx=45, sticky="w")
lb3 = Label(window, text="Observações: ").grid(row=7, column=0, padx=5, sticky="w")
lb4 = Label(window, text="- A extensão (.docx) pode ser utilizada").grid(row=8, column=0, padx=1, sticky="w")
lb4 = Label(window, text="  mas não é obrigatória, por exemplo:").grid(row=9, column=0, padx=1, sticky="w")
lb5 = Label(window, text="-> teste           		- Correto!").grid(row=10, column=0, padx=1, sticky="w")
lb6 = Label(window, text="-> teste.docx 		- Correto!").grid(row=11, column=0, padx=1, sticky="w")

window.mainloop()