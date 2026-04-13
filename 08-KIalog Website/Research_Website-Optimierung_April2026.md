---
tags: [website, geschaeft, research]
status: aktiv
related:
  - "[[08-KIalog Website/CLAUDE|Website — Projektstand]]"
  - "[[08-KIalog Website/KIalog 2.0/MASTERPROMPT_2_design_farben|Design Authority]]"
  - "[[15-Organisation/Luege_Erkenntnisse|Luege — System-Erkenntnisse]]"
---

# Research: Website-Optimierung kialog.ch
**Erstellt:** 5.4.2026 (Nacht)
**Zweck:** Gesammelte Erkenntnisse aus 5 parallelen Recherchen. Basis für morgen.

---

## Übersicht: 40 Funde in 5 Kategorien

| Kategorie | Funde | Top-Quick-Wins |
|-----------|-------|---------------|
| A. Conversion & Trust | 10 | Trust-Logos, Workshop als "Empfohlen", CTA-Staffelung |
| B. CSS & Animation | 12 | CSS `view()`, View Transitions, SVG Noise, `text-wrap: pretty` |
| C. SEO & GEO | 10 | Course-Schema, Person-Schema erweitern, hreflang, GBP |
| D. Accessibility & Performance | 8 | fetchpriority, width/height, manu2.webp, scroll-padding-top |
| E. Claude Code Workflow | 5 | CLAUDE.md Patterns, Screenshot-Editing, CSS-Tricks |

---

## A. CONVERSION & TRUST (10 Funde)

### A1. Trust-Logos — stärkstes Signal nach Testimonials
Institutionelle Logos (gibb Bern, PH FHNW, UZH) prominent unter Hero oder in About zeigen. Eine Schulleitung, die das gibb-Logo sieht, hat implizite Validierung ohne Testimonial.
- Trajectory Web Design (2026). *B2B Website Trust Signals*. https://www.trajectorywebdesign.com/blog/b2b-website-trust-signals

### A2. Workshop als "Empfohlen" markieren
Drei Preisstufen mit mittlerer Option visuell hervorgehoben (Badge, Akzent-Rahmen, leichte Hintergrundfarbe). Pricing mit mehr Whitespace konvertiert 28% besser.
- Ignition (2026). *Tiered Pricing Strategy*. https://www.ignitionapp.com/blog/tiered-pricing-strategy-for-professional-services-proposal-templates

### A3. Preistransparenz als Wettbewerbsvorteil
71% der B2B-Entscheider bewerten Preistransparenz als "sehr wichtig". 27% höhere Conversion bei transparenten Preisen. 39% wechseln zu transparenterem Anbieter. → Die offenen CHF-Preise auf kialog.ch sind korrekt.
- PricingLink (2025). *Transparency in Pricing*. https://pricinglink.com/blog/2025-post/transparency-in-pricing-building-client-trust-2025/

### A4. CTAs entlang des Entscheidungspfads staffeln
Nicht überall "Kontakt". Oben weichere CTAs ("Methode ansehen"), unten verbindlichere ("Erstgespräch buchen"). Ein CTA pro Sektion. E-Mails mit einem CTA = 371% mehr Klicks.
- Orange Owl (2026). *CTA in B2B Marketing*. https://orangeowl.marketing/b2b-marketing/the-power-cta-in-b2b-marketing/
- Martal (2026). *Call to Action Best Practices B2B*. https://martal.ca/b2b-sales-glossary/call-to-action/

### A5. Prozess-Transparenz ersetzt fehlende Referenzen
"So läuft ein Workshop ab"-Block (Timeline, 4-5 Schritte) reduziert Unsicherheit und demonstriert Professionalität. Walkthroughs leisten das teilweise, ein expliziter Ablauf fehlt.
- Logotio (2026). *Consultant Website Trust Elements*. https://logotio.com/blog/consultant-website-trust-elements-essential-pages/

### A6. Momentum statt absoluter Zahlen
"Pilot startet April 2026 an der gibb Bern" wirkt stärker als "3 Kunden". Earned Media (PH-Lehrauftrag, Forschungsbasis) als Third-Party-Validierung.
- Letteri, A. (2026). *Startup Credibility Before Customers*. https://allysonletteri.com/startup-credibilty-before-customers/

### A7. Eigene Forschungsdaten als Credibility
Die Dissertation, Stat-Counter und UZH-Verbindung konkret und prominent zeigen — nicht als Schmuck, sondern als Beweis.
- Briefd (2026). *Social Proof for Startups with Zero Customers*. https://briefd.it/blog/social-proof-startups-zero-customers/

### A8. Desktop konvertiert besser
82.9% Traffic mobil, aber Desktop konvertiert 8% besser. Bei Schulleitungen am Schreibtisch noch wichtiger. → Desktop-LCP (3.5s) ist ein Conversion-Problem.
- Hostinger (2026). *Landing Page Statistics*. https://www.hostinger.com/tutorials/landing-page-statistics

### A9. Headline-Optimierung = grösster Hebel
Headline-Optimierung bringt 27-104% Conversion-Lift. Hero-Claim muss sofort verständlich sein.
- Genesys Growth (2026). *Landing Page Conversion Stats*. https://genesysgrowth.com/blog/landing-page-conversion-stats-for-marketing-leaders

### A10. Kontaktformular minimal halten
Formular-Reduktion bringt 120% Lift. Name + E-Mail reicht. → kialog.ch hat kein Formular, nur Mail + WhatsApp. Das ist richtig.

---

## B. CSS & ANIMATION (12 Funde, priorisiert)

### SOFORT umsetzbar

**B1. CSS `animation-timeline: view()` statt IntersectionObserver**
Bestehende `.reveal`-Klassen komplett in CSS abbilden — null JavaScript, Compositor-Thread. Fallback: bestehendes JS für ältere Browser.
```css
.reveal { animation: fade-in linear both; animation-timeline: view(); animation-range: entry 0% entry 100%; }
```
- MDN (2026). *Scroll-driven animations*. https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations
- CSS-Tricks (2025). *Unleash the Power of Scroll-Driven Animations*. https://css-tricks.com/unleash-the-power-of-scroll-driven-animations/

**B2. View Transitions API für Walkthrough-Seiten**
Native Page-Transitions zwischen index.html und Walkthroughs — eine CSS-Zeile pro Seite:
```css
@view-transition { navigation: auto; }
```
Chrome, Safari, Firefox 144+. GPU-composited.
- Chrome Developers (2025). *View Transitions in 2025*. https://developer.chrome.com/blog/view-transitions-in-2025

**B3. SVG Noise Texture auf Beige**
Subtiler Grain-Effekt über #EDEAE1 — haptisch, papierartig, ~200 Bytes. `<feTurbulence>` als Filter, `mix-blend-mode: multiply` bei 5-15% Opacity. Passt zum Sketchy-Stil.
- CSS-Tricks (2024). *Grainy Gradients*. https://css-tricks.com/grainy-gradients/
- fffuel (2026). *gggrain Generator*. https://www.fffuel.co/gggrain/

**B4. Cubic-Bezier Hover-Timing**
`transition: transform 0.25s cubic-bezier(0.34, 1.56, 0.64, 1)` — minimales Federn, signalisiert Premium.
- Comeau, J. W. (2025). *Interactive Guide to CSS Transitions*. https://www.joshwcomeau.com/animation/css-transitions/

**B5. Font `size-adjust` gegen CLS**
```css
@font-face { font-family: 'Figtree-fallback'; src: local('system-ui'); size-adjust: 104%; ascent-override: 95%; }
```
Eliminiert Layout Shift beim Font-Swap.
- DebugBear (2025). *Fixing Layout Shifts from Web Fonts*. https://www.debugbear.com/blog/web-font-layout-shift

**B6. `text-wrap: pretty` für Body-Text**
Vermeidet Hurenkinder in Absätzen. Eine Zeile CSS, null Performance-Kosten.
```css
h1, h2, h3 { text-wrap: balance; } p { text-wrap: pretty; }
```
- State of CSS (2025). https://2025.stateofcss.com/en-US/features/

### BALD umsetzbar

**B7. `:has()` für zustandsabhängiges Styling**
Ersetzt JS-Klassen-Toggles. Z.B. transparente Nav im Hero-Bereich. 100% Browser-Support.
- Comeau, J. W. (2025). *The Undeniable Utility of CSS :has()*. https://www.joshwcomeau.com/css/has/

**B8. Variable Font-Weight-Animationen mit Figtree**
Smooth `font-variation-settings: 'wght'` Transitions auf Hover. Vorsicht: kann Layout-Shifts verursachen.

### BEI REFACTOR

**B9. CSS Nesting** (native, kein Preprocessor) — Wartbarkeitsgewinn bei 48KB Inline-CSS.
**B10. Container Queries** — nur relevant wenn Cards in verschiedenen Kontexten wiederverwendet werden.

### BEI BEDARF

**B11. GSAP ScrollTrigger** — nur für komplexe Sequenzen (SVG-Schritte animieren). ~30KB Overhead.
**B12. Scroll-Triggered Animations (Chrome 145)** — noch zu früh (Juni 2026).

---

## C. SEO & GEO (10 Funde, priorisiert)

### SOFORT

**C1. Course-Schema für die 3 Formate**
Impuls, Workshop, Fachbegleitung als je ein `Course` mit `offers` + `provider`. Qualifiziert für Google-Kurs-Rich-Results. ~30 Min.
- Google Search Central (2026). *Course Structured Data*. https://developers.google.com/search/docs/appearance/structured-data/course

**C2. Person-Schema erweitern**
`sameAs` (LinkedIn, ORCID, PH FHNW-Profil, UZH-Profil, gibb-Profil), `hasCredential`, erweiterte `alumniOf`. Verbindet Manuel als Entität mit den Institutionen. ~20 Min.
- Averi.ai (2026). *Google AI Overviews Optimization*. https://www.averi.ai/blog/google-ai-overviews-optimization-how-to-get-featured-in-2026

**C3. `hreflang="de-CH"` im HTML-Head**
5 Sekunden. Verhindert, dass Google den Content für Deutschland/Österreich ausspielt.
- EWM Swiss (2026). *SEO in Switzerland*. https://ewm.swiss/en/blog/seo-in-switzerland-effective-techniques-to-boost-your-visibility

**C4. Google Business Profile einrichten**
Falls nicht vorhanden. Lokale Telefonnummer, Schweizer Adressformat, NAP-Konsistenz. ~30 Min.

**C5. Hub-Spoke-Links**
Walkthroughs zurück zur Hauptseite mit beschreibendem Anchor-Text. BreadcrumbList-Schema auf Unterseiten. FAQ-Antworten mit internen Links zu Walkthroughs.
- SEO-Day Wiki (2026). *Hub-and-Spoke SEO Model*. https://www.seo-day.de/wiki/on-page-seo/interne-verlinkung/link-struktur/hub-and-spoke.php

### BALD

**C6. FAQ-Antworten GEO-optimieren**
Direkte Antwort in Satz 1-2, Statistik in Satz 3-4. LLMs zitieren bevorzugt die ersten 40-60 Wörter.
- Search Engine Land (2026). *Mastering GEO in 2026*. https://searchengineland.com/mastering-generative-engine-optimization-in-2026-full-guide-469142

**C7. Semantische Vollständigkeit**
Seiten mit Score 8.5/10+ werden 4.2x häufiger in AI Overviews zitiert. 96% der Zitationen von Seiten mit starken E-E-A-T-Signalen.
- Wellows (2026). *Google AI Overviews Ranking Factors*. https://wellows.com/blog/google-ai-overviews-ranking-factors/

**C8. local.ch + search.ch Einträge** — Low-Effort für lokale Sichtbarkeit.

### WISSEN

**C9. llms.txt hat keinen nachgewiesenen Einfluss** — bestehende Datei behalten, nicht weiter optimieren.
- SE Ranking (2025). *LLMs.txt: Why It Doesn't Work*. https://seranking.com/blog/llms-txt/

**C10. GEO-Zeithorizont: 8-12 Wochen bis Wirkung**
Technische Fixes wirken in 2-4 Wochen. KI-Zitationen frühestens Juni/Juli.
- Go Fish Digital (2026). *GEO Strategies*. https://gofishdigital.com/blog/generative-engine-optimization-strategies/

---

## D. ACCESSIBILITY & PERFORMANCE (8 Funde, priorisiert)

### SOFORT — Desktop LCP (3.5s → Ziel: <1.5s)

**D1. `fetchpriority="high"` + `width`/`height` auf Hero-Bild**
Desktop-Threshold ist 1.2s (strenger als Mobile 2.5s). `fetchpriority="high"` spart 200-800ms. Mehrere `<img>`-Tags haben kein `width`/`height`.
- web.dev (2026). *Optimize LCP*. https://web.dev/articles/optimize-lcp

**D2. manu2.webp komprimieren (228KB → ~60KB)**
Für 254px Display reichen 60-80KB. ~300ms LCP-Gewinn.

**D3. AVIF als WebP-Upgrade**
20-30% kleiner bei gleicher Qualität. `<picture>` mit AVIF-First, WebP-Fallback. Hero von 120KB → ~80KB.
- Elementor (2026). *AVIF vs WebP*. https://elementor.com/blog/webp-vs-avif/

**D4. `srcset` + `sizes` für responsive Bilder**
Drei Varianten pro Hero-Bild (400w, 800w, 1200w). Mobile lädt kleinere Version.

### SOFORT — Accessibility

**D5. `scroll-padding-top` für Sticky Nav**
WCAG 2.2 SC 2.4.11 (Focus Not Obscured). Fokussierte Elemente unter der Nav verdeckt. Fix: `scroll-padding-top: 80px` auf `<html>`.
- W3C (2023). *What's New in WCAG 2.2*. https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/

**D6. Touch Targets min. 24x24px**
WCAG 2.2 SC 2.5.8 (Target Size). Nav-Links, Footer-Links, Tab-Buttons prüfen.

### BALD

**D7. Reduced Motion: Opacity-Transitions statt Kill-All**
Nicht alle Animationen entfernen, sondern durch Fading ersetzen. Vestibulär empfindliche User haben kein Problem mit Opacity.
- Smashing Magazine (2021). *Respecting Motion Preferences*. https://www.smashingmagazine.com/2021/10/respecting-users-motion-preferences/

**D8. Font `size-adjust` auf Fallback** (= B5, siehe oben)

---

## E. CLAUDE CODE WORKFLOW (5 Funde)

**E1. CLAUDE.md Pattern:** Design Tokens als strukturierte Liste. Anti-Patterns explizit auflisten ("Nie: box-shadow auf Cards"). Responsive Breakpoints mit Beschreibung was sich ändert.

**E2. CSS-only Animationen** funktionieren am besten mit Claude — kein Dependency-Overhead, Claude schreibt saubere @keyframes.

**E3. Screenshot + präzise Anweisung** ist der effektivste Edit-Workflow. Vergleichs-Screenshots (Ist vs. Soll) besonders stark. Limitation: Hover-States und Scroll-Verhalten nicht sichtbar.

**E4. Container Queries und `:has()`** — Claude setzt beide korrekt um wenn angewiesen.

**E5. AOS (Animate on Scroll)** — data-attribute-basiert, Claude setzt es zuverlässig um. Leichtere Alternative zu GSAP.

---

## MORGEN-PLAN: Priorisierte Aktionsliste

### Block 1: Performance-Fixes (Desktop LCP 3.5s → <1.5s)
1. `fetchpriority="high"` + `width`/`height` auf alle `<img>` (D1)
2. manu2.webp komprimieren (D2)
3. AVIF-Versionen aller Bilder generieren + `<picture>` (D3)
4. Font `size-adjust` auf Fallback (B5/D8)

### Block 2: Schema.org + SEO (30 Min)
5. Course-Schema für 3 Formate (C1)
6. Person-Schema erweitern: sameAs, hasCredential (C2)
7. `hreflang="de-CH"` (C3)
8. BreadcrumbList auf Unterseiten (C5)

### Block 3: Accessibility (15 Min)
9. `scroll-padding-top: 80px` (D5)
10. Touch Targets prüfen (D6)
11. `width`/`height` auf alle Bilder (D1)

### Block 4: CSS Quick Wins (30 Min)
12. `text-wrap: pretty` auf `p` (B6)
13. SVG Noise auf Beige-Hintergrund (B3)
14. Cubic-Bezier Hover-Timing (B4)
15. View Transitions für Walkthroughs (B2)

### Block 5: Conversion (bei Gelegenheit)
16. Trust-Logos (gibb, PH FHNW, UZH) unter Hero (A1)
17. Workshop als "Empfohlen" markieren (A2)
18. CTA-Staffelung weich→verbindlich (A4)
19. "So läuft es ab"-Block für SL (A5)

### Block 6: Inhalt (vor Push)
20. Starter-Dossier PDF bauen oder Link entfernen
21. Masterprompt 1 aktualisieren (Cards statt Tabs, Argument-Satz)

---

*Quellen: 30+ Webquellen, vollständig zitiert in den Sektionen oben.*

---

---

# NotebookLM-Synthese: 9 Notebooks, April 2026

**Erstellt:** 8.4.2026  
**Notebooks:** Web-UX Bildung · Copywriter Bildung · LP-Stimmen & KI-Akzeptanz · SEO AEO 2026 · Schule 2.0 · Bildungsfinanzierung CH · KI in Schweizer Hochschulen · Evaluative Judgement & Feedback · Lehrpläne EBA/EFZ (ABU)

---

## Priorisierte Aktionsliste (Gesamtübersicht)

| # | Aktion | Kategorie | Aufwand | Wirkung |
|---|--------|-----------|---------|---------|
| 1 | nRLP-Legitimation: 4 Lehrplan-Zitate sichtbar einbauen | Copy | 1h | ⭐⭐⭐⭐⭐ |
| 2 | Hero-Text transformation-orientiert umschreiben | Copy | 30 Min | ⭐⭐⭐⭐⭐ |
| 3 | Institutionelle Logos unter Hero | Trust | 20 Min | ⭐⭐⭐⭐⭐ |
| 4 | "Pilot startet April 2026 an der gibb Bern" als Momentum-Signal | Trust | 15 Min | ⭐⭐⭐⭐ |
| 5 | Workshop als "Empfohlen" markieren + Persona-Zeilen | Pricing | 30 Min | ⭐⭐⭐⭐ |
| 6 | SCHILW-buchbar + BKD-rückvergütbar als Badge | Pricing | 15 Min | ⭐⭐⭐⭐ |
| 7 | "So läuft der Workshop ab"-Block (4–5 Schritte) | Trust | 45 Min | ⭐⭐⭐⭐ |
| 8 | Course-Schema für alle 3 Formate (JSON-LD) | SEO | 30 Min | ⭐⭐⭐⭐ |
| 9 | Person-Schema: ORCID, LinkedIn, PH FHNW, UZH als sameAs | SEO | 20 Min | ⭐⭐⭐⭐ |
| 10 | Forschungsbasis sichtbar: Sadler, Nicol, Bearman, Tai namentlich | Trust | 30 Min | ⭐⭐⭐ |
| 11 | Widerstandsmuster der LP direkt adressieren (FAQ-Erweiterung) | Copy | 45 Min | ⭐⭐⭐ |
| 12 | Dringlichkeit "ab August 2026" als Zeitrahmen verankern | Copy | 15 Min | ⭐⭐⭐ |
| 13 | FAQs GEO-optimieren: Antwort in Satz 1–2, Statistik in Satz 3–4 | SEO | 30 Min | ⭐⭐⭐ |
| 14 | hreflang="de-CH" im HTML-Head | SEO | 5 Min | ⭐⭐⭐ |
| 15 | EJ-Begriff einführen + kurz erklären (1 Satz) | Copy | 15 Min | ⭐⭐⭐ |

---

## I. COPY & MESSAGING

### I.1 nRLP-Legitimation — sofort einbauen

Der neue ABU-Rahmenlehrplan (nRLP) tritt 2026 in Kraft. Er verankert KI-Urteilskompetenz als **gesetzlich geforderte Lernziele**. Vier exakte Formulierungen dienen als direkte Verkaufsargumente:

| Argument | nRLP-Formulierung | Kapitel |
|----------|-------------------|---------|
| Quellenkritik | „Mit der Vielfalt der Quellen und Medieninhalte, **inklusive Anwendungen der künstlichen Intelligenz**, kritisch umgehen" | 3.2.1 |
| KI als Kommunikationswerkzeug | „**Mit Tools der künstlichen Intelligenz interagieren**" | 4.2.3.3 |
| Chancen/Risiken reflektieren | „**Chancen und Risiken von künstlicher Intelligenz** analysieren … Risiken wie Falschinformation (Fake News)" | 5.2.7.2 |
| Prüfungsordnung KI | „die zugelassenen Hilfsmittel, **insbesondere den Umgang mit künstlicher Intelligenz**" | 7.1 |

**Konkrete Website-Aktion:** Im Angebots-Abschnitt oder in einer separaten Box: *„KIalog deckt 4 Kompetenzbereiche des neuen ABU-Rahmenlehrplans (nRLP 2026) ab."* mit Kurzliste der 4 Punkte.

**Warum:** Schulen unter dem Anpassungsdruck des nRLP (Einführung August 2026) suchen Weiterbildungen, die rechtlich legitimierte Kompetenzfelder abdecken. Das ist kein Nice-to-have mehr — es ist Bildungsauftrag.

*Quelle: Notebook Lehrpläne EBA/EFZ (ABU)*

---

### I.2 Hero-Text: Transformation statt Anbieter-Perspektive

**Problem:** Heutiger Hero kommuniziert aus Manuels Perspektive ("Ich biete", "Meine Methode"). Entscheider (Schulleitung, AL AVK) fragen: *Was ändert sich für meine LP?*

**Vorschlag Hero-Claim:**
> "Ihre Lehrpersonen beurteilen KI-Output — statt ihn blind zu übernehmen."

Subline:
> "KIalog vermittelt die Urteilskompetenz, die der neue Lehrplan fordert — in 2×90 Minuten, sofort einsetzbar."

**Warum:** Copywriter-Bildung-Notebook: Transformation-oriented Copy konvertiert 27–104% besser als provider-focused. Die Entscheider-Logik: "Was bringt das meinen LP?" kommt vor "Wer ist das?".

*Quellen: Notebook Copywriter Bildung, Notebook Web-UX Bildung (A9)*

---

### I.3 Widerstandsmuster der LP direkt adressieren

Aus dem Notebook LP-Stimmen & KI-Akzeptanz: LP im Sek II / BFS zeigen drei typische Widerstände, die kialog.ch aktuell **nicht beantwortet**:

1. **"Ich muss keine KI-Expertin sein"** → Antwort: "KIalog lehrt Beurteilung, nicht Bedienung. Du brauchst kein technisches Vorwissen."
2. **"Die Lernenden nutzen KI sowieso — warum soll ich das noch unterrichten?"** → Antwort: "Genau deshalb. LP-Feedback verliert an Gewicht, wenn es nicht erklärt, *warum* die KI falsch liegt."
3. **"Das ist schon wieder ein Tool-Kurs"** → Antwort kialog.ch muss explizit sein: "Kein Tool-Kurs. Keine App. Ein didaktisches Verfahren für jede Unterrichtssituation."

**Konkrete Website-Aktion:** FAQ um diese 3 Fragen erweitern — jeweils mit 2-Satz-Antwort.

*Quelle: Notebook LP-Stimmen & KI-Akzeptanz*

---

### I.4 Dringlichkeit "ab August 2026"

Der nRLP wird ab August 2026 an Berufsfachschulen eingeführt. Kantonale Schullehrpläne werden aktuell erarbeitet.

**Konkrete Website-Aktion:** Unter dem Pilot-Hinweis: *„Der neue ABU-Lehrplan tritt August 2026 in Kraft. KIalog-Piloten jetzt buchen."*

*Quelle: Notebook Lehrpläne EBA/EFZ (ABU)*

---

### I.5 EJ-Begriff einführen

Evaluative Judgement (EJ) ist der wissenschaftliche Kern von KIalog. Er fehlt auf der Seite fast vollständig.

**1-Satz-Erklärung für die Website:**
> "Evaluative Judgement — die Fähigkeit, Qualität zu beurteilen, nicht nur zu produzieren — ist laut aktueller Bildungsforschung (Sadler 1989, Bearman 2024, Tai et al.) die Schlüsselkompetenz im KI-Zeitalter."

Dieser Satz verankert die Forschungsbasis, ohne akademisch zu wirken.

*Quelle: Notebook Evaluative Judgement & Feedback*

---

## II. TRUST & CREDIBILITY

### II.1 Institutionelle Logos unter Hero

**Aktion:** Logos von gibb Bern, PH FHNW, UZH im "Trusted by"-Band unter Hero. Label: *"Pilotstandort · Lehrauftrag · Forschungsbasis"*

**Warum:** Eine Schulleitung, die das gibb-Logo sieht, hat implizite Peer-Validierung ohne Testimonial. Logos von Institutionen, die die Zielgruppe kennt, sind der stärkste Trust-Hebel bei null Kundenreferenzen.

*Quelle: Notebook Web-UX Bildung (A1)*

---

### II.2 Pilot-Momentum sichtbar machen

**Aktion:** Nicht versteckt in "Über mich" — prominent im Angebots-Block:
> *"Pilot April/Mai 2026 · gibb Bern · 6–8 Lehrpersonen"*

**Warum:** "Pilot startet" wirkt stärker als "3 bisherige Kunden". Earned Momentum ("kommt gerade") übertrifft vergangene Referenzen bei Early-Stage-Produkten.

*Quelle: Notebook Web-UX Bildung (A6)*

---

### II.3 Forschungsbasis namentlich sichtbar

**Aktion:** Im Abschnitt "Warum KIalog wirkt" oder im Footer: *"Basiert auf Evaluative Judgement (Sadler 1989), Feedback Literacy (Nicol 2021, Carless & Boud) und aktueller KI-Feedback-Forschung (Bearman 2024, Tai et al.)."*

**Warum:** LP-Akzeptanz-Forschung zeigt: Lehrpersonen und Dozierende an PH/FH reagieren auf wissenschaftliche Legitimation — besonders wenn eigene Forschungsinstitution (UZH/PH FHNW) erkennbar ist.

*Quelle: Notebook Evaluative Judgement & Feedback*

---

### II.4 "So läuft es ab"-Block

**Aktion:** 4-Schritte-Timeline für eine Schulleitung, die zum ersten Mal auf die Seite kommt:
1. Erstgespräch (30 Min, kostenlos) — Bedarf klären
2. Impuls-Workshop (60 Min) — Methode erleben
3. KIalog Workshop (2×90 Min) — Transfer in den eigenen Unterricht
4. Optional: Fachbegleitung (1 Semester)

**Warum:** Fehlende Prozess-Transparenz ist nach Testimonials der zweitgrösste Vertrauenshemmer bei Dienstleistungen ohne öffentliche Preisliste.

*Quelle: Notebook Web-UX Bildung (A5)*

---

## III. PRICING

### III.1 Workshop als "Empfohlen" markieren

**Aktion:** Mittlere Option (KIalog Workshop, CHF 1'800–3'000) visuell hervorheben: Lime-Rahmen, Badge "Empfohlen", leicht grössere Karte.

**Warum:** Tiered Pricing mit hervorgehobener mittlerer Option erhöht Conversion auf diese Option um ~28%. Anchoring-Effekt: Fachbegleitung (CHF 9'000) lässt Workshop erschwinglich wirken.

*Quelle: Notebook Web-UX Bildung (A2)*

---

### III.2 Persona-Zeilen pro Tier

**Aktion:** Unter jedem Angebot eine Zeile:
- Impuls: *"Für Schulleitungen: Überblick in einer Stunde."*
- Workshop: *"Für Lehrpersonen-Teams: Sofort einsetzbar im eigenen Unterricht."*
- Fachbegleitung: *"Für Fachgruppen: Strukturierte Begleitung über ein Semester."*

**Warum:** B2B-Entscheider (SL, AL, Studienleitende PH) und direkte Nutzer (LP) haben unterschiedliche Entscheidungslogiken. Persona-Zeilen vermeiden Misspassung.

*Quelle: Notebook Web-UX Bildung, Bildungsfinanzierung CH*

---

### III.3 Finanzierungs-Badges

**Aktion:** Pro Angebot sichtbar: *"SCHILW-buchbar · BKD-rückvergütbar (Kanton Bern)"*

**Warum:** Budgetverantwortliche in Kantonsschulen denken in Kostenstellen. "BKD-rückvergütbar" ist ein Entscheidungs-Enabler, der Preiswiderstände auflöst — besonders wenn CHF 1'800–3'000 intern genehmigt werden muss.

*Quelle: Notebook Bildungsfinanzierung CH*

---

## IV. SEO / AEO

### IV.1 Course-Schema für alle 3 Formate

**Aktion:** JSON-LD für Impuls, Workshop, Fachbegleitung als je ein `Course` mit `offers` (price + currency + availability) + `provider` (Organization). Qualifiziert für Google-Kurs-Rich-Results.

```json
{
  "@type": "Course",
  "name": "KIalog Workshop",
  "description": "2×90 Min. KI-Urteilskompetenz für Lehrpersonen",
  "provider": { "@type": "Organization", "name": "KIalog" },
  "offers": { "@type": "Offer", "price": "1800", "priceCurrency": "CHF" }
}
```

*Quelle: Notebook SEO AEO 2026, Web-UX Bildung (C1)*

---

### IV.2 Person-Schema erweitern

**Aktion:** `sameAs`-Array um ORCID, LinkedIn, PH FHNW-Profil, UZH-Profil, gibb-Profil erweitern. `hasCredential` für Lehrauftrag + Doktorat. Verbindet Manuel als Entität mit den Institutionen.

*Quelle: Notebook SEO AEO 2026 (C2)*

---

### IV.3 FAQ GEO-optimieren

**Prinzip:** LLMs (ChatGPT, Gemini, Perplexity) zitieren bevorzugt die ersten 40–60 Wörter einer FAQ-Antwort. Struktur: Direkte Antwort Satz 1–2, Begründung/Statistik Satz 3–4.

**Beispiel:**
> F: Was ist KI-Urteilskompetenz?  
> A: KI-Urteilskompetenz (Evaluative Judgement) ist die Fähigkeit, KI-Output zu beurteilen — zu entscheiden, was zu übernehmen, anzupassen oder zu verwerfen ist. Sie ist laut ABU-Rahmenlehrplan 2026 eine verbindliche Schlüsselkompetenz an Berufsfachschulen der Deutschschweiz.

*Quelle: Notebook SEO AEO 2026 (C6)*

---

### IV.4 hreflang="de-CH"

**Aktion:** `<link rel="alternate" hreflang="de-CH" href="https://kialog.ch/" />` im `<head>`. 5 Minuten. Verhindert Ausspielung für DE/AT statt CH.

*Quelle: Notebook SEO AEO 2026 (C3)*

---

## V. POSITIONIERUNG (nicht direkt Website, aber Kommunikation)

### V.1 Externe Anbieter vs. Inhouse — die richtige Antwort

Lehrpersonenverbände (LCH) bevorzugen interne Weiterbildung. Die richtige Antwort auf diesen Einwand ist **nicht** "wir sind besser als Inhouse", sondern:

*"KIalog ist kein Tool-Kurs, den eine Fachlehrperson auch machen könnte. Es ist eine Methode, die an Forschung (UZH, EJ-Literatur) und Schulpraxis (gibb, PH FHNW) gleichzeitig entwickelt wurde — das ist die Kombination, die intern nicht replizierbar ist."*

**Konkrete Website-Aktion:** Im "Über mich"-Abschnitt das Dreifachprofil als strukturierte Liste: *Praxis (gibb) · Ausbildung (PH FHNW) · Forschung (UZH).* Nicht als Biografie, sondern als Kompetenz-Tripel.

*Quelle: Notebook KI in Schweizer Hochschulen, LP-Stimmen & KI-Akzeptanz*

---

### V.2 ABU-Themenfelder als Szenario-Anker

Fünf ABU-Themenfelder eignen sich als Ankerpunkte für Walkthrough-Seiten oder den "Szenarien"-Abschnitt:

| ABU-Thema | KIalog-Szenario |
|-----------|-----------------|
| Demokratie & Mitgestaltung | KI-generierte Abstimmungsargumente kritisch prüfen |
| Arbeit & Zukunft | KI-Bewerbungsschreiben auf Authentizität beurteilen |
| Wohnen / Geld & Kauf | Algorithmenlogik bei Wohnungssuche verstehen |
| Risiko & Gesundheit | KI-Gesundheitsratschläge auf Verlässlichkeit prüfen |
| Sprache & Kommunikation | KI-Feedback auf eigenen Text beurteilen |

*Quelle: Notebook Lehrpläne EBA/EFZ (ABU)*

---

## VI. QUICK-WIN-LISTE (unter 1h gesamt)

1. `hreflang="de-CH"` im `<head>` → 5 Min
2. "Pilot April/Mai 2026 · gibb Bern" prominent einbauen → 10 Min
3. SCHILW-buchbar + BKD-rückvergütbar Badge → 15 Min
4. Persona-Zeilen unter Preistabelle → 15 Min
5. "Empfohlen"-Badge auf Workshop → 10 Min

---

*Quellen: 9 NotebookLM-Notebooks, April 2026. Aufbauend auf Web-Research-Funde (Sektion A–E oben).*
