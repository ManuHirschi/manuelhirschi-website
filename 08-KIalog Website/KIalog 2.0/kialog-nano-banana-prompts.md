---
tags: [website, kreativ]
status: aktiv
related:
  - "[[08-KIalog Website/KIalog 2.0/README|KIalog 2.0 Briefing]]"
  - "[[08-KIalog Website/CLAUDE|KIalog Website]]"
---

# NANO BANANA PROMPTS — KIALOG.CH ILLUSTRATIONEN
## Stil: therapyin.london — Bold, gesättigt, handgezeichnet
**Stand:** April 2026 | **Verbindlich für alle 5 Illustrationen**

---

## STIL-ENTSCHEID

Der ursprüngliche Stil war: subtil, Pastell, dezent.
Der neue Stil ist: mutig, gesättigt, charakterstark.

Begründung: kialog.ch verkauft eine Methode die Mut verlangt —
KI-Output nicht blind übernehmen, aktiv urteilen.
Der visuelle Stil muss denselben Mut ausstrahlen.
therapyin.london macht das vor: starke Linien, volle Farben, klarer Charakter.

---

## STIL-BLOCK — IN JEDEN PROMPT KOPIEREN

Diesen Block unverändert in jeden der 5 Prompts einfügen.
Er definiert den Stil für die gesamte Illustrations-Serie.

```
STYLE — BOLD HAND-DRAWN, THERAPYIN.LONDON INSPIRED:

Line weight: 3.5–4px ink outlines, bold and confident.
NOT thin, NOT delicate. The outline is the dominant element.

Line quality: Strokes are NOT ruler-straight.
They wobble slightly, overshoot corners by 2–3px,
curves are imperfect ovals not perfect arcs.
This is intentional character — the mark of a real hand.

Color fills: FULLY SATURATED. Not pastel, not tinted, not transparent.
Use full-strength colors directly:
  Primary blue: #3881F1 (full strength as fill color)
  Primary orange: #F6612E (full strength as fill color)
  Accent green (only for plants): #22C55E
  Neutral fill: warm off-white #F5F0E8
  Black for outlines: #1A1A1A

Color bleeding: The fill color extends OUTSIDE the ink outline
by 5–8 pixels on at least 1–2 sides of each colored shape.
This is the key effect. It looks like coloring outside the lines
with a thick marker — intentional, not a mistake.
The overflow is always slightly too large, never too small.

Background: TRANSPARENT — the illustration floats freely on the page.
No background rectangle. No drop shadow. No glow.

Reference feel: "Drawn with a thick marker in 30 seconds
by someone who is very good at drawing."
Think: bold children's book illustration crossed with modern editorial sketch.

DO NOT: use gradients, drop shadows, digital smoothing, thin lines,
pastel colors, or geometric perfection.
```

---

## STIL-REFERENZ HOCHLADEN

Lade vor der ersten Illustration DIESES Bild als Stil-Referenz hoch:
→ Screenshot von therapyin.london (Wohnzimmer-Szene mit orangem Sessel,
  blauem Sofa, lila Kissen, grüner Pflanze)

Und füge oben im Prompt hinzu:
```
STYLE REFERENCE: [Referenzbild]
Match exactly: bold 4px outlines, fully saturated fill colors,
color bleeding 5–8px outside outlines, imperfect hand-drawn strokes.
All 5 illustrations must feel like they come from the same hand.
```

Nach der ersten gelungenen Illustration: diese als neue Stil-Referenz
für alle weiteren verwenden. So entsteht Konsistenz.

---

## PROMPT 1 — HERO-ILLUSTRATION

**Dateiname:** `asset/hero-lehrperson.png`
**Einsatz:** Hero-Sektion, rechts neben Headline (Desktop) / unter Buttons (Mobile)
**Grösse:** max 480px Desktop, 280px Mobile
**Funktion:** Erkennung — "Das bin ich. Das kenne ich."

```
STYLE REFERENCE: [Referenzbild therapyin.london]

STYLE — BOLD HAND-DRAWN, THERAPYIN.LONDON INSPIRED:
[Stil-Block von oben hier vollständig einfügen]

SCENE:
A teacher sits at a wooden desk, viewed from a 3/4 angle.
The desk has simple, mid-century modern legs — thin, angled, like the
furniture in therapyin.london illustrations.

ON THE DESK:
An open laptop. The laptop body is filled with BOLD BLUE (#3881F1).
The screen shows a text document — visible white rectangle with
3–4 horizontal lines representing text.
ONE line on the screen is highlighted: a thick orange stroke (#F6612E)
drawn over it, like a highlighter mark. Bold, bleeds slightly.

THE TEACHER:
Body visible from shoulders down — no face needed.
Wearing a simple shirt or cardigan.
ONE hand holds a thick marker pen, the pen is ORANGE (#F6612E).
The hand is mid-movement — caught in the act of marking something
on a notebook beside the laptop.
The notebook is open, a few rough lines visible inside.

BACKGROUND ELEMENT:
A small plant in the background — simple pot, 3–4 leaves in bold green
(#22C55E), outline in #1A1A1A. Leaves slightly imperfect, organic.

COMPOSITION:
Horizontal, approximately 3:2 ratio.
Figure fills 75% of frame. Generous transparent space on all sides.
The scene reads instantly: teacher, laptop, active work.
```

---

## PROMPT 2 — ARBEITSBLATT (Tab Berufsfachschule)

**Dateiname:** `asset/illust-arbeitsblatt.png`
**Einsatz:** Praxis-Tab 1, oben links im Tab
**Grösse:** max 160px Desktop, 120px Mobile
**Funktion:** Soforterkennung — "Drei Niveaus. Das kenne ich."

```
STYLE REFERENCE: [Referenzbild therapyin.london]

STYLE — BOLD HAND-DRAWN, THERAPYIN.LONDON INSPIRED:
[Stil-Block von oben hier vollständig einfügen]

SCENE:
A single worksheet / Arbeitsblatt, seen from above, slight tilt.

PAPER:
Rectangle with slightly uneven edges — not a perfect shape.
Fill: warm off-white (#F5F0E8). Outline: bold #1A1A1A, 4px.
Top-right corner has a dog-ear fold. The fold is filled with a
slightly darker beige (#DDD8CF).

THREE COLUMNS:
Two bold vertical lines dividing the paper into 3 equal columns.
Lines are slightly wobbly, not ruler-straight.

COLUMN HEADERS (top of each column):
Large bold letters: A  B  C
Letter A: filled with ORANGE (#F6612E) — bold, slightly overflows its
          own letterform
Letter B: filled with BLUE (#3881F1) — same treatment
Letter C: outlined only, no fill, #1A1A1A

TEXT LINES (in each column):
3–4 horizontal wavy strokes per column, representing text.
Strokes: 2px, #1A1A1A, irregular length, genuine hand-drawn wobble.

CHECKMARK (in column B only):
A large, bold checkmark drawn in ORANGE (#F6612E), 4px stroke.
The checkmark is the most prominent element on the worksheet.
It overshoots its expected bounds slightly — authentic hand-drawn feel.

PENCIL (bottom-right corner of paper):
Simple pencil shape, 45-degree angle. Body: ORANGE (#F6612E) fill.
Tip: small dark triangle. Bold outline.

COMPOSITION:
Square format. Worksheet fills 65% of frame.
Generous transparent margin on all sides.
```

---

## PROMPT 3 — TEXTVERGLEICH (Tab Gymnasium / FMS)

**Dateiname:** `asset/illust-vergleich.png`
**Einsatz:** Praxis-Tab 2, oben links im Tab
**Grösse:** max 160px Desktop, 120px Mobile
**Funktion:** Soforterkennung — "Vergleichen. Urteilen."

```
STYLE REFERENCE: [Referenzbild therapyin.london]

STYLE — BOLD HAND-DRAWN, THERAPYIN.LONDON INSPIRED:
[Stil-Block von oben hier vollständig einfügen]

SCENE:
Two documents side by side with a bold arrow between them.

LEFT DOCUMENT:
Rectangle, slightly imperfect edges.
Fill: ORANGE (#F6612E) — the whole document body is orange.
The fill bleeds outside the outline on the left and bottom.
Outline: bold #1A1A1A, 4px.
Inside: 3 horizontal wavy lines (representing text), color #1A1A1A.
Top-right corner: a tiny simple robot icon — two square eyes, rectangular
body, two small arms. Drawn in #1A1A1A, outline only, no fill. Small but clear.

RIGHT DOCUMENT:
Rectangle, same size as left, slightly imperfect.
Fill: BLUE (#3881F1) — the whole document body is blue.
Fill bleeds outside outline on right and top.
Outline: bold #1A1A1A, 4px.
Inside: 3 horizontal wavy lines, color #FFFFFF (white, for contrast on blue).
Top-right corner: a bold checkmark in #FFFFFF. Large, confident, 4px stroke.

ARROW BETWEEN THE DOCUMENTS:
Bold curved arrow pointing from left document to right document.
Color: #1A1A1A. Stroke: 4px. Arrowhead: solid, filled.
The arrow is the center of attention — slightly oversized for the composition.

COMPOSITION:
Landscape format, 4:3 ratio.
Both documents and arrow fill 80% of frame.
Documents overlap the arrow slightly — they feel close together, in dialogue.
```

---

## PROMPT 4 — KI-FEEDBACK WIRD BEARBEITET (Tab PH / Hochschule)

**Dateiname:** `asset/illust-laptop-feedback.png`
**Einsatz:** Praxis-Tab 3, oben links im Tab
**Grösse:** max 160px Desktop, 120px Mobile
**Funktion:** "Du übernimmst nicht blind. Du greifst ein."

```
STYLE REFERENCE: [Referenzbild therapyin.london]

STYLE — BOLD HAND-DRAWN, THERAPYIN.LONDON INSPIRED:
[Stil-Block von oben hier vollständig einfügen]

SCENE:
An open laptop with a hand actively correcting something on the screen.

LAPTOP:
Seen from a 3/4 angle, open at approximately 100 degrees.
Laptop body (base): filled with BLUE (#3881F1). Bold, saturated, bleeds
outside outline slightly.
Screen: lighter blue (#DBE4FF) fill as the screen area, outlined bold.
Hinge: simple bold line, #1A1A1A.

SCREEN CONTENT:
4 horizontal wavy lines representing text.
Line 1: normal (#1A1A1A wavy line)
Line 2: STRUCK THROUGH — a bold ORANGE (#F6612E) horizontal line
         crossing through it. 4px, confident, bleeds at ends.
Line 3: Represents a correction — shorter, slightly different position,
         drawn in BLUE (#3881F1) as if added by a pen.
Line 4: normal

HAND:
Enters from the right side of the frame.
Holds a thick marker/pen — the pen is ORANGE (#F6612E), bold.
The hand is positioned as if it just made the strikethrough correction.
Fingers visible, drawn in simple thick strokes, #1A1A1A outline,
warm skin-tone fill (#FFD8A8 — this one time, slightly less saturated
is fine for skin).
Only hand and pen visible — no arm, no body.

COMPOSITION:
Landscape format. Laptop occupies 60% of frame left-center.
Hand enters from right edge, pen tip nearly touching the screen.
The interaction is the story: human hand correcting machine output.
```

---

## PROMPT 5 — HAND TIPPT NACHRICHT (Kontakt)

**Dateiname:** `asset/illust-smartphone.png`
**Einsatz:** Kontakt-Sektion (blauer Hintergrund #3881F1)
**Grösse:** max 200px Desktop, 160px Mobile
**Funktion:** "Ein Satz reicht. Das ist einfach."

**WICHTIG:** Diese Illustration wird auf blauem Hintergrund (#3881F1) angezeigt.
Daher: Outlines in WEISS (#FFFFFF), keine blaue Farbe im Objekt selbst.

```
STYLE REFERENCE: [Referenzbild therapyin.london]

STYLE — BOLD HAND-DRAWN FOR BLUE BACKGROUND:
Same bold hand-drawn style as all other illustrations.
EXCEPTION: All ink outlines are WHITE (#FFFFFF) instead of #1A1A1A.
This is because the illustration sits on a blue (#3881F1) background.
Line weight: 3.5–4px white outlines.
Color fills: ORANGE (#F6612E) for the message text / accent.
             Warm off-white (#F5F0E8) for the phone body.
Color bleeds outside outlines as usual: 5–8px.
Background: TRANSPARENT (blue comes from the webpage, not the illustration).

SCENE:
A hand holds a smartphone upright.

SMARTPHONE:
Simple rounded rectangle shape, slightly imperfect corners.
Phone body fill: warm off-white (#F5F0E8).
Outline: bold white (#FFFFFF), 4px.
Screen area: slightly lighter rectangle inside the phone body.

SCREEN CONTENT:
Simple chat interface:
- Top 30%: one or two previous message bubbles — just rounded rectangles,
  white outline, no text. One bubble aligned left, one right.
- Bottom area: a text input field (long rounded rectangle, white outline).
  Inside the input field: partial text "Hallo Manuel..." drawn as
  ORANGE (#F6612E) strokes/wiggles — representing typed characters.
  An orange blinking cursor at the end (simple vertical rectangle, orange).

HAND:
Holds the phone from below.
Thumb positioned on the screen as if it just typed.
Hand outline: white (#FFFFFF), 4px.
Hand fill: warm skin tone (#FFD8A8), slightly less saturated — OK here.
Only hand visible, no arm, no body.

COMPOSITION:
Portrait format, 2:3 ratio.
Phone fills 55% of frame, centered.
Hand visible at bottom, entering from below.
Generous transparent space above and to the sides.
The mood: easy, approachable, one tap away.
```

---

## REIHENFOLGE DER ERSTELLUNG

**Empfohlene Reihenfolge:**

1. PROMPT 2 (Arbeitsblatt) — einfachstes Objekt, keine Person.
   Damit den Stil und die Farbsättigung kalibrieren.

2. Wenn Arbeitsblatt stimmt: als neue Stil-Referenz für alle weiteren hochladen.

3. PROMPT 3 (Textvergleich) — ähnlich einfach, nur Objekte.

4. PROMPT 4 (Laptop mit Hand) — mittlere Komplexität.

5. PROMPT 1 (Hero — Lehrperson) — aufwändigste, dafür mit kalibriertem Stil.

6. PROMPT 5 (Smartphone) — zuletzt, weil weisse Linien ein Sonderfall sind.
   Auf blauem Hintergrund testen bevor als final akzeptieren.

---

## QUALITÄTSPRÜFUNG FÜR JEDE ILLUSTRATION

Vor dem Ablegen in `asset/`:

- [ ] Outline-Stärke: mindestens 3px, deutlich sichtbar?
- [ ] Farben vollgesättigt: kein Pastell, keine Transparenz?
- [ ] Farbüberlauf sichtbar: Farbe geht über Outline hinaus?
- [ ] Linien nicht ruler-straight: erkennbare Hand-Qualität?
- [ ] Hintergrund transparent: kein weisses oder beiges Rechteck?
- [ ] Stil konsistent mit vorherigen Illustrationen?
- [ ] Illustration 5 (Smartphone): weisse Linien, auf blauem Hintergrund sichtbar?

---

## DATEINAMEN UND ZIELDATEIPFADE

```
asset/hero-lehrperson.png          ← Prompt 1
asset/illust-arbeitsblatt.png      ← Prompt 2
asset/illust-vergleich.png         ← Prompt 3
asset/illust-laptop-feedback.png   ← Prompt 4
asset/illust-smartphone.png        ← Prompt 5
```

Alle als PNG mit transparentem Hintergrund exportieren.
Maximale Dateigrösse: 300KB pro Bild.
Wenn möglich: WebP zusätzlich exportieren (kleinere Dateigrösse).

---

*Diese Datei ersetzt alle früheren Nano Banana Prompt-Beschreibungen.*
*Stand: April 2026. Einzige gültige Prompt-Referenz für kialog.ch Illustrationen.*
