from tkinter import *
import random
from PIL import Image, ImageTk
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, filedialog, ttk
import sqlite3
import os
import subprocess
from reportlab.lib.pagesizes import landscape, letter, legal
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, TableStyle, LongTable, Paragraph
from reportlab.lib.styles import ParagraphStyle
import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# from animationgif import my_label

ctk.set_appearance_mode("Dark")

champs = tk.Tk()
champs.geometry("2000x900")
champs.title("FNG FERME AGRICOL")
Image_Tk = tk.PhotoImage(file="MY_IMAGES\\fleur kabakudi.png")
champs.iconphoto(True, Image_Tk)
champs.config(bg='gray40')

imge1 = tk.PhotoImage(file="MY_IMAGES\\fleur1.png")
btimage = tk.PhotoImage(file="MY_IMAGES\\mangue.png", width=70, height=90)
colection = tk.PhotoImage(file="MY_IMAGES/colection fruits.png")
colection1 = tk.PhotoImage(file="MY_IMAGES/colection3.png")
colection2 = tk.PhotoImage(file="MY_IMAGES/colection5.png")

label_1 = Label(champs, bg="cyan", image=imge1, bd=340)
#ans = messagebox(message='Do You Want To Leave\This registration Form?')
#if ans:

compteur = 0

"""from gestion_ferme import FermeApp

def lancer_mon_application():
    # Importation de la classe FermeApp à partir du fichier gestion_ferme.py
    Crée une instance de la classe FermeApp et la lance.
    
    app = FermeApp()
    app.mainloop()

# Exécute l'application si ce fichier est le programme principal
if __name__ == "__main__":
    lancer_mon_application()

# Exécute l'application si ce fichier est le programme principal
if __name__ == "__main__":
    lancer_mon_application()"""

# lllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll

def database():
    conn = sqlite3.connect("my_ferme.db")
    cursor = conn.cursor()

    cursor.execute(""" CREATE TABLE IF NOT EXISTS Produits(nom_produit text, id_produit text, fournisseur text, prix_produit text,quantite_produit text,total_prix text)""")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Recoltes_Ventes (
            id_recolte INTEGER PRIMARY KEY AUTOINCREMENT,
            nom_produit TEXT,
            quantite REAL,
            prix_unitaire REAL,
            montant_total REAL,
            date_recolte TEXT,
            CONSTRAINT fk_produit
                FOREIGN KEY (nom_produit)
                REFERENCES Produits(nom_produit)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Acheteurs (
            id_acheteur INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT,
            prenom TEXT,
            contact TEXT,
            adresse TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Travailleurs (
            id_travailleur INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT,
            prenom TEXT,
            poste TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Terrains (
            id_terrain INTEGER PRIMARY KEY AUTOINCREMENT,
            nom_terrain TEXT,
            superficie REAL,
            unite_superficie TEXT,
            localisation TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Intrants (
            id_intrant INTEGER PRIMARY KEY AUTOINCREMENT, 
            nom_intrant TEXT, 
            quantite REAL, 
            unite TEXT, 
            date_achat TEXT, 
            fournisseur TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS UtilisationIntrants (
            id_utilisation INTEGER PRIMARY KEY AUTOINCREMENT, 
            id_intrant INTEGER, 
            id_terrain INTEGER, 
            quantite_utilisee REAL, 
            date_utilisation TEXT, 
            FOREIGN KEY(id_intrant) REFERENCES Intrants(id_intrant), 
            FOREIGN KEY(id_terrain) REFERENCES Terrains(id_terrain)
        )
    """)

    # Nouvelle table pour les ventes
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Ventes (
            id_vente INTEGER PRIMARY KEY AUTOINCREMENT,
            produit TEXT,
            acheteur TEXT,
            quantite REAL,
            prix_total REAL,
            prix_par_kg,
            date_vente TEXT,
            FOREIGN KEY (produit) REFERENCES Produits(nom_produit),
            FOREIGN KEY (acheteur) REFERENCES Acheteurs(nom)
        )
    """)

    # NOUVELLE TABLE POUR LEs EMPLACEMENTS
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Stock 
        (
            nom_produit TEXT PRIMARY KEY,
            quantite REAL,
            FOREIGN KEY (nom_produit) REFERENCES Produits(nom_produit)
        )
    """)



    cursor.execute(""" CREATE TABLE IF NOT EXISTS Emplacement(
    id_produit INTEGER PRIMARY KEY AUTOINCREMENT,
    ivestissement REAL,
    Total_Hectares TEXT, 
    TotalHectares_a_Exploiter TEXT, 
    PH_du_Secteur TEXT, 
    nom_produit TEXT,  
    Surface TEXT,
    Kg_de_semance_hectare TEXT, 
    N_mesure_d_angree TEXT,
    RECOLTE_ENVISAGEE TEXT, 
    RECOLTEREEL TEXT, 
    Depences_effectuer TEXT, 
    Detail_sur_les_Depences TEXT, 
    Date TEXT,
    CONSTRAINT nom_produit FOREIGN KEY (nom_produit) REFERENCES Produits(nom_produit))              
    """)
    conn.commit()
    conn.close()


def add_data(nom_produit, id_produit, fournisseur,prix_produit ,quantite_produit ,total_prix):
    conn = sqlite3.connect("my_ferme.db")
    cursor = conn.cursor()
    cursor.execute(""" INSERT INTO Produits VALUES (?, ?, ?, ?, ?, ?)""", (nom_produit, id_produit, fournisseur,prix_produit ,quantite_produit ,total_prix))
    conn.commit()
    conn.close()


# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& debut page animmee$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#def annimmee_page():
#    fenetre = tk.Frame(champs)
#
#    # Chargez le GIF
#    # Remplacez 'votre_gif.gif' par le chemin de votre fichier GIF
#    gif_path = 'GIF_IMAGES/notification.gif'
#    gif = Image.open(gif_path)
#
#    gif_pa = 'GIF_IMAGES/bon.gif'
#    gif1 = Image.open(gif_pa)
#
#    # Créez un label pour afficher le GIF
#    label_gif = tk.Label(fenetre)
#    label_gif.place(x=0, y=20, width=300, height=400)
#
#    # Liste pour stocker toutes les frames du GIF
#    frames = []
#    try:
#        while True:
#            frames.append(ImageTk.PhotoImage(gif.copy()))
#            gif.seek(len(frames))  # Passer à la prochaine frame
#    except EOFError:
#        pass  # Fin de l'animation
#
#    # Fonction pour animer le GIF
#    def animate_gif(frame_index=0):
#        """
#        Met à jour l'image du label avec la prochaine frame du GIF.
#        """
#        # Configure l'image du label avec la frame actuelle
#        label_gif.config(image=frames[frame_index])
#
#        # Calcule l'index de la prochaine frame
#        prochain_frame_index = (frame_index + 1) % len(frames)
#
#        # Planifie la prochaine mise à jour (durée en millisecondes)
#        # 50 millisecondes = 20 images par seconde
#        fenetre.after(50, animate_gif, prochain_frame_index)
#
#    # Démarrez l'animation
#    # animate_gif()
#
#    fenetre.place(x=50, y=50, width=500, height=500)


# ggggggggggggggggggggggggggggggggggggggggggggiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiifffffffffffffffffffffffffffff

# le gif qui boullie sur le feux le label qui contien l'image est page travalleurs
# Remplacez "votre_gif_anime.gif" par le chemin de votre fichier GIF
gif_path = "GIF_IMAGES/disabaa.gif"
gif_pa = "GIF_IMAGES//notification.gif"

class SmallGifLabel(tk.Label):
    def __init__(self, master, gif_path, size, text=""):
        tk.Label.__init__(self, master, text=text, compound="center", bg='gray12')


        # Charger le GIF et le décomposer en frames
        self.gif = Image.open(gif_path)
        self.frames = []
        try:
            while True:
                # Copier et redimensionner chaque frame
                frame = self.gif.copy()
                frame.thumbnail(size, Image.LANCZOS)  # Redimensionne la frame à la taille désirée
                self.frames.append(frame)
                self.gif.seek(len(self.frames))
        except EOFError:
            pass  # Fin de la séquence du GIF
        self.tk_frames = [ImageTk.PhotoImage(frame) for frame in self.frames]
        self.current_frame = 0
        self.delay = self.gif.info.get("duration", 100)  # Durée de chaque frame (100ms par défaut)
        self.animate()

    def animate(self):
        """Met à jour l'image affichée pour créer l'animation."""
        self.config(image=self.tk_frames[self.current_frame])
        self.current_frame = (self.current_frame + 1) % len(self.tk_frames)
        self.after(self.delay, self.animate)


# --- Créer l'interface ---
# root = tk.Tk()
# root.title("Label avec petit GIF")

# Définir la nouvelle taille pour le GIF
petite_taille = (370, 370)
petite_taillea = (260, 120)


# Créer une instance de notre label personnalisé avec la nouvelle taille
# my_label = SmallGifLabel(root, gif_path, petite_taille, text="Ceci est un petit GIF animé !")
# my_label.pack(pady=10, padx=10)

#mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmeeeeeeeeeeeeeeesssssssssssssssssssssaaaaaaaaaaaaaaaaaaaaggggggeeeeeeeeebbbbbbbbbbboooooooooxxxxxxxxxxx
def cofirmation_box(message):

    answer  = tk.BooleanVar()
    answer.set(False)

    def action(ans):
        answer.set(ans)
        confirmation_box_fr.destroy()

    confirmation_box_fr = tk.Frame(champs,highlightbackground="gray12",
                                   highlightcolor="cyan", highlightthickness=3)

    message_lab = tk.Label(confirmation_box_fr,text=message, font=('Bold',15))
    message_lab.pack(pady=20)

    concel_btn = tk.Button(confirmation_box_fr, text='Cancel',font=('Bold',15),bd=0,bg='red',fg='white',
                           command=lambda:action(False))
    concel_btn.place(x=50,y=160)

    yes_btn = tk.Button(confirmation_box_fr, text='Yes', font=('Bold', 15), bd=0, bg='red', fg='white',
                        command=lambda:action(True))
    yes_btn.place(x=190, y=160,width=80)

    confirmation_box_fr.place(x=100,y=120,width=320,height=220)
    #print('code reached st line 35')

    champs.wait_window(confirmation_box_fr)
    #print('code reached st line 37')
    return answer.get()

def message_box(message):
    message_box_fm = tk.Frame(champs, highlightbackground="gray12",
                                   highlightcolor="cyan", highlightthickness=3,bg='#fff')

    close_btn = tk.Button(message_box_fm, text='Ok', font=('Bold', 15),bd=0, bg='#fff',fg='gray12',command=lambda:message_box_fm.destroy())
    close_btn.place(x=280, y=0)

    my_label = SmallGifLabel(message_box_fm, gif_pa, petite_taillea,text='Message !\t\t')# text="\n \n \n \n FELICITATION \nPRODUIT ENREGISTRER \nAVEC SUCEE !" )
    my_label.place(x=28, y=20, width=260, height=120)
    my_label.config(bg='#fff', fg='#000',font=('Bold', 14))

    eror_label = tk.Label(message_box_fm,text=message)  # text="\n \n \n \n FELICITATION \nPRODUIT ENREGISTRER \nAVEC SUCEE !" )
    eror_label.place(x=28, y=135, width=260, height=40)
    eror_label.config(bg='#fff', fg='red', font=('Bold',12))

    #my_label.pack(pady=50)

    #message_lab = tk.Label(message_box_fm, text=message, font=('Bold', 15))
    #message_lab.pack(pady=50)

    message_box_fm.place(x=100, y=120, width=320, height=200)

# ==============================DEBUT PAGE PRODUITS ===========================================




def page_produits():
    def forwaard_to_champs():

         # ans permet que si la reponse est  oui la ppage se detruit
        #ans = cofirmation_box(message="Do You Want To Leave\nThis registration Form?")
        #if ans:
       produit.destroy()
       champs.update()

    couleur_par_defaut = ctk.ThemeManager.theme["CTkEntry"]["border_color"]
    couleur_avertissement = "red"

    def remove_highlight_warning(entry):
        if entry.cget("border_color") == couleur_avertissement and entry.get() != "":
            entry.configure(border_color=couleur_par_defaut)

    def simuler_avertissement():
        if nom_produit_ent.get() == "":
            nom_produit_ent.configure(border_color=couleur_avertissement)

    def check_if_id_allready_exist(id_produit_a_verifier):
        conn = sqlite3.connect("my_ferme.db")
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM Produits WHERE id_produit = ?", (id_produit_a_verifier,))
        response = cursor.fetchone()
        conn.close()
        return response is not None

    def check_if_name_allready_exist(nom_produit_a_verifier):
        conn = sqlite3.connect("my_ferme.db")
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM Produits WHERE nom_produit = ?", (nom_produit_a_verifier,))
        response = cursor.fetchone()
        conn.close()
        return response is not None

    def check_inpoot_validation():
        nom_p = nom_produit_ent.get()
        id_p = id_de_produit_ent.get()
        fournisseur_p = fournisseur_produit_ent.get()
        px = prix_produit_ent.get()
        qt = qt_produit_ent.get()
        tp=total_prix_ent.get()

        if nom_p == "Choisissez une culture" or nom_p == "":
            nom_produit_ent.configure(border_color='red')
            nom_produit_ent.focus()
            #messagebox.showerror("Erreur", "Veuillez choisir un Nom de Produit.")
            message_box(message="Erreur, \nLe Champs Nom est Vide")
        elif id_p == "":
            id_de_produit_ent.configure(border_color='red')
            id_de_produit_ent.focus()
        elif fournisseur_p == "":
            fournisseur_produit_ent.configure(border_color='red')
            fournisseur_produit_ent.focus()
            #messagebox.showerror("Erreur", "Veuillez remplir le nom de fournisseur.")
            message_box(message="Erreur, \nLe Champs Fournisseur est Vide")
        elif check_if_id_allready_exist(id_produit_a_verifier=id_p):
            id_de_produit_ent.configure(border_color='red')
            id_de_produit_ent.focus()
            message_box(message=f"Erreur,l'ID {id_p} existe déjà. \nVeuillez utiliser un autre ID.")
            #messagebox.showerror("Erreur", f"Le produit avec \n l'ID {id_p} existe déjà. \nVeuillez utiliser \nun autre ID.")
        elif check_if_name_allready_exist(nom_produit_a_verifier=nom_p):
            nom_produit_ent.configure(border_color='red')
            nom_produit_ent.focus()
            #messagebox.showerror("Erreur", f"Le produit \n'{nom_p}' est déjà enregistré. ")
            message_box(message=f"Erreur,le nom {nom_p} existe déjà. \nVeuillez utiliser un autre Nom")
        else:
            add_data(nom_produit=nom_p,
                     id_produit=id_p,
                     fournisseur=fournisseur_p,prix_produit=px,quantite_produit=qt,total_prix=tp)
            message_box(message=f'Felicitation,{nom_p} a été enregistré \navec succès !')
            nom_produit_ent.set('Choisissez une culture')
            id_de_produit_ent.configure(state=ctk.NORMAL)
            id_de_produit_ent.delete(0, ctk.END)
            fournisseur_produit_ent.delete(0, ctk.END)
            prix_produit_ent.delete(0, ctk.END)
            qt_produit_ent.delete(0, ctk.END)
            total_prix_ent.delete(0, ctk.END)
            generate_id_number()

    def coulleur1(event):
        live.config(bg="red")

    def couleur2(event):
        live.config(bg='gray12')

    produit = tk.Frame(champs, bg='gray12', bd=7)

    scrollbar = tk.Scrollbar(produit)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    titre = Label(produit, text="PAGE GESTION LOGISTIQUE  AGRICOLES FNG FERME", font=("TIMES NEW ROMAN", 20),
                  bg='gray12', fg='cyan')
    titre.place(x=140, y=0, width=900, height=30)
    live = tk.Button(produit, text='X', bd=0, bg='gray12', fg='white', font=("Arial", 13), command=forwaard_to_champs)
    live.place(x=1319, y=0, width=40)
    live.bind("<Enter>", coulleur1)
    live.bind("<Leave>", couleur2)

    options = ["Haricot", "Pommes de terre", "Maïs", "Tomate", "Soja", "Riz", "Amarente", "Oseil", "Gourge", "Gombo",
               "Choux", 'Obrgeine', 'Amorel', 'Matembele', 'Epinard']

    nom_produit = Label(produit, text="Nom de Produit Entrant semances a reproduire", font=("Arial", 20), bg='gray12', fg='#fff')
    nom_produit.place(x=50, y=90)
    nom_produit_ent = ctk.CTkComboBox(master=produit,
                                      values=options,
                                      width=290,
                                      state=NORMAL,
                                      height=40,
                                      font=("Arial", 20),
                                      corner_radius=20, border_color='yellow',
                                      border_width=2)
    nom_produit_ent.place(x=50, y=150)
    nom_produit_ent.bind("<Key>", lambda event: remove_highlight_warning(nom_produit_ent))

    id_de_produit = Label(produit, text="ID de Produit", font=("Arial", 20), bg='gray12', fg='#fff')
    id_de_produit.place(x=50, y=290)
    id_de_produit_ent = ctk.CTkEntry(produit, font=("Arial", 20), corner_radius=20, width=290, height=40)
    id_de_produit_ent.place(x=50, y=350)

    def generate_id_number():
        generated_id = ''
        for _ in range(4):
            generated_id += str(random.randint(0, 9))

        if not check_if_id_allready_exist(id_produit_a_verifier=generated_id):
            id_de_produit_ent.configure(state=ctk.NORMAL)
            id_de_produit_ent.delete(0, ctk.END)
            id_de_produit_ent.insert(ctk.END, generated_id)
            id_de_produit_ent.configure(state=ctk.DISABLED)
        else:
            generate_id_number()

    def calculate_total_amount(event=None):
        try:
            quantite = float(qt_produit_ent.get())
            prix = float(prix_produit_ent.get())
            montant_total = quantite * prix
            total_prix_ent.delete(0,END)
            total_prix_ent.insert(0,montant_total)
            #total_prix_ent.configure(state=DISABLED)
        except ValueError:
            total_prix_ent.configure(placeholder_text=" Total est 0.0 fc")

    fournisseur_produit = Label(produit, text="Nom de fournisseur", font=("Arial", 20), bg='gray12', fg='#fff')
    fournisseur_produit.place(x=420, y=290)
    fournisseur_produit_ent = ctk.CTkEntry(produit, font=("Arial", 20), corner_radius=20, width=290, height=40,
                                           placeholder_text="entrer le nom de fournisseur", border_color='yellow',
                                           border_width=2)
    fournisseur_produit_ent.place(x=390, y=350)
    fournisseur_produit_ent.bind("<Key>", lambda event: remove_highlight_warning(fournisseur_produit_ent))
    # prix produit
    prix_produit = Label(produit, text="Prix de Produit", font=("Arial", 20), bg='gray12', fg='#fff')
    prix_produit.place(x=50, y=410)
    prix_produit_ent = ctk.CTkEntry(produit, font=("Arial", 20), corner_radius=20, width=290, height=40,placeholder_text="Entree le prix de produits", border_color='yellow',border_width=2)
    prix_produit_ent.place(x=50, y=460)
    prix_produit_ent.bind("<Key>", lambda event: remove_highlight_warning(nom_produit_ent))
    prix_produit_ent.bind("<KeyRelease>",calculate_total_amount)
    # total prix
    total_prix = Label(produit, text="Total Prix", font=("Arial", 20), bg='gray12', fg='#fff')
    total_prix.place(x=420, y=410)
    total_prix_ent = ctk.CTkEntry(produit, font=("Arial", 20), corner_radius=20, width=290, height=40,placeholder_text="entrer la quantites de produit", border_color='yellow',border_width=2)
    total_prix_ent.place(x=390, y=460)
    total_prix_ent.bind("<Key>", lambda event: remove_highlight_warning(fournisseur_produit_ent))


    qt_produit = Label(produit, text="Quantite Produit", font=("Arial", 20), bg='gray12', fg='#fff')
    qt_produit.place(x=50, y=520)
    qt_produit_ent = ctk.CTkEntry(produit, font=("Arial", 20), corner_radius=20, width=290, height=40,placeholder_text="entrer la quantites de produit", border_color='yellow',border_width=2)
    qt_produit_ent.place(x=50, y=560)
    qt_produit_ent.bind("<Key>", lambda event: remove_highlight_warning(fournisseur_produit_ent))
    qt_produit_ent.bind("<KeyRelease>",calculate_total_amount)



    register_btn = ctk.CTkButton(produit, font=("Arial", 20), corner_radius=20, width=290, height=40,
                                 text="Enregistrer le nom de produits ", command=check_inpoot_validation)
    register_btn.place(x=390, y=550)

    voir_produits_btn = ctk.CTkButton(produit, font=("Arial", 20), corner_radius=20, width=290, height=40,
                                      text=" liste de produits", command=liste_produits)
    voir_produits_btn.place(x=390, y=150)

    generate_id_number()
    frame = tk.Frame(produit, width=340, height=300, bg="gray12")
    frame.place(x=700, y=25, width=700, height=700)
    frame.pack_propagate()

    chemin_photos = ["MY_IMAGES/fleur kabakudi.png", "MY_IMAGES/fleur1.png", "MY_IMAGES/Screenshot_20250625-173837.jpg",
                     "MY_IMAGES/Screenshot_20250823-163958.jpg", "MY_IMAGES/Screenshot_20250829-210511.jpg",
                     "MY_IMAGES/Screenshot_20250907-172704.jpg", "MY_IMAGES/Screenshot_20250904-215017.jpg",
                     'MY_IMAGES/ditala.jpg', 'MY_IMAGES/fruits.jpg', 'MY_IMAGES/mayang.jpg']
    photos = []
    for chemin in chemin_photos:
        image = Image.open(chemin)
        image = image.resize((600, 600))
        photos.append(ImageTk.PhotoImage(image))

    label_photo = tk.Label(frame)
    label_photo.pack(expand=True)

    def changer_photo():
        global compteur
        label_photo.config(image=photos[compteur])
        compteur = (compteur + 1) % len(photos)
        produit.after(5000, changer_photo)

    changer_photo()
    # annimmee_page()
    produit.place(x=0, y=0, width=2000, height=900)


# ==============================FIN PAGE PRODUITS =========================================

# ==============================DEBUT LISTE PRODUITS =======================================
def liste_produits():
    def fetch_product_data(query="SELECT * FROM Produits"):
        conn = sqlite3.connect("my_ferme.db")
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        conn.close()
        return data

    def display_products(query="SELECT * FROM Produits"):
        for item in product_tree.get_children():
            product_tree.delete(item)

        products = fetch_product_data(query)

        for product in products:
            product_tree.insert("", tk.END, values=product)

    def search_products():
        search_term = find_by_entry.get().strip()
        search_option = find_by_option_ent.get().strip()

        if not search_term:
            messagebox.showwarning("Avertissement", "Veuillez entrer un terme de recherche.")
            display_products()
            return

        if search_option == "ID":
            query = f"SELECT * FROM Produits WHERE id_produit LIKE '%{search_term}%'"
        elif search_option == "Name":
            query = f"SELECT * FROM Produits WHERE nom_produit LIKE '%{search_term}%'"
        elif search_option == "Id Fournisseur":
            query = f"SELECT * FROM Produits WHERE fournisseur LIKE '%{search_term}%'"
        else:
            messagebox.showerror("Erreur", "Option de recherche invalide.")
            return

        display_products(query)

    def delete_product():
        selected_item = product_tree.selection()
        if not selected_item:
            messagebox.showwarning("Avertissement", "Veuillez sélectionner un produit à supprimer.")
            return

        product_id = product_tree.item(selected_item)['values'][1]

        confirmation = messagebox.askyesno("Confirmer la suppression",
                                           f"Êtes-vous sûr de vouloir supprimer le produit avec l'ID {product_id} ?")
        if confirmation:
            conn = sqlite3.connect("my_ferme.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Produits WHERE id_produit = ?", (product_id,))
            conn.commit()
            conn.close()
            display_products()
            messagebox.showinfo("Succès", "Produit supprimé avec succès.")

    def forwaard_to_champs():
        liste_prod.destroy()
        champs.update()

    liste_prod = tk.Frame(champs, bg='red')

    list_frame = ttk.LabelFrame(liste_prod, text="Liste des Produits")
    list_frame.place(x=0, y=0, width=1200, height=900)
    product_tree = ttk.Treeview(list_frame, columns=("Nom_de_produit", "id_produit", "fournisseur","prix_produit","quantite_produit","total_prix"),
                                show="headings")
    product_tree.heading("Nom_de_produit", text="Nom Produit")
    product_tree.heading("id_produit", text="ID Produit")
    product_tree.heading("fournisseur", text="Fournisseur")
    product_tree.heading("prix_produit", text="Prix de Produit")
    product_tree.heading("quantite_produit", text="Quantite de Produit")
    product_tree.heading("total_prix", text=" Prix Total")

    product_tree.column("Nom_de_produit", width=150)
    product_tree.column("id_produit", width=150)
    product_tree.column("fournisseur", width=120)
    product_tree.column("prix_produit", width=150)
    product_tree.column("quantite_produit", width=150)
    product_tree.column("total_prix", width=150)
    product_tree.pack(fill="both", expand=True)

    action_frame = ttk.Frame(liste_prod)
    action_frame.place(x=1200, y=0, width=200, height=900)

    find_by_entry = ctk.CTkEntry(action_frame, font=("Arial", 16), width=160, height=30,
                                 placeholder_text="Rechercher...")
    find_by_entry.place(x=0, y=40)

    search_button = ctk.CTkButton(action_frame, text="Rechercher", command=search_products, width=150, height=30)
    search_button.place(x=0, y=90)

    options = ['ID', 'Name', 'Id Fournisseur']
    find_by_option_ent = ctk.CTkComboBox(master=action_frame, values=options, width=160, state=NORMAL, height=40,
                                         font=("Arial", 16), corner_radius=20, border_color='yellow', border_width=2)
    find_by_option_ent.set("Name")
    find_by_option_ent.place(x=0, y=140)

    delete_button = ctk.CTkButton(action_frame, text="Supprimer Produit", command=delete_product, width=150, height=30)
    delete_button.place(x=0, y=200)

    refresh_button = ctk.CTkButton(action_frame, text="Actualiser Liste", command=lambda: display_products(), width=150,
                                   height=30)
    refresh_button.place(x=0, y=250)

    def coulleur1(event):
        live.config(bg="red")

    def couleur2(event):
        live.config(bg='gray12')

    live = tk.Button(action_frame, text='X', bd=0, bg='gray53', fg='white', font=("Arial", 13),
                     command=forwaard_to_champs)
    live.place(x=119, y=0, width=40)
    live.bind("<Enter>", coulleur1)
    live.bind("<Leave>", couleur2)

    display_products()
    liste_prod.place(x=0, y=0, width=2000, height=900)


# ==============================FIN LISTE PRODUITS =======================================

# ----------------- NOUVELLES PAGES -----------------
import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
import customtkinter as ctk
from datetime import datetime

# Assurez-vous que les images sont chargées si nécessaire
# colection = tk.PhotoImage(file="chemin/vers/image1.png")
# colection1 = tk.PhotoImage(file="chemin/vers/image2.png")
# colection2 = tk.PhotoImage(file="chemin/vers/image3.png")

# Cette fonction doit être définie dans votre script principal
# def champs.update():
#    pass

import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
import customtkinter as ctk
from datetime import datetime

# --- Refactorisation de la logique de la base de données ---

import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
import customtkinter as ctk
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# --- Configuration du Thème pour CustomTkinter et Matplotlib ---
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


# ====================================================================
# CLASSE 1 : DatabaseManager
# Gère toutes les interactions avec la base de données.
# ====================================================================
def RecolteVentePage():
    class DatabaseManager:
        """Gère toutes les interactions avec la base de données."""

        def __init__(self, db_name="my_ferme.db"):
            self.db_name = db_name
            self.create_tables()

        def create_tables(self):
            """Crée ou met à jour les tables de la base de données."""
            try:
                conn = sqlite3.connect(self.db_name)
                cursor = conn.cursor()

                # Création de la table Produits (nécessaire pour les FK)
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS Produits(
                        nom_produit TEXT PRIMARY KEY, 
                        id_produit TEXT, 
                        fournisseur TEXT
                    )
                """)

                # Création/Mise à jour de la table Stock
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS Stock 
                    (
                        nom_produit TEXT PRIMARY KEY,
                        quantite REAL,
                        FOREIGN KEY (nom_produit) REFERENCES Produits(nom_produit)
                    )
                """)

                # Création de la table Dépenses
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS Depenses (
                        id_depense INTEGER PRIMARY KEY AUTOINCREMENT,
                        libelle TEXT,
                        montant REAL,
                        prix REAL,
                        qt REAL,
                        date TEXT
                    )
                """)

                # Création/Mise à jour de la table Recoltes_Ventes
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS Recoltes_Ventes (
                        id_recolte INTEGER PRIMARY KEY AUTOINCREMENT,
                        nom_produit TEXT,
                        quantite REAL,
                        prix_unitaire REAL,
                        montant_total REAL,
                        date_recolte TEXT,
                        type TEXT DEFAULT 'recolte',
                        CONSTRAINT fk_produit
                            FOREIGN KEY (nom_produit)
                            REFERENCES Produits(nom_produit)
                    )
                """)

                # Ajout de la colonne 'type' si elle manque (pour les anciens schémas)
                cursor.execute("PRAGMA table_info(Recoltes_Ventes)")
                columns = [column[1] for column in cursor.fetchall()]
                if 'type' not in columns:
                    cursor.execute("ALTER TABLE Recoltes_Ventes ADD COLUMN type TEXT DEFAULT 'recolte'")

                conn.commit()
            except sqlite3.Error as e:
                print(f"Erreur de Base de Données lors de la création des tables: {e}")
            finally:
                conn.close()

        def fetch_produits(self):
            """Récupère tous les produits disponibles (simulé pour l'exemple si la table Produits est vide)."""
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute("SELECT nom_produit FROM Produits")
            produits = [row[0] for row in cursor.fetchall()]
            conn.close()

            # Simulation: Assure qu'il y a des options dans le ComboBox même si Produits est vide
            if not produits:
                return ["0"]
            return produits

        def add_recolte_transaction(self, nom_produit, quantite, prix_unitaire, montant_total, date):
            """Enregistre une récolte et met à jour le stock."""
            try:
                conn = sqlite3.connect(self.db_name)
                cursor = conn.cursor()

                # Assure que le produit existe dans la table Produits
                cursor.execute("INSERT OR IGNORE INTO Produits (nom_produit) VALUES (?)", (nom_produit,))

                # Insérer la récolte
                cursor.execute("""
                    INSERT INTO Recoltes_Ventes (nom_produit, quantite, prix_unitaire, montant_total, date_recolte, type)
                    VALUES (?, ?, ?, ?, ?, 'recolte')
                """, (nom_produit, quantite, prix_unitaire, montant_total, date))

                # Mettre à jour le stock
                cursor.execute("SELECT quantite FROM Stock WHERE nom_produit = ?", (nom_produit,))
                result = cursor.fetchone()
                if result:
                    nouvelle_quantite = result[0] + quantite
                    cursor.execute("UPDATE Stock SET quantite = ? WHERE nom_produit = ?", (nouvelle_quantite, nom_produit))
                else:
                    cursor.execute("INSERT INTO Stock (nom_produit, quantite) VALUES (?, ?)", (nom_produit, quantite))

                conn.commit()
                return True
            except sqlite3.Error as e:
                messagebox.showerror("Erreur de Base de Données", f"Erreur lors de l'enregistrement de la récolte: {e}")
                return False
            finally:
                conn.close()

        def add_vente_transaction(self, nom_produit, quantite, prix_unitaire, montant_total, date):
            """Enregistre une vente et met à jour le stock."""
            try:
                conn = sqlite3.connect(self.db_name)
                cursor = conn.cursor()

                # Assure que le produit existe dans la table Produits
                cursor.execute("INSERT OR IGNORE INTO Produits (nom_produit) VALUES (?)", (nom_produit,))

                # Vérifier le stock
                cursor.execute("SELECT quantite FROM Stock WHERE nom_produit = ?", (nom_produit,))
                result = cursor.fetchone()
                if not result or result[0] < quantite:
                    messagebox.showerror("Erreur de Stock",
                                         f"Stock insuffisant pour cette vente. Stock actuel: {result[0] if result else 0} {nom_produit}")
                    return False

                # Décrémenter le stock
                nouvelle_quantite = result[0] - quantite
                cursor.execute("UPDATE Stock SET quantite = ? WHERE nom_produit = ?", (nouvelle_quantite, nom_produit))

                # Insérer la vente (quantité en négatif pour tracking si besoin)
                cursor.execute("""
                    INSERT INTO Recoltes_Ventes (id_recolte, nom_produit, quantite, prix_unitaire, montant_total, date_recolte, type)
                    VALUES (NULL, ?, ?, ?, ?, ?, 'vente')
                """, (nom_produit, -quantite, prix_unitaire, montant_total, date))  # Utilisation de NULL pour l'ID auto

                conn.commit()
                return True
            except sqlite3.Error as e:
                messagebox.showerror("Erreur de Base de Données", f"Erreur lors de l'enregistrement de la vente: {e}")
                return False
            finally:
                conn.close()

        def get_all_recoltes_ventes(self):
            """Récupère toutes les entrées de récoltes et de ventes."""
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id_recolte, nom_produit, quantite, prix_unitaire, montant_total, date_recolte, type FROM Recoltes_Ventes ORDER BY date_recolte DESC")
            data = cursor.fetchall()
            conn.close()
            return data

        def get_all_stocks(self):
            """Récupère tous les stocks de produits."""
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute("SELECT nom_produit, quantite FROM Stock WHERE quantite > 0 ORDER BY nom_produit")
            data = cursor.fetchall()
            conn.close()
            return data

        def delete_entry(self, entry_id, nom_produit, quantite, entry_type):
            """Supprime une entrée et met à jour le stock."""
            try:
                conn = sqlite3.connect(self.db_name)
                cursor = conn.cursor()

                # Ajuster le stock
                cursor.execute("SELECT quantite FROM Stock WHERE nom_produit = ?", (nom_produit,))
                result = cursor.fetchone()
                if not result:
                    messagebox.showwarning("Stock manquant",
                                           "Impossible d'ajuster le stock car le produit n'est pas répertorié.")
                    return False

                current_stock = result[0]

                # La quantité stockée est toujours positive.
                # En Recoltes_Ventes, 'quantite' est positive pour récolte, négative pour vente.

                quantite_abs = abs(float(quantite))

                if entry_type == 'vente':
                    # Si on supprime une VENTE, le stock DOIT REMONTER.
                    new_stock = current_stock + quantite_abs
                else:  # type == 'recolte'
                    # Si on supprime une RECOLTE, le stock DOIT BAISSER.
                    new_stock = current_stock - quantite_abs
                    if new_stock < 0:
                        messagebox.showwarning("Erreur Stock",
                                               "La suppression de cette récolte mènerait à un stock négatif. Annulé.")
                        return False

                cursor.execute("UPDATE Stock SET quantite = ? WHERE nom_produit = ?", (new_stock, nom_produit))

                # Supprimer l'entrée
                cursor.execute("DELETE FROM Recoltes_Ventes WHERE id_recolte = ?", (entry_id,))

                conn.commit()
                return True
            except sqlite3.Error as e:
                messagebox.showerror("Erreur de Base de Données", f"Erreur lors de la suppression: {e}")
                return False
            finally:
                conn.close()

        # --- Méthodes pour les Graphiques et le Tableau de Bord ---

        def get_recolte_quantities_by_product(self):
            """Récupère les quantités totales récoltées par produit pour le graphique en barres."""
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute("""
                SELECT nom_produit, SUM(quantite)
                FROM Recoltes_Ventes
                WHERE type = 'recolte' AND quantite > 0
                GROUP BY nom_produit
                ORDER BY SUM(quantite) DESC
            """)
            data = cursor.fetchall()
            conn.close()
            return data

        def get_vente_amounts_by_product(self):
            """Récupère les montants totaux des ventes par produit pour le graphique en camembert."""
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute("""
                SELECT nom_produit, SUM(montant_total)
                FROM Recoltes_Ventes
                WHERE type = 'vente'
                GROUP BY nom_produit
                ORDER BY SUM(montant_total) DESC
                LIMIT 5
            """)
            data = cursor.fetchall()
            conn.close()
            return data

        def add_depense(self, libelle, montant,prix,qt,date):
            """Ajoute une dépense à la table Depenses."""
            try:
                conn = sqlite3.connect(self.db_name)
                cursor = conn.cursor()
                cursor.execute("INSERT INTO Depenses (libelle, montant, prix,qt,date) VALUES (?, ?, ?, ?, ?)",
                               (libelle, montant,prix,qt,date))
                conn.commit()
                return True
            except sqlite3.Error as e:
                messagebox.showerror("Erreur de Base de Données", f"Erreur lors de l'ajout de la dépense: {e}")
                return False
            finally:
                conn.close()

        def get_total_ventes(self):
            """Calcule et retourne le total des ventes."""
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute("SELECT SUM(montant_total) FROM Recoltes_Ventes WHERE type = 'vente'")
            total = cursor.fetchone()[0]
            conn.close()
            return total if total else 0

        def get_total_depenses(self):
            """Calcule et retourne le total des dépenses."""
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute("SELECT SUM(montant) FROM Depenses")
            total = cursor.fetchone()[0]
            conn.close()
            return total if total else 0


    # ====================================================================
    # CLASSE 2 : TableauDeBordGlobal
    # Affiche les indicateurs financiers et le graphique Bénéfice/Dépense.
    # ====================================================================

    class TableauDeBordGlobal:
        """Gère l'interface graphique du tableau de bord global, incluant les indicateurs financiers et le graphique."""

        def __init__(self, parent, db, back_to_recolte_vente_callback):
            self.parent = parent
            self.db = db
            self.back_to_recolte_vente_callback = back_to_recolte_vente_callback
            self.page = tk.Frame(parent, bg='gray12', bd=7)
            self.finance_canvas = None
            self.create_widgets()

        # --- Méthode Utile pour le Graphique Matplotlib ---
        def _create_chart_canvas(self, parent_frame, figsize=(3, 3)):
            """Initialise la figure Matplotlib avec un thème sombre et retourne le canvas, figure et axes."""
            fig, ax = plt.subplots(figsize=figsize)
            DARK_BG = '#333333'
            fig.patch.set_facecolor(DARK_BG)
            ax.set_facecolor('#1F1F1F')

            canvas = FigureCanvasTkAgg(fig, master=parent_frame)
            canvas_widget = canvas.get_tk_widget()
            canvas_widget.pack(expand=True, fill='both')
            return canvas, fig, ax

# des calcule entre les Entry
        def calculate_total_amount(self,event=None):
            try:
                quantite = float(self.quantite_entry.get())
                prix = float(self.prix_entry.get())
                montant_total = quantite * prix
                self.montant_entry.delete(0, END)
                self.montant_entry.insert(0, montant_total)
                # total_prix_ent.configure(state=DISABLED)
            except ValueError:
                self.montant_entry.configure(placeholder_text="Total est 0.0 fc")
                self.add_depense_btn.configure(state=tk.NORMAL)

                #LE TREEVIEW POUR VOIR DES DEPENCES



        def create_widgets(self):



            main_frame = tk.Frame(self.page, bg='gray12')
            main_frame.pack(fill='both', expand=True, padx=70, pady=10)

            back_btn = ctk.CTkButton(main_frame, text="Retour", command=self.back_to_recolte_vente_callback)
            back_btn.place(x=0, y=510)

            # Cadre pour les indicateurs financiers + Chart
            indicators_frame = ctk.CTkFrame(main_frame, fg_color='gray20')
            indicators_frame.pack( pady=3, padx=1,anchor='w')

            ctk.CTkLabel(indicators_frame, text="Indicateurs Financiers (en $)", font=("Arial", 18, "bold"),
                         text_color='white').pack(pady=5,ipadx=10 )



            self.total_ventes_label = ctk.CTkLabel(indicators_frame, text="Total Ventes: 0.00 $", font=("Arial", 16),
                                                   text_color='white')
            self.total_ventes_label.pack(anchor='w', pady=5, padx=10)

            self.total_depenses_label = ctk.CTkLabel(indicators_frame, text="Total Dépenses: 0.00 $",
                                                     font=("Arial", 16),
                                                     text_color='white')
            self.total_depenses_label.pack(anchor='w', pady=5, padx=10)

            self.benefice_net_label = ctk.CTkLabel(indicators_frame, text="Bénéfice Net: 0.00 $",
                                                   font=("Arial", 16, "bold"))
            self.benefice_net_label.pack(anchor='w', pady=10, padx=10)

            # --- Ajout du Graphique Financier ---
            self.finance_chart_frame = ctk.CTkFrame(indicators_frame, fg_color='gray30', height=200)
            self.finance_chart_frame.pack(fill='x', padx=10, pady=10)
            self.finance_canvas, self.finance_fig, self.finance_ax = self._create_chart_canvas(self.finance_chart_frame)

            # Cadre pour l'ajout de dépenses
            depense_frame = ctk.CTkFrame(main_frame, fg_color='gray20',width=800,height=800)
            depense_frame.place(x=350, y=10)
            #pack(fill='x', pady=10, padx=10,anchor='s')#pady=5, padx=10, ipady=20,ipadx=10)

            ctk.CTkLabel(depense_frame, text="Enregistrer une Dépense ", font=("Arial", 18, "bold"),
                         text_color='yellow').pack(pady=5)

            form_depense_frame = ctk.CTkFrame(depense_frame, fg_color='gray20')
            form_depense_frame.pack()

            ctk.CTkLabel(form_depense_frame, text="Justitifier vos depenses:", font=("Arial", 14), text_color='yellow').grid(row=0, column=0,
                                                                                                           sticky='w',
                                                                                                           padx=5)
            self.libelle_entry = ctk.CTkEntry(form_depense_frame, width=200, font=("Arial", 14))
            self.libelle_entry.grid(row=0, column=1, padx=5, pady=5)

            ctk.CTkLabel(form_depense_frame, text="Montant Total (Fc):", font=("Arial", 14), text_color='white').grid(row=1,column=0,sticky='w',padx=5)
            self.montant_entry = ctk.CTkEntry(form_depense_frame, width=200, font=("Arial", 14),placeholder_text="Total est 0.0 fc",placeholder_text_color="green",state=NORMAL)
            self.montant_entry.grid(row=1, column=1, padx=5, pady=5)
            self.montant_entry.bind("<KeyRelease>", self.calculate_total_amount)

            ctk.CTkLabel(form_depense_frame, text="PRIX unitaire", font=("Arial", 14), text_color='yellow').grid(row=2,column=0,sticky='w',padx=5)
            self.prix_entry = ctk.CTkEntry(form_depense_frame, width=200, font=("Arial", 14),placeholder_text="0")
            self.prix_entry.grid(row=2, column=1, padx=5, pady=5)
            self.prix_entry.bind("<KeyRelease>", self.calculate_total_amount)

            ctk.CTkLabel(form_depense_frame, text="Quantitee", font=("Arial", 14), text_color='yellow').grid(row=3,column=0,sticky='w',padx=5)
            self.quantite_entry = ctk.CTkEntry(form_depense_frame, width=200, font=("Arial", 14),placeholder_text="0")
            self.quantite_entry.grid(row=3, column=1, padx=5, pady=5)
            self.quantite_entry.bind("<KeyRelease>", self.calculate_total_amount)

            ctk.CTkLabel(form_depense_frame, text="Date (AAAA-MM-JJ):", font=("Arial", 14), text_color='yellow').grid(row=4,column=0,sticky='w',padx=5)
            self.date_depense_entry = ctk.CTkEntry(form_depense_frame, width=200, font=("Arial", 14))
            self.date_depense_entry.grid(row=4, column=1, padx=5, pady=5)

            self.date_depense_entry.insert(0, datetime.now().strftime('%Y-%m-%d'))

            self.add_depense_btn = ctk.CTkButton(depense_frame, text="Ajouter Dépense", command=self.add_depense_to_db,
                                                 fg_color="blue", state="disabled")
            self.add_depense_btn.pack(pady=10)

            self.update_indicators()


            self.depence_tree = ttk.Treeview(main_frame, columns=("ID", "libelle", "montant", "prix", "qt","date"),show="headings")
            self.depence_tree.heading("ID", text="ID DEPENSE")
            self.depence_tree.heading("libelle", text="JUSTIFICATION DE DEPENSES")
            self.depence_tree.heading("montant", text="TOTAL SUR DEPENSES")
            self.depence_tree.heading("prix", text="PRIX ou SOMME DEPENSEE")
            self.depence_tree.heading("qt", text="NOMBRES/Qt")
            self.depence_tree.heading("date",text="date direct")
            self.depence_tree.place(x=350,y=300,width=900,height=300)

            self.scrollbar_y = ttk.Scrollbar(self.depence_tree, orient="vertical", command=self.depence_tree.yview)
            self.scrollbar_y.place(x=848,y=0,height = 300)#self.scrollbar_y.grid(row=0, column=1, sticky="ns")
            self.scrollbar_x = ttk.Scrollbar(self.depence_tree, orient="horizontal", command=self.depence_tree.xview)
            self.scrollbar_x.place(x=0, y=287,width=850,height=16)#self.scrollbar_x.grid(row=1, column=0, sticky="ew")
            self.depence_tree.configure(yscrollcommand=self.scrollbar_y.set, xscrollcommand=self.scrollbar_x.set)

            def display_terrains():
                for item in self.depence_tree.get_children():
                    self.depence_tree.delete(item)
                conn = sqlite3.connect("my_ferme.db")
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM Depenses")
                data = cursor.fetchall()
                conn.close()
                for row in data:
                    self.depence_tree.insert("", tk.END, values=row)

            display_terrains()


        def check_montant_depense(self, event=None):
            """Active/désactive le bouton de dépense si le champ Montant est valide."""
            montant_str = self.montant_entry.get().strip()
            is_valid = False
            if montant_str:
                try:
                    if float(montant_str) > 0:
                        is_valid = True
                except ValueError:
                    pass

            if is_valid:
                self.add_depense_btn.configure(state="normal")
            else:
                self.add_depense_btn.configure(state="disabled")

        def update_indicators(self):
            """Met à jour les labels et le graphique avec les données de la base de données."""
            total_ventes = self.db.get_total_ventes()
            total_depenses = self.db.get_total_depenses()
            benefice_net = total_ventes - total_depenses

            self.total_ventes_label.configure(text=f"Total Ventes: {total_ventes:.2f} $")
            self.total_depenses_label.configure(text=f"Total Dépenses: {total_depenses:.2f} $")

            if benefice_net >= 0:
                self.benefice_net_label.configure(text=f"Bénéfice Net: {benefice_net:.2f} $", text_color='green')
            else:
                self.benefice_net_label.configure(text=f"Perte Nette: {abs(benefice_net):.2f} $", text_color='red')

            self.update_finance_chart(total_ventes, total_depenses, benefice_net)

        def update_finance_chart(self, total_ventes, total_depenses, benefice_net):
            """Met à jour le graphique financier (Tarte Bénéfice vs. Dépenses)."""
            self.finance_ax.clear()

            labels = ['Bénéfice Net', 'Dépenses Totales']
            # On affiche le Bénéfice Net (ou 0 s'il est négatif) et les Dépenses Totales
            sizes = [max(0, benefice_net), total_depenses]
            colors = ['green', 'red']

            if total_ventes > 0 and (benefice_net > 0 or total_depenses > 0):
                # Calcul du ratio si bénéfice net est positif
                if benefice_net >= 0:
                    self.finance_ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90,
                                        colors=colors, textprops={'color': "white"})
                    self.finance_ax.set_title("Répartition du Revenu Brut", color='cyan', fontsize=10)
                else:
                    # Si perte, on affiche Ventes vs Dépenses totales
                    self.finance_ax.pie([total_ventes, total_depenses], labels=['Ventes', 'Dépenses'], autopct='%1.1f%%',
                                        startangle=90,
                                        colors=['gold', 'red'], textprops={'color': "white"})
                    self.finance_ax.set_title("Ventes (vs Coûts)", color='cyan', fontsize=10)
            else:
                self.finance_ax.text(0, 0, "Pas de données financières.", ha='center', va='center', color='white')

            self.finance_fig.tight_layout()
            self.finance_canvas.draw()

        def add_depense_to_db(self):
            """Récupère les données du formulaire et ajoute la dépense à la DB."""
            libelle = self.libelle_entry.get()
            montant_str = self.montant_entry.get()
            prix=self.prix_entry.get()
            qt = self.quantite_entry.get()
            date = self.date_depense_entry.get()

            if not all([libelle, montant_str,prix,qt,date]):
                messagebox.showerror("Erreur", "Veuillez remplir tous les champs de dépense.")
                return

            try:
                montant = float(montant_str)
                if montant <= 0:
                    messagebox.showerror("Erreur", "Le montant doit être un nombre positif.")
                    return
            except ValueError:
                messagebox.showerror("Erreur", "Le montant doit être un nombre valide.")
                return

            try:
                datetime.strptime(date, '%Y-%m-%d')
            except ValueError:
                messagebox.showerror("Erreur", "Format de date invalide. Utilisez AAAA-MM-JJ.")
                return

            if self.db.add_depense(libelle, montant,prix,qt, date):
                messagebox.showinfo("Succès", "Dépense enregistrée avec succès.")
                self.libelle_entry.delete(0, tk.END)
                self.montant_entry.delete(0, tk.END)
                self.prix_entry.delete(0, tk.END)
                self.quantite_entry.delete(0, tk.END)
                # Ne pas effacer la date, juste la réinitialiser au format du jour si besoin
                self.date_depense_entry.delete(0, tk.END)
                self.date_depense_entry.insert(0, datetime.now().strftime('%Y-%m-%d'))
                self.update_indicators()
                self.check_montant_depense()

        def place(self, **kwargs):
            self.page.place(**kwargs)


    # ====================================================================
    # CLASSE 3 : RecolteVentePage
    # Gère le formulaire, les historiques (séparés) et les graphiques spécifiques.
    # ====================================================================

    class RecolteVentePage:
        """Gère l'interface graphique de la page de récolte et vente avec historique séparé et graphiques par catégorie."""


        def __init__(self, parent, db, forward_to_champs_callback, forward_to_dashboard_callback):
            self.parent = parent
            self.db = db
            self.forward_to_champs_callback = forward_to_champs_callback
            self.forward_to_dashboard_callback = forward_to_dashboard_callback
            self.page = tk.Frame(parent, bg='gray12', bd=7)
            self.recolte_canvas = None
            self.vente_canvas = None
            self.create_widgets()

        def forward_to_champs_callback(self):
            self.parent.destroy()
            root.update()
            page_produits()
        def _create_chart_canvas(self, parent_frame, figsize=(6, 4)):
            """Initialise la figure Matplotlib avec un thème sombre et retourne le canvas, figure et axes."""
            fig, ax = plt.subplots(figsize=figsize)
            DARK_BG = '#333333'
            fig.patch.set_facecolor(DARK_BG)
            ax.set_facecolor('#1F1F1F')

            canvas = FigureCanvasTkAgg(fig, master=parent_frame)
            canvas_widget = canvas.get_tk_widget()
            canvas_widget.pack(expand=True, fill='both')
            return canvas, fig, ax

        def _create_history_treeview(self, parent_frame):
            """Crée un Treeview standard pour les onglets de récolte ou vente."""
            tree = ttk.Treeview(parent_frame,
                                columns=("ID", "Produit", "Quantité", "Prix Unitaire", "Total", "Date"),
                                show="headings")

            # Style des Treeviews pour customtkinter
            style = ttk.Style()
            style.theme_use("default")
            style.configure("Treeview",
                            background="#2A2D2E",
                            foreground="white",
                            fieldbackground="#2A2D2E",
                            bordercolor="#3E4042",
                            lightcolor="#3E4042",
                            darkcolor="#3E4042")
            style.map('Treeview', background=[('selected', 'cyan')])

            columns_widths = {"ID": 50, "Produit": 150, "Quantité": 100, "Prix Unitaire": 100, "Total": 100, "Date": 120}

            for col, width in columns_widths.items():
                tree.heading(col, text=col.replace(" Unitaire", "").strip(),
                             command=lambda c=col: self.sort_column(tree, c, False))
                tree.column(col, width=width, stretch=tk.NO)

            return tree

        def create_recolte_view(self, parent_tab):
            """Crée le Treeview et le Chart spécifiques aux Récoltes dans l'onglet."""

            # 1. Treeview (Haut)
            tree_frame = ctk.CTkFrame(parent_tab, fg_color='gray30')
            tree_frame.pack(fill='x', padx=10, pady=(10, 5))

            self.recolte_tree = self._create_history_treeview(tree_frame)
            self.recolte_tree.pack(fill='x', expand=False, padx=5, pady=5)

            # 2. Chart (Bas)
            chart_frame = ctk.CTkFrame(parent_tab, fg_color='#333333')
            chart_frame.pack(fill='both', expand=True, padx=10, pady=(5, 10))

            ctk.CTkLabel(chart_frame, text="Graphique Récoltes par Produit", font=("Arial", 14, "bold"),
                         text_color='white').pack(pady=5)
            self.recolte_canvas, self.recolte_fig, self.recolte_ax = self._create_chart_canvas(chart_frame)

        def create_vente_view(self, parent_tab):
            """Crée le Treeview et le Chart spécifiques aux Ventes dans l'onglet."""

            # 1. Treeview (Haut)
            tree_frame = ctk.CTkFrame(parent_tab, fg_color='gray30')
            tree_frame.pack(fill='x', padx=10, pady=(10, 5))

            self.vente_tree = self._create_history_treeview(tree_frame)
            self.vente_tree.pack(fill='x', expand=False, padx=5, pady=5)
            self.vente_tree.tag_configure('vente', background='lightcoral', foreground='white')

            # 2. Chart (Bas)
            chart_frame = ctk.CTkFrame(parent_tab, fg_color='#333333')
            chart_frame.pack(fill='both', expand=True, padx=10, pady=(5, 10))

            ctk.CTkLabel(chart_frame, text="Graphique Montant des Ventes (Top 5)", font=("Arial", 14, "bold"),
                         text_color='white').pack(pady=5)
            self.vente_canvas, self.vente_fig, self.vente_ax = self._create_chart_canvas(chart_frame)

        # --- MÉTHODES DE CRÉATION DE WIDGETS ---
        def create_widgets(self):
            """Crée et positionne tous les widgets de la page."""

            titre = tk.Label(self.page, text="PAGE DE GESTION DES RÉCOLTES ET VENTES", font=("TIMES NEW ROMAN", 20),
                             bg='gray12', fg='cyan')
            titre.pack(pady=10)

            dashboard_btn = ctk.CTkButton(self.page, text="Tableau de Bord", command=self.forward_to_dashboard_callback)
            dashboard_btn.place(x=10, y=10)

            # Bouton factice 'X' pour la cohérence de l'interface
            #live = tk.Button(self.page, text='X', bd=0, bg='gray12', fg='white', font=("Arial", 13),
                             #command=self.forward_to_champs_callback)
            #live.place(x=1319, y=0, width=40)
            #live.bind("<Enter>", lambda e: live.config(bg="red"))
            #live.bind("<Leave>", lambda e: live.config(bg="gray12"))

            main_frame = tk.Frame(self.page, bg='gray12')
            main_frame.pack(expand=True, fill='both', padx=20, pady=10)

            # --- Gauche : Formulaire et Stock ---
            left_frame = tk.Frame(main_frame, bg='gray12')
            left_frame.pack(side=tk.LEFT, fill='y', padx=(0, 20))

            form_frame = tk.Frame(left_frame, bg='gray20', padx=20, pady=20)
            form_frame.pack(pady=10)

            tk.Label(form_frame, text="Nouvelle Opération", font=("Arial", 18, "bold"), bg='gray20', fg='white').grid(row=0,
                                                                                                                      columnspan=2,
                                                                                                                      pady=(
                                                                                                                          0,
                                                                                                                          10))

            tk.Label(form_frame, text="Produit:", font=("Arial", 16), bg='gray20', fg='white').grid(row=1, column=0,
                                                                                                    sticky='w')
            self.produit_ent = ctk.CTkComboBox(form_frame, values=self.db.fetch_produits(), width=250, font=("Arial", 16))
            self.produit_ent.grid(row=1, column=1, padx=10, pady=5)

            tk.Label(form_frame, text="Quantité (kg/unité):", font=("Arial", 16), bg='gray20', fg='white').grid(row=2,
                                                                                                                column=0,
                                                                                                                sticky='w')
            self.quantite_ent = ctk.CTkEntry(form_frame, width=250, font=("Arial", 16))
            self.quantite_ent.grid(row=2, column=1, padx=10, pady=5)
            self.quantite_ent.bind("<KeyRelease>", self.calculate_total_amount)

            tk.Label(form_frame, text="Prix Unitaire ($):", font=("Arial", 16), bg='gray20', fg='white').grid(row=3,
                                                                                                              column=0,
                                                                                                              sticky='w')
            self.prix_unitaire_ent = ctk.CTkEntry(form_frame, width=250, font=("Arial", 16))
            self.prix_unitaire_ent.grid(row=3, column=1, padx=10, pady=5)
            self.prix_unitaire_ent.bind("<KeyRelease>", self.calculate_total_amount)

            self.montant_total_label = tk.Label(form_frame, text="Montant Total: 0.00 $", font=("Arial", 16), bg='gray20',
                                                fg='white')
            self.montant_total_label.grid(row=4, column=0, columnspan=2, pady=5)

            tk.Label(form_frame, text="Date (AAAA-MM-JJ):", font=("Arial", 16), bg='gray20', fg='white').grid(row=5,
                                                                                                              column=0,
                                                                                                              sticky='w')
            self.date_ent = ctk.CTkEntry(form_frame, width=250, font=("Arial", 16))
            self.date_ent.grid(row=5, column=1, padx=10, pady=5)
            self.date_ent.insert(0, datetime.now().strftime('%Y-%m-%d'))

            button_frame = tk.Frame(form_frame, bg='gray20')
            button_frame.grid(row=6, columnspan=2, pady=10)

            add_recolte_btn = ctk.CTkButton(button_frame, text="Enregistrer Récolte", command=self.add_recolte,
                                            fg_color="green")
            add_recolte_btn.pack(side=tk.LEFT, padx=5)

            add_vente_btn = ctk.CTkButton(button_frame, text="Enregistrer Vente", command=self.add_vente, fg_color="red")
            add_vente_btn.pack(side=tk.LEFT, padx=5)

            stock_display_frame = tk.Frame(left_frame, bg='gray20', padx=10, pady=10)
            stock_display_frame.pack(pady=10, fill='both', expand=True)
            tk.Label(stock_display_frame, text="Stock Actuel", font=("Arial", 18, "bold"), bg='gray20', fg='white').pack(
                pady=(0, 10))

            self.stock_tree = ttk.Treeview(stock_display_frame, columns=("Produit", "Quantité"), show="headings")
            self.stock_tree.heading("Produit", text="Produit")
            self.stock_tree.heading("Quantité", text="Quantité (kg/unité)")
            self.stock_tree.column("Produit", width=150, stretch=tk.NO)
            self.stock_tree.column("Quantité", width=150, stretch=tk.NO)
            self.stock_tree.pack(expand=True, fill='both')

            # --- Droite : TabView pour Historiques et Graphiques Séparés ---
            right_frame = tk.Frame(main_frame, bg='gray12')
            right_frame.pack(side=tk.RIGHT, fill='both', expand=True)

            self.history_tabview = ctk.CTkTabview(right_frame, fg_color="gray20", segmented_button_selected_color="cyan")
            self.history_tabview.pack(fill='both', expand=True, padx=10, pady=10)

            # Création des vues spécifiques
            self.create_recolte_view(self.history_tabview.add("Historique des Récoltes"))
            self.create_vente_view(self.history_tabview.add("Historique des Ventes"))

            delete_btn = ctk.CTkButton(right_frame, text="Supprimer la sélection (dans l'onglet actif)",
                                       command=self.delete_entry,
                                       fg_color="firebrick")
            delete_btn.pack(pady=5)

            self.display_all_data()

        # --- MÉTHODES DE MISE À JOUR DES GRAPHIQUES SPÉCIFIQUES ---

        def update_recolte_chart(self):
            """Met à jour le graphique des Récoltes (Quantité par Produit) avec les données réelles."""
            if not self.recolte_canvas: return
            self.recolte_ax.clear()

            data = self.db.get_recolte_quantities_by_product()

            if not data:
                self.recolte_ax.text(0.5, 0.5, "Aucune donnée de récolte.", ha='center', va='center', color='white',
                                     transform=self.recolte_ax.transAxes)
                self.recolte_ax.set_title("Quantité Totale Récoltée", color='cyan', fontsize=12)
                self.recolte_ax.axis('off')
            else:
                produits = [d[0] for d in data]
                quantites = [d[1] for d in data]

                self.recolte_ax.bar(produits, quantites, color='green')
                self.recolte_ax.set_title("Quantité Totale Récoltée", color='cyan', fontsize=12)
                self.recolte_ax.set_ylabel('Quantité (kg/unité)', color='white')
                self.recolte_ax.tick_params(axis='x', rotation=45, colors='white')
                self.recolte_ax.tick_params(axis='y', colors='white')
                self.recolte_ax.grid(axis='y', linestyle='--', alpha=0.5, color='gray')
                self.recolte_ax.set_facecolor('#1F1F1F')  # Réapplique le fond sombre

            self.recolte_fig.tight_layout()
            self.recolte_canvas.draw()

        def update_vente_chart(self):
            """Met à jour le graphique des Ventes (Montant Total par Produit) avec les données réelles."""
            if not self.vente_canvas: return
            self.vente_ax.clear()

            data = self.db.get_vente_amounts_by_product()

            if not data:
                self.vente_ax.text(0.5, 0.5, "Aucune donnée de vente.", ha='center', va='center', color='white',
                                   transform=self.vente_ax.transAxes)
                self.vente_ax.set_title("Proportion des Ventes par Produit ($)", color='cyan', fontsize=12)
                self.vente_ax.axis('off')
            else:
                produits = [d[0] for d in data]
                montants = [d[1] for d in data]

                self.vente_ax.pie(montants, labels=produits, autopct='%1.1f%%', startangle=90,
                                  colors=plt.cm.RdYlBu(range(len(produits))), textprops={'color': "white"})
                self.vente_ax.set_title("Proportion des Ventes par Produit (Top 5 en $)", color='cyan', fontsize=12)
                self.vente_ax.axis('equal')

            self.vente_fig.tight_layout()
            self.vente_canvas.draw()

        def update_chart(self):
            """Mise à jour générale des graphiques de la page."""
            self.update_recolte_chart()
            self.update_vente_chart()

        # --- MÉTHODES D'AFFICHAGE ET DE LOGIQUE ---
        def display_all_data(self):
            self.display_recoltes()
            self.display_ventes()
            self.display_stocks()
            self.update_chart()

        def display_recoltes(self):
            for item in self.recolte_tree.get_children():
                self.recolte_tree.delete(item)

            recoltes_ventes = self.db.get_all_recoltes_ventes()
            for row in recoltes_ventes:
                # row: (id_recolte, nom_produit, quantite, prix_unitaire, montant_total, date_recolte, type)
                if row[6] == 'recolte':
                    # Afficher la quantité en positif pour la récolte
                    values = list(row[:6])
                    values[2] = abs(values[2])
                    self.recolte_tree.insert("", tk.END, values=tuple(values))

        def display_ventes(self):
            for item in self.vente_tree.get_children():
                self.vente_tree.delete(item)

            recoltes_ventes = self.db.get_all_recoltes_ventes()
            for row in recoltes_ventes:
                if row[6] == 'vente':
                    # Afficher la quantité en positif pour la vente (c'est la quantité VENDUE)
                    values = list(row[:6])
                    values[2] = abs(values[2])
                    self.vente_tree.insert("", tk.END, values=tuple(values), tags=('vente',))

        def display_stocks(self):
            for item in self.stock_tree.get_children():
                self.stock_tree.delete(item)

            stocks = self.db.get_all_stocks()
            for stock in stocks:
                self.stock_tree.insert("", tk.END, values=stock)

        def calculate_total_amount(self, event=None):
            try:
                quantite = float(self.quantite_ent.get())
                prix = float(self.prix_unitaire_ent.get())
                montant_total = quantite * prix
                self.montant_total_label.configure(text=f"Montant Total: {montant_total:.2f} $")
            except ValueError:
                self.montant_total_label.configure(text="Montant Total: 0.00 $")

        def validate_inputs(self):
            nom_produit = self.produit_ent.get()
            quantite_str = self.quantite_ent.get()
            prix_unitaire_str = self.prix_unitaire_ent.get()
            date = self.date_ent.get()

            if not all([nom_produit, quantite_str, prix_unitaire_str, date]):
                messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
                return None, None, None, None, None

            try:
                quantite = float(quantite_str)
                prix_unitaire = float(prix_unitaire_str)
                if quantite <= 0 or prix_unitaire <= 0:
                    messagebox.showerror("Erreur", "La quantité et le prix unitaire doivent être des nombres positifs.")
                    return None, None, None, None, None
                montant_total = quantite * prix_unitaire
            except ValueError:
                messagebox.showerror("Erreur", "La quantité et le prix unitaire doivent être des nombres valides.")
                return None, None, None, None, None

            try:
                datetime.strptime(date, '%Y-%m-%d')
            except ValueError:
                messagebox.showerror("Erreur", "Format de date invalide. Utilisez AAAA-MM-JJ.")
                return None, None, None, None, None

            return nom_produit, quantite, prix_unitaire, montant_total, date

        def add_recolte(self):
            nom_produit, quantite, prix_unitaire, montant_total, date = self.validate_inputs()
            if nom_produit is None: return

            if self.db.add_recolte_transaction(nom_produit, quantite, prix_unitaire, montant_total, date):
                messagebox.showinfo("Succès", "Récolte enregistrée avec succès. Le stock a été mis à jour.")
                self.clear_form()
                self.display_all_data()
                self.forward_to_dashboard_callback(update_only=True)  # Met à jour le tableau de bord

        def add_vente(self):
            nom_produit, quantite, prix_unitaire, montant_total, date = self.validate_inputs()
            if nom_produit is None: return

            if self.db.add_vente_transaction(nom_produit, quantite, prix_unitaire, montant_total, date):
                messagebox.showinfo("Succès", "Vente enregistrée avec succès. Le stock a été mis à jour.")
                self.clear_form()
                self.display_all_data()
                self.forward_to_dashboard_callback(update_only=True)  # Met à jour le tableau de bord

        def delete_entry(self):
            # Détermine l'arbre actif pour la suppression
            active_tab_name = self.history_tabview.get()
            if "Récoltes" in active_tab_name:
                active_tree = self.recolte_tree
                entry_type = "recolte"
            elif "Ventes" in active_tab_name:
                active_tree = self.vente_tree
                entry_type = "vente"
            else:
                return

            selected_item = active_tree.selection()
            if not selected_item:
                messagebox.showwarning("Avertissement", "Veuillez sélectionner une entrée à supprimer.")
                return

            item_values = active_tree.item(selected_item, 'values')
            entry_id = item_values[0]
            nom_produit = item_values[1]
            quantite = float(item_values[2])  # Quantité affichée est positive

            if messagebox.askyesno("Confirmation",
                                   f"Êtes-vous sûr de vouloir supprimer cette entrée de {entry_type} (ID: {entry_id}) ?"):
                if self.db.delete_entry(entry_id, nom_produit, quantite, entry_type):
                    messagebox.showinfo("Succès", "Entrée supprimée avec succès. Le stock a été corrigé.")
                    self.display_all_data()
                    self.forward_to_dashboard_callback(update_only=True)  # Met à jour le tableau de bord

        def sort_column(self, tree, col, reverse):
            l = [(tree.set(k, col), k) for k in tree.get_children('')]
            try:
                # Tente de trier numériquement
                l.sort(key=lambda t: float(t[0]), reverse=reverse)
            except ValueError:
                # Sinon, trie par chaîne de caractères
                l.sort(key=lambda t: t[0], reverse=reverse)
            for index, (val, k) in enumerate(l):
                tree.move(k, '', index)
            tree.heading(col, command=lambda: self.sort_column(tree, col, not reverse))

        def clear_form(self):
            self.quantite_ent.delete(0, tk.END)
            self.prix_unitaire_ent.delete(0, tk.END)
            self.montant_total_label.configure(text="Montant Total: 0.00 $")
            self.date_ent.delete(0, tk.END)
            self.date_ent.insert(0, datetime.now().strftime('%Y-%m-%d'))

        def place(self, **kwargs):
            self.page.place(**kwargs)


    # ====================================================================
    # CLASSE 4 : PageManager (Conteneur Principal)
    # Gère les transitions entre les pages.
    # ====================================================================

    class PageManager:
        """Gère l'application principale et le changement de pages."""

        def __init__(self, master):
            self.master = master
            self.master.title("Gestion de la Ferme")
            self.master.geometry("1366x768+10")
            self.db = DatabaseManager()

            self.recolte_vente_page = RecolteVentePage(
                master, self.db,
                self.go_to_champs_placeholder,  # PlaceHolder pour l'instant
                self.go_to_dashboard
            )
            self.dashboard_page = TableauDeBordGlobal(
                master, self.db,
                self.go_to_recolte_vente
            )

            self.current_page = None
            self.go_to_recolte_vente()

        def go_to_recolte_vente(self):
            """Affiche la page de gestion des récoltes/ventes."""
            if self.current_page:
                self.current_page.page.place_forget()
            self.recolte_vente_page.place(x=0, y=0, relwidth=1, relheight=1)
            self.recolte_vente_page.display_all_data()
            self.current_page = self.recolte_vente_page

        def go_to_dashboard(self, update_only=False):
            """Affiche le tableau de bord financier. Mise à jour uniquement si nécessaire."""
            if not update_only:
                if self.current_page:
                    self.current_page.page.place_forget()
                self.dashboard_page.place(x=0, y=0, relwidth=1, relheight=1)
                self.current_page = self.dashboard_page

            self.dashboard_page.update_indicators()

        def go_to_champs_placeholder(self):
            """Fonction factice pour le bouton 'X' (fermeture/retour à la page précédente)."""
            messagebox.showinfo("Navigation", "Action 'Retour aux Champs' (fermer l'onglet) simulée.")
            # Revenir à la page de récolte/vente comme action par défaut
            self.go_to_recolte_vente()

        # ====================================================================


    # POINT D'ENTRÉE PRINCIPAL
    # ====================================================================

    if __name__ == "__main__":
        root = ctk.CTk()
        app = PageManager(root)
        root.mainloop()

#5555555555555555555555555555555555555555555555555555555555555 FIN RECOLTE ET VENTE 55555555555555555555555555555555555
def page_liste_travailleurs():
    def forwaard_to_champs():
        page.destroy()
        champs.update()

    def create_workers_table():
        conn = sqlite3.connect("my_ferme.db")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Travailleurs (
                id_travailleur INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT,
                prenom TEXT,
                poste TEXT
            )
        """)
        conn.commit()
        conn.close()

    def add_worker():
        nom = nom_ent.get()
        prenom = prenom_ent.get()
        poste = poste_ent.get()

        if not nom or not prenom or not poste:
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
            return

        conn = sqlite3.connect("my_ferme.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Travailleurs (nom, prenom, poste) VALUES (?, ?, ?)", (nom, prenom, poste))
        conn.commit()
        conn.close()
        messagebox.showinfo("Succès", "Travailleur enregistré avec succès.")
        nom_ent.delete(0, 'end')
        prenom_ent.delete(0, 'end')
        poste_ent.delete(0, 'end')
        display_workers()

    def display_workers():
        for item in workers_tree.get_children():
            workers_tree.delete(item)

        conn = sqlite3.connect("my_ferme.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Travailleurs")
        workers = cursor.fetchall()
        conn.close()

        for worker in workers:
            workers_tree.insert("", tk.END, values=worker)

    create_workers_table()

    page = tk.Frame(champs, bg='gray12', bd=7)
    titre = Label(page, text="PAGE DE GESTION DES TRAVAILLEURS", font=("TIMES NEW ROMAN", 20),
                  bg='gray12', fg='cyan')
    titre.pack(pady=10)

    my_label = SmallGifLabel(page, gif_path, petite_taille, text="")
    my_label.place(x=90, y=-40, width=400, height=300)

    live = tk.Button(page, text='X', bd=0, bg='gray12', fg='white', font=("Arial", 13), command=forwaard_to_champs)
    live.place(x=1319, y=0, width=40)
    live.bind("<Enter>", lambda e: live.config(bg="red"))
    live.bind("<Leave>", lambda e: live.config(bg="gray12"))

    form_frame = tk.Frame(page, bg='gray20', padx=20, pady=20)
    form_frame.pack(pady=20)

    Label(form_frame, text="Nom:", font=("Arial", 16), bg='gray20', fg='white').grid(row=0, column=0, sticky='w')
    nom_ent = ctk.CTkEntry(form_frame, width=250, font=("Arial", 16))
    nom_ent.grid(row=0, column=1, padx=10, pady=5)

    Label(form_frame, text="Prénom:", font=("Arial", 16), bg='gray20', fg='white').grid(row=1, column=0, sticky='w')
    prenom_ent = ctk.CTkEntry(form_frame, width=250, font=("Arial", 16))
    prenom_ent.grid(row=1, column=1, padx=10, pady=5)

    Label(form_frame, text="Poste:", font=("Arial", 16), bg='gray20', fg='white').grid(row=2, column=0, sticky='w')
    poste_ent = ctk.CTkEntry(form_frame, width=250, font=("Arial", 16))
    poste_ent.grid(row=2, column=1, padx=10, pady=5)

    add_btn = ctk.CTkButton(form_frame, text="Ajouter Travailleur", command=add_worker)
    add_btn.grid(row=3, columnspan=2, pady=10)

    workers_frame = tk.Frame(page, bg='gray20', padx=10, pady=10)
    workers_frame.pack(expand=True, fill='both', padx=20)

    workers_tree = ttk.Treeview(workers_frame, columns=("ID", "Nom", "Prénom", "Poste"), show="headings")
    workers_tree.heading("ID", text="ID")
    workers_tree.heading("Nom", text="Nom")
    workers_tree.heading("Prénom", text="Prénom")
    workers_tree.heading("Poste", text="Poste")
    workers_tree.pack(expand=True, fill='both')
    workers_frame.place(x=0, y=300, width=1350, height=700)

    scrollbar = ttk.Scrollbar(workers_tree, orient="vertical", command=workers_tree.yview)
    scrollbar.pack(side=tk.RIGHT, fill='y')
    workers_tree.configure(yscrollcommand=scrollbar.set)

    display_workers()

    page.place(x=0, y=0, width=2000, height=900)


def page_acheteurs_produits():
    def forwaard_to_champs():
        page.destroy()
        champs.update()

    def add_acheteur():
        nom = nom_ent.get()
        prenom = prenom_ent.get()
        contact = contact_ent.get()
        adresse = adresse_ent.get()

        if not nom or not prenom:
            messagebox.showerror("Erreur", "Le nom et le prénom de l'acheteur sont obligatoires.")
            return

        conn = sqlite3.connect("my_ferme.db")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Acheteurs (nom, prenom, contact, adresse)
            VALUES (?, ?, ?, ?)
        """, (nom, prenom, contact, adresse))
        conn.commit()
        conn.close()

        messagebox.showinfo("Succès", "Acheteur enregistré avec succès.")
        nom_ent.delete(0, 'end')
        prenom_ent.delete(0, 'end')
        contact_ent.delete(0, 'end')
        adresse_ent.delete(0, 'end')
        display_acheteurs()

    def display_acheteurs():
        for item in acheteurs_tree.get_children():
            acheteurs_tree.delete(item)

        conn = sqlite3.connect("my_ferme.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Acheteurs ORDER BY nom ASC")
        acheteurs = cursor.fetchall()
        conn.close()

        for acheteur in acheteurs:
            acheteurs_tree.insert("", tk.END, values=acheteur)

    page = tk.Frame(champs, bg='gray12', bd=7)
    titre = Label(page, text="PAGE DE GESTION DES ACHETEURS DE PRODUITS", font=("TIMES NEW ROMAN", 20),
                  bg='gray12', fg='cyan')
    titre.pack(pady=10)

    live = tk.Button(page, text='X', bd=0, bg='gray12', fg='white', font=("Arial", 13), command=forwaard_to_champs)
    live.place(x=1319, y=0, width=40)
    live.bind("<Enter>", lambda e: live.config(bg="red"))
    live.bind("<Leave>", lambda e: live.config(bg="gray12"))

    form_frame = tk.Frame(page, bg='gray20', padx=20, pady=20)
    form_frame.pack(pady=20)

    Label(form_frame, text="Nom:", font=("Arial", 16), bg='gray20', fg='white').grid(row=0, column=0, sticky='w')
    nom_ent = ctk.CTkEntry(form_frame, width=250, font=("Arial", 16))
    nom_ent.grid(row=0, column=1, padx=10, pady=5)

    Label(form_frame, text="Prénom:", font=("Arial", 16), bg='gray20', fg='white').grid(row=1, column=0, sticky='w')
    prenom_ent = ctk.CTkEntry(form_frame, width=250, font=("Arial", 16))
    prenom_ent.grid(row=1, column=1, padx=10, pady=5)

    Label(form_frame, text="Contact:", font=("Arial", 16), bg='gray20', fg='white').grid(row=2, column=0, sticky='w')
    contact_ent = ctk.CTkEntry(form_frame, width=250, font=("Arial", 16))
    contact_ent.grid(row=2, column=1, padx=10, pady=5)

    Label(form_frame, text="Adresse:", font=("Arial", 16), bg='gray20', fg='white').grid(row=3, column=0, sticky='w')
    adresse_ent = ctk.CTkEntry(form_frame, width=250, font=("Arial", 16))
    adresse_ent.grid(row=3, column=1, padx=10, pady=5)

    add_btn = ctk.CTkButton(form_frame, text="Ajouter Acheteur", command=add_acheteur)
    add_btn.grid(row=4, columnspan=2, pady=10)

    acheteurs_frame = tk.Frame(page, bg='gray20', padx=10, pady=10)
    # acheteurs_frame.pack(expand=True, fill='both', padx=20)
    acheteurs_frame.place(x=0, y=400, width=1350, height=700)

    acheteurs_tree = ttk.Treeview(acheteurs_frame, columns=("ID", "Nom", "Prénom", "Contact", "Adresse"),
                                  show="headings")
    acheteurs_tree.heading("ID", text="ID")
    acheteurs_tree.heading("Nom", text="Nom")
    acheteurs_tree.heading("Prénom", text="Prénom")
    acheteurs_tree.heading("Contact", text="Contact")
    acheteurs_tree.heading("Adresse", text="Adresse")
    acheteurs_tree.pack(expand=True, fill='both')

    scrollbar = ttk.Scrollbar(acheteurs_tree, orient="vertical", command=acheteurs_tree.yview)
    scrollbar.pack(side=tk.RIGHT, fill='y')
    acheteurs_tree.configure(yscrollcommand=scrollbar.set)

    display_acheteurs()

    page.place(x=0, y=0, width=2000, height=900)


def page_terrains_enregistrements():
    def forwaard_to_champs():
        page.destroy()
        champs.update()

    def create_terrains_table():
        conn = sqlite3.connect("my_ferme.db")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Terrains (
                id_terrain INTEGER PRIMARY KEY AUTOINCREMENT,
                nom_terrain TEXT,
                superficie REAL,
                unite_superficie TEXT,
                localisation TEXT
            )
        """)
        conn.commit()
        conn.close()

    def add_terrain():
        nom_terrain = nom_ent.get()
        superficie = superficie_ent.get()
        unite_superficie = unite_ent.get()
        localisation = localisation_ent.get()

        if not nom_terrain or not superficie or not unite_superficie or not localisation:
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
            return

        try:
            superficie = superficie
        except ValueError:
            messagebox.showerror("Erreur", "La superficie doit être un nombre.")
            return

        conn = sqlite3.connect("my_ferme.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Terrains (nom_terrain, superficie, unite_superficie, localisation) VALUES (?, ?, ?, ?)",
            (nom_terrain, superficie, unite_superficie, localisation))
        conn.commit()
        conn.close()
        messagebox.showinfo("Succès", "Terrain enregistré avec succès.")
        nom_ent.delete(0, 'end')
        superficie_ent.delete(0, 'end')
        unite_ent.set("Hectare (ha)")
        localisation_ent.delete(0, 'end')
        display_terrains()

    def display_terrains():
        for item in terrains_tree.get_children():
            terrains_tree.delete(item)

        conn = sqlite3.connect("my_ferme.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Terrains")
        terrains = cursor.fetchall()
        conn.close()

        for terrain in terrains:
            terrains_tree.insert("", tk.END, values=terrain)

    def delete_terrain():
        selected_item = terrains_tree.selection()
        if not selected_item:
            messagebox.showwarning("Avertissement", "Veuillez sélectionner un terrain à supprimer.")
            return

        terrain_id = terrains_tree.item(selected_item)['values'][0]

        confirmation = messagebox.askyesno("Confirmer la suppression",
                                           f"Êtes-vous sûr de vouloir supprimer ce terrain (ID: {terrain_id}) ?")
        if confirmation:
            conn = sqlite3.connect("my_ferme.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Terrains WHERE id_terrain = ?", (terrain_id,))
            conn.commit()
            conn.close()
            display_terrains()
            messagebox.showinfo("Succès", "Terrain supprimé avec succès.")

    create_terrains_table()

    page = tk.Frame(champs, bg='gray12', bd=7)
    titre = Label(page, text="PAGE D'ENREGISTREMENT ET DE GESTION DES TERRAINS", font=("TIMES NEW ROMAN", 18),
                  bg='gray12', fg='cyan')
    titre.place(x=290, y=0, height=40, width=700)

    live = tk.Button(page, text='X', bd=0, bg='gray12', fg='white', font=("Arial", 13), command=forwaard_to_champs)
    live.place(x=1319, y=0, width=40)
    live.bind("<Enter>", lambda e: live.config(bg="red"))
    live.bind("<Leave>", lambda e: live.config(bg="gray12"))

    form_frame = tk.Frame(page, bg='gray20', padx=20, pady=20)
    form_frame.place(x=500, y=90, height=400, width=600)

    Label(form_frame, text="Nom du terrain:", font=("Arial", 16), bg='gray20', fg='white').grid(row=0, column=0,
                                                                                                sticky='w')
    nom_ent = ctk.CTkEntry(form_frame, width=250, font=("Arial", 16))
    nom_ent.grid(row=0, column=1, padx=10, pady=5)

    Label(form_frame, text="Superficie:", font=("Arial", 16), bg='gray20', fg='white').grid(row=1, column=0, sticky='w')
    superficie_ent = ctk.CTkEntry(form_frame, width=250, font=("Arial", 16))
    superficie_ent.grid(row=1, column=1, padx=10, pady=5)

    Label(form_frame, text="Unité de mesure:", font=("Arial", 16), bg='gray20', fg='white').grid(row=2, column=0,
                                                                                                 sticky='w')
    unite_options = ["Hectare (ha)", "Acre (ac)", "Mètre carré (m²)"]
    unite_ent = ctk.CTkComboBox(form_frame, values=unite_options, width=250, font=("Arial", 16))
    unite_ent.set("Hectare (ha)")
    unite_ent.grid(row=2, column=1, padx=10, pady=5)

    Label(form_frame, text="Localisation:", font=("Arial", 16), bg='gray20', fg='white').grid(row=3, column=0,
                                                                                              sticky='w')
    localisation_ent = ctk.CTkEntry(form_frame, width=250, font=("Arial", 16))
    localisation_ent.grid(row=3, column=1, padx=10, pady=5)

    add_btn = ctk.CTkButton(form_frame, text="Ajouter Terrain", command=add_terrain)
    add_btn.grid(row=4, columnspan=2, pady=10)

    terrains_frame = tk.Frame(page, bg='gray20', padx=10, pady=10)
    terrains_frame.place(x=0, y=500, width=1350, height=700)

    terrains_tree = ttk.Treeview(terrains_frame, columns=("ID", "Nom", "Superficie", "Unité", "Localisation"),
                                 show="headings")
    terrains_tree.heading("ID", text="ID")
    terrains_tree.heading("Nom", text="Nom du Terrain")
    terrains_tree.heading("Superficie", text="Superficie")
    terrains_tree.heading("Unité", text="Unité")
    terrains_tree.heading("Localisation", text="Localisation")
    terrains_tree.pack(side=tk.LEFT, expand=True, fill='both')

    scrollbar = ttk.Scrollbar(terrains_frame, orient="vertical", command=terrains_tree.yview)
    scrollbar.pack(side=tk.RIGHT, fill='y')
    terrains_tree.configure(yscrollcommand=scrollbar.set)

    action_frame = tk.Frame(page, bg='gray12')
    action_frame.pack(pady=10)

    refresh_btn = ctk.CTkButton(form_frame, text="Actualiser", command=display_terrains, height=40, width=210)
    refresh_btn.place(x=0, y=300)

    delete_btn = ctk.CTkButton(form_frame, text="Supprimer le terrain sélectionné", command=delete_terrain, height=40,
                               width=210)
    delete_btn.place(x=300, y=300)

    display_terrains()

    page.place(x=0, y=0, width=2000, height=900)


def page_logistique():
    def forwaard_to_champs():
        page.destroy()
        champs.update()

    def add_intrant():
        nom = nom_intrant_ent.get()
        quantite = quantite_intrant_ent.get()
        unite = unite_intrant_ent.get()
        date = date_achat_ent.get()
        fournisseur = fournisseur_ent.get()

        if not all([nom, quantite, unite, date, fournisseur]):
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
            return

        conn = sqlite3.connect("my_ferme.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Intrants (nom_intrant, quantite, unite, date_achat, fournisseur) VALUES (?, ?, ?, ?, ?)",
            (nom, quantite, unite, date, fournisseur))
        conn.commit()
        conn.close()
        messagebox.showinfo("Succès", "Intrant ajouté avec succès.")
        display_intrants()
        nom_intrant_ent.delete(0, 'end')
        quantite_intrant_ent.delete(0, 'end')
        unite_intrant_ent.delete(0, 'end')
        date_achat_ent.delete(0, 'end')
        fournisseur_ent.delete(0, 'end')

    def display_intrants():
        for item in intrants_tree.get_children():
            intrants_tree.delete(item)

        conn = sqlite3.connect("my_ferme.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Intrants")
        intrants = cursor.fetchall()
        conn.close()

        for intrant in intrants:
            intrants_tree.insert("", tk.END, values=intrant)

    page = tk.Frame(champs, bg='gray12', bd=7)
    titre = Label(page, text="PAGE DE GESTION LOGISTIQUE (INTRANTS)", font=("TIMES NEW ROMAN", 20), bg='gray12',
                  fg='cyan')
    titre.pack(pady=10)

    live = tk.Button(page, text='X', bd=0, bg='gray12', fg='white', font=("Arial", 13), command=forwaard_to_champs)
    live.place(x=1319, y=0, width=40)
    live.bind("<Enter>", lambda e: live.config(bg="red"))
    live.bind("<Leave>", lambda e: live.config(bg="gray12"))

    add_frame = tk.LabelFrame(page, text="Ajouter un Intrant", bg='gray20', fg='white', padx=10, pady=10)
    add_frame.pack(pady=10)

    Label(add_frame, text="Nom Intrant:", font=("Arial", 12), bg='gray20', fg='white').grid(row=0, column=0, sticky='w',
                                                                                            padx=5, pady=2)
    nom_intrant_ent = ctk.CTkEntry(add_frame, width=200, font=("Arial", 12))
    nom_intrant_ent.grid(row=0, column=1, padx=5, pady=2)

    Label(add_frame, text="Quantité:", font=("Arial", 12), bg='gray20', fg='white').grid(row=1, column=0, sticky='w',
                                                                                         padx=5, pady=2)
    quantite_intrant_ent = ctk.CTkEntry(add_frame, width=200, font=("Arial", 12))
    quantite_intrant_ent.grid(row=1, column=1, padx=5, pady=2)

    Label(add_frame, text="Unité:", font=("Arial", 12), bg='gray20', fg='white').grid(row=2, column=0, sticky='w',
                                                                                      padx=5, pady=2)
    unite_intrant_ent = ctk.CTkEntry(add_frame, width=200, font=("Arial", 12))
    unite_intrant_ent.grid(row=2, column=1, padx=5, pady=2)

    Label(add_frame, text="Date Achat (YYYY-MM-DD):", font=("Arial", 12), bg='gray20', fg='white').grid(row=3, column=0,
                                                                                                        sticky='w',
                                                                                                        padx=5, pady=2)
    date_achat_ent = ctk.CTkEntry(add_frame, width=200, font=("Arial", 12))
    date_achat_ent.grid(row=3, column=1, padx=5, pady=2)

    Label(add_frame, text="Fournisseur:", font=("Arial", 12), bg='gray20', fg='white').grid(row=4, column=0, sticky='w',
                                                                                            padx=5, pady=2)
    fournisseur_ent = ctk.CTkEntry(add_frame, width=200, font=("Arial", 12))
    fournisseur_ent.grid(row=4, column=1, padx=5, pady=2)

    ctk.CTkButton(add_frame, text="Ajouter Intrant", command=add_intrant).grid(row=5, columnspan=2, pady=10)

    display_frame = tk.LabelFrame(page, text="Liste des Intrants", bg='gray20', fg='white', padx=10, pady=10)
    display_frame.pack(fill='both', expand=True, padx=20, pady=10)

    intrants_tree = ttk.Treeview(display_frame,
                                 columns=("ID", "Nom", "Quantité", "Unité", "Date d'Achat", "Fournisseur"),
                                 show="headings")
    intrants_tree.heading("ID", text="ID")
    intrants_tree.heading("Nom", text="Nom Intrant")
    intrants_tree.heading("Quantité", text="Quantité")
    intrants_tree.heading("Unité", text="Unité")
    intrants_tree.heading("Date d'Achat", text="Date d'Achat")
    intrants_tree.heading("Fournisseur", text="Fournisseur")
    # intrants_tree.pack(side=tk.LEFT, fill='both', expand=True)
    intrants_tree.place(x=-10, y=0, width=1300, height=300)

    scrollbar = ttk.Scrollbar(display_frame, orient="vertical", command=intrants_tree.yview)
    scrollbar.pack(side=tk.RIGHT, fill='y')
    intrants_tree.configure(yscrollcommand=scrollbar.set)

    display_intrants()

    page.place(x=0, y=0, width=1380, height=700)


# ==================== NOUVELLE PAGE: GESTION DES VENTES ====================
def page_gestion_ventes():
    def forwaard_to_champs():
        page.destroy()
        champs.update()

    def fetch_produits():
        conn = sqlite3.connect("my_ferme.db")
        cursor = conn.cursor()
        cursor.execute("SELECT nom_produit FROM Produits")
        produits = [row[0] for row in cursor.fetchall()]
        conn.close()
        return produits

    def fetch_acheteurs():
        conn = sqlite3.connect("my_ferme.db")
        cursor = conn.cursor()
        cursor.execute("SELECT nom FROM Acheteurs")
        acheteurs = [row[0] for row in cursor.fetchall()]
        conn.close()
        return acheteurs

    def record_sale():
        produit_vendu = produit_ventes_ent.get()
        prix_par_kg_vendu = prix_ent.get()
        acheteur_vendu = acheteur_ventes_ent.get()
        quantite_vendue = quantite_ventes_ent.get()
        prix_total = prix_total_ent.get()
        date_vente = date_ventes_ent.get()

        if not all([produit_vendu, prix_par_kg_vendu,acheteur_vendu, quantite_vendue, prix_total, date_vente]):
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs de la vente.")
            return

        try:
            quantite = float(quantite_vendue)
            prix = float(prix_par_kg_vendu)
        except ValueError:
            messagebox.showerror("Erreur", "La quantité et le prix total doivent être des nombres.")
            return

        # VÉRIFICATION DU STOCK AVANT LA VENTE
        conn = sqlite3.connect("my_ferme.db")
        cursor = conn.cursor()
        cursor.execute("SELECT quantite FROM Stock WHERE nom_produit = ?", (produit_vendu,))
        stock_actuel = cursor.fetchone()

        if stock_actuel and stock_actuel[0] >= quantite:
            # Procéder à la vente et mettre à jour le stock
            nouvelle_quantite = stock_actuel[0] - quantite
            cursor.execute("UPDATE Stock SET quantite = ? WHERE nom_produit = ?", (nouvelle_quantite, produit_vendu))
            cursor.execute(
                "INSERT INTO Ventes (produit, acheteur, quantite, prix_total,prix_par_kg, date_vente) VALUES (?, ?, ?, ?, ?,?)",
                (produit_vendu, acheteur_vendu, quantite, prix,prix_par_kg_vendu, date_vente))
            conn.commit()
            messagebox.showinfo("Succès", "Vente enregistrée avec succès. Le stock a été mis à jour.")
            quantite_ventes_ent.delete(0, 'end')
            #prix_total_ent.delete(0, 'end')
        else:
            messagebox.showerror("Erreur de Stock",
                                 f"Stock insuffisant pour le produit '{produit_vendu}'. Stock actuel: {stock_actuel[0] if stock_actuel else 0}.")

        conn.close()
        display_ventes()
        update_total_sales()

    def display_ventes():
        for item in ventes_tree.get_children():
            ventes_tree.delete(item)

        conn = sqlite3.connect("my_ferme.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Ventes ORDER BY date_vente DESC")
        ventes = cursor.fetchall()
        conn.close()

        for vente in ventes:
            ventes_tree.insert("", tk.END, values=vente)

    def update_total_sales():
        conn = sqlite3.connect("my_ferme.db")
        cursor = conn.cursor()
        cursor.execute("SELECT SUM(prix_total) FROM Ventes")
        total = cursor.fetchone()[0]
        conn.close()

        if total is None:
            total = 0.0

        total_sales_label.configure(text=f"Total des ventes cumulées : {total:.2f} $")

    page = tk.Frame(champs, bg='gray12', bd=7)
    titre = Label(page, text="PAGE DE GESTION DES VENTES", font=("TIMES NEW ROMAN", 20),
                  bg='gray12', fg='cyan')
    titre.pack(pady=10)

    live = tk.Button(page, text='X', bd=0, bg='gray12', fg='white', font=("Arial", 13), command=forwaard_to_champs)
    live.place(x=1319, y=0, width=40)
    live.bind("<Enter>", lambda e: live.config(bg="red"))
    live.bind("<Leave>", lambda e: live.config(bg="gray12"))

    # Formulaire d'enregistrement de vente
    form_frame = tk.Frame(page, bg='gray20', padx=20, pady=20)
    form_frame.pack(pady=20,ipadx=200)

    Label(form_frame, text="Produit vendu:", font=("Arial", 16), bg='gray20', fg='white').grid(row=0, column=0,
                                                                                               sticky='w')
    produit_ventes_ent = ctk.CTkComboBox(form_frame, values=fetch_produits(), width=250, font=("Arial", 16))
    produit_ventes_ent.grid(row=0, column=1, padx=10, pady=5)

    Label(form_frame, text="Acheteur:", font=("Arial", 16), bg='gray20', fg='white').grid(row=1, column=0, sticky='w')
    acheteur_ventes_ent = ctk.CTkComboBox(form_frame, values=fetch_acheteurs(), width=250, font=("Arial", 16))
    acheteur_ventes_ent.grid(row=1, column=1, padx=10, pady=5)

    Label(form_frame, text="Quantité:", font=("Arial", 16), bg='gray20', fg='white').grid(row=2, column=0, sticky='w')
    quantite_ventes_ent = ctk.CTkEntry(form_frame, width=250, font=("Arial", 16))
    quantite_ventes_ent.grid(row=2, column=1, padx=10, pady=5)

    Label_prix=Label(form_frame, text="Prix Total (Fc):", font=("Arial", 16), bg='gray20', fg='white').grid(row=3, column=0,
                                                                                                sticky='w')
    prix_ent = ctk.CTkEntry(form_frame, width=250, font=("Arial", 16))
    prix_ent.grid(row=3, column=1, padx=10, pady=5)

    Label(form_frame, text="Prix Par Kg (fc):", font=("Arial", 16), bg='gray20', fg='white').grid(row=0, column=2,
                                                                                                sticky='w')
    prix_total_ent = ctk.CTkComboBox(form_frame, width=250, font=("Arial", 16))
    prix_total_ent.grid(row=0, column=3, padx=10, pady=5)


    Label(form_frame, text="Date (AAAA-MM-JJ):", font=("Arial", 16), bg='gray20', fg='white').grid(row=4, column=0,
                                                                                                   sticky='w')
    date_ventes_ent = ctk.CTkEntry(form_frame, width=250, font=("Arial", 16))
    date_ventes_ent.grid(row=4, column=1, padx=10, pady=5)
    date_ventes_ent.insert(0, datetime.now().strftime("%Y-%m-%d"))

    add_btn = ctk.CTkButton(form_frame, text="Enregistrer la vente", command=record_sale)
    add_btn.grid(row=5, columnspan=2, pady=10)

    # Affichage des ventes et de la sommation
    display_frame = tk.Frame(page, bg='gray20', padx=10, pady=10)
    display_frame.pack(expand=True, fill='both', padx=20, pady=10)

    ventes_tree = ttk.Treeview(display_frame, columns=("ID", "Produit", "Acheteur", "Quantité", "Prix Total", "Date"),
                               show="headings")
    ventes_tree.heading("ID", text="ID Vente")
    ventes_tree.heading("Produit", text="Produit Vendu")
    ventes_tree.heading("Acheteur", text="Acheteur")
    ventes_tree.heading("Quantité", text="Quantité")
    ventes_tree.heading("Prix Total", text="Prix Total ($)")
    ventes_tree.heading("Date", text="Date")
    ventes_tree.pack(expand=True, fill='both')

    scrollbar = ttk.Scrollbar(display_frame, orient="vertical", command=ventes_tree.yview)
    # scrollbar.pack(side=tk.RIGHT, fill='y')
    scrollbar.place(x=1270, y=0, width=20, height=270)
    ventes_tree.configure(yscrollcommand=scrollbar.set)

    total_sales_label = Label(page, text="Total des ventes cumulées : 0.00 $", font=("Arial", 20), bg='gray12',
                              fg='yellow')
    total_sales_label.place(x=0, y=0, height=40, width=710)

    display_ventes()
    update_total_sales()

    page.place(x=0, y=0, width=1360, height=700)


# ==================== FIN NOUVELLE PAGE ====================
#def page_emplacement():
#    def forwaard_to_champs():
#        emplacement_fm.destroy()
#        champs.update()
#
#    def fetch_produits():
#        conn = sqlite3.connect("my_ferme.db")
#        cursor = conn.cursor()
#        cursor.execute("SELECT nom_produit FROM Produits")
#        produits = [row[0] for row in cursor.fetchall()]
#        conn.close()
#        #print(produits)
#        return produits
#
#    def fetch_superficie():
#        conn = sqlite3.connect("my_ferme.db")
#        cursor = conn.cursor()
#        cursor.execute("SELECT superficie FROM Terrains")
#        superficie= [row[0] for row in cursor.fetchall()]
#        conn.close()
#        #print(superficie)
#        return superficie
#    fetch_superficie()
#
#
#    def add_data_emplacemet(Total_Hectares, TotalHectares_a_Exploiter, PH_du_Secteur, Produits_a_Exploiter, Surface,
#                            Kg_de_semance_hectare, N_mesure_d_angree, RECOLTE_ENVISAGEE, RECOLTEREEL,
#                            Depences_effectuer, Detail_sur_les_Depences, Date):
#        conn = sqlite3.connect("my_ferme.db")
#        cursor = conn.cursor()
#        cursor.execute(f"""INSERT INTO Emplacement VALUES("{Total_Hectares}","{TotalHectares_a_Exploiter}","{PH_du_Secteur}","{Produits_a_Exploiter}","{Surface}","{Kg_de_semance_hectare}","{N_mesure_d_angree}","{RECOLTE_ENVISAGEE}", "{RECOLTEREEL}","{Depences_effectuer}","{Detail_sur_les_Depences}","{Date}") """)
#        conn.commit()
#        conn.close()
#    def check_inpoot_validation():
#
#        if tolat_hectare_ent.get() == "":
#            tolat_hectare_ent.configure(border_color='red')
#            tolat_hectare_ent.focus()
#            #messagebox.showerror("Erreur", "Veuillez choisir un Nom de Produit.")
#            message_box(message="Erreur, \nLe Champs Nom est Vide")
#        elif tolat_hectare_ent_aexploiter_ent.get() == "":
#            tolat_hectare_ent_aexploiter_ent.configure(border_color='red')
#            tolat_hectare_ent_aexploiter_ent.focus()
#            message_box(message="Erreur, \nLe Champs Fournisseur est Vide")
#        elif Ph_du_secteur_ent.get()== '':
#            Ph_du_secteur_ent.configure(border_color='red')
#            Ph_du_secteur_ent.focus()
#            #messagebox.showerror("Erreur", "Veuillez remplir le nom de fournisseur.")
#            message_box(message="Erreur, \nLe Champs Fournisseur est Vide")
#        elif Produit_aexoloiter_ent.get() == "":
#            Produit_aexoloiter_ent.configure(border_color='red')
#            Produit_aexoloiter_ent.focus()
#            message_box(message="Erreur, \nLe Champs Fournisseur est Vide")
#        elif Nombre_heta_ent.get()=='':
#            Nombre_heta_ent.configure(border_color='red')
#            Nombre_heta_ent.focus()
#            message_box(message="Erreur, \nLe Champs Fournisseur est Vide")
#        elif Nombre_Kg_ent.get()=="":
#            Nombre_Kg_ent.configure(border_color='red')
#            Nombre_Kg_ent.focus()
#            message_box(message="Erreur, \nLe Champs Fournisseur est Vide")
#        elif nombre_mesur_amgree_heta_ent.get()=="":
#            nombre_mesur_amgree_heta_ent.configure(border_color='red')
#            nombre_mesur_amgree_heta_ent.focus()
#            message_box(message="Erreur, \nLe Champs Fournisseur est Vide")
#        elif recolt_envisager_ent.get()=="":
#            recolt_envisager_ent.configure(border_color='red')
#            recolt_envisager_ent.focus()
#            message_box(message="Erreur, \nLe Champs Fournisseur est Vide")
#        elif recolt_reel_ent.get()=="":
#            recolt_reel_ent.configure(border_color='red')
#            recolt_reel_ent.focus()
#            message_box(message="Erreur, \nLe Champs Fournisseur est Vide")
#        elif depenxe_effectuer_ent.get() =="":
#            depenxe_effectuer_ent.configure(border_color='red')
#            depenxe_effectuer_ent.focus()
#            message_box(message="Erreur, \nLe Champs Fournisseur est Vide")
#        elif detail_sur_depence_ent.get("0.0","end").strip() =="":
#            detail_sur_depence_ent.configure(border_color='red')
#            detail_sur_depence_ent.focus()
#            message_box(message="Erreur, \nLe Champs Fournisseur est Vide")
#        elif date_ent.get()=="":
#            date_ent.configure(border_color='red')
#            date_ent.focus()
#            message_box(message="Erreur, \nLe Champs Fournisseur est Vide")
#        else:
#            add_data_emplacemet(Total_Hectares = tolat_hectare_ent.get(),TotalHectares_a_Exploiter = tolat_hectare_ent_aexploiter_ent.get(),PH_du_Secteur = Ph_du_secteur_ent.get(),Produits_a_Exploiter = Produit_aexoloiter_ent.get(),Surface = Nombre_heta_ent.get(),
#                            Kg_de_semance_hectare = Nombre_Kg_ent.get(),N_mesure_d_angree = nombre_mesur_amgree_heta_ent.get(),RECOLTE_ENVISAGEE = recolt_envisager_ent.get(),RECOLTEREEL = recolt_reel_ent.get() ,
#                            Depences_effectuer = depenxe_effectuer_ent.get(),Detail_sur_les_Depences = detail_sur_depence_ent.get("0.0","end").strip(),Date=date_ent.get())
#        message_box(message='Les Donnees Enregistrer Avec succee')
#
#    #def coulleur1(event):
#       # live.config(bg="red")
#
#    #def couleur2(event):
#       # live.config(bg='gray12')
#    emplacement_fm=tk.Frame(champs,bg='gray12')
#
#    LISTE= ["Hectare (ha)", "Acre (ac)", "Mètre carré (m²)"]
#
#    titre = Label(emplacement_fm, text="TABLEAU EMPLACEMT (INVESTISSEMEMT & DEPENCES)", font=("TIMES NEW ROMAN", 20),
#                  bg='gray12', fg='cyan')
#    titre.pack(pady=10)
#
#    live = tk.Button(emplacement_fm, text='X', bd=0, bg='gray12', fg='white', font=("Arial", 13), command=forwaard_to_champs)
#    live.place(x=1319, y=0, width=40)
#    live.bind("<Enter>", lambda e: live.config(bg="red"))
#    live.bind("<Leave>", lambda e: live.config(bg="gray12"))
#
#    # Formulaire d'enregistrement de vente
#    form_frame = tk.Frame(emplacement_fm, bg='gray20', padx=20, pady=20)
#    #form_frame.pack(pady=20)
#    form_frame.place(x=10,y=90,width=1360, height=600)
#
#    Label(form_frame, text="Total Hectares:", font=("Arial", 16), bg='gray20', fg='white').grid(row=0, column=0,
#                                                                                               sticky='w')
#    tolat_hectare_ent = ctk.CTkComboBox(form_frame, width=250, font=("Arial", 16))
#    tolat_hectare_ent.grid(row=0, column=1, padx=10, pady=5)
#
#    Label(form_frame, text="Total Hectares a Exploiter :", font=("Arial", 16), bg='gray20', fg='white').grid(row=1, column=0, sticky='w')
#    tolat_hectare_ent_aexploiter_ent = ctk.CTkEntry(form_frame, width=250, font=("Arial", 16))
#    tolat_hectare_ent_aexploiter_ent.grid(row=1, column=1, padx=10, pady=5)
#
#    Label(form_frame, text="PH du Secteur:", font=("Arial", 16), bg='gray20', fg='white').grid(row=2, column=0, sticky='w')
#    Ph_du_secteur_ent = ctk.CTkEntry(form_frame, width=250, font=("Arial", 16))
#    Ph_du_secteur_ent.grid(row=2, column=1, padx=10, pady=5)
#
#    Label(form_frame, text="Produits a Exploiter :", font=("Arial", 16), bg='gray20', fg='white').grid(row=3, column=0,
#                                                                                                sticky='w')
#    Produit_aexoloiter_ent = ctk.CTkComboBox(form_frame, width=250, font=("Arial", 16),values=fetch_produits())
#    Produit_aexoloiter_ent.grid(row=3, column=1, padx=10, pady=5)
#
#    Label(form_frame, text=" Surface ", font=("Arial", 16), bg='gray20', fg='white').grid(row=2, column=2,
#                                                                                                       sticky='w')
#    Nombre_heta_ent = ctk.CTkComboBox(form_frame, width=150, font=("Arial", 16),values=LISTE)
#    Nombre_heta_ent.grid(row=3, column=2, padx=10, pady=5)
#
#    Label(form_frame, text="Kg de semance/hectare", font=("Arial", 16), bg='gray20', fg='gray40').grid(row=2, column=3,
#                                                                                                  sticky='w')
#    Nombre_Kg_ent = ctk.CTkEntry(form_frame, width=150, font=("Arial", 16))
#    Nombre_Kg_ent.grid(row=3, column=3, padx=10, pady=5)
#
#    Label(form_frame, text="N* mesure d'angree", font=("Arial", 16), bg='gray20', fg='cyan').grid(row=2, column=4,
#                                                                                                       sticky='nw')
#    nombre_mesur_amgree_heta_ent = ctk.CTkEntry(form_frame, width=150, font=("Arial", 16))
#    nombre_mesur_amgree_heta_ent.grid(row=3, column=4, padx=10, pady=5)
#
#    Label(form_frame, text="RECOLTE ENVISAGEE :", font=("Arial", 16), bg='gray20', fg='white').grid(row=4, column=0,
#                                                                                                       sticky='w')
#    recolt_envisager_ent = ctk.CTkEntry(form_frame, width=250, font=("Arial", 16))
#    recolt_envisager_ent.grid(row=4, column=1, padx=10, pady=5)
#
#    Label(form_frame, text="RECOLTE REEL :", font=("Arial", 16), bg='gray20', fg='white').grid(row=4, column=2,
#                                                                                                    sticky='w')
#    recolt_reel_ent = ctk.CTkEntry(form_frame, width=250, font=("Arial", 16))
#    recolt_reel_ent.grid(row=4, column=3, padx=10, pady=5)
#
#    Label(form_frame, text="Depences effectuer", font=("Arial", 16), bg='gray20', fg='white').grid(row=5, column=0,
#                                                                                               sticky='w')
#    depenxe_effectuer_ent = ctk.CTkEntry(form_frame, width=250, font=("Arial", 16))
#    depenxe_effectuer_ent.grid(row=5, column=1, padx=10, pady=5)
#
#    Label(form_frame, text="Detail sur les Depences ", font=("Arial", 16), bg='gray20', fg='white').grid(row=9, column=0,
#                                                                                                   sticky='w')
#    detail_sur_depence_ent = ctk.CTkTextbox(form_frame, width=350, height=260,font=("Arial", 16))
#    detail_sur_depence_ent.grid(row=10, column=0, padx=10, pady=0)
#
#
#
#    Label(form_frame, text="Date (AAAA-MM-JJ):", font=("Arial", 16), bg='gray20', fg='white').grid(row=7, column=2,
#                                                                                                   sticky='w')
#    date_ent = ctk.CTkEntry(form_frame, width=250, font=("Arial", 16))
#    date_ent.grid(row=7, column=3, padx=10, pady=5)
#    date_ent.insert(0, datetime.now().strftime("%Y-%m-%d"))
#
#    add_btn = ctk.CTkButton(form_frame, text="Enregistrer les donees", command=check_inpoot_validation,width=250)
#    add_btn.grid(row=10, columnspan=7, pady=10)
#
#
##        elif check_if_id_allready_exist(id_produit_a_verifier=id_p):
##            id_de_produit_ent.configure(border_color='red')
##            id_de_produit_ent.focus()
##            message_box(message=f"Erreur,l'ID {id_p} existe déjà. \nVeuillez utiliser un autre ID.")
##            #messagebox.showerror("Erreur", f"Le produit avec \n l'ID {id_p} existe déjà. \nVeuillez utiliser \nun autre ID.")
##        elif check_if_name_allready_exist(nom_produit_a_verifier=nom_p):
##            nom_produit_ent.configure(border_color='red')
##            nom_produit_ent.focus()
##            #messagebox.showerror("Erreur", f"Le produit \n'{nom_p}' est déjà enregistré. ")
##            message_box(message=f"Erreur,le nom {nom_p} existe déjà. \nVeuillez utiliser un autre Nom")
##        else:
##            add_data(nom_produit=nom_p,
##                     id_produit=id_p,
##                     fournisseur=fournisseur_p)
##            message_box(message=f'Felicitation,{nom_p} a été enregistré \navec succès !')
##            nom_produit_ent.set('Choisissez une culture')
##            id_de_produit_ent.configure(state=ctk.NORMAL)
##            id_de_produit_ent.delete(0, ctk.END)
##            fournisseur_produit_ent.delete(0, ctk.END)
##            generate_id_number()
#
#
#
#
#
#    emplacement_fm.place(x=0, y=0, width=1360, height=700)
#    fetch_produits()
#
#
#
#
#
## Remarque : Les fonctions `donnnees_emplacement`, `champs`, `delete_terrain`
## et `display_terrains` ne sont pas définies dans le code ci-dessous.
## Ce code suppose qu'elles existent dans le reste de votre application.
#
#def donnnees_emplacement(champs):
#    """
#    Fonction principale pour l'interface utilisateur des données d'emplacement.
#    Modifiée pour une meilleure génération de PDF.
#    """
#
#    def forwaard_to_champs():
#        emplacement_fm.destroy()
#        champs.update()
#
#    def fetch_emplacement():
#        conn = sqlite3.connect("my_ferme.db")
#        cursor = conn.cursor()
#        cursor.execute("SELECT * FROM Emplacement")
#        super = cursor.fetchall()
#        conn.close()
#        print(super)
#        return super
#
#    def save_to_pdf():
#        """
#        Sauvegarde les données du treeview dans un fichier PDF en demandant
#        à l'utilisateur un emplacement de sauvegarde.
#        """
#        headers = [emplacement_tree.heading(col)['text'] for col in emplacement_tree['columns']]
#        data = [list(emplacement_tree.item(item)['values']) for item in emplacement_tree.get_children()]
#
#        if not data:
#            messagebox.showerror(title="Erreur", message="Le tableau est vide, rien à exporter.")
#            return
#
#        # Demande à l'utilisateur l'emplacement et le nom du fichier à enregistrer
#        output_filename = filedialog.asksaveasfilename(
#            defaultextension=".pdf",
#            filetypes=[("PDF files", "*.pdf")],
#            title="Enregistrer le rapport PDF"
#        )
#
#        # Si l'utilisateur a annulé la sauvegarde, on ne fait rien
#        if not output_filename:
#            return
#
#        # Création d'un style de paragraphe pour les en-têtes.
#        header_style = ParagraphStyle('HeaderStyle', alignment=1, fontSize=7, fontName='Helvetica-Bold')
#
#        # Conversion des en-têtes en objets Paragraph pour qu'ils s'enroulent.
#        wrapped_headers = [Paragraph(h, header_style) for h in headers]
#
#        table_data = [wrapped_headers] + data
#
#        try:
#            # Créer le document PDF en mode paysage.
#            doc = SimpleDocTemplate(output_filename, pagesize=landscape(letter))
#
#            # Définir le style du tableau
#            style = TableStyle([
#                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
#                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
#                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
#                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
#                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
#                ('FONTSIZE', (0, 0), (-1, -1), 8),
#                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
#                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
#                ('GRID', (0, 0), (-1, -1), 1, colors.black),
#                ('WORDWRAP', (0, 0), (-1, -1), 1),
#            ])
#
#            # Définir les largeurs de colonne de manière proportionnelle.
#            proportional_widths = [
#                0.07,  # "Total Hectares"
#                0.08,  # "Total Hectares a Exploiter "
#                0.06,  # "PH du Secteur"
#                0.15,  # "Produits a Exploiter "
#                0.06,  # "Surface"
#                0.09,  # "Kg de semance/hectare"
#                0.09,  # "N* mesure d'angree"
#                0.10,  # "RECOLTE ENVISAGEE"
#                0.10,  # "RECOLTE REEL"
#                0.15,  # "Depences effectuer"
#                0.25,  # "Detail sur les Depences "
#                0.08,  # "Date (AAAA-MM-JJ)"
#            ]
#
#            # Normaliser les largeurs pour que leur somme soit de 1.
#            total_proportional_width = sum(proportional_widths)
#            doc_width = landscape(letter)[0] - 2 * doc.leftMargin
#            col_widths = [width / total_proportional_width * doc_width for width in proportional_widths]
#
#            # Utilisation de LongTable pour gérer les tableaux qui peuvent s'étendre sur plusieurs pages
#            t = LongTable(table_data, colWidths=col_widths)
#            t.setStyle(style)
#            doc.build([t])
#
#            messagebox.showinfo(title="Succès", message=f"Tableau exporté avec succès dans '{output_filename}'")
#
#        except Exception as e:
#            messagebox.showerror(title="Erreur", message=f"Une erreur est survenue lors de l'exportation: {e}")
#
#    emplacement_fm = tk.Frame(champs, bg='gray12')
#    titre = Label(emplacement_fm, text="DONNEES EMPLACEMT (INVESTISSEMEMT & DEPENCES)", font=("TIMES NEW ROMAN", 20),
#                  bg='gray12', fg='cyan')
#    titre.pack(pady=10, ipadx=300)
#
#    live = tk.Button(emplacement_fm, text='X', bd=0, bg='gray12', fg='white', font=("Arial", 13),
#                     command=forwaard_to_champs)
#    live.place(x=1319, y=0, width=40)
#    live.bind("<Enter>", lambda e: live.config(bg="red"))
#    live.bind("<Leave>", lambda e: live.config(bg="gray12"))
#
#    refresh_btn = ctk.CTkButton(emplacement_fm, text="Actualiser", command='display_terrains', height=40)
#    refresh_btn.place(x=1215, y=100)
#
#    delete_btn = ctk.CTkButton(emplacement_fm, text="Supprimer le donnee", command='delete_terrain', height=40)
#    delete_btn.place(x=1215, y=200)
#
#    pdf_button = ctk.CTkButton(emplacement_fm, text="Exporter en PDF", command=save_to_pdf)
#    pdf_button.place(x=1215, y=500)
#
#    display_frame = tk.Frame(emplacement_fm, bg='gray20', padx=10, pady=10)
#    display_frame.place(x=0, y=90, width=1210, height=700)
#
#    emplacement_tree = ttk.Treeview(display_frame,
#                                    columns=("Total Hectares", "Total Hectares a Exploiter ", "PH du Secteur",
#                                             "Produits a Exploiter ", "Surface", "Kg de semance/hectare",
#                                             "N* mesure d'angree", "RECOLTE ENVISAGEE", "RECOLTE REEL",
#                                             "Depences effectuer", "Detail sur les Depences ", "Date (AAAA-MM-JJ)"),
#                                    show="headings")
#
#    for item in fetch_emplacement():
#        emplacement_tree.insert("", tk.END, values=item)
#
#    emplacement_tree.heading("Total Hectares", text="Tot Hectaresuuuuuu")
#    emplacement_tree.heading("Total Hectares a Exploiter ", text="Tot a Exploiter ")
#    emplacement_tree.heading("PH du Secteur", text="PH du Secteur")
#    emplacement_tree.heading("Produits a Exploiter ", text="Produits cultiver ")
#    emplacement_tree.heading("Surface", text="Surface")
#    emplacement_tree.heading("Kg de semance/hectare", text="semance kg/hectare")
#    emplacement_tree.heading("N* mesure d'angree", text="qt d'angree")
#    emplacement_tree.heading("RECOLTE ENVISAGEE", text="RECOLTE ENVISAGEE")
#    emplacement_tree.heading("RECOLTE REEL", text="RECOLTE REEL")
#    emplacement_tree.heading("Depences effectuer", text="Depences")
#    emplacement_tree.heading("Detail sur les Depences ", text="Detail Depences ")
#    emplacement_tree.heading("Date (AAAA-MM-JJ)", text="Date (AAAA-MM-JJ)")
#
#    emplacement_tree.pack(expand=True, fill='both')
#    scrollbar = ttk.Scrollbar(display_frame, orient="horizontal", command=emplacement_tree.xview)
#    scrollbar.place(x=0, y=580, width=1200, height=23)
#    emplacement_tree.configure(xscrollcommand=scrollbar.set)
#    emplacement_fm.place(x=0, y=0, width=1360, height=700)


#def donnnees_emplacement():
#
#
#
#    def forwaard_to_champs():
#        emplacement_fm.destroy()
#        champs.update()
#
#    def fetch_emplacement():
#        conn = sqlite3.connect("my_ferme.db")
#        cursor = conn.cursor()
#        cursor.execute("SELECT * FROM Emplacement")
#        super= cursor.fetchall()
#        conn.close()
#        print(super)
#        return super
#    #fetch_emplacement()
#
#    def save_to_pdf():
#        """Sauvegarde les données du treeview dans un fichier PDF."""
#        headers = [emplacement_tree.heading(col)['text'] for col in emplacement_tree['columns']]
#        data = [list(emplacement_tree.item(item)['values']) for item in emplacement_tree.get_children()]
#
#        if not data:
#            messagebox.showerror(title="Erreur", message="Le tableau est vide, rien à exporter.")
#            return
#
#        table_data = [headers] + data
#        output_filename = "tableau_export.pdf"
#
#        try:
#            # Créer le document PDF en mode paysage pour accommoder les 12 colonnes
#            doc = SimpleDocTemplate(output_filename, pagesize=landscape(letter))
#
#            # Définir le style du tableau
#            style = TableStyle([
#                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
#                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
#                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
#                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
#                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
#                ('FONTSIZE', (0, 0), (-1, -1), 8),
#                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
#                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
#                ('GRID', (0, 0), (-1, -1), 1, colors.black),
#            ])
#
#            # Définir les largeurs de colonne pour une meilleure mise en page
#            col_widths = [doc.width / 12] * 12
#            t = Table(table_data, colWidths=col_widths)
#            t.setStyle(style)
#            doc.build([t])
#
#            messagebox.showinfo(title="Succès", message=f"Tableau exporté avec succès dans '{output_filename}'")
#
#        except Exception as e:
#            messagebox.showerror(title="Erreur", message=f"Une erreur est survenue lors de l'exportation: {e}")
#
#    emplacement_fm = tk.Frame(champs, bg='gray12')
#    titre = Label(emplacement_fm, text="DONNEES EMPLACEMT (INVESTISSEMEMT & DEPENCES)", font=("TIMES NEW ROMAN", 20),
#                  bg='gray12', fg='cyan')
#    titre.pack(pady=10,ipadx=300)
#    #titre.place(x=0,y=0,width=1360,height=700)
#
#    live = tk.Button(emplacement_fm, text='X', bd=0, bg='gray12', fg='white', font=("Arial", 13),
#                     command=forwaard_to_champs)
#    live.place(x=1319, y=0, width=40)
#    live.bind("<Enter>", lambda e: live.config(bg="red"))
#    live.bind("<Leave>", lambda e: live.config(bg="gray12"))
#
#    refresh_btn = ctk.CTkButton(emplacement_fm, text="Actualiser", command='display_terrains', height=40)
#    refresh_btn.place(x=1215, y=100)
#
#    delete_btn = ctk.CTkButton(emplacement_fm, text="Supprimer le donnee", command='delete_terrain', height=40)
#    delete_btn.place(x=1215, y=200)
#
#    pdf_button = ctk.CTkButton(emplacement_fm, text="Exporter en PDF", command=save_to_pdf)
#    pdf_button.place(x=1215, y=500)
#
## # Affichage des ventes et de la sommation
#    display_frame = tk.Frame(emplacement_fm, bg='gray20', padx=10, pady=10)
#    #display_frame.pack(expand=True, fill='both', padx=20, pady=80)
#    display_frame.place(x=0, y=90, width=1210, height=700)
#
#    #columns =
#        #(
#    # "Total_Hectares", "TotalHectares_a_Exploiter", "PH_du_Secteur", "Produits_a_Exploiter", "Surface",
#        #"Kg_de_semance_hectare", "N_mesure_d_angree", "RECOLTE_ENVISAGEE", "RECOLTE_REEL",
#        #"Depences_effectuer", "Detail_sur_les_Depences", "Date"
#    #)
#
#    emplacement_tree = ttk.Treeview(display_frame,columns=("Total Hectares", "Total Hectares a Exploiter ", "PH du Secteur", "Produits a Exploiter ", "Surface","Kg de semance/hectare","N* mesure d'angree","RECOLTE ENVISAGEE","RECOLTE REEL","Depences effectuer","Detail sur les Depences ","Date (AAAA-MM-JJ)"),
#                               show="headings")
#    # Définition des en-têtes de colonnes
#    #for col in fetch_emplacement():
#    #    emplacement_tree.heading(col)#, text=col.replace('_', ' ').title())
#    #    emplacement_tree.column(col, width=100)
#
#        # Insérer les données de l'exemple dans le tableau
#    for item in fetch_emplacement():
#        emplacement_tree.insert("", tk.END, values=item)
#        #emplacement_tree.column(width=500)
#
#    emplacement_tree.heading("Total Hectares", text="Total Hectares")
#    emplacement_tree.heading("Total Hectares a Exploiter ", text="Total Hectares a Exploiter ")
#    emplacement_tree.heading("PH du Secteur", text="PH du Secteur")
#    emplacement_tree.heading("Produits a Exploiter ", text="Produits a Exploiter ")
#    emplacement_tree.heading("Surface", text="Surface")
#    emplacement_tree.heading("Kg de semance/hectare",text="Kg de semance/hectare")
#    emplacement_tree.heading("N* mesure d'angree", text="N* mesure d'angree")
#    emplacement_tree.heading("RECOLTE ENVISAGEE", text="RECOLTE ENVISAGEE")
#    emplacement_tree.heading("RECOLTE REEL", text="RECOLTE REEL")
#    emplacement_tree.heading("Depences effectuer",text="Depences effectuer")
#    emplacement_tree.heading("Detail sur les Depences ",text="Detail sur les Depences ")
#    emplacement_tree.heading("Date (AAAA-MM-JJ)", text="Date (AAAA-MM-JJ)")
#
#    emplacement_tree.pack(expand=True, fill='both')
#    scrollbar = ttk.Scrollbar(display_frame, orient="horizontal", command=emplacement_tree.xview)
#    scrollbar.place(x=0, y=580, width=1200, height=23)
#    emplacement_tree.configure(xscrollcommand=scrollbar.set)
#    #total_sales_label = Label(emplacement_fm, text="Total des ventes cumulées : 0.00 $", font=("Arial", 20), bg='gray12',fg='yellow')
#    #total_sales_label.place(x=0, y=0, height=40, width=710)
#    emplacement_fm.place(x=0, y=0, width=1360, height=700)





# ==================== NOUVELLE PAGE : TABLEAU DE BORD (INVENTAIRE & FINANCES) ====================
def page_tableau_de_bord():
    def forwaard_to_champs():
        page.destroy()
        champs.update()

    def get_stock_data():
        conn = sqlite3.connect("my_ferme.db")
        cursor = conn.cursor()
        cursor.execute("SELECT nom_produit, quantite FROM Stock")
        data = cursor.fetchall()
        conn.close()
        return data

    def get_financial_summary():
        conn = sqlite3.connect("my_ferme.db")
        cursor = conn.cursor()

        # Total des ventes
        cursor.execute("SELECT SUM(prix_total) FROM Ventes")
        ventes_totales = cursor.fetchone()[0] or 0.0

        # Total des dépenses (intrants)
        cursor.execute(
            "SELECT SUM(quantite * prix_unitaire) FROM Recoltes_Ventes")  # Exemple de dépenses, à adapter pour les vrais coûts d'intrants
        depenses_totales = cursor.fetchone()[0] or 0.0

        # Vous pouvez ajouter d'autres dépenses ici, par exemple:
        # cursor.execute("SELECT SUM(cout) FROM DépensesIntrants")

        benefice_net = ventes_totales - depenses_totales

        conn.close()
        return ventes_totales, depenses_totales, benefice_net

    def display_data():
        # Afficher le stock
        for item in stock_tree.get_children():
            stock_tree.delete(item)
        stock_data = get_stock_data()
        for row in stock_data:
            stock_tree.insert("", tk.END, values=row)

        # Afficher le résumé financier
        ventes, depenses, benefice = get_financial_summary()
        ventes_label.configure(text=f"Total des Ventes : {ventes:.2f} $")
        depenses_label.configure(text=f"Total des Dépenses : {depenses:.2f} $")
        benefice_label.configure(text=f"Bénéfice Net : {benefice:.2f} $")

    page = tk.Frame(champs, bg='gray12', bd=7)
    titre = Label(page, text="TABLEAU DE BORD (FINANCES & INVENTAIRE)", font=("TIMES NEW ROMAN", 20),
                  bg='gray12', fg='cyan')
    titre.pack(pady=10)

    live = tk.Button(page, text='X', bd=0, bg='gray12', fg='white', font=("Arial", 13), command=forwaard_to_champs)
    live.place(x=1319, y=0, width=40)
    live.bind("<Enter>", lambda e: live.config(bg="red"))
    live.bind("<Leave>", lambda e: live.config(bg="gray12"))

    # Section Récapitulatif Financier
    financier_frame = tk.LabelFrame(page, text="Récapitulatif Financier", bg='gray20', fg='white', padx=10, pady=10)
    financier_frame.pack(pady=20, padx=20, fill='x')

    ventes_label = Label(financier_frame, text="Total des Ventes : 0.00 $", font=("Arial", 18), bg='gray20', fg='green')
    ventes_label.pack(anchor='w', pady=5)

    depenses_label = Label(financier_frame, text="Total des Dépenses : 0.00 $", font=("Arial", 18), bg='gray20',
                           fg='red')
    depenses_label.pack(anchor='w', pady=5)

    benefice_label = Label(financier_frame, text="Bénéfice Net : 0.00 $", font=("Arial", 20), bg='gray20', fg='yellow')
    benefice_label.pack(anchor='w', pady=10)

    # Section Inventaire
    stock_frame = tk.LabelFrame(page, text="Inventaire des Produits", bg='gray20', fg='white', padx=10, pady=10)
    stock_frame.pack(pady=20, padx=20, fill='both', expand=True)

    stock_tree = ttk.Treeview(stock_frame, columns=("Produit", "Quantité"), show="headings")
    stock_tree.heading("Produit", text="Produit")
    stock_tree.heading("Quantité", text="Quantité en Stock")
    stock_tree.pack(side=tk.LEFT, fill='both', expand=True)

    scrollbar = ttk.Scrollbar(stock_frame, orient="vertical", command=stock_tree.yview)
    scrollbar.pack(side=tk.RIGHT, fill='y')
    stock_tree.configure(yscrollcommand=scrollbar.set)

    display_data()

    page.place(x=0, y=0, width=2000, height=900)

#yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy

# customtkinter appearance settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
def get_hectars_option():
    options = []
    try:
        conn = sqlite3.connect("my_ferme.db")
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT Total Hectares FROM Emplacement WHERE Total Hectares IS NOT NULL AND Total Hectares !="" ")
        options = [str(row[0]) for row in cursor.fetchall()]
        conn.close()
    except sqlite3.Error as e:
        print('Erreur BDD lors de la recuperation des doneeL: {e}')
    if not options:
        options = ["4","10","20","30","Autre(a saisir)"]
    return options

def get_produit_option():
    options = []
    try:
        conn = sqlite3.connect("my_ferme.db")
        cursor = conn.cursor()
        cursor.execute("SELECT nom_produit FROM Produits ORDER BY nom_produit")
        options = [row[0] for row in cursor.fetchall()]
        conn.close()
    except sqlite3.Error as e:
        print('Erreur BDD lors de la recuperation des doneeL: {e}')
    return options
def gestion_ferm():

   class FermeApp(ctk.CTk):
       def __init__(self):
           super().__init__()
           self.title("Application de Gestion de Ferme")
           self.geometry("2000x700+40")
           self.configure(bg='gray12')

           # Initialize the database
           #self.init_db()

           # Configure main window grid layout
           self.grid_columnconfigure(0, weight=1)
           self.grid_rowconfigure(0, weight=1)

           # Main frame for the application content
           self.main_frame = ctk.CTkFrame(self, bg_color='gray12', fg_color='gray12')
           self.main_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

           # Configure the grid within the main frame
           self.main_frame.grid_columnconfigure(0, weight=1)  # Treeview column
           self.main_frame.grid_columnconfigure(1, weight=0)  # Buttons column
           self.main_frame.grid_rowconfigure(0, weight=0)
           self.main_frame.grid_rowconfigure(1, weight=1)

           # Title
           titre = ctk.CTkLabel(self.main_frame, text="DONNÉES EMPLACEMENT", font=("TIMES NEW ROMAN", 24),
                                text_color='cyan')
           titre.grid(row=0, column=0, columnspan=2, pady=10, sticky="n")

           # Frame for displaying the table
           self.display_frame = ctk.CTkFrame(self.main_frame, bg_color='gray20', fg_color='gray20', corner_radius=10)
           self.display_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

           self.display_frame.grid_rowconfigure(0, weight=1)
           self.display_frame.grid_columnconfigure(0, weight=1)

           # Frame for the buttons
           self.button_frame = ctk.CTkFrame(self.main_frame, bg_color='gray12', fg_color='gray12')
           self.button_frame.grid(row=1, column=1, padx=10, pady=10, sticky="ns")

           # Buttons placed using pack() inside the button frame
           self.refresh_btn = ctk.CTkButton(self.button_frame, text="Actualiser", command=self.display_data, height=40)
           self.refresh_btn.pack(pady=10)

           self.delete_btn = ctk.CTkButton(self.button_frame, text="Supprimer la donnée", command=self.delete_data,
                                           height=40)
           self.delete_btn.pack(pady=10)

           self.add_btn = ctk.CTkButton(self.button_frame, text="Ajouter une donnée", command=self.open_add_data_window,
                                        height=40)
           self.add_btn.pack(pady=10)

           self.print_btn = ctk.CTkButton(self.button_frame, text="Imprimer", command=self.print_pdf, height=40)
           self.print_btn.pack(pady=10)

           self.pdf_button = ctk.CTkButton(self.button_frame, text="Exporter en PDF", command=self.save_to_pdf)
           self.pdf_button.pack(pady=10)

           self.manage_files_btn = ctk.CTkButton(self.button_frame, text="Gérer les fichiers",
                                                 command=self.open_manage_files_window, height=40)
           self.manage_files_btn.pack(pady=10)

           # Treeview styling
           style = ttk.Style()
           style.theme_use("default")
           style.configure("Treeview",
                           background="#D3D3D3",
                           foreground="black",
                           rowheight=25,
                           fieldbackground="#D3D3D3")
           style.map("Treeview",
                     background=[('selected', '#528B8B')])

           style.configure("Treeview.Heading",
                           font=("TIMES NEW ROMAN", 10, 'bold'),
                           background="gray20",
                           foreground="white",
                           relief="flat")
           style.map("Treeview.Heading",
                     background=[('active', 'gray20')])

           self.emplacement_tree = ttk.Treeview(self.display_frame,
                                                columns=("ID","Total Hectares", "Total Hectares a Exploiter",
                                                         "PH du Secteur", "Produits a Exploiter", "Surface",
                                                         "Kg de semance/hectare", "N* mesure d'angree",
                                                         "RECOLTE ENVISAGEE", "RECOLTE REEL", "Depences effectuer",
                                                         "Detail sur les Depences", "Date"), show="headings")

           self.emplacement_tree.heading("ID", text="ID produit")
           self.emplacement_tree.heading("Total Hectares", text="Total Hectares")
           self.emplacement_tree.heading("Total Hectares a Exploiter", text="Total Hectares à Exploiter")
           self.emplacement_tree.heading("PH du Secteur", text="PH du Secteur")
           self.emplacement_tree.heading("Produits a Exploiter", text="Produits à Exploiter")
           self.emplacement_tree.heading("Surface", text="Surface")
           self.emplacement_tree.heading("Kg de semance/hectare", text="Kg de semence/hectare")
           self.emplacement_tree.heading("N* mesure d'angree", text="N° Mesure d'engrais")
           self.emplacement_tree.heading("RECOLTE ENVISAGEE", text="RÉCOLTE ENVISAGÉE")
           self.emplacement_tree.heading("RECOLTE REEL", text="RÉCOLTE RÉELLE")
           self.emplacement_tree.heading("Depences effectuer", text="Dépenses à effectuer")
           self.emplacement_tree.heading("Detail sur les Depences", text="Détail sur les Dépenses")
           self.emplacement_tree.heading("Date", text="Date")

           self.emplacement_tree.column("ID", width=30)
           self.emplacement_tree.column("Total Hectares", width=100)
           self.emplacement_tree.column("Total Hectares a Exploiter", width=120)
           self.emplacement_tree.column("PH du Secteur", width=80)
           self.emplacement_tree.column("Produits a Exploiter", width=150)
           self.emplacement_tree.column("Surface", width=70)
           self.emplacement_tree.column("Kg de semance/hectare", width=120)
           self.emplacement_tree.column("N* mesure d'angree", width=100)
           self.emplacement_tree.column("RECOLTE ENVISAGEE", width=120)
           self.emplacement_tree.column("RECOLTE REEL", width=120)
           self.emplacement_tree.column("Depences effectuer", width=120)
           self.emplacement_tree.column("Detail sur les Depences", width=200)
           self.emplacement_tree.column("Date", width=100)

           self.emplacement_tree.grid(row=0, column=0, sticky="nsew")
           self.scrollbar_y = ttk.Scrollbar(self.display_frame, orient="vertical", command=self.emplacement_tree.yview)
           self.scrollbar_y.grid(row=0, column=1, sticky="ns")
           self.scrollbar_x = ttk.Scrollbar(self.display_frame, orient="horizontal", command=self.emplacement_tree.xview)
           self.scrollbar_x.grid(row=1, column=0, sticky="ew")
           self.emplacement_tree.configure(yscrollcommand=self.scrollbar_y.set, xscrollcommand=self.scrollbar_x.set)

           # Display data on startup
           self.display_data()



       def fetch_emplacement(self):
           """Fetches all data from the Emplacement table."""
           conn = sqlite3.connect("my_ferme.db")
           cursor = conn.cursor()
           cursor.execute("SELECT * FROM Emplacement")
           data = cursor.fetchall()
           conn.close()
           #print(data)
           return data


       def display_data(self):
           """Displays fetched data in the Treeview."""
           for item in self.emplacement_tree.get_children():
               self.emplacement_tree.delete(item)
           data = self.fetch_emplacement()
           for row in data:
               self.emplacement_tree.insert("", "end", values=row)

       def delete_data(self):
           """Deletes a selected row from the database and the Treeview."""
           selected_item = self.emplacement_tree.focus()
           if not selected_item:
               messagebox.showerror(title="Erreur", message="Veuillez sélectionner une ligne à supprimer.")
               return

           confirmation = messagebox.askyesno(
               "Confirmation de suppression",
               "Êtes-vous sûr de vouloir supprimer cette ligne ?"
           )

           if confirmation:
               item_values = self.emplacement_tree.item(selected_item, 'values')
               row_id = item_values[0]
               conn = sqlite3.connect("my_ferme.db")
               cursor = conn.cursor()
               cursor.execute("DELETE FROM Emplacement WHERE id_produit = ?", (row_id,))
               conn.commit()
               conn.close()
               self.emplacement_tree.delete(selected_item)
               messagebox.showinfo("Succès", "La ligne a été supprimée avec succès.")

       def open_add_data_window(self):


           """Ouvre une nouvelle fenêtre pour ajouter une nouvelle entrée de données, avec une barre de défilement."""
           add_window = ctk.CTkToplevel(self)
           add_window.title("Ajouter une nouvelle donnée")
           add_window.geometry("500x750+200")
           add_window.resizable(True, True)
           add_window.grab_set()

           # Cadre avec barre de défilement pour contenir les champs de saisie et le bouton
           scrollable_frame = ctk.CTkScrollableFrame(add_window, fg_color="gray12")
           scrollable_frame.pack(fill="both", expand=True, padx=10, pady=10)


           # Labels et champs de saisie pour la nouvelle fenêtre
           labels = ["chiffre d investissement du projet","Total Hectares","nom_produit","Total Hectares a Exploiter", "PH du Secteur", "Surface", "Kg de semance/hectare",
               "N° Mesure d'engrais", "RECOLTE ENVISAGEE", "RECOLTE REELLE",
               "Depenses a effectuer", "Detail sur les Depenses", "Date"
           ]
           hectare_option = get_hectars_option()

           produit_option = get_produit_option()

           self.entries = {}
           self.combobox = {}

           for i, text in enumerate(labels):
            label = ctk.CTkLabel(scrollable_frame, text=text, font=("Arial", 12))
            label.pack(pady=5, padx=10, anchor="w")

            if text == "Total Hectares":
                combobox = ctk.CTkComboBox(scrollable_frame,values=hectare_option,width=450)
                if hectare_option:
                    combobox.set(hectare_option[0])
                    combobox.pack(pady=5, padx=10, anchor="w")
                    self.combobox[text] = combobox

            elif text == "nom_produit":
                 combobox = ctk.CTkComboBox(scrollable_frame, values=produit_option, width=450)
                 if produit_option:
                    combobox.set(produit_option[0])
                    combobox.pack(pady=5, padx=10, anchor="w")
                    self.combobox[text] = combobox

            elif text == "Date":
                current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                enty = ctk.CTkEntry(scrollable_frame, width=450)
                enty.insert(0,current_datetime)
                enty.configure(state="readonly")
                enty.pack(pady=5, padx=10)
                self.entries[text] = enty
            else:
                entry = ctk.CTkEntry(scrollable_frame, width=450)
                entry.pack(pady=5, padx=10)
                self.entries[text] = entry
           #labele = ["Total Hectares","Produits a Exploiter"]


           hectaer_option =  ["4","5","6","Autres"]


           # Bouton pour ajouter les données, maintenant placé dans le cadre défilable
           add_button = ctk.CTkButton(scrollable_frame, text="Ajouter", command=lambda: self.add_data(add_window), height=40)
           add_button.pack(pady=20, padx=10)

       def add_data(self, window):
           """Adds new data to the database from the entry fields."""
           investissement = self.entries["chiffre d investissement du projet"].get()
           total_hectares = self.combobox["Total Hectares"].get()
           total_hectares_exploiter = self.entries["Total Hectares a Exploiter"].get()
           ph = self.entries["PH du Secteur"].get()
           produits = self.combobox["nom_produit"].get()
           surface = self.entries["Surface"].get()
           semence_kg = self.entries["Kg de semance/hectare"].get()
           mesure_angree = self.entries["N° Mesure d'engrais"].get()
           recolte_envisagee = self.entries["RECOLTE ENVISAGEE"].get()
           recolte_reelle = self.entries["RECOLTE REELLE"].get()
           depenses = self.entries["Depenses a effectuer"].get()
           details_depenses = self.entries["Detail sur les Depenses"].get()
           date = self.entries["Date"].get()
           conn = sqlite3.connect("my_ferme.db")
           cursor = conn.cursor()
           cursor.execute("""
               INSERT INTO Emplacement (investissement,Total_Hectares, TotalHectares_a_Exploiter, PH_du_Secteur, nom_produit, Surface, Kg_de_semance_hectare, N_mesure_d_angree, RECOLTE_ENVISAGEE, RECOLTEREEL, Depences_effectuer, Detail_sur_les_Depences, Date)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
           """, (investissement,total_hectares, total_hectares_exploiter, ph, produits, surface, semence_kg, mesure_angree,
                 recolte_envisagee, recolte_reelle, depenses, details_depenses, date))
           conn.commit()
           conn.close()
           messagebox.showinfo("Succès", "Donnée ajoutée avec succès.")
           self.display_data()
           window.destroy()
           gestion_ferm()
           

       def save_to_pdf(self):
           """
           Saves the treeview data to a PDF file by asking the user for a save location.
           """
           headers = [self.emplacement_tree.heading(col)['text'] for col in self.emplacement_tree['columns']]
           data = [list(self.emplacement_tree.item(item)['values']) for item in self.emplacement_tree.get_children()]

           if not data:
               messagebox.showerror(title="Erreur", message="Le tableau est vide, rien à exporter.")
               return

           output_filename = filedialog.asksaveasfilename(
               defaultextension=".pdf",
               filetypes=[("PDF files", "*.pdf")],
               title="Enregistrer le rapport PDF"
           )

           if not output_filename:
               return None

           header_style = ParagraphStyle('HeaderStyle', alignment=1, fontSize=7, fontName='Helvetica-Bold')
           wrapped_headers = [Paragraph(h, header_style) for h in headers]
           table_data = [wrapped_headers] + data

           try:
               doc = SimpleDocTemplate(output_filename, pagesize=landscape(legal))
               style = TableStyle([
                   ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                   ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                   ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                   ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                   ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                   ('FONTSIZE', (0, 0), (-1, -1), 8),
                   ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                   ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                   ('GRID', (0, 0), (-1, -1), 1, colors.black),
                   ('WORDWRAP', (0, 0), (-1, -1), 1),
               ])

               proportional_widths = [0.07, 0.07, 0.08, 0.06, 0.15, 0.06, 0.09, 0.09, 0.10, 0.10, 0.35, 0.10, 0.08]
               doc_width = landscape(legal)[0] - 4 * doc.leftMargin
               col_widths = [width * doc_width for width in proportional_widths]

               t = LongTable(table_data, colWidths=col_widths)
               t.setStyle(style)
               (doc.build([t]))

               messagebox.showinfo(title="Succès", message=f"Tableau exporté avec succès dans '{output_filename}'")
               return output_filename

           except Exception as e:
               messagebox.showerror(title="Erreur", message=f"Une erreur est survenue lors de l'exportation: {e}")
               return None

       def print_pdf(self):
           """Generates the PDF and opens it in the default program for printing."""
           pdf_path = self.save_to_pdf()
           if pdf_path:
               try:
                   if os.name == 'nt':  # For Windows
                       os.startfile(pdf_path, 'print')
                   else:  # For other systems like macOS and Linux
                       subprocess.Popen(['xdg-open', pdf_path])
               except Exception as e:
                   messagebox.showerror(title="Erreur d'impression", message=f"Impossible d'ouvrir le fichier PDF : {e}")

       def open_manage_files_window(self):
           """Opens a new window to manage saved PDF files."""
           manage_window = ctk.CTkToplevel(self)
           manage_window.title("Gérer les fichiers PDF")
           manage_window.geometry("600x400")
           manage_window.grab_set()

           ctk.CTkLabel(manage_window, text="Fichiers PDF enregistrés", font=("Arial", 16, 'bold')).pack(pady=10)

           # Frame for the treeview
           file_frame = ctk.CTkFrame(manage_window)
           file_frame.pack(padx=10, pady=5, fill="both", expand=True)

           # Treeview to list files
           file_tree = ttk.Treeview(file_frame, columns=("Fichier"), show="headings")
           file_tree.heading("Fichier", text="Nom du fichier")
           file_tree.pack(fill="both", expand=True)
           self.populate_file_tree(file_tree)

           # Frame for buttons
           button_frame = ctk.CTkFrame(manage_window)
           button_frame.pack(pady=10)

           open_btn = ctk.CTkButton(button_frame, text="Ouvrir", command=lambda: self.open_file(file_tree))
           open_btn.pack(side="left", padx=5)

           delete_btn = ctk.CTkButton(button_frame, text="Supprimer", command=lambda: self.delete_file(file_tree))
           delete_btn.pack(side="left", padx=5)

           # New button to print the selected file directly
           print_btn = ctk.CTkButton(button_frame, text="Imprimer",
                                     command=lambda: self.print_file_from_manager(file_tree))
           print_btn.pack(side="left", padx=5)

       def populate_file_tree(self, tree):
           """Populates the file treeview with PDF files from the current directory."""
           for item in tree.get_children():
               tree.delete(item)

           pdf_files = [f for f in os.listdir('.') if f.endswith('.pdf')]
           for pdf in pdf_files:
               tree.insert("", "end", values=(pdf,))

       def open_file(self, tree):
           """Opens the selected PDF file."""
           selected_item = tree.focus()
           if not selected_item:
               messagebox.showerror("Erreur", "Veuillez sélectionner un fichier à ouvrir.")
               return

           file_name = tree.item(selected_item, 'values')[0]
           try:
               if os.name == 'nt':  # For Windows
                   os.startfile(file_name)
               else:  # For other systems like macOS and Linux
                   subprocess.Popen(['xdg-open', file_name])
           except Exception as e:
               messagebox.showerror("Erreur d'ouverture", f"Impossible d'ouvrir le fichier : {e}")

       def delete_file(self, tree):
           """Deletes the selected PDF file."""
           selected_item = tree.focus()
           if not selected_item:
               messagebox.showerror("Erreur", "Veuillez sélectionner un fichier à supprimer.")
               return

           file_name = tree.item(selected_item, 'values')[0]
           confirmation = messagebox.askyesno("Confirmation",
                                              f"Êtes-vous sûr de vouloir supprimer le fichier '{file_name}' ?")

           if confirmation:
               try:
                   os.remove(file_name)
                   tree.delete(selected_item)
                   messagebox.showinfo("Succès", "Fichier supprimé avec succès.")
               except Exception as e:
                   messagebox.showerror("Erreur de suppression", f"Impossible de supprimer le fichier : {e}")

       def print_file_from_manager(self, tree):
           """Prints the selected PDF file from the file manager window."""
           selected_item = tree.focus()
           if not selected_item:
               messagebox.showerror("Erreur", "Veuillez sélectionner un fichier à imprimer.")
               return

           file_name = tree.item(selected_item, 'values')[0]
           try:
               if os.name == 'nt':  # For Windows
                   os.startfile(file_name, 'print')
               else:  # For other systems like macOS and Linux
                   # On systems other than Windows, the 'print' verb is not standard
                   subprocess.Popen(['xdg-open', file_name])
                   messagebox.showinfo("Information",
                                       "Le fichier a été ouvert dans votre visionneuse de PDF par défaut. Veuillez utiliser la fonction d'impression de l'application.")
           except Exception as e:
               messagebox.showerror("Erreur d'impression", f"Impossible d'imprimer le fichier : {e}")


   if __name__ == "__main__":
       app = FermeApp()
       app.mainloop()

#yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy



# ==================== FIN NOUVELLE PAGE ====================

def page_inventaire():


    def forwaard_to_champs():
        page.destroy()
        champs.update()

    page = tk.Frame(champs, bg='gray12', bd=7)
    titre = Label(page, text="TABLEAU DE BORD ET INVENTAIRE GLOBAL", font=("TIMES NEW ROMAN", 20),
                  bg='gray12', fg='cyan')
    titre.pack(pady=10)

    live = tk.Button(page, text='X', bd=0, bg='gray12', fg='white', font=("Arial", 13), command=forwaard_to_champs)
    live.place(x=1319, y=0, width=40)
    live.bind("<Enter>", lambda e: live.config(bg="red"))
    live.bind("<Leave>", lambda e: live.config(bg="gray12"))

    notebook = ttk.Notebook(page)
    notebook.pack(expand=True, fill='both', padx=20, pady=10)

    produits_frame = tk.Frame(notebook, bg='gray20')
    notebook.add(produits_frame, text="Produits")

    produits_tree = ttk.Treeview(produits_frame, columns=("Nom", "ID", "Fournisseur"), show="headings")
    produits_tree.heading("Nom", text="Nom du Produit")
    produits_tree.heading("ID", text="ID du Produit")
    produits_tree.heading("Fournisseur", text="Fournisseur")
    produits_tree.pack(fill='both', expand=True, padx=10, pady=10)

    def display_produits():
        for item in produits_tree.get_children():
            produits_tree.delete(item)
        conn = sqlite3.connect("my_ferme.db")
        cursor = conn.cursor()
        cursor.execute("SELECT nom_produit, id_produit, fournisseur FROM Produits")
        data = cursor.fetchall()
        conn.close()
        for row in data:
            produits_tree.insert("", tk.END, values=row)

    display_produits()

    recoltes_frame = tk.Frame(notebook, bg='gray20')
    notebook.add(recoltes_frame, text="Récoltes & Ventes")

    recoltes_tree = ttk.Treeview(recoltes_frame,
                                 columns=("ID", "Produit", "Quantité", "Prix Unitaire", "Total", "Date"),
                                 show="headings")
    recoltes_tree.heading("ID", text="ID Récolte")
    recoltes_tree.heading("Produit", text="Produit")
    recoltes_tree.heading("Quantité", text="Quantité")
    recoltes_tree.heading("Prix Unitaire", text="Prix Unitaire ($)")
    recoltes_tree.heading("Total", text="Montant Total ($)")
    recoltes_tree.heading("Date", text="Date de Récolte")
    recoltes_tree.pack(fill='both', expand=True, padx=10, pady=10)

    def display_recoltes():
        for item in recoltes_tree.get_children():
            recoltes_tree.delete(item)
        conn = sqlite3.connect("my_ferme.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Recoltes_Ventes ORDER BY date_recolte DESC")
        data = cursor.fetchall()
        conn.close()
        for row in data:
            recoltes_tree.insert("", tk.END, values=row)

    display_recoltes()

    intrants_frame = tk.Frame(notebook, bg='gray20')
    notebook.add(intrants_frame, text="Intrants")

    intrants_tree = ttk.Treeview(intrants_frame,
                                 columns=("ID", "Nom", "Quantité", "Unité", "Date d'Achat", "Fournisseur"),
                                 show="headings")
    intrants_tree.heading("ID", text="ID Intrant")
    intrants_tree.heading("Nom", text="Nom Intrant")
    intrants_tree.heading("Quantité", text="Quantité")
    intrants_tree.heading("Unité", text="Unité")
    intrants_tree.heading("Date d'Achat", text="Date d'Achat")
    intrants_tree.heading("Fournisseur", text="Fournisseur")
    intrants_tree.pack(fill='both', expand=True, padx=10, pady=10)

    def display_intrants():
        for item in intrants_tree.get_children():
            intrants_tree.delete(item)
        conn = sqlite3.connect("my_ferme.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Intrants")
        data = cursor.fetchall()
        conn.close()
        for row in data:
            intrants_tree.insert("", tk.END, values=row)

    display_intrants()

    terrains_frame = tk.Frame(notebook, bg='gray20')
    notebook.add(terrains_frame, text="Terrains")

    terrains_tree = ttk.Treeview(terrains_frame, columns=("ID", "Nom", "Superficie", "Unité", "Localisation"),
                                 show="headings")
    terrains_tree.heading("ID", text="ID Terrain")
    terrains_tree.heading("Nom", text="Nom du Terrain")
    terrains_tree.heading("Superficie", text="Superficie")
    terrains_tree.heading("Unité", text="Unité")
    terrains_tree.heading("Localisation", text="Localisation")
    terrains_tree.pack(fill='both', expand=True, padx=10, pady=10)

    def display_terrains():
        for item in terrains_tree.get_children():
            terrains_tree.delete(item)
        conn = sqlite3.connect("my_ferme.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Terrains")
        data = cursor.fetchall()
        conn.close()
        for row in data:
            terrains_tree.insert("", tk.END, values=row)

    display_terrains()

    travailleurs_frame = tk.Frame(notebook, bg='gray20')
    notebook.add(travailleurs_frame, text="Travailleurs")

    travailleurs_tree = ttk.Treeview(travailleurs_frame, columns=("ID", "Nom", "Prénom", "Poste"), show="headings")
    travailleurs_tree.heading("ID", text="ID Travailleur")
    travailleurs_tree.heading("Nom", text="Nom")
    travailleurs_tree.heading("Prénom", text="Prénom")
    travailleurs_tree.heading("Poste", text="Poste")
    travailleurs_tree.pack(fill='both', expand=True, padx=10, pady=10)

    def display_travailleurs():
        for item in travailleurs_tree.get_children():
            travailleurs_tree.delete(item)
        conn = sqlite3.connect("my_ferme.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Travailleurs")
        data = cursor.fetchall()
        conn.close()
        for row in data:
            travailleurs_tree.insert("", tk.END, values=row)

    display_travailleurs()

    page.place(x=0, y=0, width=2000, height=900)


    #if __name__ == "__main__":
    #    app = FermeApp()
    #    app.mainloop()

imframe = Frame(champs, bg='gray')

## Création et placement des boutons
y_position = 0
button_height = 690
button_width = 450
image_width = 100
image_height = 56
#

# Création d'un Canvas et d'une Scrollbar
container = Frame(imframe, bg="#f0f0f0")
# container.pack(fill="both", expand=True)
container.place(x=0, y=y_position, width=button_width, height=button_height)

canvas = Canvas(container, bg="#f0f0f0", highlightthickness=0)
scrollbar = Scrollbar(container, orient="vertical", command=canvas.yview)
scrollable_frame = Frame(canvas, bg="#fff")

# Configuration du canvas pour utiliser la scrollbar
canvas.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

# Ajout du frame contenant les boutons dans la fenêtre du canvas
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")


# Fonction pour mettre à jour la zone de défilement
def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))


# Lie la fonction de mise à jour au frame
scrollable_frame.bind("<Configure>", on_frame_configure)

# Dictionnaire pour stocker les informations de chaque bouton
# : page_emplacements(),
button_info = {
    "bt1": {"text": "                             REGISTER PRODUCTS", "path": "MY_IMAGES//colection3.png",
            "command": lambda: page_produits()},
    "bt2": {"text": "                             EMPLACEMENT", "path": "MY_IMAGES/colection5.png",
            "command": lambda: gestion_ferm()},
    "bt3": {"text": "                             RECOLTE ET VENTE DE PRODUITS",
            "path": "MY_IMAGES/colection fruits.png",
            "command": lambda:RecolteVentePage()},
    "bt4": {"text": "                                 liste de travalleurs", "path": "MY_IMAGES//support-dequipe.png",
            "command": lambda: page_liste_travailleurs()},
    "bt5": {"text": "                             ACHETEURS DE PRODUITS", "path": "MY_IMAGES//acheteur.png",
            "command": lambda: page_acheteurs_produits()},
    "bt6": {"text": "                             LISTE ET ENREGISTREMENT DES TERRAINS",
            "path": "MY_IMAGES/terrain-de-football.png",
            "command": lambda: page_terrains_enregistrements()},
    "bt7": {"text": "                             LOGISTIQUE", "path": "MY_IMAGES/finance.png",
            "command": lambda: page_logistique()},
    "bt8": {"text": "                             INVENTAIRE GLOBAL", "path": "MY_IMAGES/inventaire.png",
            "command": lambda: page_inventaire()},
    "bt9": {"text": "                             GESTION DES VENTES", "path": "MY_IMAGES/ajouter-un-panier.png",
            "command": lambda: page_gestion_ventes()},
    "bt10": {"text": "                           TABLEAU DE BORD", "path": "MY_IMAGES/tableau-de-bord.png",
             "command": lambda: page_tableau_de_bord()},
}

images_cache = {}


def get_image(path, width, height):
    """Charge, redimensionne et met en cache l'image."""
    key = (path, width, height)
    if key in images_cache:
        return images_cache[key]

    try:
        pil_image = Image.open(path)
        pil_image = pil_image.resize((width, height), Image.Resampling.LANCZOS)
        tk_image = ImageTk.PhotoImage(pil_image)
        images_cache[key] = tk_image
        return tk_image
    except FileNotFoundError:
        print(f"Erreur: Le fichier image '{path}' n'a pas été trouvé.")
        return None


# Création et placement des boutons dans le scrollable_frame
for key, info in button_info.items():
    image = get_image(info["path"], 100, 100)

    button = Button(
        scrollable_frame,
        text=info["text"],
        image=image,
        compound=tk.LEFT,
        bg="#fff",
        bd=0,
        command=info["command"],
        padx=10,
        width=400,
        height=100
    )
    # Utilisez .pack() au lieu de .place()
    button.pack(pady=5)

    button.image = image

imframe.place(x=903, y=0, width=500, height=1140)  # Agrandir la hauteur
label_1.place(x=0, y=0, width=900, height=900)




database()
#page_liste_travailleurs()
#page_produits()
#page_logistique() non utilier
# page_terrains_enregistrements()
#gestion_ferm()
#page_inventaire()
#RecolteVentePage()
#page_gestion_ventes() non utoliser. a changer au future
#message_box(message='wewa kabanga')
champs.mainloop()
