import cv2
import numpy as np
import torch
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from ultralytics import YOLO

# Charger le modèle YOLOv5 pré-entraîné
model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt')

# Définir les nouvelles catégories à détecter
categories = ["cow", "creeper", "house", "pig", "villager", "white_sheep"]

# Créer la fenêtre Tkinter
root = tk.Tk()
root.title("Minecraft Detection")

# Créer un menu déroulant pour sélectionner la catégorie
category_var = tk.StringVar()
category_var.set(categories[0])  # Catégorie par défaut
category_menu = ttk.Combobox(root, textvariable=category_var, values=categories)
category_menu.pack(pady=10)

# Affichage vidéo et détection
cap = cv2.VideoCapture(2)  # Utilisez l'identifiant 0 pour la webcam par défaut

# Créer un cadre pour la vidéo
video_frame = tk.Frame(root)
video_frame.pack()

# Créer un canvas pour afficher la vidéo
canvas = tk.Canvas(video_frame)
canvas.pack()

# Créer un terminal pour afficher les objets détectés
terminal_text = tk.Text(root, height=3, width=30)
terminal_text.pack(pady=10)

# Fonction pour afficher les objets détectés
def display_detected_objects():
    # Lire un frame de la webcam
    ret, img = cap.read()

    # Effectuer la détection
    results = model(img)
    class_names = results.names
    bboxes = results.xyxy[0].cpu().numpy()

    detected_categories = set()  # Pour suivre les catégories détectées

    # Parcourir les objets détectés
    detected_objects = []
    for bbox in bboxes:
        class_index = int(bbox[5])  # Indice de la classe détectée
        class_name = class_names[class_index]
        x_min, y_min, x_max, y_max = map(int, bbox[:4])  # Coordonnées du rectangle englobant

        # Vérifier si la classe détectée fait partie des nouvelles catégories à détecter
        if class_name in categories:
            detected_categories.add(class_name)
            detected_objects.append(class_name)

            # Dessiner un rectangle autour de l'objet détecté
            class_color = (0, 255, 0)  # Couleur verte par défaut
            if class_name == "creeper":
                class_color = (0, 0, 255)  # Couleur rouge pour "creeper"

            cv2.rectangle(img, (x_min, y_min), (x_max, y_max), class_color, 2)  # Dessiner un rectangle

    # Mettre à jour le terminal avec les objets détectés
    if detected_objects:
        detected_objects_str = ", ".join(detected_objects)
        terminal_text.insert(tk.END, f"Détecté : {detected_objects_str}\n")
        terminal_text.see(tk.END)

    # Mettre à jour l'image dans le canvas
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (400, 300))
    photo = ImageTk.PhotoImage(image=Image.fromarray(img))
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)
    canvas.image = photo

    # Mettre à jour l'interface Tkinter
    root.after(10, display_detected_objects)

# Bouton pour commencer la détection
start_button = tk.Button(root, text="Démarrer la détection", command=display_detected_objects)
start_button.pack(pady=10)

# Attendre et gérer les événements Tkinter
root.mainloop()

# Fermer la webcam et libérer les ressources
cap.release()
cv2.destroyAllWindows()
