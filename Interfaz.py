import tkinter as tk
from tkinter import messagebox
from CurpGenerator import generar_curp
from datetime import datetime
from GetStates import states_abbreviations 

def actualizar_dias(*args):
    mes = int(var_mes.get())
    anio = int(var_anio.get())
    dias_del_mes = 30 if mes in [4, 6, 9, 11] else 29 if mes == 2 and (anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)) else 28 if mes == 2 else 31
    menu_dia['menu'].delete(0, 'end')
    for dia in range(1, dias_del_mes + 1):
        menu_dia['menu'].add_command(label=dia, command=lambda d=dia: var_dia.set(d))
    var_dia.set(1)

def generar_curp_gui():
    try:
        nombre = entry_nombre.get().strip().upper()
        apellido_paterno = entry_apellido_paterno.get().strip().upper()
        apellido_materno = entry_apellido_materno.get().strip().upper()
        anio = int(var_anio.get())
        mes = str(var_mes.get()).zfill(2)
        dia = str(var_dia.get()).zfill(2)
        sexo = var_sexo.get()
        estado = var_estado.get().upper()

        if not nombre.isalpha() or not apellido_paterno.isalpha() or not apellido_materno.isalpha():
            raise ValueError("Los nombres y apellidos solo deben contener letras.")
        
        curp = generar_curp(nombre, apellido_paterno, apellido_materno, anio, mes, dia, sexo, estado)
        curp_label.config(text=f"CURP Generada: {curp}")

    except ValueError as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Formulario de Generación de CURP - CURPGenerator")
root.geometry("400x500")
root.configure(bg="#051426") 
form_frame = tk.Frame(root, padx=20, pady=20, bg="#0C2240", bd=2, relief="groove")
form_frame.pack(pady=20)

tk.Label(form_frame, text="Generador de CURP", font=("Arial", 16, "bold"), bg="#244673", fg="#ffffff").grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(form_frame, text="Nombre:", bg="#0C2240", anchor="w", fg="#ffffff").grid(row=1, column=0, sticky="w", pady=5)
entry_nombre = tk.Entry(form_frame, width=25, bd=1, relief="solid")
entry_nombre.grid(row=1, column=1, pady=5)

tk.Label(form_frame, text="Apellido Paterno:", bg="#0C2240", anchor="w", fg="#ffffff").grid(row=2, column=0, sticky="w", pady=5)
entry_apellido_paterno = tk.Entry(form_frame, width=25, bd=1, relief="solid")
entry_apellido_paterno.grid(row=2, column=1, pady=5)

tk.Label(form_frame, text="Apellido Materno:", bg="#0C2240", anchor="w", fg="#ffffff").grid(row=3, column=0, sticky="w", pady=5)
entry_apellido_materno = tk.Entry(form_frame, width=25, bd=1, relief="solid")
entry_apellido_materno.grid(row=3, column=1, pady=5)

tk.Label(form_frame, text="Año de Nacimiento:", bg="#0C2240", anchor="w", fg="#ffffff").grid(row=4, column=0, sticky="w", pady=5)
anios = [str(anio) for anio in range(1924, datetime.now().year + 1)]
var_anio = tk.StringVar(root)
var_anio.set(anios[-1])
menu_anio = tk.OptionMenu(form_frame, var_anio, *anios, command=actualizar_dias)
menu_anio.grid(row=4, column=1, pady=5)

tk.Label(form_frame, text="Mes de Nacimiento:", bg="#0C2240", anchor="w", fg="#ffffff").grid(row=5, column=0, sticky="w", pady=5)
meses = list(range(1, 13))
var_mes = tk.IntVar(root)
var_mes.set(1)
menu_mes = tk.OptionMenu(form_frame, var_mes, *meses, command=actualizar_dias)
menu_mes.grid(row=5, column=1, pady=5)

tk.Label(form_frame, text="Día de Nacimiento:", bg="#0C2240", anchor="w", fg="#ffffff").grid(row=6, column=0, sticky="w", pady=5)
var_dia = tk.IntVar(root)
var_dia.set(1)
menu_dia = tk.OptionMenu(form_frame, var_dia, *range(1, 32))
menu_dia.grid(row=6, column=1, pady=5)

tk.Label(form_frame, text="Sexo (H/M):", bg="#0C2240", anchor="w", fg="#ffffff").grid(row=7, column=0, sticky="w", pady=5)
var_sexo = tk.StringVar(root)
var_sexo.set("H")
menu_sexo = tk.OptionMenu(form_frame, var_sexo, "H", "M")
menu_sexo.grid(row=7, column=1, pady=5)

tk.Label(form_frame, text="Estado:", bg="#0C2240", anchor="w", fg="#ffffff").grid(row=8, column=0, sticky="w", pady=5)
var_estado = tk.StringVar(root)
var_estado.set(list(states_abbreviations.keys())[0])
menu_estado = tk.OptionMenu(form_frame, var_estado, *states_abbreviations.keys())
menu_estado.grid(row=8, column=1, pady=5)

generate_button = tk.Button(form_frame, text="Generar CURP", command=generar_curp_gui, bg="#4E7DA6", fg="white", font=("Arial", 10, "bold"), relief="flat")
generate_button.grid(row=9, column=0, columnspan=2, pady=10)

curp_label = tk.Label(form_frame, text="CURP Generada: ", font=("Arial", 10, "italic"), bg="#0C2240", fg="#4E7DA6")
curp_label.grid(row=10, column=0, columnspan=2, pady=10)

root.mainloop()