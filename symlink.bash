#!/bin/bash

# Pfad zum Zielverzeichnis
target_dir="/home/nao/.local/share/PackageManager/apps/"

# Name des symbolischen Links
link_name="voice_handler"

# Pfad zum Quellverzeichnis
source_dir="/home/nao/voice_handler"

# Erstellen des symbolischen Links
ln -s "$source_dir" "$target_dir$link_name"

# Ausgabe der Erfolgsmeldung
echo "Symbolischer Link für Webapplikation wurde erfolgreich erstellt."

# Pfad zum Zielverzeichnis für Videos
target_dir_videos="/home/nao/voice_handler/html/"
# Pfad zum Quellverzeichnis für Videos
source_dir_videos="/home/nao/voice_handler/videos"

# Erstellen des symbolischen Links für Videos
ln -s "$source_dir_videos" "$target_dir_videos"

# Ausgabe der Erfolgsmeldung für Videos
echo "Symbolischer Link für Videos wurde erfolgreich erstellt."

# Pfad zum Zielverzeichnis für Bilder
target_dir_images="/home/nao/voice_handler/html/"
# Pfad zum Quellverzeichnis für Bilder
source_dir_images="/home/nao/voice_handler/images"

# Erstellen des symbolischen Links für Bilder
ln -s "$source_dir_images" "$target_dir_images"

# Ausgabe der Erfolgsmeldung für Bilder
echo "Symbolischer Link für Bilder wurde erfolgreich erstellt."