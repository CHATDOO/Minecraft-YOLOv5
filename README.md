
# Détection d'Objets dans Minecraft avec YOLOv5

Ce dépôt contient un script Python pour la détection en temps réel d'objets dans Minecraft en utilisant le modèle YOLOv5 avec des catégories personnalisées. Le script utilise le modèle YOLOv5 du référentiel Ultralytics pour détecter des objets à partir d'un flux vidéo en direct. Vous pouvez sélectionner la catégorie que vous souhaitez détecter à partir d'un menu déroulant et visualiser les résultats de détection en temps réel sur l'interface utilisateur graphique.

## Prérequis

Avant d'exécuter le script, vous devez avoir les dépendances suivantes installées :

- Python (>=3.6)
- OpenCV (cv2)
- NumPy
- PyTorch
- tkinter
- Pillow (PIL)
- ultralytics

Vous pouvez installer les dépendances requises en utilisant la commande suivante :

```bash
pip install opencv-python numpy torch tkinter pillow git+https://github.com/ultralytics/yolov5.git
```

## Utilisation

1. Clonez le dépôt sur votre machine locale :

```bash
git clone https://github.com/CHATDOO/Minecraft-YOLOv5
cd Minecraft-YOLOv5
```

2. Exécutez le script :

```bash
python detection_objets.py
```

3. L'interface utilisateur graphique (GUI) s'ouvrira, affichant le flux vidéo en direct de votre webcam. Utilisez le menu déroulant pour sélectionner la catégorie que vous souhaitez détecter.

4. Cliquez sur le bouton "Démarrer la Détection" pour lancer le processus de détection d'objets. Les objets détectés seront mis en évidence dans le flux vidéo, et leurs noms seront affichés dans le terminal situé sous la vidéo.

5. Pour arrêter la détection, fermez simplement la fenêtre de l'interface utilisateur.

## Catégories Personnalisées

Le script prend en charge des catégories personnalisées pour la détection d'objets. Par défaut, les catégories suivantes sont incluses :

- vache
- creeper
- maison
- cochon
- villageois
- mouton_blanc

Vous pouvez modifier la liste `categories` dans le script pour ajouter ou supprimer des catégories en fonction de vos besoins.

## Remerciements

Ce script utilise le modèle YOLOv5 du référentiel Ultralytics. Pour plus d'informations sur YOLOv5 et le référentiel Ultralytics, veuillez vous référer à leur documentation.

Référentiel Ultralytics : https://github.com/ultralytics/yolov5

# Si vous souhaitez reprendre le modèle pré-entraîné (model.pt) ou des morceaux du script pour vos propres projets, n'hésitez pas à effectuer un fork de ce dépôt.

