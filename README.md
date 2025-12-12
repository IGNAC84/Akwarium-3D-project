# Aquarium 3D Project — Start / Extended pack

Zawartość:
- aquarium_scene.json        — opis sceny 3D (punkty referencyjne, pozycje korzeni, skał, filtra)
- aquarium_blender.py       — starter Python script (Blender) do zaimportowania sceny (ustawienia kamer, prosty materiał drewna)
- aquarium_layout.svg       — widok 2D (front/top) rozkładu elementów
- aquarium_roots.svg        — wektorowy szkic korzeni (przygotowane ścieżki do modelowania)
- feeding_schedule.txt      — plan karmienia ogólny
- feeding_schedule_color_intensity.txt — plan karmienia z naciskiem na intensyfikację barw tęczanek
- project_structure.txt     — krótka instrukcja gdzie co wrzucić / jak złożyć ZIP

Instrukcja szybkiego użycia:
1. Wypakuj paczkę.
2. W Blender: otwórz `aquarium_blender.py` (zakłada Blender 3.x) i uruchom skrypt (File → New → Text Editor → Open → Run Script). Skrypt ustawi prostą scenę, zaimportuje `aquarium_scene.json` (parsing) i utworzy kamerę + światła.
3. SVG możesz wykorzystać jako referencję (wczytać do programu do modelowania lub edytować).
4. Plan karmienia służy do generowania PDF (skopiuj do edytora i eksportuj jako PDF).

Licencja: pliki w paczce służą do użytku prywatnego. Możesz je wersjonować w repo GitHub.

Kontakt: jeśli chcesz wersję z dokładnym modelem 3D (mesh korzeni), daj znać — dopracuję walidowany OBJ/GLTF.