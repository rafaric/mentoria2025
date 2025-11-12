import tkinter as tk
from tkinter import messagebox
import db


def iniciar_gui():
    global entry_nombre, entry_apellido, entry_telefono, entry_email, lista

    def agregar():
        nombre = entry_nombre.get().strip()
        apellido = entry_apellido.get().strip()
        telefono = entry_telefono.get().strip()
        email = entry_email.get().strip()

        if not nombre or not apellido or not telefono or not email:
            messagebox.showwarning(
                "Campos vacíos", "Todos los campos son obligatorios.")
            return

        db.insertar_contacto(nombre, apellido, telefono, email)
        listar()
        limpiar()
        messagebox.showinfo("Agenda", "Contacto agregado exitosamente.")

    def listar():
        lista.delete(0, tk.END)
        for indice, fila in enumerate(db.obtener_contactos()):
            lista.insert(
                tk.END, f"{indice + 1} - {fila[1]} {fila[2]} | {fila[3]} | {fila[4]}")

    def eliminar():
        seleccion = lista.curselection()
        if not seleccion:
            messagebox.showwarning(
                "Eliminar", "Seleccioná un contacto para eliminar.")
            return

        id_contacto = lista.get(seleccion[0]).split(" - ")[0]
        confirmar = messagebox.askyesno(
            "Confirmar eliminación", "¿Estás seguro de eliminar este contacto?")
        if confirmar:
            db.eliminar_contacto(id_contacto)
            listar()
            messagebox.showinfo("Agenda", "Contacto eliminado.")

    def limpiar():
        entry_nombre.delete(0, tk.END)
        entry_apellido.delete(0, tk.END)
        entry_telefono.delete(0, tk.END)
        entry_email.delete(0, tk.END)

    root = tk.Tk()
    root.title("Agenda de Contactos")

    # Frame para listado y botones de gestión
    frame_listado = tk.Frame(root, relief="ridge", bd=2)
    frame_listado.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    lista = tk.Listbox(frame_listado, width=60)
    lista.grid(row=0, column=0, columnspan=2, rowspan=4, padx=10, pady=10)

    tk.Button(frame_listado, text="Listar", command=listar).grid(
        row=1, column=2, sticky="ew", padx=5, pady=2)
    tk.Button(frame_listado, text="Eliminar", command=eliminar).grid(
        row=2, column=2, sticky="ew", padx=5, pady=2)

    # Frame para formulario y botón agregar
    frame_formulario = tk.Frame(root, relief="ridge", bd=2)
    frame_formulario.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    tk.Label(frame_formulario, text="Nombre").grid(
        row=0, column=0, padx=5, pady=5)
    tk.Label(frame_formulario, text="Apellido").grid(
        row=0, column=2, padx=5, pady=5)
    tk.Label(frame_formulario, text="Teléfono").grid(
        row=1, column=0, padx=5, pady=5)
    tk.Label(frame_formulario, text="Email").grid(
        row=1, column=2, padx=5, pady=5)

    entry_nombre = tk.Entry(frame_formulario)
    entry_apellido = tk.Entry(frame_formulario)
    entry_telefono = tk.Entry(frame_formulario)
    entry_email = tk.Entry(frame_formulario)

    entry_nombre.grid(row=0, column=1, padx=5, pady=5)
    entry_apellido.grid(row=0, column=3, padx=5, pady=5)
    entry_telefono.grid(row=1, column=1, padx=5, pady=5)
    entry_email.grid(row=1, column=3, padx=5, pady=5)

    tk.Button(frame_formulario, text="Agregar", command=agregar).grid(
        row=2, column=1, columnspan=2, sticky="ew", padx=5, pady=10)

    listar()
    root.mainloop()
