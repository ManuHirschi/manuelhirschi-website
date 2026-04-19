---
tags: [meta, organisation, system]
status: aktiv
related:
  - "[[15-Organisation/CLAUDE|Organisations-Projekt]]"
  - "[[15-Organisation/Luege_Erkenntnisse|Luege — System-Monitor-Erkenntnisse]]"
---

# COWORK Benutzerhandbuch — Systemdokumentation

Wie das System funktioniert, warum es so gebaut ist, und wie man es rekonstruiert.

---

## Tägliche Routine

```
Sessionstart:  /start → arbeiten
Projektwechsel: /start website (oder einfach sagen)
Sessionende:   /ende (einmal, im letzten Chat)
Themenwechsel:  /clear (statt /compact)
```

**Zwei Befehle tragen das System:** `/start` und `/ende`. Alles andere macht Claude.

### Session-Befehle

| Befehl | Wann | Was passiert |
|--------|------|-------------|
| `/start` | Beginn jeder Session | Dashboard öffnen, Deadlines + Kontext laden, Git-Diff, HOME lesen, Fokus vorschlagen |
| `/start website` | Bestimmtes Projekt | Zusätzlich: Projekt-CLAUDE.md + related + Personen laden |
| `/ende` | Ende des Tages | CLAUDE.md aktualisieren, Memories nachführen, HOME prüfen, Backup |

Memory-Hygiene läuft als Teil von `/ende` (Schritt 2b): berührte Memories prüfen, Stale-Check wenn >7 Tage, Zählung im Report.

**Projektnamen für /start:** exposé, trading, ph, bwz, philosophie, silbenfall, website, weiterbildung, ial, schule, haus, organisation

### Mehrere Terminals

| Situation | Was tun |
|-----------|---------|
| 2 Terminals, verschiedene Projekte | Normal arbeiten |
| 2 Terminals, gleiches Projekt | Nur in einem `/ende` machen |
| Chat wird langsam | "Schreib den Stand auf", dann `/clear` |

Pre-Compact Hook sichert den Session-Stand automatisch vor Kontext-Komprimierung.

---

## Architektur — 3 Schichten

### Schicht 1: Obsidian-Vault (_COWORK/)

Alle Projekte, Dokumente, Personen, Quellen an einem Ort. Google Drive synchronisiert, Git für Versionierung.

**Navigation:** CLAUDE.md → `related:` → Wikilinks → HOME. Nicht über den Obsidian-Graph.

**Jede CLAUDE.md folgt derselben Struktur:**
```yaml
---
tags: [kategorie, thema]
status: entwurf | aktiv | final | archiv
related:
  - "[[Ordner/Datei|Beschreibung]]"
---
# Projekt: {Name}
## Personen
## Ordnerstruktur
## Status ({Datum})
### Erledigt / ### Offen
```

Pflichtstruktur + Lifecycle-Regeln: `~/.claude/references/claude-md-template.md`

**Schlüsseldateien im Vault:**
- `00-HOME.md` — Map of Content, Querschnittsthemen, Dataview-Deadlines
- `00-Dashboard.html` — Generiertes HTML-Dashboard (via `15-Organisation/generate_dashboard.py`)
- `_tags.md` — Kontrolliertes Tag-Vokabular
- `_Personen/` — Personen-Notes mit Projekt-Zuordnungen

### Schicht 2: Claude Code (~/.claude/)

```
~/.claude/
├── CLAUDE.md              ← Globale Regeln (Sprache, Haltung)
├── rules/                 ← 3 Regeldateien (soul, arbeitsregeln, architektur)
├── references/            ← Nachschlagewerke (claude-md-template, tool-registry, rollen, orchestrierung)
├── commands/              ← Slash-Commands (.md)
├── skills/                ← Skills (je Ordner mit SKILL.md)
├── plugins/               ← Plugins (extern, Marketplace)
├── hooks/                 ← security-guard.sh, pre-compact-save.sh
├── mcp.json               ← Lokale MCP-Server (context7, lighthouse, notebooklm, gemini, ollama)
├── settings.json          ← Permissions, Hooks, Statusline
└── projects/.../memory/   ← Memory-Dateien + MEMORY.md Index
```

Git-Repo: github.com/ManuHirschi/claude-setup.git

**Regelhierarchie (bei Konflikten):**
1. `rules/soul.md` — Identität, nicht verhandelbar
2. `rules/arbeitsregeln.md` — Alle Arbeitsregeln + Kurzfassungen der Feedback-Memories
3. `rules/architektur.md` — Wie Navigation funktioniert, Session-Rituale
4. Feedback-Memories (`feedback_*.md`) — Kontext (Why/How to apply)
5. Projekt-CLAUDE.md — Projektspezifisch

### Schicht 3: Memory (Persistenz zwischen Sessions)

**5 Typen:**

| Typ | Zweck | Beispiel |
|-----|-------|---------|
| `user_*.md` | Wer Manuel ist | Rollen, Arbeitsweise, Kommunikation |
| `feedback_*.md` | Korrekturen + bestätigte Ansätze | "Redundanzen sofort fixen", "ADHS = Stärke" |
| `project_*.md` | Projektstände (Schnappschüsse) | Expose-Stand, Website-Version, Trading-Position |
| `reference_*.md` | Zeiger auf externe Systeme | NotebookLM CLI, Zotero, ElevenLabs |
| `MEMORY.md` | Index aller Memories | Immer geladen, max 200 Zeilen |

**Feedback-Autorität:** `arbeitsregeln.md` = Kurzregel (gewinnt immer). `feedback_*.md` = Kontext mit Why/How (bei Bedarf laden).

**Hygiene:** Projekt-Memories >30 Tage ohne Abruf = Löschkandidat. `/ende` prüft jede Session (berührte Memories + Stale-Check wenn >7 Tage). Konsolidierung manuell bei >55 Memories.

### Externe Dienste

**Lokale MCP-Server** (in mcp.json): context7, lighthouse, notebooklm, gemini, ollama
**Konnektoren** (in claude.ai): Gmail, Google Calendar, Consensus, Excalidraw, Figma, Mermaid Chart, Netlify, Scholar Gateway, tldraw, ElevenLabs, Stitch, computer-use

Aktuelles Inventar: `~/.claude/references/tool-registry.md`

---

## Session-Lifecycle

### /start — Lesen + Orientierung

1. Dashboard generieren + in Chrome öffnen
2. Deadlines mit Kontext laden (deadline + next + prio aus CLAUDE.md)
3. Git-Diff (letzte 3 Tage)
4. Bei Projekt-Argument: CLAUDE.md + related (1-Hop) + Personen (max 2) laden
5. Memory-Hygiene (wöchentlich, max 5 Memories prüfen)
6. HOME.md lesen
7. Briefing ausgeben + Fokus vorschlagen
8. Selbstwartung: Rules-Gewicht, Skill-Audit (monatlich)

### /ende — Schreiben + Sichern

1. Änderungen erkennen (git diff)
2. CLAUDE.md aktualisieren (pro betroffenes Projekt)
3. Memory aktualisieren
4. Personen-Notes (nur mit Bestätigung)
5. HOME nachführen
6. Entscheidungs-Propagation (grep + aktualisieren)
7. Systemdoku-Check: Wenn Commands/Skills/Rules/Hooks geändert → Benutzerhandbuch + tool-registry prüfen
8. Vault-Sync + Dream (sonntags)
9. Report
10. Infrastruktur-Backup (git commit in ~/.claude/)

### Kontext-Komprimierung

Bei `/compact`: Pre-Compact Hook sichert automatisch. Bei `/clear`: Erst manuell sichern ("schreib den Stand auf"). Bewahrt werden: Dateiänderungen, offene Aufgaben, Entscheidungen, Fehler.

---

## Designentscheidungen

### Warum CLAUDE.md statt Datenbank?
Markdown ist universell: Obsidian liest es, Claude liest es, git trackt es. Wenn Claude Code verschwindet, bleibt das Vault intakt.

### Warum Memory + CLAUDE.md (scheinbare Dopplung)?
CLAUDE.md = Quelle der Wahrheit (vollständig, pro Projekt). Memory = Schnellzugriff (verdichtet, projektübergreifend, immer geladen).

### Warum Feedback-Memories UND arbeitsregeln.md?
Arbeitsregeln = Kurzregel, immer geladen, gewinnt bei Konflikt. Feedback-Memory = Kontext (Why/How to apply), wird bei Bedarf geladen. Die Kurzregel sagt WAS, die Memory sagt WARUM.

### Warum Skills statt alles in CLAUDE.md?
Skills sind modulare Expertise — einzeln verbesserbar, testbar, versionierbar.

### Warum Obsidian statt RAG/Vector-DB?
Vault hat ~700 Dateien — unter der Schwelle wo RAG Vorteile bringt. Wikilinks sind manuell kuratiert und präziser als automatische Entities. Kein Infrastruktur-Overhead.

### Warum keine harten Zahlen in diesem Dokument?
Zahlen veralten am Tag nach dem Schreiben. Inventare leben in `tool-registry.md` und werden bei `/check` geprüft. Dieses Dokument beschreibt Architektur und Prinzipien.

---

## Rekonstruktionsanleitung

Falls das System von Grund auf neu aufgebaut werden muss.

### Phase 1: Grundstruktur (30 Min)
1. Claude Code installieren
2. `~/.claude/CLAUDE.md` anlegen (Sprache, Haltung)
3. `~/.claude/rules/` anlegen: soul.md, arbeitsregeln.md, architektur.md
4. `~/.claude/references/` anlegen: claude-md-template.md, tool-registry.md, rollen-und-kontexte.md, orchestrierte-gegenpruefung.md
5. `~/.claude/settings.json` mit Permissions und Hooks
6. `~/.claude/mcp.json` mit MCP-Server-Konfigurationen

### Phase 2: Vault aufsetzen (1 Stunde)
1. COWORK-Ordner mit `CLAUDE.md` (Router)
2. `00-HOME.md` als Map of Content
3. `_tags.md` mit kontrolliertem Vokabular
4. `_Personen/` mit Schlüsselpersonen
5. Pro Projekt: Ordner + CLAUDE.md (Pflichtstruktur aus claude-md-template.md)
6. `15-Organisation/generate_dashboard.py` für Dashboard-Generierung

### Phase 3: Memory aufbauen (15 Min)
1. `memory/MEMORY.md` als Index
2. `memory/user_manuel.md` als Profil
3. Feedback-Memories als Einzeldateien (Kontext zu arbeitsregeln.md)
4. Projekt-Memories bei Bedarf

### Phase 4: Commands + Skills (1 Stunde)
1. `/start` und `/ende` als Commands (tragen das System)
2. Weitere Commands nach Bedarf
3. Skills nach Domäne (alle mit SKILL.md)

### Phase 5: Hooks + Sicherheit (15 Min)
1. Security-Guard Hook (warnt bei Write auf sensible Dateien)
2. Pre-Compact Hook (sichert Session-Stand)

### Git-Repos
- `~/.claude/` → github.com/ManuHirschi/claude-setup.git
- `_COWORK/` → github.com/ManuHirschi/manuelhirschi-website.git

---

## Wartung

| Was | Wann | Wie |
|-----|------|-----|
| Memory-Hygiene | Bei /ende (jede Session) | Berührte prüfen, Stale-Check (>7d), Zählung |
| Vault-Sync | Sonntags via /ende | Obsidian-Frontmatter, HOME.md |
| Rules-Gewicht | Bei /start (wöchentlich) | Warnung wenn >200 Zeilen |
| Skill-Audit | Monatlich (1.–3.) bei /start | last_checked >30 Tage → Warnung |
| System-Vollaudit | Bei Bedarf | `/check` |
| Benutzerhandbuch + tool-registry | Bei /ende, wenn Systemdateien geändert | Automatische Warnung |

## Sicherheit

- **API-Keys** gehören in `~/.zshrc`, nie in synchronisierte Dateien
- **Security-Guard Hook** warnt bei Write/Edit auf SKILL.md, CLAUDE.md, settings.json
- **Pre-Compact Hook** sichert Session-Stand automatisch vor Komprimierung
- **Verifikations-Hook** (19.4., Scope abends erweitert) markiert Änderungen an 9 Systemdatei-Klassen (commands/*.md, skills/*/SKILL.md, hooks/*, rules/*.md, agents/*.md, references/*.md, scripts/*, settings.json, settings.local.json) als verifikationspflichtig. Blockiert `/compact`, wenn kein dokumentierter Pfadtest in `~/.claude/logs/verifikation-tests/` vorliegt. Erzwingt: Inhalt geprüft ≠ Vollzug geprüft.
- **Extern vorsichtig:** Git Push, Mails, Commits — bestätigen lassen

---

*Dieses Dokument beschreibt Architektur und Prinzipien. Für aktuelle Inventare (Skills, Commands, MCP-Server) siehe `~/.claude/references/tool-registry.md`.*

*Zuletzt verifiziert: 14.04.2026*
