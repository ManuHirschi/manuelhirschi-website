---
tags:
  - meta
  - organisation
  - system
status: aktiv
related:
  - "[[00-HOME|Map of Content — Vault-Übersicht]]"
  - "[[13-KIalog Wissensbasis/06-KI-Bildung-Monitor/CLAUDE|Monitor — KI-Didaktik-Pendant zu Luege]]"
  - "[[15-Organisation/Luege_Erkenntnisse|Luege Erkenntnisse — Sammel-Dokument]]"
gruppe: meta
prio: ref
next: Remote-MCPs deaktivieren (Zapier, Canva, Gamma)
---

# Projekt: Organisation — Dashboard & Systemdoku

Zentraler Ort für Vault-weite Infrastruktur: Dashboard, Architektur-Diagramm, Konvertierungs-Scripts, Audit-Framework. Skills, Commands, Rules und Automations leben in `~/.claude/` — nicht hier.

## Personen

- **Manuel Hirschi** — System-Owner

## Ordnerstruktur

```
15-Organisation/
├── CLAUDE.md                              ← Du bist hier
├── Benutzerhandbuch.md                    ← Systemdoku + Designentscheidungen + Rekonstruktion
├── Bruchanalyse.md                        ← Wo das System trägt, kippt, unnötig schwer wird (7.4.2026)
├── generate_dashboard.py                  ← Generiert 00-Dashboard.html aus CLAUDE.md-Frontmatter
├── COWORK-Systemarchitektur.excalidraw    ← 5-Schichten-Architektur
├── COWORK-Systemarchitektur.png           ← Gerendert
├── Bericht_Lokale-KI-Erweiterungen.md     ← Ollama, NotebookLM, Whisper (Recherche 4.4.)
├── Systemaudit/                           ← 7-Schichten-Auditplan für /audit
├── Luege_Erkenntnisse.md                  ← Lebendes Dokument: System-Erkenntnisse (APA 7)
├── 00-Commands.md                         ← Slash Commands Übersicht
├── konvertiere.py                         ← PDF/DOCX → Markdown
├── reorganisiere.py                       ← Scan + Reorganisation
└── _archiv/
```

## Was wo lebt

| Was | Ort |
|-----|-----|
| Skills, Commands, Rules | `~/.claude/` |
| Automations (Deadline, Backup, Memory) | `~/.claude/automations/` |
| MCP-Server (Ollama) | `~/.claude/mcp-servers/` |
| Memory | `~/.claude/projects/.../memory/` |
| Dashboard | `00-Dashboard.md` (Dataview, Obsidian) |
| Architektur-Diagramm | Hier: `COWORK-Systemarchitektur.*` |

## Luege — System-Monitor

Vollständig definiert im Skill `inbox` (`~/.claude/skills/inbox/SKILL.md`). Codewort "luege" triggert den Skill. Erkenntnisse landen in `Luege_Erkenntnisse.md`.

---

## Status (19.04.2026)

### Erledigt (19.4.) — inbox v2 + Verifikations-Hook
- ✅ **inbox-Skill v2**: Triage/Apply-Split (Default triage), Zotero-Kanonik-Check (E1), Triage-Persistenz konditional (E3). Trockenlauf auf 2 Fixtures grün, 5 Minimalchecks bestanden.
- ✅ **Arbeitsregeln Abschnitt "Vollzug und Prüfung"** (Commit `f41b672`): 6 Regeln in `~/.claude/rules/arbeitsregeln.md`. Kern: Keine Vollzugsbehauptung ohne echten Pfadtest. Skill-Text ≠ Command-Vollzug.
- ✅ **Verifikations-Hook LIVE bestätigt** (19.4. Nachmittag): Vollzugstest durchlaufen — PostToolUse erzeugt Pending automatisch, PreCompact blockiert bei offenem Pending, nach Nachweis läuft `/compact` durch. Guard-Bugfix: ursprüngliche Logik hatte Deckungslücke (`ergebnis: ungeprüft` deckte fälschlich). Neue Logik: nur exaktes `objekt:` + `vollzug_getestet: ja` + `ergebnis: trägt` + mtime > Pending deckt.
- ✅ **arbeitsregeln.md v2** (19.4.): Normverdichtung 100 → 90 Zeilen, ca. −25% Wörter, keine Regel verloren. Rollenblock auf Verweis reduziert (kialog-SoT-Zeile bewusst erhalten, da in `references/rollen-und-kontexte.md` nicht verankert). Zwei neue Regeln im Abschnitt "Vollzug und Prüfung": Drei-Kategorien-Trennung (Inhalt/Vollzug/offen), Verifikations-Hook verbindlich.
- 🔲 **Offen — Hook-Loophole:** PostToolUse matcht nur `Write|Edit`, nicht Bash-`cp`. Systemdatei-Änderungen via Bash umgehen den Pending-Mechanismus. Als eigene Regel merken: für `~/.claude/**` nie cp, immer Write/Edit.
- 🔲 **Offen — Vollzugstest arbeitsregeln v2 in Folgesession:** Greift die neue Kurzfassung via SessionStart-Kontext?

### Erledigt (18.4.) — Durchdringung Claude-System
- ✅ **Plan G Phase 1+2 abgearbeitet und gepusht.** Commits: `c5c856f` (~/.claude), `1e6a860` (_COWORK). Details: `Durchdringungen/2026-04-18-claude-system/`
- ✅ **Autoritätsordnung** (7-stufig) in `rules/architektur.md`
- ✅ **TTL-Template** für Memory in `references/memory-template.md`, TTL-Check in `commands/ende.md`
- ✅ **Auto-Validatoren**: `hooks/session-start.sh` erweitert (Symlink + Wikilink), `hooks/access-tracking.sh` neu, `commands/check.md` Drift-Scan + priorisiertes Reporting
- ✅ **Archive durchsucht, 4 Ordner + 8 Einzeldateien reaktiviert** (16-Architekt-Protokoll, Faehigkeiten-Karte, Prioritaetsentscheid, Paper-Projekt-Scaffolding, GEM_Upload, HS26_Materialdrop, compass_artifact, KIalog-Methode, Quellen_Website, Marktrecherche_SCHILW, Produkt-Strategie-Analyse, Claudes-Gehirn-Wissensarchitektur, BV-Tag_Tagesgestaltung, Moderationskarten_Share)
- ✅ **Zwei neue harte Regeln** in arbeitsregeln.md: Archivieren = nie autonom (Verletzung war Ursache der Unsichtbarkeit); Kein "du hast recht"
- ✅ **EJ-USP = Deutschschweiz** entschieden (nicht DACH-Raum). SSOT: `13-KIalog Wissensbasis/CLAUDE.md`
- ✅ **Briefing für Folgesession**: `Durchdringungen/2026-04-18-claude-system/08-briefing-fuer-folgesitzung.md` (Codex-geprüft, angepasst)

### Erledigt (14.4.) — Wiki-LLM-Aufbau
- ✅ Wiki-LLM Vault (Karpathy-Pattern, 38 PDFs, 25 Seiten)
- ✅ Inbox-Skill (Phase 2 Tiefenprüfung, Wiki-LLM-Routing)
- ✅ Dashboard + Zotero MCP + Healthcheck-Erweiterung
- ✅ Luege +5 Einträge
- ✅ Dashboard v3, Kepano Skills, Obsidian Base (13.4.)

### Erledigt (18.–19.4.) — Mechanik-Schicht A–E
- ✅ **Phase A LIVE** (18.4.): 3 Hooks in `~/.claude/hooks/`, 27/27 Tests grün, Echtbetrieb bestätigt.
- ✅ **Phase B1 abgeschlossen** (18.4.): 56/56 Memories mit Schema (`gilt_ab`, `gilt_bis`, `letzte_pruefung`, `quelle`), idempotent.
- ✅ **Phase C1 abgeschlossen** (18.4.): 3a Normalisierung `created → erstellt`, 44/44 Dateien. 3b, 3d bewusst abgelehnt.
- ✅ **Phase C2-v1 abgenommen** (18.4./19.4.): Drift-Messung gegen settings.json als Source of Truth. `_CODE/scripts/c2_drift_check.py`, Bericht `_CODE/drift-log/2026-04-18-c2.md`.
- ✅ **Phase D abgenommen** (19.4.): Regel-Metadaten-Frontmatter in `~/.claude/rules/*.md`. Variante A (leer, kein Pseudo-Datum). Werkzeug `migrate-rules.py` nur bedingt abgenommen — Guard-Härtung vor Wiederverwendung.
- ✅ **Phase E-v1 abgeschlossen** (19.4.): memsearch Collection `vault` (17603 Chunks), Memory-Collection `memsearch_chunks` unberührt. Reversibel via Backup.

### Erledigt (19.4.) — Quellenablage v1 + /quellenlage
- ✅ **`/quellenlage` v0 abgenommen** (19.4.): Read-only Audit-Command für 5-System-Topologie. `~/.claude/commands/quellenlage.md`, Logik `_CODE/scripts/quellenlage.py`. Erstlauf 14:30: 3 trägt · 2 driftet · 2 unklar.
- ✅ **Quellenablage v1 normativ festgelegt** (19.4.): `~/.claude/references/quellenablage-v1.md` (4 Kategorien, Ablage je Quellentyp, Buchkapitel-Ausnahme, `status_source`, Sensibilitätsregel, Ist-Snapshot). Kurzregel in `arbeitsregeln.md` verankert.
- ✅ **Mini-Patch** (19.4., 15:00): `quellenablage-v1.md` in Quellenbasis des Audits aufgenommen; `quellen handy` jetzt gegen v1-Regel bewertet statt `unklar`.
- Sperren: keine Migration, keine Trigger, keine Pipeline-Automation. Regel gilt vorwärtsgerichtet.

### Offen — Nächste Session
- 🔲 Bauplan-Korrektur `~/.claude/mcp.json` → aktueller Stand (drei Scopes) in `_CODE/01-mechanik-reihenfolge.md`.
- 🔲 `migrate-rules.py` Guard-Härtung (Pfad-Allowlist oder Datei-Allowlist).
- 🔲 Reindex-Strategie für Vault-Collection (manuell / `memsearch watch` / Hook).
- 🔲 MCP-Integration memsearch (falls später gewünscht).
- 🔲 3b, 3d, Thematische Paar-Prüfung bleiben gesperrt.
- 🔲 `arbeitsregeln.md` >200 Zeilen (Kürzungs- oder Split-Entscheidung).
- 🔲 Audit 4–9, Wiki-LLM Tier 3, Evals Top-5-Skills (Vorsession).

### Struktureller Befund
Claude ist **Ausführer, nicht Pfleger**. Mechanik-Schicht A–E ist damit bauplan-konform durch. Systemmechanik pausiert ohne neuen Auftrag. Quelle der Wahrheit für Systemmechanik: `_CODE/03-zwischenstand.md`.
