---
tags: [moc, navigation]
---

# COWORK — Map of Content

## Forschung
- [[01-UZH Exposee/CLAUDE|Dissertation UZH]] — Evaluative Judgement bei KI-Feedback, Exposé abgabebereit
- [[06-Philosophie/CLAUDE|Philosophie]] — Grenzform-Ontologie, Brücke zu EJ in Punkt 8

## Lehre
- [[03-PH FHNW/Lehrauftrag/CLAUDE|PH FHNW]] — Reflexionsseminare Basis- und Fokusphase, Fallanalysen
- [[04-BWZ Lyss/CLAUDE|BWZ Lyss]] — ABU EFZ (Logistiker, Gärtner), 1. Lehrjahr
- [[11-gibb Lernbegleitung/CLAUDE|Lernbegleitung gibb]] — ILB-Professionalisierung, BV-Tag 17.4.2026

## Geschäft & Strategie
- [[13-KIalog Wissensbasis/CLAUDE|KIalog Wissensbasis]] — Strategische Wissensbasis KI-Didaktik-Geschäft
- [[08-KIalog Website/CLAUDE|Website kialog.ch]] — Marke, Vertrieb, Positionierung

## Produkte
- [[10-werkraum/CLAUDE|Werkraum]] — Didaktische Brücke: Fachidee → Laufpaket → Coding-Agent, EJ-basiert
- [[09-KIalog Produkte/Produktarchitektur_Entwurf|Produktarchitektur]] — 3-Schritt-Methode (Prüfen→Urteilen→Belegen), Stufenmodell
- [[09-KIalog Produkte/KIalog/CLAUDE|KIalog Workshop]] — 2×90 Min, EJ-Workflow, Pilot gibb April 2026
- [[09-KIalog Produkte/difflab/CLAUDE|KIalog diff]] — Next.js-Prototyp, archiviert
- [[09-KIalog Produkte/dipFund/CLAUDE|dipFund II]] — Förderantrag BeLEARN, Deadline 26.4.2026

## Privat & Finanzen
- [[02-M&K Trading Playbook/CLAUDE|M&K Trading]] — BTC Bärenmarkt-Strategie, Short live
- [[14-Haus-Erbschaft/CLAUDE|Haus & Erbschaft]] — Nachlassplanung, Hypothek Mutter 2028 kritisch

## Kreativ
- [[07-Silbenfall/CLAUDE|Silbenfall]] — Instagram-Mikropoesie @silbenfall, 61 Posts

## Archiv
- [[05-ARCHIV-Digital Competencies/README|Digital Competencies]] — KI-Skills Handover Kit (archiviert 1.3.2026)

## Wissen
- Wiki-LLM — Karpathy-Pattern Wissensbasis, 80 Seiten (44 Quellen + 35 Konzepte + 1 Projekt), Schicht 4 in Architektur

## Meta
- [[15-Organisation/CLAUDE|Organisation]] — Wissensmanagement, Skills, Dateistruktur

---

## Querschnittsthemen

> [!abstract] Evaluative Judgement — der rote Faden
> [[01-UZH Exposee/CLAUDE|Forschung]] → [[09-KIalog Produkte/KIalog/CLAUDE|Workshop-Kern]] → [[13-KIalog Wissensbasis/CLAUDE|Geschäfts-USP]] → [[06-Philosophie/CLAUDE|Grenzform-Brücke]]
> EJ ist Manuels einzigartiger Beitrag: Niemand sonst verschränkt KI-Didaktik + EJ in der Deutschschweiz.

> [!abstract] Berufsbildung Schweiz — drei Schulen, ein Feld
> [[04-BWZ Lyss/CLAUDE|BWZ Lyss (ABU EFZ)]] + [[11-gibb Lernbegleitung/CLAUDE|gibb (ILB/EBA)]] + [[03-PH FHNW/Lehrauftrag/CLAUDE|PH FHNW (Ausbildung)]]
> Gleiche Zielgruppe (LP an Berufsfachschulen), unterschiedliche Perspektiven.

> [!abstract] Dreifachprofil — Forscher + Praktiker + Ausbilder
> [[01-UZH Exposee/CLAUDE|UZH (Forschung)]] × [[11-gibb Lernbegleitung/CLAUDE|gibb (Praxis)]] × [[03-PH FHNW/Lehrauftrag/CLAUDE|PH FHNW (Ausbildung)]]
> Dieses Profil ist der USP für [[08-KIalog Website/CLAUDE|Website]] und [[13-KIalog Wissensbasis/CLAUDE|Geschäft]].

> [!abstract] Produktkette — von Methode zu Tool zu Förderung
> [[09-KIalog Produkte/KIalog/CLAUDE|KIalog Workshop (Methode)]] → [[09-KIalog Produkte/dipFund/CLAUDE|dipFund (Geld)]]
> KIalog ist das einzige aktive Produkt. difflab aktiv (Prototyp).

> [!abstract] ABU & DaZ — wo sich alles trifft
> [[04-BWZ Lyss/CLAUDE|BWZ Lyss]] liefert Praxis → [[09-KIalog Produkte/KIalog/CLAUDE|KIalog Workshop]] macht daraus Weiterbildung → [[09-KIalog Produkte/difflab/CLAUDE|KIalog diff]] automatisiert den Workflow → [[01-UZH Exposee/CLAUDE|Dissertation]] evaluiert die Wirkung.

> [!abstract] Zwei Wissensströme — Monitor + Luege
> **"Monitor"** → KI-Didaktik, Bildung, Policy → [[13-KIalog Wissensbasis/06-KI-Bildung-Monitor/KI_Bildung_Erkenntnisse|KI_Bildung_Erkenntnisse.md]]
> **"Luege"** → System, Tools, Produktivität → [[15-Organisation/Luege_Erkenntnisse|Luege_Erkenntnisse.md]]
> Codewort + Quelle reicht. APA 7, datiert, vernetzt.

---

## Deadlines

```dataview
TABLE WITHOUT ID
  deadline AS "Datum",
  regexreplace(file.path, "/CLAUDE.md", "") AS "Projekt",
  next AS "Nächster Schritt"
FROM ""
WHERE file.name = "CLAUDE" AND deadline AND status = "aktiv"
SORT deadline ASC
```

---

## Personennetzwerk

```dataview
TABLE WITHOUT ID
  file.link AS "Person",
  rolle AS "Rolle",
  projekte AS "Projekte"
FROM "_Personen"
WHERE rolle
SORT file.name ASC
```
