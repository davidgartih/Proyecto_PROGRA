from tkinter import *
from PIL import Image, ImageTk
from tkinter import simpledialog as ci
from tkinter import messagebox as ca
from tkinter import ttk
import sqlite3

class Aplicacion:
    #Conector de la base de datos a tkinter
    def conectorBD(self):
        self.conexion=sqlite3.connect("Matricula(CURC).db")
        self.cursor=self.conexion.cursor()
        try:
            #CREACION TABLA ESTUDIANTES
            self.cursor.execute("""create table Estudiantes
                           (ID_Alumno integer primary key,
                            Nombre text,
                            Apellido text,
                            Telefono integer,
                            Direccion text)""")            
            #CREACION TABLA MAESTROS
            self.cursor.execute("""create table Maestros
                           (ID_Maestro integer primary key,
                            Nombre text,
                            Apellido text,
                            Telefono integer,
                            Direccion text)""")            
            #CREACION DE TABLA SECCIONES
            self.cursor.execute("""CREATE TABLE Secciones (
                    ID_Seccion INTEGER PRIMARY KEY AUTOINCREMENT,
                    ID_Docente INTEGER,
                    ID_Clase INTEGER,
                    Hora_Inicio TEXT,
                    Hora_Fin TEXT,
                    FOREIGN KEY (ID_Docente) REFERENCES Maestros(ID_Docente) ON DELETE CASCADE,
                    FOREIGN KEY (ID_Clase) REFERENCES Clases(ID_Clase) ON DELETE CASCADE);""")            
            #CREACION DE TABLA MATRICULA
            self.cursor.execute("""CREATE TABLE Matricula (
                    ID_Matricula INTEGER PRIMARY KEY AUTOINCREMENT,
                    ID_Alumno INTEGER,
                    ID_Seccion INTEGER,
                    FOREIGN KEY(ID_Alumno) REFERENCES Estudiantes(ID_Alumno) ON DELETE CASCADE,
                    FOREIGN KEY(ID_Seccion) REFERENCES Secciones(ID_Seccion) ON DELETE CASCADE);""")
            
            #CREACION DE TABLA CLASES
            self.cursor.execute("""create table Clases(
                    ID_Clase integer primary key autoincrement,
                    Nombre_Clase text);""")

            self.conexion.commit()
        except sqlite3.OperationalError:
            print("")

        
    #Ventana principal
    def __init__(self):
        self.ven = Tk()
        self.ven.geometry("430x340")
        self.ven.title("Login")
        self.ven.config(bg="lightblue")
        self.ven.iconbitmap("UNAH-version-horizontal.ico")

        #Imagen
        img = Image.open("UNAH-version-horizontal.png")
        imgdim=img.resize((100,60))
        logo = ImageTk.PhotoImage(imgdim) 

        img2=Image.open("person_fill_icon_159457.webp")
        img2dim=img2.resize((50,50))
        logo2=ImageTk.PhotoImage(img2dim)

        img3=Image.open("1001008.png")
        img3dim=img3.resize((50,50))
        logo3=ImageTk.PhotoImage(img3dim)

        #Colocar imagen en el label
        self.lbl1 = Label(self.ven, image=logo, bg="lightblue")
        self.lbl1.place(x=160,y=10)

        self.lbl2 = Label(self.ven, image=logo2, bg="lightblue")
        self.lbl2.place(x=100,y=70)

        self.lbl2 = Label(self.ven, image=logo3, bg="lightblue")
        self.lbl2.place(x=100,y=150)
        
        #Informacion Personal, labels
        self.lbl2=Label(self.ven,text="Correo Electronico:", bg="lightblue",font=("Times New Roman", 14))
        self.lbl2.place(x=160,y=70)

        self.lbl3=Label(self.ven,text="Contraseña:",bg="lightblue",font=("Times New Roman", 14))
        self.lbl3.place(x=160,y=150)
        #Entrys
        self.var1=StringVar()
        self.var2=StringVar()

        self.txt1=Entry(self.ven,textvariable=self.var1)
        self.txt1.place(x=160,y=100)

        self.txt2=Entry(self.ven,textvariable=self.var2,show="*")
        self.txt2.place(x=160,y=180)

        #Mostrar contraseña
        self.var3=IntVar()
        self.chck1=Checkbutton(self.ven,text="Mostrar contraseña",font=("Times New Roman",14),variable=self.var3,onvalue=1,offvalue=0,command=self.pw, bg="lightblue")
        self.chck1.place(x=160,y=230)

        #Boton de acceso
        self.btn1=Button(self.ven,text="Acceder", height=1,width=10, font=("Times New Roman", 14),command=self.acceder)
        self.btn1.place(x=175,y=270)

        #Cerrar metodo constructor
        self.ven.mainloop()
    

    #Ventana de informacion general
    def pw(self):
        if self.var3.get()==1:
            self.txt2.config(show="")
        else:
            self.txt2.config(show="*")
            
            
    def acceder(self):
        va=self.var1.get()
        va2=self.var2.get()
        listacorreos=["hugozuniga@gmail.com","angelvelasquez@gmail.com","davidgarcia@gmail.com","marcomadrid@gmail.com"]
        #Validar que el correo y la contraseña sena las correctas
        if va in listacorreos and self.var2.get()=="Maria":
            # Limpia el login al acceder
            self.var1.set("")
            self.var2.set("")
                
            # Limpia el login al acceder
            
            self.var1.set("")
            self.var2.set("")
            
            #Desaparecer la ventana principal
            self.ven.geometry("0x0")
    
            # Accede a la información general de la bd
            self.venInfo = Toplevel(self.ven)
            self.venInfo.geometry("480x450")
            self.venInfo.title("Información General")
            self.venInfo.config(bg="lightblue")
            self.venInfo.iconbitmap("UNAH-version-horizontal.ico")
    
            # Cargar y mostrar imagen en la segunda ventana
            imgInfo = Image.open("UNAH-version-horizontal.png")
            imgInfodim = imgInfo.resize((100, 60))
            self.logoInfo = ImageTk.PhotoImage(imgInfodim)  
    
            self.lblInfo = Label(self.venInfo, image=self.logoInfo, bg="lightblue")
            self.lblInfo.place(x=180, y=10)
    
            # lbl info con wraplength
            self.lbl2Info = Label(
            self.venInfo,
            text="El CURC (Centro Universitario Regional del Centro) en Honduras es una institución de educación superior que forma parte de la Universidad Nacional Autónoma de Honduras (UNAH). En este proyecto, desarrollamos una base de datos que permite controlar y gestionar eficientemente el proceso de matrícula de los estudiantes, facilitando el registro, consulta y administración de la información académica de manera ordenada y segura.",
            bg="lightblue",
            font=("Times New Roman", 12),
            justify="center",
            wraplength=440
            )
            self.lbl2Info.place(x=20, y=100)
    
            
            #menu bar
            self.menubar = Menu(self.venInfo)
    
           
            info_menu = Menu(self.menubar, tearoff=0)
            info_menu.add_command(label="Misión y Visión", command=self.misionVision)
            info_menu.add_command(label="Quiénes Somos", command=self.quienes_somos)
            info_menu.add_command(label="Contáctanos", command=self.contacto)
    
            info_menu2 = Menu(self.menubar, tearoff=0)
            info_menu2.add_command(label="Alumnos", command=self.alumnos)
            info_menu2.add_command(label="Maestros", command=self.maestros)
            info_menu2.add_command(label="Clases", command=self.clases)
            info_menu2.add_command(label="Seccion", command=self.seccion)
            info_menu2.add_command(label="Matricula", command=self.matricula)
    
    
    
            self.menubar.add_cascade(label="Información", menu=info_menu)
            self.menubar.add_cascade(label="Gestión", menu=info_menu2)
    
    
            self.venInfo.config(menu=self.menubar)
            
        #Condicion si correo no se encuentra en la lista y la contraseña es incorrecta    
        elif va not in listacorreos and va2!="Maria":
            ca.showerror("Eror","El correo y la contraseña son incorrecotos.") 
        #Condicion si solo el correo esta incorrecto
        elif va not in listacorreos and va2=="Maria":
            ca.showerror("Error", "El correo electronico no existe")
        #Condicion si solo la contraseña esta incorrecta
        elif va in listacorreos and va2!="Maria":
            ca.showerror("Error", "La contraseña es incorrecta")
            
            
    #Ventana Mision y Vision
    def misionVision(self):
        self.Mv = Toplevel(self.venInfo)
        self.Mv.geometry("350x380")
        self.Mv.title("Misión y Visión")
        self.Mv.config(bg="lightblue")
        self.Mv.iconbitmap("UNAH-version-horizontal.ico")

        #Vision
        self.lblmv = Label(self.Mv, text="Visión", font=("Times New Roman", 14, "bold"), bg="lightblue")
        self.lblmv.place(x=140, y=10)

        self.lblmv2 = Label(
        self.Mv,
        text="Ser una herramienta tecnológica eficiente, segura y moderna que facilite y optimice el proceso de matrícula en el CURC, apoyando la transformación digital de la gestión académica en beneficio de los estudiantes y del personal administrativo.",
        wraplength=320,
        justify="center",
        font=("Times New Roman", 11),
        bg="lightblue"
        )
        self.lblmv2.place(x=10, y=40)

        #Mision
        self.lblmv3 = Label(self.Mv, text="Misión", font=("Times New Roman", 14, "bold"), bg="lightblue")
        self.lblmv3.place(x=140, y=170)

        self.lblmv4 = Label(
        self.Mv,
        text="Desarrollar y mantener un sistema de base de datos funcional y accesible que permita el registro, consulta y administración de la información académica de los estudiantes del CURC, contribuyendo a una gestión educativa más ordenada, rápida y confiable.",
        wraplength=320,
        justify="center",
        font=("Times New Roman", 11),
        bg="lightblue"
        )
        self.lblmv4.place(x=10, y=200)

        #Boton, regresar a pantalla principal
        self.btntMv=Button(self.Mv,text="Regresar",height=1,width=10,font=("Times New Roman", 12),command=self.regresar)
        self.btntMv.place(x=140,y=310)

    #Metodo destruir ventana, Mision y Vision
    def regresar(self):
        self.Mv.destroy()

    #Ventana de Quienes Somos
    def quienes_somos(self):
        self.qs = Toplevel(self.venInfo)
        self.qs.geometry("450x450")
        self.qs.title("Quienes Somos")
        self.qs.config(bg="lightblue")
        self.qs.iconbitmap("UNAH-version-horizontal.ico")

        self.lblqs = Label(
        self.qs,
        text="Somos un grupo de estudiantes de 17 años que cursamos el último año del Bachillerato Técnico en Computación en el Instituto Marista La Inmaculada de Comayagua. \n\nComprometidos con la excelencia académica, desarrollamos este proyecto como parte de nuestra formación, aplicando nuestros conocimientos para ofrecer soluciones tecnológicas prácticas y funcionales.",
        bg="lightblue",
        font=("Times New Roman", 12),
        justify="center",
        wraplength=450
        )
        self.lblqs.place(x=10, y=20)

        self.lblqs2=Label(self.qs,text="Nuestros curriculums:",bg="lightblue",font=("Times New Roman", 12))
        self.lblqs2.place(x=10,y=200)

        self.lblqs3=Label(self.qs,text="17 Angel Rodriguez:",bg="lightblue",font=("Times New Roman", 12))
        self.lblqs3.place(x=10,y=250)

        self.lblqs3=Label(self.qs,text="23 David Garcia:",bg="lightblue",font=("Times New Roman", 12))
        self.lblqs3.place(x=10,y=280)

        self.lblqs3=Label(self.qs,text="31 Hugo Varela:",bg="lightblue",font=("Times New Roman", 12))
        self.lblqs3.place(x=10,y=310)

        #Boton, regresar a pantalla principal
        self.btnqs=Button(self.qs,text="Regresar",height=1,width=10,font=("Times New Roman", 12),command=self.regresarDos)
        self.btnqs.place(x=170,y=340)
    
    #Metodo de destruir ventana, Quienes somos
    def regresarDos(self):
        self.qs.destroy()

    #Ventana de contactanos
    def contacto(self):
        self.ctc = Toplevel(self.venInfo)
        self.ctc.geometry("450x320")
        self.ctc.title("Contáctanos")
        self.ctc.config(bg="lightblue")
        self.ctc.iconbitmap("UNAH-version-horizontal.ico")

    # Título subrayado y centrado
        self.lblctc = Label(
        self.ctc,
        text="Contáctanos",
        font=("Times New Roman", 14, "underline"),
        bg="lightblue"
    )
        self.lblctc.place(x=160, y=20)

    # Imágenes
        imgcel = Image.open("phone_icon_172267.webp").resize((40, 40))
        self.logoCel = ImageTk.PhotoImage(imgcel)

        imgcel2 = Image.open("phone_icon_172267.webp").resize((40, 40))
        self.logoCel2 = ImageTk.PhotoImage(imgcel2)

        imgcel3 = Image.open("phone_icon_172267.webp").resize((40, 40))
        self.logoCel3 = ImageTk.PhotoImage(imgcel3)

    # Imagen + número 1
        self.lblcel1 = Label(self.ctc, image=self.logoCel, bg="lightblue")
        self.lblcel1.place(x=110, y=80)
        self.lblnum1 = Label(self.ctc, text="8936-0668", font=("Times New Roman", 12), bg="lightblue")
        self.lblnum1.place(x=170, y=85)

    # Imagen + número 2
        self.lblcel2 = Label(self.ctc, image=self.logoCel2, bg="lightblue")
        self.lblcel2.place(x=110, y=140)
        self.lblnum2 = Label(self.ctc, text="3198-3454", font=("Times New Roman", 12), bg="lightblue")
        self.lblnum2.place(x=170, y=145)

    # Imagen + número 3
        self.lblcel3 = Label(self.ctc, image=self.logoCel3, bg="lightblue")
        self.lblcel3.place(x=110, y=200)
        self.lblnum3 = Label(self.ctc, text="9934-9804", font=("Times New Roman", 12), bg="lightblue")
        self.lblnum3.place(x=170, y=205)

        #Boton, regresar a pantalla principal
        self.btnctc=Button(self.ctc,text="Regresar",height=1,width=10,font=("Times New Roman", 12),command=self.regresarTres)
        self.btnctc.place(x=170,y=250)

    #Metodo destruir ventana, Contactanos
    def regresarTres(self):
        self.ctc.destroy()
    #Ventana,Gestion-Alumnos
    def alumnos(self):
        self.alum = Toplevel(self.venInfo)
        self.alum.geometry("450x320")
        self.alum.title("Alumnos")
        self.alum.config(bg="lightblue")
        self.alum.iconbitmap("UNAH-version-horizontal.ico")

        self.lblalum = Label(
        self.alum,
        text="A continuación se le presenta una serie de botones que le permitirá manejar las distintas consultas",
        font=("Times New Roman", 14),
        bg="lightblue",
        wraplength=450,
        justify="center"
        )
        self.lblalum.place(x=10, y=30)

        #Botones para manejar consultas
        self.btnalum=Button(self.alum,text="Ingresar",height=1,width=10,font=("Times New Roman", 12),command=self.ingresarA)
        self.btnalum.place(x=100,y=100)

        self.btnalum2=Button(self.alum,text="Actualizar",height=1,width=10,font=("Times New Roman", 12),command=self.actualizarA)
        self.btnalum2.place(x=240,y=100)

        self.btnalum3=Button(self.alum,text="Eliminar",height=1,width=10,font=("Times New Roman", 12),command=self.eliminarA)
        
        self.btnalum3.place(x=170,y=180)
        
        

    #Metodos de consultas-Alumnos
    def ingresarA(self):
        self.VenIngresarA = Toplevel(self.venInfo)
        self.VenIngresarA.geometry("830x320+300+300")
        self.VenIngresarA.title("Tabla Estudiantes_Ingresar Datos")
        self.VenIngresarA.config(bg="lightblue")
        self.VenIngresarA.iconbitmap("UNAH-version-horizontal.ico")

        #Entry y Label para ID
        self.lblIngresarIDA=Label(self.VenIngresarA, text="ID del estudiante:", bg="lightblue", font=("Time New Roman", 12)).place(x=40,y=60)

        self.vIngresarIDA=IntVar()
        self.txtIngresarIDA=Entry(self.VenIngresarA, width=25, textvariable=self.vIngresarIDA)
        self.txtIngresarIDA.place(x=230, y=60)

        #Entry y Label para Nombre
        self.lblIngresarNombreA=Label(self.VenIngresarA, text="Nombre del estudiante:", bg="lightblue", font=("Time New Roman", 12)).place(x=40,y=90)

        self.vIngresarNombreA=StringVar()
        self.txtIngresarNombreA=Entry(self.VenIngresarA, width=25, textvariable=self.vIngresarNombreA)
        self.txtIngresarNombreA.place(x=230, y=90)

        #Entry y Label para Apellido
        self.lblIngresarApellidoA=Label(self.VenIngresarA, text="Apellido del estudiante:", bg="lightblue", font=("Time New Roman", 12)).place(x=40,y=120)

        self.vIngresarApellidoA=StringVar()
        self.txtIngresarApellidoA=Entry(self.VenIngresarA, width=25, textvariable=self.vIngresarApellidoA)
        self.txtIngresarApellidoA.place(x=230, y=120)

        #Entry y Label para Telefono
        self.lblIngresarTelefonoA=Label(self.VenIngresarA, text="Teléfono del estudiante:", bg="lightblue", font=("Time New Roman", 12)).place(x=40,y=150)

        self.vIngresarTelefonoA=StringVar()
        self.txtIngresarTelefonoA=Entry(self.VenIngresarA, width=25, textvariable=self.vIngresarTelefonoA)
        self.txtIngresarTelefonoA.place(x=230, y=150)

        #Entry y Label para Direccion
        self.lblIngresarDireccionA=Label(self.VenIngresarA, text="Dirección del estudiante:", bg="lightblue", font=("Time New Roman", 12)).place(x=40,y=180)

        self.vIngresarDireccionA=StringVar()
        self.txtIngresarDireccionA=Entry(self.VenIngresarA, width=25, textvariable=self.vIngresarDireccionA)
        self.txtIngresarDireccionA.place(x=230, y=180)

        #Boton para Ingresar Datos a la Base de Datos
        self.btnIngresarA=Button(self.VenIngresarA, text="Ingresar Alumno", font=("Times New Roman", 14), command=self.Alumno_Ingresar)
        self.btnIngresarA.place(x=160, y=230)
        
        #Reporte en Pantalla
        self.treeIngresarA=ttk.Treeview(self.VenIngresarA, columns=("#1","#2","#3","#4"), height=10)
        self.treeIngresarA.place(x=420, y=55)
        self.treeIngresarA.heading("#0", text="ID", anchor=CENTER)
        self.treeIngresarA.heading("#1", text="Nombre", anchor=CENTER)
        self.treeIngresarA.heading("#2", text="Apellido", anchor=CENTER)
        self.treeIngresarA.heading("#3", text="Telefono", anchor=CENTER)
        self.treeIngresarA.heading("#4", text="Dirección", anchor=CENTER)
        
        #Ancho de cada columna
        self.treeIngresarA.column("#0", width=30, anchor=CENTER)
        self.treeIngresarA.column("#1", width=75, anchor=CENTER)
        self.treeIngresarA.column("#2", width=75, anchor=CENTER)
        self.treeIngresarA.column("#3", width=70, anchor=CENTER)
        self.treeIngresarA.column("#4", width=130, anchor=CENTER)
        
        #Cargar los datos en el reporte
        self.cargar_datos_alumnos()


    #Funcion para agregar alumno a base de datos   
    def Alumno_Ingresar(self):
        self.conectorBD()
        #Recolectar todas las variables
        ida=self.vIngresarIDA.get()
        nom=self.vIngresarNombreA.get()
        ape=self.vIngresarApellidoA.get()
        tel=self.vIngresarTelefonoA.get()
        dire=self.vIngresarDireccionA.get()
        
        #Validar que el registro no existe
        self.cursor.execute(f"select count(*) from Estudiantes where ID_Alumno={ida}")
        va=self.cursor.fetchone()
        if va[0]>0:
            ca.showerror("Eror","Ese ID ya existe")
        else:     
            #Agregar los datos a la base de datos
            self.cursor.execute(f"""insert into Estudiantes
                           (ID_Alumno, Nombre, Apellido, Telefono, Direccion) values 
                           ({ida},'{nom}','{ape}',{tel},'{dire}')""")
            self.conexion.commit()
            
        #Para actualizar los datos del treeview
        self.cargar_datos_alumnos()

    
    #Funcion para cargar los datos al treeview
    def cargar_datos_alumnos(self):
        self.conectorBD()
    
        # Limpiar el treeview antes de cargar los nuevos datos
        for item in self.treeIngresarA.get_children():
            self.treeIngresarA.delete(item)
    
        # Obtener los datos de la base de datos
        self.cursor.execute("SELECT ID_Alumno, Nombre, Apellido, Telefono, Direccion FROM Estudiantes")
        registros = self.cursor.fetchall()
    
        # Insertar los datos en el treeview
        for fila in registros:
            id_alumno, nombre, apellido, telefono, direccion = fila
            self.treeIngresarA.insert("", "end", text=id_alumno, values=(nombre, apellido, telefono, direccion))
    

    def actualizarA(self):
        self.VenActualizarA = Toplevel(self.venInfo)
        self.VenActualizarA.geometry("450x320+300+300")
        self.VenActualizarA.title("Tabla Estudiantes_Actualizar Datos")
        self.VenActualizarA.config(bg="lightblue")
        self.VenActualizarA.iconbitmap("UNAH-version-horizontal.ico")

        #Entry y Label para ID alumno
        self.lblActualizarNombreA=Label(self.VenActualizarA, text="ID de alumno:", bg="lightblue", font=("Time New Roman", 12)).place(x=40,y=60)

        self.vActualizarNombreA=IntVar()
        self.txtActualizarNombreA=Entry(self.VenActualizarA, width=25, textvariable=self.vActualizarNombreA)
        self.txtActualizarNombreA.place(x=230, y=60)

        
        #Boton para Actualizar Datos a la Base de Datos
        self.btnActualizarA=Button(self.VenActualizarA, text="Actualizar Clase", font=("Times New Roman", 14), command=self.Alumno_Actualizar)
        self.btnActualizarA.place(x=160, y=110)
        
    #Funcion para Actualizar Alumno de base de datos
    def Alumno_Actualizar(self):
        ida = self.vActualizarNombreA.get()
        nom = ci.askstring("Actualizar Nombre", "Ingrese el nuevo nombre:")
        ape = ci.askstring("Actualizar Apellido", "Ingrese el nuevo apellido:")
        tel = ci.askstring("Actualizar Teléfono", "Ingrese el nuevo teléfono:")
        dire = ci.askstring("Actualizar Dirección", "Ingrese la nueva dirección:")
    
        if not ida or not nom or not ape or not tel or not dire:
            ca.showerror("Error", "Todos los campos deben estar llenos")
            return   
        self.conectorBD()
        self.cursor.execute(f"SELECT count(*) FROM Estudiantes WHERE ID_Alumno = {ida}")
        existe = self.cursor.fetchone()[0]
    
        if existe == 0:
            ca.showerror("Error", "El ID del estudiante no existe")
            return
        try:
            self.cursor.execute(f"""
                UPDATE Estudiantes
                SET Nombre = '{nom}',
                    Apellido = '{ape}',
                    Telefono = {tel},
                    Direccion = '{dire}'
                WHERE ID_Alumno = {ida}
            """)
            self.conexion.commit()
            ca.showinfo("Éxito", "Datos actualizados correctamente")
            self.cargar_datos_alumnos()
        except Exception as e:
            print("")


    def eliminarA(self):
        self.VenEliminarA = Toplevel(self.venInfo)
        self.VenEliminarA.geometry("350x200+300+300")
        self.VenEliminarA.title("Tabla Estudiantes_Eliminar Datos")
        self.VenEliminarA.config(bg="lightblue")
        self.VenEliminarA.iconbitmap("UNAH-version-horizontal.ico")

        #Entry y Label para Id estudiante
        self.lblEliminarIDA=Label(self.VenEliminarA, text="Id del estudiante:", bg="lightblue", font=("Time New Roman", 12)).place(x=40,y=60)

        self.vEliminarIDA=IntVar()
        self.txtEliminarIDA=Entry(self.VenEliminarA, width=15, textvariable=self.vEliminarIDA)
        self.txtEliminarIDA.place(x=230, y=60)

        
        #Boton para Eliminar Datos a la Base de Datos
        self.btnEliminarA=Button(self.VenEliminarA, text="Eliminar Alumno", font=("Times New Roman", 14), command=self.Alumno_Eliminar)
        self.btnEliminarA.place(x=120, y=110)
        
        
    #Funcion para eliminar alumno a base de datos   
    def Alumno_Eliminar(self):
        ida = self.vEliminarIDA.get() 
        #Confirmacion antes de eliminar
        confirmar = ca.askyesno("Eliminar Estudiante", "¿Está seguro de eliminar este estudiante?")
        if not confirmar:
            return 
        self.conectorBD()
        self.cursor.execute(f"SELECT count(*) FROM Estudiantes WHERE ID_Alumno = {ida}")
        existe = self.cursor.fetchone()[0]
        
        #Validar que el registro existe
        if existe == 0:
            ca.showerror("Error", "El ID del estudiante no existe")
            return   
        try:
            self.cursor.execute(f"DELETE FROM Estudiantes WHERE ID_Alumno = {ida}")
            self.conexion.commit()
            ca.showinfo("Eliminado", "Estudiante eliminado correctamente")
            self.cargar_datos_alumnos()
        except Exception as e:
            print("")


    #Ventana,Gestion-Maestros
    def maestros(self):
        self.maes = Toplevel(self.venInfo)
        self.maes.geometry("450x320")
        self.maes.title("Maestros")
        self.maes.config(bg="lightblue")
        self.maes.iconbitmap("UNAH-version-horizontal.ico")

        self.lblmaes = Label(
        self.maes,
        text="A continuación se le presenta una serie de botones que le permitirá manejar las distintas consultas",
        font=("Times New Roman", 14),
        bg="lightblue",
        wraplength=450,
        justify="center"
        )
        self.lblmaes.place(x=10, y=30)

        #Botones para manejar consultas
        self.btnmaes=Button(self.maes,text="Ingresar",height=1,width=10,font=("Times New Roman", 12),command=self.ingresarM)
        self.btnmaes.place(x=100,y=100)

        self.btnmaes2=Button(self.maes,text="Actualizar",height=1,width=10,font=("Times New Roman", 12),command=self.actualizarM)
        self.btnmaes2.place(x=240,y=100)

        self.btnmaes3=Button(self.maes,text="Eliminar",height=1,width=10,font=("Times New Roman", 12),command=self.eliminarM)
        self.btnmaes3.place(x=170,y=180)
   
   
   #Metodos de consultas-Maestros
    def ingresarM(self):
        self.VenIngresarM = Toplevel(self.venInfo)
        self.VenIngresarM.geometry("800x320+300+300")
        self.VenIngresarM.title("Tabla Maestros_Ingresar Datos")
        self.VenIngresarM.config(bg="lightblue")
        self.VenIngresarM.iconbitmap("UNAH-version-horizontal.ico")
        
        #Entry y Label para ID
        self.lblIngresarIDM=Label(self.VenIngresarM, text="ID del estudiante:", bg="lightblue", font=("Time New Roman", 12)).place(x=40,y=60)

        self.vIngresarIDM=IntVar()
        self.txtIngresarIDM=Entry(self.VenIngresarM, width=25, textvariable=self.vIngresarIDM)
        self.txtIngresarIDM.place(x=230, y=60)

        #Entry y Label para Nombre
        self.lblIngresarNombreM=Label(self.VenIngresarM, text="Nombre del Maestro:", bg="lightblue", font=("Time New Roman", 12)).place(x=40,y=90)

        self.vIngresarNombreM=StringVar()
        self.txtIngresarNombreM=Entry(self.VenIngresarM, width=25, textvariable=self.vIngresarNombreM)
        self.txtIngresarNombreM.place(x=230, y=90)

        #Entry y Label para Apellido
        self.lblIngresarApellidoM=Label(self.VenIngresarM, text="Apellido del Maestro:", bg="lightblue", font=("Time New Roman", 12)).place(x=40,y=120)

        self.vIngresarApellidoM=StringVar()
        self.txtIngresarApellidoM=Entry(self.VenIngresarM, width=25, textvariable=self.vIngresarApellidoM)
        self.txtIngresarApellidoM.place(x=230, y=120)

        #Entry y Label para Telefono
        self.lblIngresarTelefonoM=Label(self.VenIngresarM, text="Teléfono del Maestro:", bg="lightblue", font=("Time New Roman", 12)).place(x=40,y=150)

        self.vIngresarTelefonoM=IntVar()
        self.txtIngresarTelefonoM=Entry(self.VenIngresarM, width=25, textvariable=self.vIngresarTelefonoM)
        self.txtIngresarTelefonoM.place(x=230, y=150)

        #Entry y Label para Direccion
        self.lblIngresarDireccionM=Label(self.VenIngresarM, text="Dirección del Maestro:", bg="lightblue", font=("Time New Roman", 12)).place(x=40,y=180)

        self.vIngresarDireccionM=StringVar()
        self.txtIngresarDireccionM=Entry(self.VenIngresarM, width=25, textvariable=self.vIngresarDireccionM)
        self.txtIngresarDireccionM.place(x=230, y=180)

        #Boton para Ingresar Datos a la Base de Datos
        self.btnIngresarM=Button(self.VenIngresarM, text="Ingresar Maestro", font=("Times New Roman", 14), command=self.Maestro_Ingresar)
        self.btnIngresarM.place(x=160, y=230)
        
        #Reporte de Maestros
        self.treeIngresarM=ttk.Treeview(self.VenIngresarM, columns=("#1","#2","#3","#4"), height=10)
        self.treeIngresarM.place(x=420, y=55)
        self.treeIngresarM.heading("#0", text="ID", anchor=CENTER)
        self.treeIngresarM.heading("#1", text="Nombre", anchor=CENTER)
        self.treeIngresarM.heading("#2", text="Apellido", anchor=CENTER)
        self.treeIngresarM.heading("#3", text="Telefono", anchor=CENTER)
        self.treeIngresarM.heading("#4", text="Dirección", anchor=CENTER)
        
        #Ancho de cada columna
        self.treeIngresarM.column("#0", width=30, anchor=CENTER)
        self.treeIngresarM.column("#1", width=75, anchor=CENTER)
        self.treeIngresarM.column("#2", width=75, anchor=CENTER)
        self.treeIngresarM.column("#3", width=70, anchor=CENTER)
        self.treeIngresarM.column("#4", width=90, anchor=CENTER)
        
        #Llamar a la funcion para los datos del treeview
        self.cargar_datos_maestros()
        
        
    #Funcion para meter los datos al treeview
    def cargar_datos_maestros(self):
        self.conectorBD()
        self.cursor.execute("SELECT * FROM Maestros")
        datos = self.cursor.fetchall()
    
        # Limpiar el Treeview antes de cargar nuevos datos
        for item in self.treeIngresarM.get_children():
            self.treeIngresarM.delete(item)
    
        # Insertar datos actualizados
        for fila in datos:
            self.treeIngresarM.insert("", END, text=fila[0], values=(fila[1], fila[2], fila[3], fila[4]))

        
    #Funcion para ingresar maestro a base de datos
    def Maestro_Ingresar(self):
        self.conectorBD()
        
        #Recolectar todas las variables
        ida=self.vIngresarIDM.get()
        nom=self.vIngresarNombreM.get()
        ape=self.vIngresarApellidoM.get()
        tel=self.vIngresarTelefonoM.get()
        dire=self.vIngresarDireccionM.get()
        
        #Validar que el registro no existe
        self.cursor.execute(f"select count(*) from Maestros where ID_Maestro={ida}")
        va=self.cursor.fetchone()
        if va[0]>0:
            ca.showerror("Eror","Ese ID ya existe")
        else:
            #Agregar los datos a la base de datos
            self.cursor.execute(f"""insert into Maestros
                           (ID_Maestro, Nombre, Apellido, Telefono, Direccion) values 
                           ({ida},'{nom}','{ape}',{tel},'{dire}')""")
            self.conexion.commit()
            ca.showinfo("Registrado","Registro agregado correctamente")
        
        #Funcion para actualizar los datos en el reporte
        self.cargar_datos_maestros()


    def actualizarM(self):
        self.VenActualizarM = Toplevel(self.venInfo)
        self.VenActualizarM.geometry("420x220+300+300")
        self.VenActualizarM.title("Tabla Clases_Actualizar Datos")
        self.VenActualizarM.config(bg="lightblue")
        self.VenActualizarM.iconbitmap("UNAH-version-horizontal.ico")

        #Entry y Label para Nombre
        self.lblActualizarNombreM=Label(self.VenActualizarM, text="ID de maestro:", bg="lightblue", font=("Time New Roman", 12)).place(x=40,y=60)

        self.vActualizarNombreM=IntVar()
        self.txtActualizarNombreM=Entry(self.VenActualizarM, width=25, textvariable=self.vActualizarNombreM)
        self.txtActualizarNombreM.place(x=230, y=60)

        
        #Boton para Actualizar Datos a la Base de Datos
        self.btnActualizarM=Button(self.VenActualizarM, text="Actualizar Maestro", font=("Times New Roman", 14), command=self.Maestro_Actualizar)
        self.btnActualizarM.place(x=160, y=110)
    #Funcion para Actualizar maestro de base de datos
    def Maestro_Actualizar(self):
        idm = self.vActualizarNombreM.get()
        #Pedir todos los nuevos datos
        nom = ci.askstring("Nombre", "Nuevo nombre del maestro:")
        ape = ci.askstring("Apellido", "Nuevo apellido del maestro:")
        tel = ci.askstring("Teléfono", "Nuevo teléfono del maestro:")
        dire = ci.askstring("Dirección", "Nueva dirección del maestro:")
        #Validar que los campos no esten vacios
        if not idm or not nom or not ape or not tel or not dire:
            ca.showerror("Error", "Todos los campos son obligatorios")
            return    
        self.conectorBD()
        self.cursor.execute(f"SELECT count(*) FROM Maestros WHERE ID_Maestro={idm}")
        if self.cursor.fetchone()[0] == 0:
            ca.showerror("Error", "ID no existe")
            return
        self.cursor.execute(f"""
            UPDATE Maestros SET 
            Nombre='{nom}', Apellido='{ape}', Telefono='{tel}', Direccion='{dire}'
            WHERE ID_Maestro={idm}
        """)
        self.conexion.commit()
        ca.showinfo("Éxito", "Maestro actualizado")
        self.cargar_datos_maestros()


    def eliminarM(self):
        self.VenEliminarM = Toplevel(self.venInfo)
        self.VenEliminarM.geometry("350x200+300+300")
        self.VenEliminarM.title("Tabla Maestros_Eliminar Datos")
        self.VenEliminarM.config(bg="lightblue")
        self.VenEliminarM.iconbitmap("UNAH-version-horizontal.ico")

        #Entry y Label para Id maestro
        self.lblEliminarIDM=Label(self.VenEliminarM, text="Id del maestro:", bg="lightblue", font=("Time New Roman", 12)).place(x=40,y=60)

        self.vEliminarIDM=IntVar()
        self.txtEliminarIDM=Entry(self.VenEliminarM, width=15, textvariable=self.vEliminarIDM)
        self.txtEliminarIDM.place(x=230, y=60)

        
        #Boton para Eliminar Datos a la Base de Datos
        self.btnEliminarM=Button(self.VenEliminarM, text="Eliminar Maestro", font=("Times New Roman", 14), command=self.Maestro_Eliminar)
        self.btnEliminarM.place(x=120, y=110)
        
    #Funcion para eliminar maestro a base de datos   
    def Maestro_Eliminar(self):
        idm = self.vEliminarIDM.get()
        self.conectorBD()
        self.cursor.execute(f"SELECT count(*) FROM Maestros WHERE ID_Maestro={idm}")
        if self.cursor.fetchone()[0] == 0:
            ca.showerror("Error", "ID no existe")
            return
        confirmar = ca.askyesno("Confirmar", "¿Estás seguro que deseas eliminar este maestro?")
        if confirmar:
            self.cursor.execute(f"DELETE FROM Maestros WHERE ID_Maestro={idm}")
            self.conexion.commit()
            ca.showinfo("Eliminado", "Registro eliminado correctamente")
            self.cargar_datos_maestros()


    #Ventana,Gestion-Clases
    def clases(self):
        self.clas = Toplevel(self.venInfo)
        self.clas.geometry("450x320")
        self.clas.title("Clases")
        self.clas.config(bg="lightblue")
        self.clas.iconbitmap("UNAH-version-horizontal.ico")

        self.lblclas = Label(
        self.clas,
        text="A continuación se le presenta una serie de botones que le permitirá manejar las distintas consultas",
        font=("Times New Roman", 14),
        bg="lightblue",
        wraplength=450,
        justify="center"
        )
        self.lblclas.place(x=10, y=30)

        #Botones para manejar consultas
        self.btnclas=Button(self.clas,text="Ingresar",height=1,width=10,font=("Times New Roman", 12),command=self.ingresarC)
        self.btnclas.place(x=100,y=100)

        self.btnclas2=Button(self.clas,text="Actualizar",height=1,width=10,font=("Times New Roman", 12),command=self.actualizarC)
        self.btnclas2.place(x=240,y=100)

        self.btnclas=Button(self.clas,text="Eliminar",height=1,width=10,font=("Times New Roman", 12),command=self.eliminarC)
        self.btnclas.place(x=170,y=180)
        
        
    
    #Cargar datos al treeview
    def cargar_datos_clase(self):
        self.conectorBD()
        self.cursor.execute("SELECT * FROM Clases")
        datos = self.cursor.fetchall()
        # Limpiar Treeview antes de agregar
        for x in self.treeIngresarC.get_children():
            self.treeIngresarC.delete(x)
        # Agregar los datos
        for fila in datos:
            self.treeIngresarC.insert("", END, text=fila[0], values=(fila[1],))

        
    #Metodos de consultas-Clases
    def ingresarC(self):
        self.VenIngresarC = Toplevel(self.venInfo)
        self.VenIngresarC.geometry("800x220+300+300")
        self.VenIngresarC.title("Tabla Clases_Ingresar Datos")
        self.VenIngresarC.config(bg="lightblue")
        self.VenIngresarC.iconbitmap("UNAH-version-horizontal.ico")
        
        #Entry y Label para ID de clase
        self.lblIngresarIDC=Label(self.VenIngresarC, text="ID de la clase:", bg="lightblue", font=("Time New Roman", 12)).place(x=40,y=60)

        self.vIngresarIDC=IntVar()
        self.txtIngresarIDC=Entry(self.VenIngresarC, width=25, textvariable=self.vIngresarIDC)
        self.txtIngresarIDC.place(x=230, y=60)

        #Entry y Label para Nombre de clase
        self.lblIngresarNombreC=Label(self.VenIngresarC, text="Nombre de la clase:", bg="lightblue", font=("Time New Roman", 12)).place(x=40,y=90)

        self.vIngresarNombreC=StringVar()
        self.txtIngresarNombreC=Entry(self.VenIngresarC, width=25, textvariable=self.vIngresarNombreC)
        self.txtIngresarNombreC.place(x=230, y=90)

        
        #Boton para Ingresar Datos a la Base de Datos
        self.btnIngresarC=Button(self.VenIngresarC, text="Ingresar Clase", font=("Times New Roman", 14), command=self.Clase_Ingresar)
        self.btnIngresarC.place(x=160, y=140)
        
        #Reporte en Pantalla
        self.treeIngresarC=ttk.Treeview(self.VenIngresarC, columns=("#1"), height=5)
        self.treeIngresarC.place(x=420, y=55)
        self.treeIngresarC.heading("#0", text="ID Clase", anchor=CENTER)
        self.treeIngresarC.heading("#1", text="Nombre de Clase", anchor=CENTER)
        
        
        #Ancho de cada columna
        self.treeIngresarC.column("#0", width=100, anchor=CENTER)
        self.treeIngresarC.column("#1", width=200, anchor=CENTER)
        
        #Para que el treeview muestre los datos
        self.cargar_datos_clase()
        
        
    #Funcion para ingresar clase a base de datos
    def Clase_Ingresar(self):
        self.conectorBD()
        #Recolectar todas las variables
        ida=self.vIngresarIDC.get()
        nom=self.vIngresarNombreC.get()
        
        #Validar que el registro no existe
        self.cursor.execute(f"select count(*) from Clases where ID_Clase={ida}")
        va=self.cursor.fetchone()
        if va[0]>0:
            ca.showerror("Eror","Ese ID ya existe")
        else:     
            #Agregar los datos a la base de datos
            self.cursor.execute(f"""insert into Clases
                           (ID_Clase, Nombre_Clase) values 
                           ({ida},'{nom}')""")
            self.conexion.commit()
            ca.showinfo("Registrado","Registro agregado correctamente")
        
        #LLamar a la funcion para que se actualicen los datos del treeview
        self.cargar_datos_clase()


    def actualizarC(self):
        self.VenActualizarC = Toplevel(self.venInfo)
        self.VenActualizarC.geometry("420x220+300+300")
        self.VenActualizarC.title("Tabla Clases_Actualizar Datos")
        self.VenActualizarC.config(bg="lightblue")
        self.VenActualizarC.iconbitmap("UNAH-version-horizontal.ico")

        #Entry y Label para Id clase
        self.lblActualizarNombreC=Label(self.VenActualizarC, text="ID de la clase:", bg="lightblue", font=("Time New Roman", 12)).place(x=40,y=60)

        self.vActualizarNombreC=IntVar()
        self.txtActualizarNombreC=Entry(self.VenActualizarC, width=25, textvariable=self.vActualizarNombreC)
        self.txtActualizarNombreC.place(x=230, y=60)

        
        #Boton para Actualizar Datos a la Base de Datos
        self.btnActualizarC=Button(self.VenActualizarC, text="Actualizar Clase", font=("Times New Roman", 14), command=self.Clase_Actualizar)
        self.btnActualizarC.place(x=160, y=110)
    #Funcion para Actualizar clase a base de datos
    def Clase_Actualizar(self):
        self.conectorBD()
        ida = self.vActualizarNombreC.get()
    
        # Verificar si el ID existe
        self.cursor.execute(f"SELECT count(*) FROM Clases WHERE ID_Clase={ida}")
        va = self.cursor.fetchone()[0]
        if va == 0:
            ca.showerror("Error", "No existe ninguna clase con ese ID")
            return
        nuevo_nombre = ci.askstring("Nuevo Nombre", "Ingrese el nuevo nombre para la clase:")
        #Validar que se ingresaron datos
        if nuevo_nombre:
            self.cursor.execute(f"UPDATE Clases SET Nombre_Clase='{nuevo_nombre}' WHERE ID_Clase={ida}")
            self.conexion.commit()
            ca.showinfo("Actualizado", "La clase se actualizó correctamente")
        else:
            ca.showwarning("Cancelado", "No se ingresó ningún nombre nuevo")



    def eliminarC(self):
        self.VenEliminarC = Toplevel(self.venInfo)
        self.VenEliminarC.geometry("350x200+300+300")
        self.VenEliminarC.title("Tabla Clases_Eliminar Datos")
        self.VenEliminarC.config(bg="lightblue")
        self.VenEliminarC.iconbitmap("UNAH-version-horizontal.ico")

        #Entry y Label para id clase
        self.lblEliminarIDC=Label(self.VenEliminarC, text="Id de la clase:", bg="lightblue", font=("Time New Roman", 12)).place(x=40,y=60)

        self.vEliminarIDC=IntVar()
        self.txtEliminarIDC=Entry(self.VenEliminarC, width=15, textvariable=self.vEliminarIDC)
        self.txtEliminarIDC.place(x=230, y=60)

        
        #Boton para Eliminar Datos a la Base de Datos
        self.btnEliminarC=Button(self.VenEliminarC, text="Eliminar Clase", font=("Times New Roman", 14), command=self.Clase_Eliminar)
        self.btnEliminarC.place(x=120, y=110)
        
        
    #Funcion para eliminar clase de base de datos   
    def Clase_Eliminar(self):
        self.conectorBD()
        ida = self.vEliminarIDC.get()
    
        # Verificar si el ID existe
        self.cursor.execute(f"SELECT count(*) FROM Clases WHERE ID_Clase={ida}")
        existe = self.cursor.fetchone()[0]
    
        if existe == 0:
            ca.showerror("Error", "No existe ninguna clase con ese ID")
            return
    
        confirmar = ca.askyesno("Eliminar Clase", f"¿Está seguro de eliminar la clase con ID {ida}?")
        if confirmar:
            self.cursor.execute(f"DELETE FROM Clases WHERE ID_Clase={ida}")
            self.conexion.commit()
            ca.showinfo("Eliminado", "Clase eliminada correctamente")
            self.cargarClasesTreeview()
        else:
            ca.showinfo("Cancelado", "No se eliminó ninguna clase")
            
            
    #Ventana, Gestion-seccion
    def seccion(self):
        self.sec = Toplevel(self.venInfo)
        self.sec.geometry("450x320")
        self.sec.title("Secciones")
        self.sec.config(bg="lightblue")
        self.sec.iconbitmap("UNAH-version-horizontal.ico")

        self.lblsec = Label(
        self.sec,
        text="A continuación se le presenta una serie de botones que le permitirá manejar las distintas consultas",
        font=("Times New Roman", 14),
        bg="lightblue",
        wraplength=450,
        justify="center"
        )
        self.lblsec.place(x=10, y=30)

        #Botones para manejar consultas
        self.btnsec=Button(self.sec,text="Ingresar",height=1,width=10,font=("Times New Roman", 12),command=self.ingresarS)
        self.btnsec.place(x=100,y=100)

        self.btnsec2=Button(self.sec,text="Actualizar",height=1,width=10,font=("Times New Roman", 12),command=self.actualizarS)
        self.btnsec2.place(x=240,y=100)

        self.btnsec3=Button(self.sec,text="Eliminar",height=1,width=10,font=("Times New Roman", 12),command=self.eliminarS)
        self.btnsec3.place(x=170,y=180)

    #Metodos de consultas-Seccion
    def ingresarS(self):
        self.VenIngresarS = Toplevel(self.venInfo)
        self.VenIngresarS.geometry("800x320+300+300")
        self.VenIngresarS.title("Tabla Secciones_Ingresar Datos")
        self.VenIngresarS.config(bg="lightblue")
        self.VenIngresarS.iconbitmap("UNAH-version-horizontal.ico")

        #Entry y Label para ID Seccion
        self.lblIngresarNombreS=Label(self.VenIngresarS, text="ID de la sección:", bg="lightblue", font=("Time New Roman", 12)).place(x=40,y=60)

        self.vIngresarIDSeccionS=IntVar()
        self.txtIngresarIDSeccionS=Entry(self.VenIngresarS, width=25, textvariable=self.vIngresarIDSeccionS)
        self.txtIngresarIDSeccionS.place(x=230, y=60)

        #Entry y Label para ID Docente
        self.lblIngresarIDDocenteS=Label(self.VenIngresarS, text="ID del docente:", bg="lightblue", font=("Time New Roman", 12)).place(x=40,y=90)

        self.vIngresarIDDocenteS=IntVar()
        self.txtIngresarIDDocenteS=Entry(self.VenIngresarS, width=25, textvariable=self.vIngresarIDDocenteS)
        self.txtIngresarIDDocenteS.place(x=230, y=90)

        #Entry y Label para ID Clase
        self.lblIngresarClaseS=Label(self.VenIngresarS, text="ID de la clase:", bg="lightblue", font=("Time New Roman", 12)).place(x=40,y=120)

        self.vIngresarIDClaseS=IntVar()
        self.txtIngresarIDClaseS=Entry(self.VenIngresarS, width=25, textvariable=self.vIngresarIDClaseS)
        self.txtIngresarIDClaseS.place(x=230, y=120)

        #Entry y Label para Hora Inicio
        self.lblIngresarHoraInicioS=Label(self.VenIngresarS, text="Hora de inicio:", bg="lightblue", font=("Time New Roman", 12)).place(x=40,y=150)

        self.vIngresarHoraInicioS=StringVar()
        self.txtIngresarHoraInicioS=Entry(self.VenIngresarS, width=25, textvariable=self.vIngresarHoraInicioS)
        self.txtIngresarHoraInicioS.place(x=230, y=150)

        #Entry y Label para Hora Fin
        self.lblIngresarHoraFinS=Label(self.VenIngresarS, text="Hora de fin:", bg="lightblue", font=("Time New Roman", 12)).place(x=40,y=180)

        self.vIngresarHoraSalidaS=StringVar()
        self.txtIngresarHoraSalidaS=Entry(self.VenIngresarS, width=25, textvariable=self.vIngresarHoraSalidaS)
        self.txtIngresarHoraSalidaS.place(x=230, y=180)
        #Boton para Ingresar Datos a la Base de Datos
        self.btnIngresarS=Button(self.VenIngresarS, text="Ingresar Sección", font=("Times New Roman", 14), command=self.Sección_Ingresar)
        self.btnIngresarS.place(x=160, y=220)
        
        #Reporte en Pantalla
        self.treeIngresarS=ttk.Treeview(self.VenIngresarS, columns=("#1","#2","#3","#4"), height=10)
        self.treeIngresarS.place(x=420, y=55)
        self.treeIngresarS.heading("#0", text="ID Seccion", anchor=CENTER)
        self.treeIngresarS.heading("#1", text="ID Docente", anchor=CENTER)
        self.treeIngresarS.heading("#2", text="ID Clase", anchor=CENTER)
        self.treeIngresarS.heading("#3", text="Hora Inicio", anchor=CENTER)
        self.treeIngresarS.heading("#4", text="Hora Fin", anchor=CENTER)
        
        #Ancho de cada columna
        self.treeIngresarS.column("#0", width=75, anchor=CENTER)
        self.treeIngresarS.column("#1", width=75, anchor=CENTER)
        self.treeIngresarS.column("#2", width=75, anchor=CENTER)
        self.treeIngresarS.column("#3", width=70, anchor=CENTER)
        self.treeIngresarS.column("#4", width=75, anchor=CENTER)
        
        #Llamar a la funcion para cargar el treeview
        self.cargar_datos_secciones()
    
    
    #Funcion para cargar los datos al treeview
    def cargar_datos_secciones(self):
        self.conectorBD()
        self.cursor.execute("SELECT * FROM Secciones")
        datos = self.cursor.fetchall()
    
        for x in self.treeIngresarS.get_children():
            self.treeIngresarS.delete(x)
    
        for fila in datos:
            self.treeIngresarS.insert("", END, text=fila[0], values=(fila[1], fila[2], fila[3], fila[4]))

    
    #Funcion para ingresar sección a base de datos
    def Sección_Ingresar(self):
        self.conectorBD()
        #Recolectar todas las variables
        ids=self.vIngresarIDSeccionS.get()
        idd=self.vIngresarIDDocenteS.get()
        cla=self.vIngresarIDClaseS.get()
        ini=self.vIngresarHoraInicioS.get()
        sal=self.vIngresarHoraSalidaS.get()
        
        #Validar que el registro no existe
        self.cursor.execute(f"select count(*) from Secciones where ID_Seccion={ids}")
        va=self.cursor.fetchone()
        if va[0]>0:
            ca.showerror("Eror","Ese ID ya existe")
        else:     
            #Agregar los datos a la base de datos
            self.cursor.execute(f"""insert into Secciones
                           (ID_Seccion, ID_Docente, ID_Clase, Hora_Inicio, Hora_Fin) values 
                           ({ids},{idd},{cla},'{ini}','{sal}')""")
            self.conexion.commit()
            ca.showinfo("Registrado","Registro agregado corectamente")
            
        #Funcion para actualizar los datos en el treeview
        self.cargar_datos_secciones()
        
    
    #Ventana para Actualizar los datos
    def actualizarS(self):
        self.VenActualizarS = Toplevel(self.venInfo)
        self.VenActualizarS.geometry("420x220+300+300")
        self.VenActualizarS.title("Tabla Secciones_Actualizar Datos")
        self.VenActualizarS.config(bg="lightblue")
        self.VenActualizarS.iconbitmap("UNAH-version-horizontal.ico")

        #Entry y Label para id sección
        self.lblActualizarNombreS=Label(self.VenActualizarS, text="ID de la seccion:", bg="lightblue", font=("Time New Roman", 12)).place(x=40,y=60)

        self.vActualizarNombreS=IntVar()
        self.txtActualizarNombreS=Entry(self.VenActualizarS, width=25, textvariable=self.vActualizarNombreS)
        self.txtActualizarNombreS.place(x=230, y=60)

        
        #Boton para Actualizar Datos a la Base de Datos
        self.btnActualizarS=Button(self.VenActualizarS, text="Actualizar Seccion", font=("Times New Roman", 14), command=self.Seccion_Actualizar)
        self.btnActualizarS.place(x=160, y=110)
    #Funcion para Actualizar Seccion a base de datos
    def Seccion_Actualizar(self):
        self.conectorBD()
        ids = self.vActualizarNombreS.get()
    
        # Validar que la sección exista
        self.cursor.execute(f"SELECT count(*) FROM Secciones WHERE ID_Seccion={ids}")
        va = self.cursor.fetchone()[0]
        if va == 0:
            ca.showerror("Error", "No existe ninguna sección con ese ID")
            return
        # Solicitar nuevos valores
        nuevoIDClase = ci.askstring("Nuevo ID Clase", "Ingrese el nuevo ID para la clase:")
        nuevoIDDocente = ci.askstring("Nuevo ID Docente", "Ingrese el nuevo ID para el docente:")
        nuevaHoraInicio = ci.askstring("Hora de inicio", "Ingrese la nueva hora de inicio:")
        nuevaHoraFin = ci.askstring("Hora de fin", "Ingrese la nueva hora de fin:")
        # Validar que no estén vacíos
        if nuevoIDClase and nuevoIDDocente and nuevaHoraInicio and nuevaHoraFin:
            self.cursor.execute(f"""
                UPDATE Secciones SET
                ID_Docente = {nuevoIDDocente},
                ID_Clase = {nuevoIDClase},
                Hora_Inicio = '{nuevaHoraInicio}',
                Hora_Fin = '{nuevaHoraFin}'
                WHERE ID_Seccion = {ids}
            """)
            self.conexion.commit()
            ca.showinfo("Actualizado", "La sección se actualizó correctamente")
            self.cargarSeccionesTreeview()
        else:
            ca.showwarning("Cancelado", "No se actualizaron los datos")


    def eliminarS(self):
        self.VenEliminarS = Toplevel(self.venInfo)
        self.VenEliminarS.geometry("350x200+300+300")
        self.VenEliminarS.title("Tabla Secciones_Eliminar Datos")
        self.VenEliminarS.config(bg="lightblue")
        self.VenEliminarS.iconbitmap("UNAH-version-horizontal.ico")

        #Entry y Label ID Clase
        self.lblEliminarIDS=Label(self.VenEliminarS, text="Id de la clase:", bg="lightblue", font=("Time New Roman", 12)).place(x=40,y=60)

        self.vEliminarIDS=IntVar()
        self.txtEliminarIDS=Entry(self.VenEliminarS, width=15, textvariable=self.vEliminarIDS)
        self.txtEliminarIDS.place(x=230, y=60)

        
        #Boton para Eliminar Datos a la Base de Datos
        self.btnEliminarS=Button(self.VenEliminarS, text="Eliminar Sección", font=("Times New Roman", 14), command=self.Seccion_Eliminar)
        self.btnEliminarS.place(x=120, y=110)
        
    #Funcion para eliminar seccion de base de datos   
    def Seccion_Eliminar(self):
        self.conectorBD()
        ids = self.vEliminarIDS.get()
        
        # Verificar que la sección exista
        self.cursor.execute(f"SELECT count(*) FROM Secciones WHERE ID_Seccion={ids}")
        va = self.cursor.fetchone()[0]
        if va == 0:
            ca.showerror("Error", "No existe ninguna sección con ese ID")
            return
        # Confirmar eliminación
        confirmar = ca.askyesno("Eliminar Sección", f"¿Está seguro de eliminar la sección con ID {ids}?")
        if confirmar:
            self.cursor.execute(f"DELETE FROM Secciones WHERE ID_Seccion = {ids}")
            self.conexion.commit()
            ca.showinfo("Eliminado", "Sección eliminada correctamente")
            self.cargarSeccionesTreeview()
        else:
            ca.showinfo("Cancelado", "No se eliminó ninguna sección")


    #Ventana, Gestion-matricula
    def matricula(self):
        self.mtc = Toplevel(self.venInfo)
        self.mtc.geometry("450x320")
        self.mtc.title("Matricula")
        self.mtc.config(bg="lightblue")
        self.mtc.iconbitmap("UNAH-version-horizontal.ico")

        self.lblmtc = Label(
        self.mtc,
        text="A continuación se le presenta una serie de botones que le permitirá manejar las distintas consultas",
        font=("Times New Roman", 14),
        bg="lightblue",
        wraplength=450,
        justify="center"
        )
        self.lblmtc.place(x=10, y=30)

        #Botones para manejar consultas
        self.btnmtc=Button(self.mtc,text="Ingresar",height=1,width=10,font=("Times New Roman", 12),command=self.ingresarMt)
        self.btnmtc.place(x=100,y=100)

        self.btnmtc2=Button(self.mtc,text="Actualizar",height=1,width=10,font=("Times New Roman", 12),command=self.actualizarMt)
        self.btnmtc2.place(x=240,y=100)

        self.btnmtc3=Button(self.mtc,text="Eliminar",height=1,width=10,font=("Times New Roman", 12),command=self.eliminarMt)
        self.btnmtc3.place(x=170,y=180)
    
    #Funcion para cargar los datos en el treeview
    def cargar_datos_matricula(self):
        self.conectorBD()
    
        # Limpiar Treeview antes de cargar nuevos datos
        for item in self.treeIngresarMT.get_children():
            self.treeIngresarMT.delete(item)
    
        # Obtener datos de la base de datos
        self.cursor.execute("SELECT ID_Matricula, ID_Seccion, ID_Alumno FROM Matricula")
        registros = self.cursor.fetchall()
    
        # Insertarlos al Treeview
        for fila in registros:
            id_matricula, id_seccion, id_alumno = fila
            self.treeIngresarMT.insert("", "end", text=id_matricula, values=(id_seccion, id_alumno))


    #Metodos de consultas-Matricula
    def ingresarMt(self):
        self.VenIngresarMt = Toplevel(self.venInfo)
        self.VenIngresarMt.geometry("750x250+300+300")
        self.VenIngresarMt.title("Tabla Matricula_Ingresar Datos")
        self.VenIngresarMt.config(bg="lightblue")
        self.VenIngresarMt.iconbitmap("UNAH-version-horizontal.ico")
        
        #Entry y Label para ID Seccion
        self.lblIngresarIDMT=Label(self.VenIngresarMt, text="ID de la matricula:", bg="lightblue", font=("Time New Roman", 12)).place(x=40,y=60)

        self.vIngresarIDMT=IntVar()
        self.txtIngresarIDMT=Entry(self.VenIngresarMt, width=25, textvariable=self.vIngresarIDMT)
        self.txtIngresarIDMT.place(x=230, y=60)

        #Entry y Label para ID Seccion
        self.lblIngresarNombreMt=Label(self.VenIngresarMt, text="ID de la sección:", bg="lightblue", font=("Time New Roman", 12)).place(x=40,y=90)

        self.vIngresarIDSeccionMt=IntVar()
        self.txtIngresarIDSeccionMt=Entry(self.VenIngresarMt, width=25, textvariable=self.vIngresarIDSeccionMt)
        self.txtIngresarIDSeccionMt.place(x=230, y=90)

        #Entry y Label para ID Alumno
        self.lblIngresarIDAlumnoMt=Label(self.VenIngresarMt, text="ID de alumno:", bg="lightblue", font=("Time New Roman", 12)).place(x=40,y=120)

        self.vIngresarIDAlumnoMt=IntVar()
        self.txtIngresarIDAlumnoMt=Entry(self.VenIngresarMt, width=25, textvariable=self.vIngresarIDAlumnoMt)
        self.txtIngresarIDAlumnoMt.place(x=230, y=120)

        #Boton para Ingresar Datos a la Base de Datos
        self.btnIngresarMt=Button(self.VenIngresarMt, text="Ingresar Matricula", font=("Times New Roman", 14), command=self.Matricula_Ingresar)
        self.btnIngresarMt.place(x=160, y=180)
        
        #Reporte en Pantalla
        self.treeIngresarMT=ttk.Treeview(self.VenIngresarMt, columns=("#1","#2"), height=4)
        self.treeIngresarMT.place(x=420, y=55)
        self.treeIngresarMT.heading("#0", text="ID Matricula", anchor=CENTER)
        self.treeIngresarMT.heading("#1", text="ID Sección", anchor=CENTER)
        self.treeIngresarMT.heading("#2", text="ID Alumno", anchor=CENTER)

        
        #Ancho de cada columna
        self.treeIngresarMT.column("#0", width=100, anchor=CENTER)
        self.treeIngresarMT.column("#1", width=100, anchor=CENTER)
        self.treeIngresarMT.column("#2", width=100, anchor=CENTER)
        
        #Llamar a la funcion para cargar los datos al treeview
        self.cargar_datos_matricula()


    def Matricula_Ingresar(self):
        self.conectorBD()
        #Recolectar todas las variables
        idm=self.vIngresarIDMT.get()
        ida=self.vIngresarIDAlumnoMt.get()
        ids=self.vIngresarIDSeccionMt.get()
        
        #Validar que el registro no existe
        self.cursor.execute(f"select count(*) from Matricula where ID_Matricula={idm}")
        va=self.cursor.fetchone()
        if va[0]>0:
            ca.showerror("Eror","Ese ID ya existe")
        else:     
            #Agregar los datos a la base de datos
            self.cursor.execute(f"""insert into Matricula
                           (ID_Matricula, ID_Alumno, ID_Seccion) values 
                           ({idm},{ida},{ids})""")
            self.conexion.commit()
            ca.showinfo("Registrado","Registro agregado corectamente")
        
        #Para actualizar el treeview
        self.cargar_datos_matricula()
        

    def actualizarMt(self):
        self.VenActualizarMt = Toplevel(self.venInfo)
        self.VenActualizarMt.geometry("420x220+300+300")
        self.VenActualizarMt.title("Tabla Matricula_Actualizar Datos")
        self.VenActualizarMt.config(bg="lightblue")
        self.VenActualizarMt.iconbitmap("UNAH-version-horizontal.ico")

        #Entry y Label para ID Matricula
        self.lblActualizarIDMatricula=Label(self.VenActualizarMt, text="ID de la matricula:", bg="lightblue", font=("Time New Roman", 12)).place(x=40,y=60)

        self.vActualizarIDMatricula=IntVar()
        self.txtActualizarIDMatricula=Entry(self.VenActualizarMt, width=25, textvariable=self.vActualizarIDMatricula)
        self.txtActualizarIDMatricula.place(x=230, y=60)

        
        #Boton para Actualizar Datos a la Base de Datos
        self.btnActualizarS=Button(self.VenActualizarMt, text="Actualizar Matricula", font=("Times New Roman", 14), command=self.Matricula_Actualizar)
        self.btnActualizarS.place(x=160, y=110)
    #Funcion para Actualizar Seccion a base de datos
    def Matricula_Actualizar(self):
        # Obtener los nuevos datos ingresados por el usuario
        NuevoIDSección = ci.askstring("Nuevo ID para sección", "Ingrese el nuevo ID para la sección:")
        NuevoIDAlumno = ci.askstring("Nuevo ID para alumno", "Ingrese el nuevo ID para el alumno:")
        ID_Matricula = self.vActualizarIDMatricula.get()
    
        # Validar que todos los campos estén completos
        if not ID_Matricula or not NuevoIDSección or not NuevoIDAlumno:
            ca.showerror("Error", "Todos los campos deben estar llenos")
            return
    
        # Conectar a la base de datos
        self.conectorBD()
    
        # Verificar que el ID_Matricula exista en la base de datos
        self.cursor.execute(f"SELECT count(*) FROM Matricula WHERE ID_Matricula={ID_Matricula}")
        existe = self.cursor.fetchone()[0]
    
        if existe == 0:
            ca.showerror("Error", "El ID de matrícula no existe")
            return
    
        try:
            # Ejecutar la actualización
            self.cursor.execute(f"""
                UPDATE Matricula
                SET ID_Seccion = {int(NuevoIDSección)},
                    ID_Alumno = {int(NuevoIDAlumno)}
                WHERE ID_Matricula = {ID_Matricula}
            """)
            self.conexion.commit()
            ca.showinfo("Éxito", "Datos actualizados correctamente")
        except Exception as e:
            ca.showerror("Error", f"Ocurrió un error: {e}")

        

    def eliminarMt(self):
        self.VenEliminarMt = Toplevel(self.venInfo)
        self.VenEliminarMt.geometry("350x200+300+300")
        self.VenEliminarMt.title("Tabla Secciones_Eliminar Datos")
        self.VenEliminarMt.config(bg="lightblue")
        self.VenEliminarMt.iconbitmap("UNAH-version-horizontal.ico")

        #Entry y Label ID Matricula
        self.lblEliminarIDMt=Label(self.VenEliminarMt, text="Id de la matricula:", bg="lightblue", font=("Time New Roman", 12)).place(x=40,y=60)

        self.vEliminarIDMt=IntVar()
        self.txtEliminarIDMt=Entry(self.VenEliminarMt, width=15, textvariable=self.vEliminarIDMt)
        self.txtEliminarIDMt.place(x=230, y=60)

        
        #Boton para Eliminar Datos a la Base de Datos
        self.btnEliminarMt=Button(self.VenEliminarMt, text="Eliminar Matricula", font=("Times New Roman", 14), command=self.Matricula_Eliminar)
        self.btnEliminarMt.place(x=120, y=110)
        
    #Funcion para eliminar seccion de base de datos   
    def Matricula_Eliminar(self):
        MatriculaAEliminar = ca.askyesno("Eliminar Matrícula", "¿Está seguro de eliminar la matrícula?")
        
        if MatriculaAEliminar:
            idm = self.vEliminarIDMt.get()
            if not idm:
                ca.showerror("Error", "Debe ingresar un ID de matrícula")
                return
            # Conectar a la base de datos
            self.conectorBD()
            # Verificar si el ID existe
            self.cursor.execute(f"SELECT count(*) FROM Matricula WHERE ID_Matricula = {idm}")
            existe = self.cursor.fetchone()[0]
            if existe == 0:
                ca.showerror("Error", "El ID de matrícula no existe")
            else:
                try:
                    # Eliminar el registro
                    self.cursor.execute(f"DELETE FROM Matricula WHERE ID_Matricula = {idm}")
                    self.conexion.commit()
                    ca.showinfo("Éxito", "Matrícula eliminada correctamente")
                except Exception as e:
                    ca.showerror("Error", f"Ocurrió un error al eliminar: {e}")
app = Aplicacion()
