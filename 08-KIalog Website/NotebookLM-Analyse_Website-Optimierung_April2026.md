---
tags: [website, geschaeft, research, notebooklm]
status: aktiv
related:
  - "[[08-KIalog Website/CLAUDE|Website — Projektstand]]"
  - "[[08-KIalog Website/Research_Website-Optimierung_April2026|Research — 40 Funde]]"
  - "[[08-KIalog Website/NotebookLM-Rohdaten-April2026|Rohdaten Session 11]]"
---

# NotebookLM-Analyse: Website-Optimierung kialog.ch
**Erstellt:** 9.4.2026
**Methodik:** 8 Notebooks × 5-6 Fragen = ~40 Erkenntnisse, gegen Ist-Zustand abgeglichen

---

## Befragte Notebooks

| # | Notebook | Fokus |
|---|----------|-------|
| 1 | Web-UX Bildung | Design, Trust, UX-Patterns, Conversion |
| 2 | SEO AEO 2026 | Technisches SEO, GEO, Schema.org, Core Web Vitals |
| 3 | Copywriter Bildung | Text, Headlines, Storytelling, Dual-Audience |
| 4 | LP-Stimmen + KI-Akzeptanz | Zielgruppenpsychologie, Widerstände, Trigger |
| 5 | EJ & Feedback | Evaluative Judgement, KI- vs. Mensch-Feedback |
| 6 | Lehrpläne EBA/EFZ (ABU) | nRLP-Kompetenzbereiche, Prüfungsrelevanz |
| 7 | Schule 2.0 | Marktlücken, Positionierung, Vertrieb, Pricing |
| 8 | Bildungsfinanzierung CH | SCHILW-Budgets, Fördertöpfe, MWST, CAS-Vergleich |

---

## 10 Kernerkenntnisse (Cross-Pattern-Synthese)

### 1. Dark Mode vs. Bildungsbranche (KRITISCH)
**Web-UX-NB:** "Durchgehender Dark Mode wird mit Tech-Startups assoziiert. Warme, erdige Farbtöne vermitteln professionelle Atmosphäre im Bildungssektor."
**Ist:** `#0B0B0B` + Lime `#BEFF00` — technisch exzellent, aber visuell näher an Developer-Portfolio als Bildungsanbieter.
**Empfehlung:** Warm Dark (#1A1916) als Sofort-Fix, dann Hybrid (Dark Hero → Light Body ab Schulleitungen).

### 2. Zwei-Funnel-Architektur fehlt
**Cross-Pattern (4 NB):** Lehrpersonen (du, Autonomie, Entlastung) und Schulleitungen (Sie, Pflicht, ROI) brauchen getrennte Narrative.
**Ist:** Buttons "Ich bin LP / Ich leite eine Schule" existieren, führen aber zum selben Content.
**Empfehlung:** Echte Verzweigung oder eigenständiger Scroll-Pfad für Schulleitungen.

### 3. Text-Dichte: Zu dünn für SEO, gleichzeitig UX-Risiko
**SEO-NB:** 1500-4000 Wörter, semantische Vollständigkeit 8.5/10 → 340% mehr KI-Zitate.
**Web-UX-NB:** Progressive Disclosure — Kern sichtbar, Details in Akkordeons.
**Ist:** ~750 sichtbare Wörter. Kein expandierbarer Content.
**Sweet Spot:** Sichtbar ~1000w, expandierbar auf 2500+ via Akkordeons.

### 4. Answer-First-Architektur fehlt komplett
**SEO-NB:** "Jede H2 sofort mit 20-60 Wörter Antwort-Kapsel beginnen. KI-Modelle extrahieren nur den ersten Absatz."
**Ist:** Poetisch-emotionale Einstiege ohne extrahierbaren Informationsgehalt.
**Empfehlung:** Jede Sektion braucht einen unsichtbaren oder sichtbaren Antwort-Satz.

### 5. nRLP-Argumentation nicht ausgeschöpft
**Lehrpläne-NB liefert direkte Zitate:**
- Kap. 3.2.1: "Um mit der Vielfalt der Quellen und Medieninhalte, inklusive Anwendungen der künstlichen Intelligenz, kritisch umgehen zu können..."
- Kap. 4.2.3.3: "Mit Tools der künstlichen Intelligenz interagieren"
- Kap. 7.1: "er regelt den Umgang mit künstlicher Intelligenz" (Prüfungsrelevanz!)
**Ist:** 4 Punkte ohne Zitate, ohne Kap.-Verweise, ohne Prüfungsrelevanz.

### 6. EJ-Positionierung zu versteckt
**EJ-NB:** "KI hat die Lücke zwischen Produktionsfähigkeit und Bewertungsfähigkeit massiv vergrössert" (Bearman & Luckin). EJ = einzigartig menschliche Fähigkeit.
**Ist:** EJ nur einmal erwähnt in Schritt 2, beiläufig.
**Empfehlung:** EJ als Kern-Narrativ, nicht als Fussnote.

### 7. Trust-Signale — grösste Lücke
**Fehlend:** Video, institutionelle Logos, Testimonials, Datenschutz-Signal, Aktualisierungsdatum.
**Sofort möglich:** Forschungsdaten (bereits da), Datenschutz-Hinweis, Aktualisierungsdatum, institutionelle Zugehörigkeiten prominenter.

### 8. Refinanzierungs-Argumentation fehlt
**Bildungsfinanzierung-NB:** SCHILW Bern bis CHF 20'000/Jahr. Interessegrad 1-2: 75-100% Kostenübernahme. Keine Stellvertretungskosten. Keine Bindungsklauseln.
**Ist:** Ein Satz: "Kostenübernahme je nach Kanton möglich."
**Empfehlung:** Konkrete Zahlen, CAS-Vergleichsrechnung.

### 9. Zielgruppen-Psychologie (LP-Stimmen)
- **Stärkster Akzeptanz-Treiber:** Wahrgenommene Nützlichkeit (TAM2, Odds Ratio 2.37)
- **Stärkste Angst:** KI als Zeitfresser (45% PhV NRW), Datenschutz
- **Stärkster emotionaler Trigger:** Autonomie ("Human-in-the-Loop", Elektrofahrrad-Metapher)
- **Diskrepanz:** 80% bereit, nur 39% kompetent (SVEB 2024)

### 10. Technische SEO-Gaps
- Desktop LCP 3.5s → Ziel <2.5s (Bildkompression, fetchpriority)
- Schema: EducationalOccupationalProgram fehlt
- Answer Capsules fehlen
- Aktualisierungsdatum nicht sichtbar
- Content zu dünn für semantische Vollständigkeit

---

## Priorisierte Massnahmen-Checkliste

### Phase 1: Quick Wins (Session 13)
- [ ] Warm Dark: `--bg` von #0B0B0B auf #1A1916
- [ ] nRLP-Zitate mit Kapitelangaben + Kap. 7.1 (Prüfungsrelevanz)
- [ ] Answer Capsules für alle H2-Sektionen
- [ ] Refinanzierungs-Box (SCHILW-Budgets, CAS-Vergleich)
- [ ] Datenschutz-Signal prominent
- [ ] Aktualisierungsdatum im Footer
- [ ] EJ-Positionierung stärken (Kern-Claim)

### Phase 2: Strukturell (Session 14)
- [ ] Progressive Disclosure (Akkordeons FAQ, Methode)
- [ ] Schulleitungen-Funnel eigenständig ausbauen
- [ ] Desktop-Performance (LCP: manu2.webp, AVIF, fetchpriority)
- [ ] Schema: EducationalOccupationalProgram ergänzen
- [ ] Content-Tiefe auf 2500+ Wörter expandieren

### Phase 3: Nach Pilot
- [ ] Erklärvideo (2 Min, Manuel live mit KI)
- [ ] Testimonials + Feedback-Zitate
- [ ] Institutionelle Logos (mit Genehmigung)
- [ ] Hybrid-Design: Light ab Schulleitungen-Sektion

### Strategische Entscheidung
- [ ] Dark Mode: Warm Dark → Hybrid → oder beibehalten?

---

## Quellenübersicht (Notebook-Antworten)

Vollständige Rohdaten der 8 Notebook-Befragungen: siehe Konversation vom 9.4.2026.
Ergänzend: `Research_Website-Optimierung_April2026.md` (40 Funde, 5 Kategorien).
