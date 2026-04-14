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

## Status (14.04.2026)

### Erledigt
- ✅ **Wiki-LLM Vault aufgebaut (14.4.)** — Karpathy-Pattern, CLAUDE.md, raw/-Struktur, 38 PDFs, 25 Wiki-Seiten, Architektur-Schicht 4
- ✅ **Inbox-Skill verschärft (14.4.)** — Phase 2 Tiefenprüfung, Wiki-LLM-Routing, Command → Thin Wrapper
- ✅ **Dashboard gefixt (14.4.)** — 4 Geister-Skills raus, 2 Plugins rein, Chrome-Öffnung
- ✅ **Zotero MCP gefixt (14.4.)** — Von .mcp.json nach mcp.json verschoben, aktiv ab nächster Session
- ✅ **Healthcheck erweitert (14.4.)** — Skill-Health-Check (OpenSpace FIX-Pattern)
- ✅ **Luege +5 Einträge (14.4.)** — OpenSpace, CLI-Anything, RAG-Anything, gws CLI, Claude Peers
- ✅ System-Audit, `/start`+`/ende` bereinigt, Memory-Hygiene (14.4. früher)
- ✅ Dashboard v3, Kepano Skills, Obsidian Base (13.4.)

### Offen — Nächste Session
- 🔲 **Audit 4–9 abschliessen:**
  - (4) Trigger der 0-Aufruf-Skills prüfen (gibb-abu-lernbegleitung, bewertungspipeline, design-kohaerenz, kanoniker-check)
  - (5) 5 veraltete Projekt-Memories löschen (Webseite-Varianten + Weiterbildung)
  - (6) tool-registry.md auto-generieren (Script statt Prosa)
  - (7) Website-Stack konsolidieren (4 Autoritäten → 2)
  - (8) notebooklm-to-vault + experten zusammenführen
  - (9) /stilcheck um design-kohaerenz erweitern
- 🔲 **Wiki-LLM Tier 3** — Simondon, Barad/Bohr, Lacan aus Quellenstellen_Grenzform.md
- 🔲 Evals für Top-5-Skills schreiben
