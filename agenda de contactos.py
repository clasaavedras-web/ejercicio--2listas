#agenda.py - agenda de contactos / FPY1101

agenda = []

def agregar_contacto(nombre,telefono,email):
 contacto={
    "nombre":nombre,
    "telefono":telefono,
    "email":email
 }

 agenda.append(contacto)
 print(f"contacto´{nombre}´agregado correctamente.")

def mostrar_agenda():
    if len(agenda) == 0:
       print("la agenda esta vacia.")
       return
print("/n----contactos en la agenda---")
for i,contacto in enumerate(agenda,start=1):
   print(f"{1}.{contacto[´ nombre ']} / tel:{contacto[´telefono´]} / email:{contacto[´email ]})


