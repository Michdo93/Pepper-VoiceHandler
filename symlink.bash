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
echo "Symbolischer Link wurde erfolgreich erstellt."