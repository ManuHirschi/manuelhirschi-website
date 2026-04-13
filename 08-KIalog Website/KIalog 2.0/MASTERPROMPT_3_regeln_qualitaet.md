---
tags: [website, geschaeft]
status: aktiv
related:
  - "[[08-KIalog Website/KIalog 2.0/README|KIalog 2.0 Briefing]]"
  - "[[08-KIalog Website/CLAUDE|KIalog Website]]"
---

# MASTER PROMPT 3 — ARBEITSREGELN, QUALITÄTSSICHERUNG, PRIORISIERUNG
# kialog.ch | Claude Code | April 2026
# Lies vollständig. Diese Regeln gelten für jede Session ohne Ausnahme.
# Nie pushen ohne explizites "push" von Manuel Hirschi.

---

## ARBEITSREGELN — ABSOLUT VERBINDLICH

REGEL 1 — NIE PUSHEN OHNE EXPLIZITES "PUSH"
  Du führst git push NIEMALS aus ausser Manuel Hirschi sagt explizit "push".
  Du kannst committen, aber nicht pushen.
  Bei Unklarheit: fragen, nicht handeln.

REGEL 2 — MASTER PROMPTS ZUERST LESEN
  Vor jeder Session: MASTERPROMPT_1, MASTERPROMPT_2 und diesen Prompt vollständig lesen.
  Dann: Was ist die Aufgabe dieser Session? Welche Sektionen sind betroffen?
  Erst dann: Code schreiben.

REGEL 3 — DIAGNOSE VOR PRODUKTION
  Bevor du etwas änderst: Benennen was du änderst und warum.
  Format: "Ich ändere [X] weil [Y]. Das Ergebnis ist [Z]."
  Wenn du das nicht sagen kannst: nicht ändern.

REGEL 4 — EINE AUFGABE, DANN REPORT
  Führe eine Aufgabe aus. Berichte was du gemacht hast.
  Warte auf Bestätigung vor der nächsten Aufgabe.
  Nicht mehrere Änderungen bündeln ohne Report dazwischen.

REGEL 5 — WIDERSPRECHEN WENN NÖTIG
  Wenn eine Anweisung dem Briefing widerspricht: sofort sagen.
  Nicht ausführen und schweigen.
  Format: "Diese Anweisung widerspricht [Briefing-Punkt X]. Soll ich trotzdem?"

REGEL 6 — KEINE EIGENINITIATIVE BEI COPY
  Copy (Text, Headlines, Sätze) nie selbst erfinden oder "verbessern".
  Nur was in MASTERPROMPT_1 steht, steht auf der Seite.
  Ausnahme: Manuel gibt explizit neuen Text vor.

REGEL 7 — KEINE EIGENINITIATIVE BEI FARBEN
  Farben nur aus MASTERPROMPT_2 CSS-Variablen.
  Kein Hardcode-HEX im HTML oder CSS.
  Kein neues Grün, kein neues Lila, kein Gradient.

---

## DATEISTRUKTUR (verbindlich)

```
08-KIalog Website/
├── index.html                    ← Hauptseite
├── asset/
│   ├── logo/
│   │   └── kialog-final-blau.svg
│   ├── hero-lehrperson.png       ← Illustration Hero
│   ├── illust-methode.png        ← Methoden-Diagramm (oder inline SVG)
│   ├── illust-arbeitsblatt.png   ← Tab Berufsfachschule
│   ├── illust-vergleich.png      ← Tab Gymnasium
│   ├── illust-laptop-feedback.png ← Tab PH
│   ├── illust-smartphone.png     ← Kontakt
│   ├── manu2.webp               ← Foto Manuel
│   └── KIalog_Starter_Dossier_Schulleitungen.pdf ← Download
├── beispiel/
│   └── prototyp-praxis.html     ← Walkthrough-Seite
├── sitemap.xml
├── robots.txt
└── docs/                        ← Master Prompts (nicht im Repo nötig)
```

---

## QUALITÄTSPRÜFUNG — VOR JEDEM COMMIT

Führe diese Checks in dieser Reihenfolge durch. Alle müssen bestehen.

### CHECK A — COPY

[ ] Hero-Headline: "KI ist im Unterricht. Was jetzt?" — kursiv, H1
[ ] Hero-Schmerzsatz: vorhanden, direkt unter Headline
[ ] Hero-Dreifachprofil: "gibb Bern · PH FHNW · UZH"
[ ] Sektion 2 Anker: id="lehrpersonen" gesetzt
[ ] Sektion 5 Anker: id="schulleitungen" gesetzt
[ ] Schulleitung-Sektion: ausschliesslich Sie-Form
[ ] Alle anderen Sektionen: du-Form
[ ] Warum-ich Argument-Satz: "Ich bin der Einzige in der Deutschschweiz..."
[ ] Markensatz: "Wer mit KI arbeitet, führt einen Dialog..."
[ ] Praxis Ankersatz: "8 Minuten statt 45" sichtbar auf Ebene 1
[ ] Kostensatz LP: "Alle Formate werden von der Schule gebucht..." vor Angebote
[ ] ROI-Satz SL: "Ein CAS-Programm kostet CHF 9'900..." in SL-Sektion
[ ] Nachklick-Satz: "Ich melde mich innert 48 Stunden..." unter SL-Button
[ ] PDF-Download: in SL-Sektion, direkter Link, kein Formular
[ ] Primärer CTA: genau einer "Jetzt anfragen" als Haupt-Button
[ ] Datenschutz-Zeile: im Footer sichtbar
[ ] Keine verbotenen Begriffe (Bildungsentwickler, Marktlücke, gratis...)

### CHECK B — DESIGN

[ ] Kein Grün (#01C476) auf Buttons oder Preisen
[ ] Kein Orange (#F6612E) als Fliesstext
[ ] Kein #5A5A5A als regulärer Fliesstext (nur < 12px)
[ ] Kein Gradient irgendwo
[ ] Scalloped Edge: nur in Kontakt/Footer-Sektion
[ ] Dashed Borders: nur Platzhalter-Boxes und Angebots-Cards
[ ] Keine Lottie-Animationen
[ ] Alle Farben über CSS-Variablen (kein Hardcode-HEX)
[ ] Hero H1: kursiv
[ ] Markensatz: kursiv, blau

### CHECK C — MOBILE

[ ] Hero-Buttons: untereinander, volle Breite (max-width: 640px)
[ ] Praxis-Tabs: untereinander, nicht scrollbar (max-width: 640px)
[ ] Illustration Tab: max 120px auf Mobile, nach unten verschoben
[ ] Methode-Grid: einspaltig auf Mobile
[ ] Angebots-Karten: einspaltig auf Mobile
[ ] Schrift lesbar (min. 16px für Fliesstext)

### CHECK D — TECHNISCH

[ ] robots.txt: kein "Disallow: /"
[ ] sitemap.xml: vorhanden unter kialog.ch/sitemap.xml
[ ] Meta-Tags: Title und Description vorhanden und korrekt
[ ] Alle img-Tags: loading="lazy" (ausser Hero-Illustration)
[ ] Alle img-Tags: alt-Attribut vorhanden und beschreibend
[ ] Kein console.error in der Browser-Konsole
[ ] Keine kaputten Bilder (naturalWidth > 0 für alle img)
[ ] Alle Anker-Links funktionieren (#lehrpersonen, #schulleitungen, #kontakt etc.)
[ ] PDF-Download-Link erreichbar

### CHECK E — ACCESSIBILITY

[ ] Alle Buttons: min-height 44px
[ ] :focus-visible: sichtbarer Fokusring
[ ] Kontrastwerte eingehalten (siehe MASTERPROMPT_2)

---

## PRIORISIERTE AUFGABENLISTE

Bearbeite in dieser Reihenfolge. Nicht überspringen.

### PRIORITÄT 1 — SOFORT (aktuelle Session)

1. Hero-Schmerzsatz einbauen
   "Deine Lernenden schreiben Texte mit KI. Du weisst nicht wie du den Output beurteilen sollst."
   Position: direkt unter H1, eigene Zeile, font-weight 400, nicht kursiv.

2. Warum-ich Argument-Satz einbauen
   "Ich bin der Einzige in der Deutschschweiz, der KI-Didaktik gleichzeitig erforscht,
   in der Lehrerinnen- und Lehrerausbildung unterrichtet und täglich im eigenen
   Klassenzimmer anwendet."
   Position: erste Zeile nach H2, kursiv, font-size 1.15rem.

3. Praxis Ankersatz einbauen
   "EBA-Klasse, Lehrvertrag, DaZ-Anteil. Ein differenziertes Arbeitsblatt auf drei Niveaus.
   Mit KI und der KIalog-Methode: 8 Minuten statt 45."
   Position: vor den Tab-Buttons, fett, eigene Box.

4. PDF-Download in Schulleitung-Sektion
   href="asset/KIalog_Starter_Dossier_Schulleitungen.pdf"
   Text: "Starter-Dossier herunterladen (PDF)"
   Hinweis darunter: "Kostenlos. Kein Formular. Direkt nützlich."

5. CTAs reduzieren
   Primärer CTA: genau einer, am Ende der Angebote-Sektion.
   Alle anderen "Jetzt anfragen": entfernen oder zu Textlinks reduzieren.

### PRIORITÄT 2 — DIESE SESSION WENN ZEIT

6. Mobile: Praxis-Tabs untereinander
   CSS: .tabs-nav { flex-direction: column; } auf max-width: 640px

7. Mobile: Illustration max-width
   CSS: .illustration-tab { max-width: 120px; } auf max-width: 640px

8. Beispiel-Seite: Meta-Tags
   Title: "KIalog in der Praxis — drei echte Walkthroughs | kialog.ch"
   Description: "Drei konkrete Situationen: Arbeitsblatt auf 3 Niveaus (8 Minuten),
   KI-Feedback auf Fallanalyse, KI-resistente Prüfung."

9. Open Graph Tags auf index.html einbauen

### PRIORITÄT 3 — NÄCHSTE SESSION

10. Bilder zu WebP konvertieren (PNG → WebP, max 200KB)
11. Zahl-Counter für 93% und 23% einbauen
12. Beispiel-Seite: Zurück-Link mit sichtbarem Text "← Zurück zu KIalog"
13. Kontrastwert #5A5A5A prüfen und wo nötig durch #4A4A4A ersetzen

### PRIORITÄT 4 — NACH PILOTEN

14. Referenz-Slots befüllen (Name, Institution, konkretes Ergebnis)
15. Article-Schema.org für erste Forschungsnotiz
16. Testimonials: min. Name + Institution + ein konkreter Satz

---

## NANO BANANA PROMPTS — VERWEIS

WICHTIG: Die Nano Banana Prompts sind VERALTET in diesem Dokument.
Der aktuelle, verbindliche Illustrationsstil steht in:

  kialog-nano-banana-prompts.md

Diese Datei ist FÜR MANUEL HIRSCHI — nicht für Claude Code.
Manuel generiert die Illustrationen selbst und legt sie als fertige
PNG-Dateien in asset/ ab. Claude Code bindet sie nur ein.

Claude Code: Ignoriere alle alten Prompt-Vorlagen. Lies stattdessen
kialog-nano-banana-prompts.md wenn du den Stil-Kontext brauchst.

---

## EXCALIDRAW — METHODEN-DIAGRAMM

Wenn das Diagramm neu erstellt oder angepasst werden muss:

TOOL: Excalidraw MCP (Excalidraw:read_me zuerst aufrufen)

VERBINDLICHE SPEZIFIKATION:
```
Kamera: width 800, height 600 (4:3 — zwingend)
Hintergrund-Rechteck: #f0ede4, transparent stroke
Titel: "KIalog Methode", fontSize 30, #2A2A2A
Untertitel: "Drei Schritte. Dein Urteil.", fontSize 18, #5A5A5A
Schritt-Labels: "Schritt 1/2/3", fontSize 15, #F6612E (orange)
Boxen: backgroundColor #dbe4ff, strokeColor #3881F1, strokeWidth 2, roughness 2, roundness type 3
Pfeile: strokeColor #3881F1, endArrowhead "arrow", roughness 2
Unterzeilen Boxen: fontSize 14, #5A5A5A
  Box 1: "Stimmt das fachlich?"
  Box 2: "Übernehmen, anpassen oder verwerfen?"
  Box 3: "Warum habe ich das entschieden?"
Abschluss-Banner: backgroundColor #3881F1, weisser Text
  "Dieselbe Methode — Arbeitsblatt, Prüfung oder Feedback."
Export: SVG, inline in index.html einbinden
```

CSS für SVG-Einbindung:
```css
.methode-diagramm {
  width: 100%;
  max-width: 760px;
  margin: 2rem auto;
}
.methode-diagramm svg {
  width: 100%;
  height: auto;
}
```

---

## SESSION-START-ROUTINE

Jede Session beginnt mit:

1. MASTERPROMPT_1_narrativ_copy.md lesen (Rolle, Narrativ, Copy)
2. MASTERPROMPT_2_design_farben.md lesen (Design, Farben, Illustrationen)
3. MASTERPROMPT_3_regeln_qualitaet.md lesen (Arbeitsregeln, Checkliste)
4. kialog-typografie-underline.md lesen (Letter-Spacing, underline.svg)
5. Aufgabe dieser Session benennen:
   "Aufgabe: [X]. Betroffen: [Sektionen]. Vorgehen: [Schritte]."
6. Bestätigung abwarten, dann arbeiten.
7. Nach jeder Änderung: kurzer Report.
8. Nie pushen ohne explizites "push" von Manuel Hirschi.

---

## SESSION-END-ROUTINE

Jede Session endet mit:

1. Qualitätsprüfung Checks A–E durchführen (MASTERPROMPT_3, Sektion oben)
2. Report: Was wurde gemacht? Was ist noch offen?
3. Nächste Priorität benennen.
4. Commit (wenn alles passt): git add + git commit mit beschreibendem Message.
5. Warten auf "push" von Manuel Hirschi.

---

## COMMIT-MESSAGE FORMAT

```
Website [Bereich]: [Was wurde geändert] — [kurze Begründung]

Beispiele:
Website Hero: Schmerzsatz eingebaut — Conversion-Optimierung
Website Mobile: Praxis-Tabs untereinander — UX auf 640px
Website SL: PDF-Download ergänzt — Reciprocity-Artefakt
Website Fixes: Grün entfernt, Blau als Primärfarbe — Farbsystem
```

---

# ENDE MASTER PROMPT 3
# ALLE DREI PROMPTS ZUSAMMEN = VOLLSTÄNDIGES BRIEFING FÜR JEDE SESSION
