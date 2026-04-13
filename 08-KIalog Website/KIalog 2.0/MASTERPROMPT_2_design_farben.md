---
tags: [website, geschaeft]
status: aktiv
related:
  - "[[08-KIalog Website/KIalog 2.0/README|KIalog 2.0 Briefing]]"
  - "[[08-KIalog Website/CLAUDE|KIalog Website]]"
---

# MASTER PROMPT 2 — DESIGN, FARBEN, ILLUSTRATIONEN
# kialog.ch | Claude Code | April 2026
# Lies vollständig bevor du eine CSS-Zeile schreibst.
# Nie pushen ohne explizites "push" von Manuel Hirschi.

---

## DESIGNPRINZIP (ÜBERGEORDNET)

Design ist die visuelle Übersetzung des Inhalts. Nicht Dekoration.

Jedes Designelement muss eine Funktion erfüllen:
- Farbe → hat semantische Bedeutung (nicht dekorativ)
- Illustration → erklärt etwas (nicht schmückt etwas)
- Animation → lenkt Aufmerksamkeit oder gibt Feedback (nicht unterhält)
- Weissraum → ist Aussage (nicht Leere)

Das Grundgefühl: Handwerklich, menschlich, präzise.
NICHT: institutionell-kalt (Kanton-Ästhetik)
NICHT: edtech-hype (Neon, Gradients, KI-Gehirne)

---

## CSS-VARIABLEN — VOLLSTÄNDIG (am Anfang der CSS-Datei)

```css
:root {
  /* HINTERGRUND */
  --farbe-beige:              #EDEAE1;  /* Primärer Hintergrund — fast überall */
  --farbe-beige-dunkel:       #D9D6CD;  /* Trennlinien, Card-Hintergründe */

  /* TEXT */
  --farbe-text:               #2A2A2A;  /* Headlines, Fliesstext, Labels */
  --farbe-text-muted:         #4A4A4A;  /* Quellenangaben, Meta, FAQ-Antworten */
  --farbe-text-sehr-muted:    #5A5A5A;  /* NUR für Texte unter 12px */
  --farbe-text-weiss:         #FFFFFF;  /* Nur auf blauem Hintergrund */

  /* PRIMÄR — METHODE UND HANDLUNG */
  --farbe-blau:               #3881F1;  /* CTA-Button, Methoden-Boxen, aktiver Tab */
  --farbe-blau-hover:         #2563D4;  /* Button-Hover, 10% dunkler */
  --farbe-blau-pastell:       #DBE4FF;  /* Hintergrund Methoden-Boxen */

  /* AKZENT — KORREKTUR UND ENERGIE */
  --farbe-orange:             #F6612E;  /* Schritt-Labels, KI-Fehler in Before/After */
  --farbe-orange-pastell:     #FFD8A8;  /* Hintergrund-Tint wo Orange zu stark */

  /* ZUSTAND */
  --farbe-gruen:              #01C476;  /* NUR: ✓ Symbole in Walkthroughs */
  /* --farbe-lilac: #D7BCED  RESERVIERT — nicht verwenden */

  /* STRUKTUR */
  --border-radius:            12px;
  --border-radius-klein:      8px;
  --border-radius-gross:      20px;
  --transition:               300ms ease;
}
```

---

## FARBSEMANTIK — VERBINDLICH

BLAU (#3881F1) = Methode und Handlung.
  Einsatz: Primärer CTA-Button, Drei-Schritte-Boxen, Diagramm-Rahmen,
  aktiver Tab, Markensatz, Schulleitung-Sektion Hintergrund.
  NIEMALS: für Schritt-Labels, Fehler-Markierungen.

ORANGE (#F6612E) = Korrektur und Energie.
  Einsatz: "Schritt 1/2/3" Labels, KI-Fehler in Before/After-Visuals,
  Illustration-Akzente.
  NIEMALS: für Buttons, Preise, Flächen.
  ACHTUNG: Nur für grosse, fette Elemente (>18px bold) — kein Kontrast als Fliesstext.

GRÜN (#01C476) = Bestätigung.
  Einsatz: Ausschliesslich ✓ Symbole und "übernommen" in Walkthroughs.
  NIEMALS: für Buttons, Preise, Highlights.

BEIGE (#EDEAE1) = Ruhe und Vertrautheit.
  Einsatz: Seitenhintergrund, Card-Flächen, Illustration-Hintergrund.

---

## TYPOGRAFIE

SCHRIFT: Figtree (Google Fonts)
  @import: https://fonts.googleapis.com/css2?family=Figtree:wght@300;400;600;700;800&display=swap

GEWICHTE UND EINSATZ:
  300 Light   → Lange Fliesstexte (entlastend)
  400 Regular → Sublines, FAQ-Antworten
  600 SemiBold → Schritt-Titel, Labels, Teaser-Sätze
  700 Bold    → Headlines H2, H3, Kernaussagen
  800 ExtraBold → Hero H1, Statistik-Zahlen

SCHRIFTGRÖSSEN (clamp für responsives Scaling):
```css
h1          { font-size: clamp(2.2rem, 5.5vw, 4rem); font-weight: 800; font-style: italic; }
h2          { font-size: clamp(1.6rem, 3.5vw, 2.5rem); font-weight: 700; }
h3          { font-size: clamp(1.1rem, 2.5vw, 1.4rem); font-weight: 600; }
.subline    { font-size: clamp(1rem, 2vw, 1.2rem); font-weight: 400; }
body, p     { font-size: 1.05rem; line-height: 1.75; font-weight: 300; }
.meta       { font-size: 0.85rem; line-height: 1.5; color: var(--farbe-text-muted); }
.stat-zahl  { font-size: clamp(1.8rem, 4vw, 3rem); font-weight: 800; color: var(--farbe-blau); }
```

KURSIV-REGEL:
  Hero H1: immer kursiv (font-style: italic).
  Markensatz: kursiv, blau.
  Argument-Satz (Warum-ich): kursiv, leicht grösser als Fliesstext.
  Kursiv = flüstert eindringlich. Bold = schreit. Für Kernaussagen: kursiv bevorzugen.

---

## LAYOUT

MAX-WIDTH: 1100px, zentriert.
TEXT-CONTENT-WIDTH: 760px (für Lesebarkeit — nie breiter).
SEKTIONS-ABSTÄNDE:
```css
section { padding: 80px 40px; }           /* Desktop */
@media (max-width: 640px) {
  section { padding: 48px 24px; }          /* Mobile */
}
```

GRID — HERO:
```css
.hero-grid {
  display: grid;
  grid-template-columns: 60% 40%;
  gap: 40px;
  align-items: center;
}
@media (max-width: 640px) {
  .hero-grid { grid-template-columns: 1fr; }
}
```

GRID — DREI KARTEN (Angebote):
```css
.karten-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}
@media (max-width: 768px) {
  .karten-grid { grid-template-columns: 1fr; }
}
```

---

## BUTTONS

PRIMÄR (blau, gefüllt):
```css
.btn-primary {
  background-color: var(--farbe-blau);
  color: var(--farbe-text-weiss);
  border: 2px solid var(--farbe-blau);
  border-radius: 50px;
  padding: 14px 28px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: var(--transition);
  min-height: 44px;
  min-width: 44px;
  display: inline-flex;
  align-items: center;
}
.btn-primary:hover {
  background-color: var(--farbe-blau-hover);
  border-color: var(--farbe-blau-hover);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(56, 129, 241, 0.3);
}
```

OUTLINED (transparent, blauer Rahmen):
```css
.btn-outline {
  background-color: transparent;
  color: var(--farbe-blau);
  border: 2px solid var(--farbe-blau);
  border-radius: 50px;
  padding: 14px 28px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: var(--transition);
  min-height: 44px;
}
.btn-outline:hover {
  background-color: var(--farbe-blau);
  color: var(--farbe-text-weiss);
}
```

WEISS AUF BLAU (nur in Schulleitung-Sektion und Kontakt):
```css
.btn-weiss {
  background-color: var(--farbe-text-weiss);
  color: var(--farbe-blau);
  border: 2px solid var(--farbe-text-weiss);
  border-radius: 50px;
  padding: 14px 28px;
  font-weight: 600;
  min-height: 44px;
}
```

HERO-BUTTONS MOBILE (untereinander, volle Breite):
```css
@media (max-width: 640px) {
  .hero-buttons {
    display: flex;
    flex-direction: column;
    gap: 12px;
  }
  .hero-buttons .btn-primary,
  .hero-buttons .btn-outline {
    width: 100%;
    justify-content: center;
  }
}
```

---

## ILLUSTRATIONEN

GRUNDPRINZIP: Jede Illustration erklärt etwas. Keine Illustration schmückt nur.
MAXIMAL eine Illustration pro Sektion.

STIL (für Nano Banana Prompts — exakt so):
```
Stil: Hand-drawn sketch, single weight line, clean doodle
Hintergrund: transparent
Linien: #2A2A2A, 2px Kontur, 1.5px Innenlinien
Farbflächen: sparsam, max 2 Akzentfarben
  Blaue Fläche: #DBE4FF (nie #3881F1 als Fläche)
  Orange Fläche: #FFD8A8 (nie #F6612E als Fläche)
Kein Gradient, kein schwerer Schatten, kein Neon
Format: WebP (bevorzugt) oder PNG
```

GRÖSSEN:
```css
.illustration-hero    { max-width: 480px; width: 100%; height: auto; }
.illustration-methode { max-width: 100%; height: auto; }  /* volle Breite */
.illustration-tab     { max-width: 160px; height: auto; } /* Praxis-Tabs */
.illustration-kontakt { max-width: 200px; height: auto; }

@media (max-width: 640px) {
  .illustration-hero  { max-width: 280px; margin: 0 auto; }
  .illustration-tab   { max-width: 120px; }
}
```

ILLUSTRATIONEN UND IHRE DATEIEN:
  Hero:              asset/hero-lehrperson.png
  Methode (SVG):     asset/illust-methode.png ODER inline SVG bevorzugt
  Tab Berufsfachschule: asset/illust-arbeitsblatt.png
  Tab Gymnasium:     asset/illust-vergleich.png
  Tab PH:            asset/illust-laptop-feedback.png
  Kontakt:           asset/illust-smartphone.png

PLATZHALTER wenn Illustration fehlt:
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
}
```

---

## BEFORE/AFTER VISUAL (Praxis-Tabs)

Kein Bild — strukturiertes HTML/CSS. Zwei Spalten, Kontrast, Kernzahl.

```css
.before-after {
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  gap: 24px;
  align-items: start;
  background: var(--farbe-beige);
  border-radius: var(--border-radius);
  padding: 28px;
  margin: 20px 0;
}
.before-after .label {
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--farbe-text-muted);
  display: block;
  margin-bottom: 10px;
}
.before-after .before ul li { color: var(--farbe-orange); font-weight: 600; }
.before-after .after ul li  { color: var(--farbe-blau);   font-weight: 600; }
.before-after .pfeil        { color: var(--farbe-blau); font-size: 1.5rem; padding-top: 28px; }
.before-after .kernzahl {
  grid-column: 1 / -1;
  text-align: center;
  font-size: 1.2rem;
  font-weight: 800;
  color: var(--farbe-blau);
  padding-top: 16px;
  border-top: 1px solid var(--farbe-beige-dunkel);
  margin-top: 8px;
}
@media (max-width: 640px) {
  .before-after { grid-template-columns: 1fr; }
  .before-after .pfeil { display: none; }
}
```

---

## ANIMATIONEN

REGEL: Animation hat einen Zweck oder sie existiert nicht.
  Zweck 1: Aufmerksamkeit auf etwas Wichtiges lenken.
  Zweck 2: Einen Prozess erklären.
  Zweck 3: Feedback auf eine Handlung geben.

ERLAUBT:

1. SCROLL-FADE für Sektionen:
```css
.sektion-fade {
  opacity: 0;
  transform: translateY(16px);
  transition: opacity 300ms ease, transform 300ms ease;
}
.sektion-fade.sichtbar {
  opacity: 1;
  transform: translateY(0);
}
```
```javascript
const observer = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) e.target.classList.add('sichtbar');
  });
}, { threshold: 0.15 });
document.querySelectorAll('.sektion-fade').forEach(el => observer.observe(el));
```

2. ZAHL-COUNTER für Stats (93%, 23%):
```javascript
function countUp(el, target, duration = 800) {
  let start = 0;
  const step = target / (duration / 16);
  const timer = setInterval(() => {
    start += step;
    if (start >= target) { el.textContent = target + '%'; clearInterval(timer); return; }
    el.textContent = Math.floor(start) + '%';
  }, 16);
}
// Nur ausführen wenn Element im Viewport.
```

3. TAB-WECHSEL (opacity):
```css
.tab-content { transition: opacity 200ms ease; }
.tab-content.wechseln { opacity: 0; }
```

VERBOTEN:
- Lottie-Animationen (weg, bereits entschieden)
- Parallax-Scrolling (Mobile-Übelkeit)
- Animierter Hero-Text (Headline muss sofort lesbar sein)
- KI-typische Tipp-Animationen oder Text-Generierungs-Effekte

---

## TABS (Praxis-Sektion)

DESKTOP: Drei Tabs nebeneinander, horizontal.
MOBILE: Tabs untereinander, volle Breite.

```css
.tabs-nav {
  display: flex;
  gap: 4px;
  border-bottom: 2px solid var(--farbe-beige-dunkel);
  margin-bottom: 32px;
}
.tab-btn {
  padding: 12px 20px;
  font-weight: 600;
  color: var(--farbe-text-muted);
  background: transparent;
  border: none;
  border-bottom: 3px solid transparent;
  margin-bottom: -2px;
  cursor: pointer;
  transition: var(--transition);
}
.tab-btn.aktiv {
  color: var(--farbe-blau);
  border-bottom-color: var(--farbe-blau);
}

@media (max-width: 640px) {
  .tabs-nav {
    flex-direction: column;
    border-bottom: none;
    gap: 8px;
  }
  .tab-btn {
    width: 100%;
    text-align: left;
    border: 2px solid var(--farbe-beige-dunkel);
    border-radius: var(--border-radius-klein);
    border-bottom: 2px solid var(--farbe-beige-dunkel);
    margin-bottom: 0;
  }
  .tab-btn.aktiv {
    border-color: var(--farbe-blau);
    background: var(--farbe-blau-pastell);
  }
}
```

TAB-INHALT-LAYOUT:
```css
.tab-inhalt-grid {
  display: grid;
  grid-template-columns: 160px 1fr;
  gap: 32px;
  align-items: start;
}
@media (max-width: 640px) {
  .tab-inhalt-grid {
    grid-template-columns: 1fr;
  }
  .tab-inhalt-grid img {
    max-width: 120px;
    order: 2;  /* Illustration nach unten auf Mobile */
    margin: 0 auto;
  }
}
```

---

## METHODEN-BOXEN (Prüfen / Urteilen / Belegen)

```css
.methode-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
  margin: 32px 0;
}
.methode-box {
  background: var(--farbe-blau-pastell);
  border: 2px solid var(--farbe-blau);
  border-radius: var(--border-radius);
  padding: 24px;
}
.methode-box .schritt-label {
  color: var(--farbe-orange);
  font-size: 0.8rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  margin-bottom: 8px;
}
.methode-box h3 {
  color: var(--farbe-blau);
  font-size: 1.3rem;
  font-weight: 700;
  margin-bottom: 8px;
}
@media (max-width: 640px) {
  .methode-grid { grid-template-columns: 1fr; }
}
```

---

## SCHULLEITUNG-SEKTION

```css
.sektion-schulleitung {
  background-color: var(--farbe-blau);
  color: var(--farbe-text-weiss);
  padding: 80px 40px;
}
.sektion-schulleitung h2,
.sektion-schulleitung h3,
.sektion-schulleitung p { color: var(--farbe-text-weiss); }
.sektion-schulleitung .muted { opacity: 0.75; }
.sektion-schulleitung .roi-satz {
  font-weight: 700;
  font-size: 1.1rem;
  border-left: 4px solid rgba(255,255,255,0.4);
  padding-left: 16px;
  margin: 24px 0;
}
```

---

## FOOTER UND KONTAKT

```css
.sektion-kontakt {
  background-color: var(--farbe-blau);
  color: var(--farbe-text-weiss);
  position: relative;
}
/* Scalloped Edge — NUR hier */
.sektion-kontakt::before {
  content: '';
  position: absolute;
  top: -20px;
  left: 0;
  right: 0;
  height: 40px;
  background: radial-gradient(circle at 50% 0%, var(--farbe-blau) 70%, transparent 70%);
  background-size: 40px 40px;
  background-repeat: repeat-x;
}
```

---

## ACCESSIBILITY

PFLICHT:
- Alle Buttons: min-height 44px, min-width 44px
- Alle Illustrationen: alt="" mit beschreibendem Text
- Alle interaktiven Elemente: :focus-visible mit sichtbarem Fokusring
- Farbkontrast: WCAG AA minimum

```css
:focus-visible {
  outline: 3px solid var(--farbe-blau);
  outline-offset: 3px;
}
```

KONTRASTWERTE (geprüft):
  #2A2A2A auf #EDEAE1  → 13.2:1  ✅ AAA  (Primärtext)
  #4A4A4A auf #EDEAE1  → 8.1:1   ✅ AA   (Sekundärtext)
  #5A5A5A auf #EDEAE1  → 4.2:1   ⚠️      (nur < 12px, nie Fliesstext)
  #FFFFFF auf #3881F1  → 4.6:1   ✅ AA   (weiss auf blau)
  #F6612E auf #EDEAE1  → 3.1:1   ❌      (nur > 18px bold, nie Fliesstext)

---

## GEO / SEO — TECHNISCH

META-TAGS HAUPTSEITE:
```html
<title>KIalog — KI-Urteilskompetenz für Lehrpersonen | Manuel Hirschi</title>
<meta name="description" content="KIalog ist eine Methode die Lehrpersonen befähigt, KI-Output zu beurteilen — mit dem eigenen Material, in drei Schritten. Für Schulen in der Deutschschweiz.">
```

META-TAGS BEISPIEL-SEITE:
```html
<title>KIalog in der Praxis — drei echte Walkthroughs | kialog.ch</title>
<meta name="description" content="Drei konkrete Situationen: Arbeitsblatt auf 3 Niveaus (8 Minuten), KI-Feedback auf Fallanalyse, KI-resistente Prüfung. Schritt für Schritt mit der KIalog-Methode.">
```

SCHEMA.ORG (bereits vorhanden — nicht löschen):
  Person, Course, FAQPage — prüfen ob korrekt implementiert.

OPEN GRAPH TAGS (noch fehlend — einbauen):
```html
<meta property="og:title" content="KIalog — KI-Urteilskompetenz für Lehrpersonen">
<meta property="og:description" content="Eine Methode die mit dem anfängt, was du schon hast.">
<meta property="og:url" content="https://kialog.ch">
<meta property="og:type" content="website">
```

---

## PERFORMANCE

BILDER:
- Alle PNG → WebP konvertieren (Ausnahme: SVG bleibt SVG)
- Max-Dateigrösse: 200KB pro Bild
- Lazy Loading für alle Illustrationen unter dem Fold:
  <img loading="lazy" ...>

SCHRIFTEN:
- font-display: swap (bereits vorhanden — nicht entfernen)

---

## VERBOTENE DESIGNENTSCHEIDE

1. Grün (#01C476) auf Buttons oder als Primärfarbe
2. Orange (#F6612E) als Fliesstext oder auf kleinen Elementen
3. #5A5A5A als regulärer Fliesstext (Kontrast zu niedrig)
4. Gradient irgendwo
5. Mehr als 2 Akzentfarben pro Sektion
6. Mehr als eine Illustration pro Sektion
7. Lottie-Animationen
8. Parallax-Scrolling
9. Scalloped Edge ausserhalb von Footer/Kontakt
10. Dashed Borders ausserhalb von Platzhalter-Boxes und Angebots-Cards

---

# ENDE MASTER PROMPT 2
