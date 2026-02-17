# Image Pixelator with Binary Pattern Filter 🖼️

Ein Python-Programm, das Bilder in pixelierte Blöcke mit binären (1/0) Mustern umwandelt. Jeder Block wird mit der durchschnittlichen Farbe des Bereichs gefärbt und mit einem Schachbrett-, Diagonal- oder anderen Mustern gefüllt.

## Features ✨

- **Verschiedene Muster**: Schachbrett, Diagonal, Horizontal, Vertikal
- **Konfigurierbare Blockgröße**: Passe die Pixelgröße an
- **GUI & CLI**: Benutzerfreundliche Grafische Oberfläche + Kommandozeilenschnittstelle
- **Farberhaltung**: Behält die Originalfarben durch Durchschnittswertberechnung
- **Für GitHub bereit**: Vollständig dokumentiert und strukturiert

## Anforderungen 📋

- Python 3.8+
- Pillow (PIL) - Bildverarbeitung
- OpenCV (cv2) - Bildverarbeitung
- NumPy - Numerische Berechnungen

  
Siehe `requirements.txt` für genaue Versionen.
  
## Installation 📦

```bash
# Repository klonen
git clone https://github.com/Chaoskjell/image-pixelator.git
cd image-pixelator

# Dependencies installieren
pip install -r requirements.txt
```
oder 

Lade die datein als zip herrunter und öfne sie in einem code maniger wie VSC.
Stelle sicher das alle dipendensis insterlirt sind.

## Verwendung 🚀

### GUI starten (einfach)

```bash
python gui_pixelator.py
```

### CLI verwenden (erweitert)

```bash
# Grundlegende Nutzung
python image_pixelator.py input.jpg

# Mit Optionen
python image_pixelator.py input.jpg -b 15 -p diagonal -o output.png
```

### CLI Parameter

| Parameter | Kurz | Beschreibung | Standard |
|-----------|------|-------------|----------|
| Input | `-` | Eingabedatei-Pfad | **erforderlich** |
| --block-size | `-b` | Größe der Pixelblöcke | 10 |
| --pattern | `-p` | Mustertyp | checkerboard |
| --output | `-o` | Ausgabedatei-Pfad | output_[pattern].png |

### Verfügbare Muster

- **checkerboard** - Klassisches Schachbrettmuster
- **diagonal** - Diagonale Linien
- **horizontal** - Horizontale Streifen
- **vertical** - Vertikale Streifen

## Beispiele 💡

```bash
# GUI starten
python gui_pixelator.py

# CLI: Schachbrettmuster mit 10x10 Pixeln
python image_pixelator.py photo.jpg -b 10 -p checkerboard -o output.png

# CLI: Diagonales Muster mit größeren Blöcken
python image_pixelator.py photo.jpg -b 20 -p diagonal -o diagonal.png
```

## Wie es funktioniert 🔧

1. **Laden** - Das Eingabebild wird geladen und in RGB konvertiert
2. **Blockierung** - Das Bild wird in Blöcke der Größe `block_size × block_size` unterteilt
3. **Farbberechnung** - Für jeden Block wird die Durchschnittsfarbe berechnet
4. **Musterzeichnung** - Der Block wird mit dem gewählten Muster in der berechneten Farbe gefüllt:
   - `1` = Farbzelle (gefüllt)
   - `0` = Leere Zelle (weiß)
5. **Speicherung** - Das finale Bild wird als PNG/JPG gespeichert

## Unterstützte Bildformate 🖼️

- PNG
- JPG/JPEG
- BMP
- GIF
- TIFF

## Performance ⚡

| Blockgröße | Schnelligkeit | Details |
|-----------|---------------|---------|
| 5-15 | Mittel | Gutes Detail-Muster-Balance |
| 15-25 | Schnell | Grosse Blöcke, weniger Details |
| 25+ | Sehr schnell | Minimales Muster-Detail |

## Lizenz 📄

MIT License - Kostenlos für persönliche und kommerzielle Nutzung. Siehe [LICENSE](LICENSE) für Details.

## Beitragen 🤝

Beiträge sind willkommen! Bitte siehe [CONTRIBUTING.md](CONTRIBUTING.md) für Details.

## Community 💬

- 📧 [Issues](../../issues) - Bugs melden
- 💡 [Discussions](../../discussions) - Fragen & Ideen
- 🤝 [Pull Requests](../../pulls) - Beiträge

## Roadmap 🛣️

- [ ] GUI mit erweiterten Optionen
- [ ] Animierte GIF-Unterstützung
- [ ] Zusätzliche Muster (Noise, Wave, etc.)
- [ ] Performance-Optimierungen

## Kontakt 📧

Bei Fragen oder Problemen öffne bitte ein [Issue](../../issues) auf GitHub!

---

**Made with ❤️ in Python**
