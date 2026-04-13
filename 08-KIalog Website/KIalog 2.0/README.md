---
tags: [website, geschaeft, steuerung]
status: aktiv
related:
  - "[[08-KIalog Website/CLAUDE|KIalog Website]]"
---

# README — KIALOG.CH WEBSITE
# Für Claude Code | April 2026
# Lies diese Datei als Erstes. Dann die vier Dateien im Ordner. Dann arbeiten.

---

## WAS IN DIESEM ORDNER LIEGT

```
📁 kialog-briefing/
├── README.md                          ← Diese Datei. Zuerst lesen.
├── MASTERPROMPT_1_narrativ_copy.md    ← Rolle, Narrativ, vollständige Copy
├── MASTERPROMPT_2_design_farben.md    ← Design, Farben, CSS, Illustrationen
├── MASTERPROMPT_3_regeln_qualitaet.md ← Arbeitsregeln, Checklisten, Prioritäten
├── kialog-typografie-underline.md     ← Letter-Spacing, underline.svg (NEU)
└── kialog-nano-banana-prompts.md      ← Illustrationsstil FÜR MANUEL (nicht Claude Code)
```

WICHTIG — WELCHE DATEI FÜR WEN:

Für Claude Code (Website-Code):
  → MASTERPROMPT_1, MASTERPROMPT_2, MASTERPROMPT_3, kialog-typografie-underline.md

Für Manuel Hirschi (Illustrationen generieren):
  → kialog-nano-banana-prompts.md (Nano Banana Prompts für 5 Illustrationen)

Claude Code liest kialog-nano-banana-prompts.md NUR als Stil-Kontext.
Er erstellt keine Illustrationen und schreibt keine Prompts.

Diese Dateien sind dein vollständiges Briefing.
Du arbeitest ausschliesslich auf deren Basis.
Du erfindest keine Copy, keine Farben, keine Strukturen.

---

## DEIN ERSTES SETUP — PFLICHT VOR JEDER SESSION

Führe diese Schritte in dieser Reihenfolge durch:

```
1. MASTERPROMPT_1_narrativ_copy.md     vollständig lesen
2. MASTERPROMPT_2_design_farben.md     vollständig lesen
3. MASTERPROMPT_3_regeln_qualitaet.md  vollständig lesen
4. kialog-typografie-underline.md      vollständig lesen
5. Aufgabe dieser Session benennen
6. Auf Bestätigung warten
7. Erst dann arbeiten
```

kialog-nano-banana-prompts.md: nur lesen wenn du den Illustrationsstil
verstehen musst. Du erstellst keine Illustrationen.

Kein Schritt darf übersprungen werden.

---

## PROJEKTSTRUKTUR — SO LIEGT DIE WEBSITE

```
08-KIalog Website/
├── index.html                         ← Hauptseite (Netlify)
├── asset/
│   ├── logo/
│   │   └── kialog-final-blau.svg      ← Logo
│   ├── hero-lehrperson.png            ← Illustration 1: Hero
│   ├── illust-methode.png             ← Illustration 2: Methode (oder inline SVG)
│   ├── illust-arbeitsblatt.png        ← Illustration 3: Tab Berufsfachschule
│   ├── illust-vergleich.png           ← Illustration 4: Tab Gymnasium
│   ├── illust-laptop-feedback.png     ← Illustration 5: Tab PH
│   ├── illust-smartphone.png          ← Illustration 6: Kontakt
│   ├── manu2.webp                     ← Foto Manuel Hirschi
│   └── KIalog_Starter_Dossier_Schulleitungen.pdf  ← Download SL-Sektion
├── beispiel/
│   └── prototyp-praxis.html           ← Walkthrough-Seite (drei Tabs)
├── sitemap.xml
└── robots.txt
```

---

## ILLUSTRATIONEN — DEINE AUFGABE UND IHRE GRENZEN

### Was Manuel selbst macht

Alle 6 Illustrationen werden von Manuel Hirschi mit Nano Banana generiert
und als fertige Bilddateien in den Ordner `asset/` abgelegt.

Du erstellst KEINE Illustrationen.
Du schreibst KEINE Bildgenerierungs-Prompts.
Du wartest, bis die Bilddateien vorhanden sind.

### Was du mit den Illustrationen machst

Wenn eine Illustration als Datei in `asset/` vorhanden ist:
- Binde sie mit dem korrekten `<img>`-Tag ein
- Setze immer ein beschreibendes `alt`-Attribut
- Setze `loading="lazy"` für alle Illustrationen unter dem Fold
- Setze die korrekten CSS-Klassen für Grösse und Position

### Wenn eine Illustration noch fehlt

Setze einen Platzhalter ein. Exakt so:

```html
<div class="illustration-placeholder" aria-label="[Beschreibung]">
  Illustration: [Name der Illustration]
</div>
```

CSS für den Platzhalter (aus MASTERPROMPT_2):
```css
.illustration-placeholder {
  border: 2px dashed var(--farbe-blau);
  background-color: var(--farbe-beige);
  border-radius: var(--border-radius);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--farbe-text-muted);
  font-size: 0.85rem;
  padding: 32px;
  text-align: center;
  min-height: 120px;
}
```

### Welche Illustration gehört wohin

| Dateiname | Sektion | Position | Max-Breite Desktop | Max-Breite Mobile |
|-----------|---------|----------|-------------------|-------------------|
| hero-lehrperson.png | Hero | Rechts (40% Grid) | 480px | 280px, unter Buttons |
| illust-methode.png | Methode | Zwischen Intro und Schritte, volle Breite | 760px | 100% |
| illust-arbeitsblatt.png | Praxis Tab 1 | Links oben im Tab | 160px | 120px |
| illust-vergleich.png | Praxis Tab 2 | Links oben im Tab | 160px | 120px |
| illust-laptop-feedback.png | Praxis Tab 3 | Links oben im Tab | 160px | 120px |
| illust-smartphone.png | Kontakt | Rechts neben Text | 200px | 160px |

---

## METHODEN-DIAGRAMM — SPEZIALFALL

Das Methoden-Diagramm (Prüfen / Urteilen / Belegen) wird mit Excalidraw erstellt.
Nicht mit Nano Banana — Excalidraw ist für Strukturen und Diagramme zuständig.

### Wenn das Diagramm noch nicht existiert

Erstelle es mit dem Excalidraw MCP-Tool:
1. `Excalidraw:read_me` aufrufen (einmalig pro Session)
2. Diagramm gemäss Spezifikation aus MASTERPROMPT_3 erstellen
3. Als SVG exportieren
4. Inline in index.html einbinden (bevorzugt) oder als illust-methode.png ablegen

### Wenn das Diagramm bereits als PNG existiert

Direkt einbinden, keine Änderungen vornehmen.

---

## FARBEN — ABSOLUTE REGEL

Alle Farben ausschliesslich über CSS-Variablen.
Kein Hardcode-HEX irgendwo im HTML oder CSS.

Die CSS-Variablen stehen am Anfang der CSS-Datei:
```css
:root {
  --farbe-beige:           #EDEAE1;
  --farbe-beige-dunkel:    #D9D6CD;
  --farbe-text:            #2A2A2A;
  --farbe-text-muted:      #4A4A4A;
  --farbe-text-weiss:      #FFFFFF;
  --farbe-blau:            #3881F1;
  --farbe-blau-hover:      #2563D4;
  --farbe-blau-pastell:    #DBE4FF;
  --farbe-orange:          #F6612E;
  --farbe-orange-pastell:  #FFD8A8;
  --farbe-gruen:           #01C476;
  --border-radius:         12px;
  --border-radius-klein:   8px;
  --transition:            300ms ease;
}
```

Die vollständige Semantik jeder Farbe: kialog-farbkonzept.md

---

## COPY — ABSOLUTE REGEL

Du schreibst keine eigene Copy.
Der vollständige Text für jede Sektion steht in MASTERPROMPT_1_narrativ_copy.md.
Du nimmst ihn wörtlich. Du "verbesserst" nichts. Du ergänzt nichts.

Ausnahme: Manuel gibt dir explizit neuen Text vor.

---

## PUSH-REGEL — ABSOLUT

Du führst `git push` NIEMALS aus.
Du kannst `git add` und `git commit` ausführen.
Pushen nur wenn Manuel Hirschi explizit "push" schreibt.

---

## QUALITÄTSPRÜFUNG — VOR JEDEM COMMIT

Die vollständige Checkliste (Checks A–E) steht in MASTERPROMPT_3.
Alle Checks müssen bestehen bevor du committen darfst.

Kurzfassung der wichtigsten Punkte:
- Kein Grün auf Buttons oder Preisen
- Kein Orange als Fliesstext
- Hero H1 kursiv
- Anker #lehrpersonen und #schulleitungen gesetzt
- Schulleitung-Sektion: nur Sie-Form
- Alle anderen Sektionen: du-Form
- Primärer CTA: genau einer
- PDF-Download in SL-Sektion vorhanden
- Datenschutz-Zeile im Footer sichtbar
- Keine kaputten Bilder

---

## WENN DU UNSICHER BIST

Nicht raten. Nicht selbst entscheiden. Fragen.

Format:
"Ich bin unsicher bei [X]. Gemäss [MASTERPROMPT_Y] würde ich [Z] tun.
Ist das korrekt?"

Dann warten.

---

## COMMIT-MESSAGE FORMAT

```
Website [Bereich]: [Was] — [Warum]

Beispiele:
Website Hero: Schmerzsatz eingebaut — Conversion-Optimierung
Website Mobile: Tabs untereinander — UX 640px
Website SL: PDF-Download ergänzt — Reciprocity-Artefakt
Website Farben: Grün entfernt, Blau als Primär — Farbsystem
Website Bilder: illust-arbeitsblatt.png eingebunden — Tab Berufsfachschule
```

---

## ZUSAMMENFASSUNG IN EINEM SATZ

Du setzt um was in den vier Briefing-Dateien steht.
Nicht mehr. Nicht weniger. Nie ohne Bestätigung pushen.
