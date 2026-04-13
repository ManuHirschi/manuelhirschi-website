---
tags: [website, geschaeft]
status: aktiv
related:
  - "[[08-KIalog Website/KIalog 2.0/README|KIalog 2.0 Briefing]]"
  - "[[08-KIalog Website/CLAUDE|KIalog Website]]"
---

# TYPOGRAFIE-UPGRADE + UNDERLINE.SVG
# kialog.ch | Claude Code | April 2026
# Inspiriert durch Analyse von therapyin.london
# Nie pushen ohne explizites "push" von Manuel Hirschi.

---

## HINTERGRUND

therapyin.london verwendet dasselbe Designsystem wie kialog.ch:
identische Farben (#EDEAE1, #2A2A2A, #3881F1), identische Schrift (Figtree).

Der visuelle Unterschied entsteht durch drei Feineinstellungen:
1. Negatives Letter-Spacing auf Headlines
2. Leichteres Headline-Gewicht
3. Handgezeichnete Unterstreichung als dekoratives Akzent-Element (underline.svg)

Diese drei Änderungen sind kein Redesign — sie sind Feintuning.
Gesamtaufwand: ca. 30 Minuten.

---

## AUFGABE 1 — LETTER-SPACING

### Was zu ändern ist

In der CSS-Datei (oder im `<style>`-Block in index.html):

```css
/* VORHER — kein Letter-Spacing */
h1 { }
h2 { }
h3 { }

/* NACHHER — negatives Letter-Spacing */
h1 {
  letter-spacing: -2px;
}
h2 {
  letter-spacing: -1.5px;
}
h3 {
  letter-spacing: -0.5px;
}
```

### Warum genau diese Werte

- H1 (-2px): Grösste Headline, braucht den stärksten Effekt. therapyin.london verwendet -2px auf 40px Headlines. Auf grösseren Headlines (60px+) wirkt -2px bereits stark editorial.
- H2 (-1.5px): Leicht schwächer als H1, aber noch klar wahrnehmbar.
- H3 (-0.5px): Subtil — gibt nur einen Hauch Eleganz, ohne die Lesbarkeit zu stören.

### Wichtig

Letter-Spacing nie auf Fliesstext (p, li, span) anwenden.
Nur auf Headlines H1, H2, H3.

---

## AUFGABE 2 — HEADLINE-GEWICHT REDUZIEREN

### Was zu ändern ist

```css
/* VORHER */
h1 { font-weight: 800; }
h2 { font-weight: 700; }

/* NACHHER */
h1 { font-weight: 600; }
h2 { font-weight: 500; }
h3 { font-weight: 600; } /* H3 bleibt bei 600 — zu leicht wäre unleserlich */
```

### Ausnahme: Hero H1 bleibt kursiv

```css
.hero h1 {
  font-style: italic;
  font-weight: 600;
  letter-spacing: -2px;
}
```

### Warum leichter

Fette Headlines auf grossem Schriftgrad wirken laut.
Leichte Headlines (400–600) auf grossem Schriftgrad wirken edel, editorial, selbstsicher.
therapyin.london verwendet weight 300–400 auf 40–128px Headlines.
Für kialog.ch (Methoden-Website) ist 600 der richtige Kompromiss —
edel genug, noch klar genug.

---

## AUFGABE 3 — HERO H1 GRÖSSER

### Was zu ändern ist

```css
/* VORHER */
.hero h1 {
  font-size: clamp(2.2rem, 5.5vw, 4rem);
}

/* NACHHER */
.hero h1 {
  font-size: clamp(2.8rem, 7vw, 5.5rem);
}
```

### Warum

therapyin.london: H1 = 128px.
kialog.ch muss nicht 128px sein — das passt nicht zur Methoden-Ästhetik.
Aber der Hero-Headline darf grösser sein als Standard-Web.
5.5rem auf Desktop = ca. 88px. Das ist ein Statement, kein Schreien.

---

## AUFGABE 4 — UNDERLINE.SVG ERSTELLEN UND EINSETZEN

### Was die Datei ist

Eine handgezeichnete, wellige Unterstreichungslinie.
Kein Bild — eine SVG-Datei die inline im HTML oder als `<img>` verwendet wird.
Inspiriert von therapyin.london die dasselbe Element mehrfach einsetzt.

### Die Datei erstellen

Erstelle `asset/underline.svg` mit folgendem Inhalt:

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 12" width="200" height="12">
  <path
    d="M2,8 C20,2 40,11 60,6 C80,1 100,10 120,5 C140,0 160,9 180,5 C190,3 196,7 198,8"
    fill="none"
    stroke="#F6612E"
    stroke-width="3"
    stroke-linecap="round"
    stroke-linejoin="round"
  />
</svg>
```

### Was diese Pfad-Kurve macht

Die `d`-Koordinaten erzeugen eine sanfte, unregelmässige Welle — ähnlich wie eine echte Hand die eine Unterstreichung zieht. Die Welle ist nicht symmetrisch: das ist absichtlich. Symmetrie wirkt digital, Asymmetrie wirkt menschlich.

### Zweite Variante (stärkere Welle, für grössere Headlines)

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 16" width="240" height="16">
  <path
    d="M2,12 C25,4 50,14 75,7 C100,0 125,13 150,6 C175,0 200,12 225,7 C232,5 238,9 238,10"
    fill="none"
    stroke="#F6612E"
    stroke-width="3.5"
    stroke-linecap="round"
    stroke-linejoin="round"
  />
</svg>
```

Speichere beide:
- `asset/underline.svg` (200px, Standard)
- `asset/underline-gross.svg` (240px, für grosse Headlines)

### Blaue Variante (für die Methoden-Sektion)

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 12" width="160" height="12">
  <path
    d="M2,8 C20,3 40,10 65,5 C90,0 115,9 140,5 C150,3 156,7 158,8"
    fill="none"
    stroke="#3881F1"
    stroke-width="3"
    stroke-linecap="round"
    stroke-linejoin="round"
  />
</svg>
```

Speichere als: `asset/underline-blau.svg`

---

## AUFGABE 5 — UNDERLINE.SVG EINSETZEN

### Wo genau — drei Stellen, nicht mehr

**Stelle 1 — Methoden-Sektion, unter "Vorteil"**

In der Methoden-Sektion steht:
"Du kennst dein Material. Das ist dein **Vorteil.**"

Das Wort "Vorteil" bekommt die blaue Unterstreichung direkt darunter:

```html
<h2 class="methode-headline">
  Du kennst dein Material.<br>
  Das ist dein <span class="mit-underline">Vorteil.
    <img src="asset/underline-blau.svg" 
         alt="" 
         class="underline-deko" 
         aria-hidden="true">
  </span>
</h2>
```

```css
.mit-underline {
  position: relative;
  display: inline-block;
}
.underline-deko {
  position: absolute;
  bottom: -8px;
  left: 0;
  width: 100%;
  height: auto;
  pointer-events: none;
}
```

**Stelle 2 — Warum-ich-Sektion, unter "erforsche"**

Der Headline-Satz "Ich unterrichte das, was ich **erforsche.**"
Das Wort "erforsche" bekommt die orange Unterstreichung:

```html
<h2 class="warum-headline">
  Ich unterrichte das,<br>
  was ich <span class="mit-underline">erforsche.
    <img src="asset/underline.svg" 
         alt="" 
         class="underline-deko" 
         aria-hidden="true">
  </span>
</h2>
```

**Stelle 3 — Hero, unter "Methode" in der Subline**

Die Hero-Subline lautet:
"Das ist kein Tool-Problem. Das ist eine Kompetenzfrage. KIalog gibt dir die **Methode.**"

Das Wort "Methode" bekommt die orange Unterstreichung (kurze Variante):

```html
<p class="hero-subline">
  Das ist kein Tool-Problem. Das ist eine Kompetenzfrage.<br>
  KIalog gibt dir die <span class="mit-underline">Methode.
    <img src="asset/underline.svg" 
         alt="" 
         class="underline-deko" 
         aria-hidden="true">
  </span>
</p>
```

### Was du NICHT machst

- Keine Unterstreichung auf jedem zweiten Wort
- Keine Unterstreichung in der Schulleitungen-Sektion (falscher Ton)
- Keine Unterstreichung auf Buttons oder Links
- Maximal 3 Unterstreichungen auf der ganzen Seite — nicht mehr

---

## MOBILE-VERHALTEN

```css
@media (max-width: 640px) {
  h1 { letter-spacing: -1px; }   /* reduziert auf Mobile — eng wird es sonst */
  h2 { letter-spacing: -0.8px; }
  h3 { letter-spacing: -0.3px; }

  .hero h1 {
    font-size: clamp(2.2rem, 8vw, 3.5rem);
  }

  .underline-deko {
    bottom: -6px;  /* etwas näher am Text auf Mobile */
  }
}
```

---

## QUALITÄTSPRÜFUNG NACH UMSETZUNG

- [ ] H1 letter-spacing: -2px auf Desktop sichtbar?
- [ ] H2 letter-spacing: -1.5px auf Desktop sichtbar?
- [ ] Hero H1: kursiv, weight 600, letter-spacing -2px?
- [ ] hero-lehrperson H1 Schriftgrösse grösser als vorher?
- [ ] underline.svg in asset/ vorhanden (3 Dateien)?
- [ ] Exakt 3 Unterstreichungen auf der Seite?
- [ ] aria-hidden="true" auf allen underline img-Tags?
- [ ] Auf Mobile: letter-spacing reduziert, keine Überlappung?
- [ ] Keine Unterstreichung in Schulleitung-Sektion oder FAQ?

---

## COMMIT-MESSAGE

```
Website Typo: Letter-spacing, Headline-Gewicht, underline.svg — therapyin.london Stil
```

---

# ENDE
