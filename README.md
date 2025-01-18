# Enigma

[![Python](https://img.shields.io/badge/Python-v3.11.4-blue)](https://www.python.org/)

Emulation d'une machine Enigma

## Description

Ce projet est une émulation de la machine Enigma utilisée pendant la Seconde Guerre mondiale pour chiffrer et déchiffrer des messages. La machine Enigma utilise une série de rotors, un réflecteur et un tableau de connexions pour transformer chaque lettre du message.

## Installation

Clonez le dépôt et assurez-vous d'avoir Python installé sur votre machine.

```bash
git clone https://github.com/Nicolas-Loisy/Enigma.git
cd Enigma
```

## Utilisation

### Exécution de l'interface utilisateur

Pour exécuter l'interface utilisateur de la machine Enigma, lancez le script `app_ui.py`.

```bash
python app_ui.py
```

### Exécution du script en ligne de commande

Pour exécuter l'émulation de la machine Enigma via la ligne de commande, lancez le script `app.py`.

```bash
python app.py
```

Le script chiffrera et déchiffrera un message.

### Génération d'un exécutable

Pour générer un exécutable de l'application, utilisez `PyInstaller`. Assurez-vous d'avoir `PyInstaller` installé :

```bash
pip install pyinstaller
```

Ensuite, générez l'exécutable :

```bash
pyinstaller --onefile --windowed app_ui.py
```

L'exécutable sera créé dans le répertoire `dist`.

### Exécutable prêt à l'emploi

Un exécutable prêt à l'emploi est déjà disponible à la racine du projet. Vous pouvez l'exécuter directement sans avoir besoin de Python ou de générer un nouvel exécutable.

## Vidéo

Pour plus d'informations, vous pouvez regarder cette vidéo : [Enigma Machine](https://youtu.be/ybkkiGtJmkM?t=496)
