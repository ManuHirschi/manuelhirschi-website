#!/usr/bin/env python3
"""Generiert ein HTML-Dashboard aus den CLAUDE.md-Frontmattern im Vault."""

import os
import re
import json
import subprocess
from datetime import datetime, date
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent
OUTPUT = VAULT / "00-Dashboard.html"
CLAUDE_DIR = Path.home() / ".claude"


def parse_frontmatter(path):
    """Extrahiert YAML-Frontmatter aus einer Markdown-Datei."""
    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        return None
    if not text.startswith("---"):
        return None
    end = text.find("---", 3)
    if end == -1:
        return None
    fm = {}
    for line in text[3:end].strip().split("\n"):
        line = line.strip()
        if line.startswith("-") or ":" not in line:
            continue
        key, _, val = line.partition(":")
        fm[key.strip()] = val.strip().strip('"').strip("'")
    return fm


def find_waiting(path):
    """Findet 'wartet'/'warten'/'meldet sich' in offenen Tasks."""
    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        return []
    items = []
    for line in text.split("\n"):
        if re.match(r"\s*-\s*\[[ ]\]", line) or "🔲" in line or "⚠️" in line:
            lower = line.lower()
            if "wartet" in lower or "warten" in lower or "meldet sich" in lower or "abwarten" in lower:
                clean = re.sub(r"^\s*[-*]\s*(\[[ ]\]\s*)?[🔲⚠️]*\s*", "", line).strip()
                items.append(clean)
    return items


def extract_description(path):
    """Extrahiert die description aus YAML-Frontmatter, inkl. mehrzeiliger > Blöcke."""
    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        return ""
    if not text.startswith("---"):
        return ""
    end = text.find("---", 3)
    if end == -1:
        return ""
    fm_text = text[3:end]
    lines = fm_text.split("\n")
    desc_parts = []
    in_desc = False
    for line in lines:
        if line.strip().startswith("description:"):
            rest = line.split("description:", 1)[1].strip()
            if rest and rest not in (">", "|", ">-", "|-"):
                return rest.strip('"').strip("'").strip()
            in_desc = True
            continue
        if in_desc:
            if line.startswith("  ") or line.startswith("\t"):
                desc_parts.append(line.strip())
            else:
                break
    return " ".join(desc_parts).strip('"').strip("'").strip()


def scan_skills():
    """Scannt alle Skills aus ~/.claude/skills/."""
    skills = []
    skills_dir = CLAUDE_DIR / "skills"
    if not skills_dir.exists():
        return skills
    for skill_md in sorted(skills_dir.glob("*/SKILL.md")):
        name = skill_md.parent.name
        desc = extract_description(skill_md)
        if len(desc) > 120:
            dot = desc.find(".", 20)
            if 0 < dot < 150:
                desc = desc[:dot + 1]
            else:
                desc = desc[:120] + "..."
        fm = parse_frontmatter(skill_md)
        effort = fm.get("effort", "") if fm else ""
        skills.append({"name": name, "desc": desc, "effort": effort})
    return skills


def scan_commands():
    """Scannt alle Commands aus ~/.claude/commands/."""
    commands = []
    cmd_dir = CLAUDE_DIR / "commands"
    if not cmd_dir.exists():
        return commands
    for cmd_md in sorted(cmd_dir.glob("*.md")):
        name = cmd_md.stem
        desc = extract_description(cmd_md)
        if not desc:
            try:
                text = cmd_md.read_text(encoding="utf-8")
                in_fm = False
                for line in text.split("\n"):
                    stripped = line.strip()
                    if stripped == "---":
                        in_fm = not in_fm
                        continue
                    if in_fm:
                        continue
                    if stripped and not stripped.startswith("#") and not stripped.startswith("allowed") and not stripped.startswith("$"):
                        desc = stripped[:100]
                        break
            except Exception:
                desc = ""
        if len(desc) > 100:
            dot = desc.find(".", 20)
            if 0 < dot < 110:
                desc = desc[:dot + 1]
            else:
                desc = desc[:100] + "..."
        commands.append({"name": name, "desc": desc})
    return commands


def scan_hooks():
    """Liest Hooks aus ~/.claude/settings.json."""
    hooks = []
    for sf in [CLAUDE_DIR / "settings.json", CLAUDE_DIR / "settings.local.json"]:
        if not sf.exists():
            continue
        try:
            data = json.loads(sf.read_text(encoding="utf-8"))
            for event, hlist in data.get("hooks", {}).items():
                for h in hlist:
                    cmd = h.get("command", "")
                    hooks.append({"event": event, "command": cmd[:80]})
        except Exception:
            pass
    return hooks


def scan_rules():
    """Liest alle Rules aus ~/.claude/rules/."""
    rules = []
    rules_dir = CLAUDE_DIR / "rules"
    if not rules_dir.exists():
        return rules
    for f in sorted(rules_dir.glob("*.md")):
        name = f.stem
        try:
            lines = f.read_text(encoding="utf-8").split("\n")
            wc = len(lines)
        except Exception:
            wc = 0
        rules.append({"name": name, "lines": wc})
    return rules


def scan_git_log(vault_path, count=5):
    """Letzte N Commits aus dem Git-Repo."""
    try:
        result = subprocess.run(
            ["git", "log", "--oneline", f"-{count}", "--pretty=format:%h|%s|%ar"],
            cwd=vault_path, capture_output=True, text=True, timeout=5
        )
        commits = []
        for line in result.stdout.strip().split("\n"):
            if "|" in line:
                parts = line.split("|", 2)
                commits.append({"hash": parts[0], "msg": parts[1], "ago": parts[2] if len(parts) > 2 else ""})
        return commits
    except Exception:
        return []


def scan_memory():
    """Zählt Memory-Dateien und liest letzten Hygiene-Check."""
    memory_dirs = list(CLAUDE_DIR.glob("projects/*/memory"))
    total = 0
    last_hygiene = "unbekannt"
    for md in memory_dirs:
        mds = list(md.glob("*.md"))
        total += len([f for f in mds if f.name != "MEMORY.md"])
        index = md / "MEMORY.md"
        if index.exists():
            try:
                text = index.read_text(encoding="utf-8")
                m = re.search(r"last_hygiene_check:\s*(\S+)", text)
                if m:
                    last_hygiene = m.group(1)
            except Exception:
                pass
    return total, last_hygiene


def scan_inbox(vault_path):
    """Zählt Dateien in _inbox/."""
    inbox = vault_path / "_inbox"
    if not inbox.exists():
        return 0
    return len([f for f in inbox.iterdir() if f.is_file() and not f.name.startswith(".")])


def scan_calendar():
    """Liest Kalender-Events heute + morgen + diese Woche via AppleScript."""
    try:
        result = subprocess.run(["osascript", "-e", '''
set today to current date
set hours of today to 0
set minutes of today to 0
set seconds of today to 0
set endDate to today + (8 * days)
tell application "Calendar"
    set output to ""
    repeat with cal in calendars
        try
            set evts to (every event of cal whose start date ≥ today and start date < endDate)
            repeat with evt in evts
                set evtStart to start date of evt
                set evtEnd to end date of evt
                set isAllDay to allday event of evt
                set calName to name of cal
                set output to output & calName & "||" & (summary of evt) & "||" & evtStart & "||" & evtEnd & "||" & isAllDay & linefeed
            end repeat
        end try
    end repeat
    return output
end tell
'''], capture_output=True, text=True, timeout=120)
        events = []
        seen = set()
        skip_cals = {"Geburtstage", "Schweizerische Feiertage", "Siri-Vorschläge", "Geplante Erinnerungen"}
        for line in result.stdout.strip().split("\n"):
            if "||" not in line:
                continue
            parts = line.split("||")
            if len(parts) < 5:
                continue
            cal, title, start_str, end_str, allday = parts[0].strip(), parts[1].strip(), parts[2].strip(), parts[3].strip(), parts[4].strip()
            if cal in skip_cals:
                continue
            # Deduplizierung: gleiche Startzeit + ähnlicher Titel
            dedup_key = f"{start_str[:20]}|{title[:15].lower()}"
            if dedup_key in seen:
                continue
            seen.add(dedup_key)
            # Datum parsen (deutsches macOS Format)
            try:
                # "Montag, 13. April 2026 um 11:18:29" → datetime
                import locale
                for loc in ["de_DE.UTF-8", "de_CH.UTF-8", ""]:
                    try:
                        locale.setlocale(locale.LC_TIME, loc)
                        break
                    except Exception:
                        pass
                start_dt = None
                end_dt = None
                for fmt in ["%A, %d. %B %Y um %H:%M:%S", "%A, %d. %B %Y um %H:%M"]:
                    try:
                        start_dt = datetime.strptime(start_str, fmt)
                        end_dt = datetime.strptime(end_str, fmt)
                        break
                    except ValueError:
                        continue
                if not start_dt:
                    continue
            except Exception:
                continue
            events.append({
                "cal": cal, "title": title,
                "start": start_dt, "end": end_dt,
                "allday": allday.lower() == "true",
                "date": start_dt.date()
            })
        events.sort(key=lambda e: (e["date"], not e["allday"], e["start"]))
        return events
    except Exception:
        return []


def scan_mail():
    """Liest ungelesene Mails via AppleScript."""
    try:
        result = subprocess.run(["osascript", "-e", '''
tell application "Mail"
    set output to ""
    set relevantAccounts to {"fhnw", "gibb", "Kialog", "me", "gmail", "bwz"}
    repeat with accName in relevantAccounts
        try
            set acc to account accName
            set mboxNames to {"Posteingang", "INBOX"}
            repeat with mbName in mboxNames
                try
                    set mb to mailbox mbName of acc
                    set unreadMsgs to (messages of mb whose read status is false)
                    repeat with msg in unreadMsgs
                        set output to output & accName & "||" & (sender of msg) & "||" & (subject of msg) & "||" & (date received of msg) & linefeed
                    end repeat
                end try
            end repeat
        end try
    end repeat
    return output
end tell
'''], capture_output=True, text=True, timeout=30)
        mails = []
        spam_patterns = ["noreply", "no-reply", "marketing@", "newsletter", "stripe.com",
                         "syllaby", "moveXM", "supercard", "draytek", "swisscom", "visana",
                         "coop", "bill.swisscom"]
        account_order = {"fhnw": 0, "gibb": 1, "bwz": 2, "Kialog": 3, "me": 4, "gmail": 5}
        for line in result.stdout.strip().split("\n"):
            if "||" not in line:
                continue
            parts = line.split("||")
            if len(parts) < 4:
                continue
            acc, sender, subject, date_str = parts[0].strip(), parts[1].strip(), parts[2].strip(), parts[3].strip()
            # Spam filtern
            sender_lower = sender.lower()
            if any(sp in sender_lower for sp in spam_patterns):
                continue
            mails.append({"account": acc, "sender": sender, "subject": subject, "date": date_str})
        mails.sort(key=lambda m: account_order.get(m["account"], 9))
        return mails
    except Exception:
        return []


# MCP-Server (Cloud-managed via claude.ai, statisch erfasst)
MCP_SERVERS = [
    {"name": "ElevenLabs", "desc": "TTS, Voice Clone, Music"},
    {"name": "Gemini", "desc": "Bild-Generierung"},
    {"name": "Consensus", "desc": "Akademische Paper-Suche"},
    {"name": "Excalidraw", "desc": "Diagramme"},
    {"name": "Figma", "desc": "Design + Code Connect"},
    {"name": "Gmail", "desc": "Mails lesen + Entwürfe"},
    {"name": "Google Calendar", "desc": "Termine verwalten"},
    {"name": "Netlify", "desc": "Deploy + Projekte"},
    {"name": "computer-use", "desc": "Desktop-Steuerung"},
    {"name": "context7", "desc": "Library-Dokumentation"},
    {"name": "Lighthouse", "desc": "Performance-Audits"},
    {"name": "NotebookLM", "desc": "Notebooks + Fragen"},
    {"name": "Stitch", "desc": "Design-Systeme (Google)"},
    {"name": "tldraw", "desc": "Canvas-Editor"},
    {"name": "Scholar Gateway", "desc": "Semantische Suche"},
]

PLUGINS = [
    {"name": "pr-review-toolkit", "desc": "6 spezialisierte Review-Agenten"},
    {"name": "codex", "desc": "GPT-5.4 Gegenprüfung"},
    {"name": "frontend-design", "desc": "Design-qualitative Interfaces"},
    {"name": "code-review", "desc": "PR Code-Review"},
    {"name": "security-guidance", "desc": "Security Best Practices"},
    {"name": "claude-mem", "desc": "Cross-Session Memory + AST-Suche"},
]


# ── Skill-Kategorien ──
SKILL_CATEGORIES = {
    "Akademisch": ["apa7-checker", "begriffskonsistenz", "design-kohaerenz", "expose-stil", "kanoniker-check", "quellenaudit"],
    "KIalog / Website": ["kialog-copywriter", "website-audit", "hirschi-style", "frontend-design"],
    "Lehre": ["abu-dossier-workflow", "bewertungspipeline", "gibb-abu-lernbegleitung", "ph-fhnw-dozent"],
    "Produktion": ["docx", "pdf", "pptx", "xlsx", "excalidraw-diagram"],
    "Stil & Qualität": ["dozent-stilcheck", "prompt-science", "skill-creator", "skill-improver"],
    "System": ["browser-use", "deep-research", "obsidian-sync", "trinity-load", "experten", "inbox"],
}

# ── Projekt-Gruppen → Tab-Mapping ──
GRUPPE_TO_TAB = {
    "geschaeft": "kialog",
    "lehre": "lehre",
    "forschung": "forschung",
    "kreativ": "privat",
    "privat": "privat",
    "meta": "system",
}

LEHRE_SUB = {
    "03-PH FHNW": ("PH FHNW", "#3881F1"),
    "11-gibb": ("gibb Bern", "#22D3EE"),
    "04-BWZ": ("BWZ Lyss", "#A78BFA"),
}

TAB_ORDER = ["kialog", "lehre", "forschung", "privat", "system"]
TAB_LABELS = {"kialog": "KIalog", "lehre": "Lehre", "forschung": "Forschung", "privat": "Privat", "system": "System"}


def esc(s):
    """HTML-Escaping für &."""
    return s.replace("&", "&amp;")


def deadline_group_label(dl, today):
    """Bestimmt Gruppenname für eine Deadline basierend auf Datum."""
    days = (dl - today).days
    # Wochenstart = Montag dieser Woche
    week_start = today.toordinal() - today.weekday()
    dl_week_start = dl.toordinal() - dl.weekday()

    if dl_week_start == week_start:
        # Montag der aktuellen Woche ermitteln
        from datetime import timedelta
        mon = today - timedelta(days=today.weekday())
        sun = mon + timedelta(days=6)
        return f"Diese Woche ({mon.strftime('%d.')}–{sun.strftime('%d. %B')})"
    elif dl.month == today.month and dl.year == today.year:
        return f"Ende {dl.strftime('%B')}"
    else:
        return dl.strftime("%B") + (" +" if dl.month > today.month + 1 or dl.year > today.year else "")


def main():
    now = datetime.now()
    today = date.today()

    # Daten scannen
    skills = scan_skills()
    commands = scan_commands()
    hooks = scan_hooks()
    rules = scan_rules()
    git_commits = scan_git_log(VAULT)
    memory_count, last_hygiene = scan_memory()
    inbox_count = scan_inbox(VAULT)
    cal_events = scan_calendar()
    unread_mails = scan_mail()

    # Projekte laden
    projects = []
    for claude_path in sorted(VAULT.rglob("CLAUDE.md")):
        rel = claude_path.relative_to(VAULT)
        if "_archiv" in str(rel) or "ARCHIV" in str(rel) or ".claude" in str(rel):
            continue
        fm = parse_frontmatter(claude_path)
        if not fm or fm.get("status") != "aktiv":
            continue
        name = str(rel.parent) if str(rel.parent) != "." else "Vault Root"
        name = name.split("/")[-1]
        projects.append({
            "name": name,
            "path": str(rel),
            "gruppe": fm.get("gruppe", ""),
            "prio": fm.get("prio", ""),
            "next": fm.get("next", ""),
            "deadline": fm.get("deadline", ""),
            "waiting": find_waiting(claude_path),
        })

    deadlines = sorted([p for p in projects if p["deadline"]], key=lambda p: p["deadline"])
    high_prio = [p for p in projects if p["prio"] == "high"]
    waiting_all = []
    for p in projects:
        for w in p["waiting"]:
            waiting_all.append({"project": p["name"], "text": w})

    # Trading Config
    mk_config_path = VAULT / "02-M&K Trading Playbook" / "mk-config.json"
    try:
        mk_config = json.loads(mk_config_path.read_text(encoding="utf-8"))
        hl_wallet = mk_config.get("hyperliquid_address", "")
        short_entry = mk_config.get("short", {}).get("entry", 0)
        short_lp = mk_config.get("short", {}).get("lp", 0)
        kern_flash = mk_config.get("indikatoren", {}).get("kern_flash", 0)
        kern_total = mk_config.get("indikatoren", {}).get("kern_total", 0)
        sek_flash = mk_config.get("indikatoren", {}).get("sek_flash", 0)
        sek_total = mk_config.get("indikatoren", {}).get("sek_total", 0)
        phase_desc = mk_config.get("phase_beschreibung", "")
        next_action = mk_config.get("naechste_aktion", "")
        config_stand = mk_config.get("stand", "")
    except Exception:
        hl_wallet = short_entry = short_lp = 0
        kern_flash = sek_flash = kern_total = sek_total = 0
        phase_desc = next_action = config_stand = ""

    # ════════════════════════════════════════
    # HTML zusammenbauen
    # ════════════════════════════════════════

    css = """
  @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Inter:wght@300;400;500&family=JetBrains+Mono:wght@300;400&display=swap');
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body { font-family: 'Inter', sans-serif; background: #1A1916; color: #EAE7DF; padding: 2rem; max-width: 1200px; margin: 0 auto; }
  h1 { font-family: 'Space Grotesk', sans-serif; font-weight: 300; font-size: 2.5rem; color: #BEFF00; margin-bottom: 0.25rem; }
  .subtitle { color: #B5B0A5; font-size: 0.85rem; margin-bottom: 1.5rem; font-family: 'JetBrains Mono', monospace; }

  .stats-bar { display: flex; gap: 1.5rem; margin-bottom: 2rem; flex-wrap: wrap; }
  .stat { text-align: center; }
  .count { font-family: 'Space Grotesk', sans-serif; font-size: 1.8rem; font-weight: 700; color: #BEFF00; }
  .count-label { color: #6B7280; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.05em; }

  .main-tabs { display: flex; gap: 0; margin-bottom: 2rem; border-bottom: 2px solid #333; }
  .main-tab { font-family: 'Space Grotesk', sans-serif; font-weight: 500; font-size: 0.95rem; color: #6B7280; padding: 0.75rem 1.5rem; cursor: pointer; border-bottom: 2px solid transparent; margin-bottom: -2px; transition: color 0.2s, border-color 0.2s; user-select: none; }
  .main-tab:hover { color: #B5B0A5; }
  .main-tab.active { color: #BEFF00; border-bottom-color: #BEFF00; }
  .tab-panel { display: none; }
  .tab-panel.active { display: block; }

  .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin-bottom: 2rem; }
  .card { background: #222019; border-radius: 12px; padding: 1.5rem; border: 1px solid #333; }
  .card-full { grid-column: 1 / -1; }
  .card h2 { font-family: 'Space Grotesk', sans-serif; font-weight: 500; color: #BEFF00; margin-bottom: 1rem; text-transform: uppercase; letter-spacing: 0.05em; font-size: 0.85rem; }
  .card h3 { font-family: 'Space Grotesk', sans-serif; font-weight: 400; color: #B5B0A5; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.08em; margin-top: 1.25rem; margin-bottom: 0.5rem; padding-top: 0.75rem; border-top: 1px solid #2a2a25; }
  .card h3:first-of-type { margin-top: 0; padding-top: 0; border-top: none; }

  .deadline-row { display: flex; align-items: center; padding: 0.55rem 0; border-bottom: 1px solid #2a2a25; gap: 0.75rem; }
  .deadline-row:last-child { border-bottom: none; }
  .deadline-dot { width: 8px; height: 8px; border-radius: 50%; flex-shrink: 0; }
  .dot-red { background: #EF4444; } .dot-orange { background: #F59E0B; } .dot-yellow { background: #EAB308; } .dot-green { background: #22C55E; }
  .deadline-date { font-family: 'JetBrains Mono', monospace; font-size: 0.78rem; color: #6B7280; width: 55px; flex-shrink: 0; }
  .deadline-badge { font-family: 'JetBrains Mono', monospace; font-size: 0.7rem; font-weight: 600; padding: 0.15rem 0.5rem; border-radius: 4px; width: 80px; text-align: center; flex-shrink: 0; }
  .badge-urgent { background: #EF444420; color: #EF4444; } .badge-soon { background: #F59E0B20; color: #F59E0B; } .badge-later { background: #22C55E20; color: #22C55E; }
  .deadline-name { font-weight: 500; color: #EAE7DF; min-width: 200px; width: 200px; flex-shrink: 0; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
  .deadline-next { color: #6B7280; font-size: 0.83rem; flex: 1; min-width: 0; }

  .fokus-row { display: flex; align-items: center; padding: 0.75rem 0; border-bottom: 1px solid #2a2a25; gap: 1rem; }
  .fokus-row:last-child { border-bottom: none; }
  .fokus-name { font-weight: 600; color: #EAE7DF; min-width: 210px; width: 210px; flex-shrink: 0; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
  .fokus-next { color: #B5B0A5; font-size: 0.85rem; flex: 1; }

  .waiting-row { display: flex; padding: 0.45rem 0; border-bottom: 1px solid #2a2a25; gap: 0.75rem; align-items: baseline; }
  .waiting-row:last-child { border-bottom: none; }
  .waiting-project { color: #BEFF00; font-size: 0.78rem; font-family: 'JetBrains Mono', monospace; min-width: 160px; width: 160px; flex-shrink: 0; }
  .waiting-text { color: #6B7280; font-size: 0.83rem; flex: 1; }

  .projekt-tabs { display: flex; gap: 0; margin-bottom: 1rem; border-bottom: 1px solid #333; flex-wrap: wrap; }
  .projekt-tab { font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; color: #6B7280; padding: 0.5rem 0.8rem; cursor: pointer; border-bottom: 2px solid transparent; margin-bottom: -1px; transition: color 0.15s, border-color 0.15s; text-transform: uppercase; letter-spacing: 0.05em; user-select: none; }
  .projekt-tab:hover { color: #B5B0A5; }
  .projekt-tab.active { color: #BEFF00; border-bottom-color: #BEFF00; }
  .projekt-panel { display: none; }
  .projekt-panel.active { display: block; }

  .project-row { display: flex; align-items: center; padding: 0.5rem 0; gap: 0.75rem; }
  .prio-badge { display: inline-block; padding: 0.15rem 0.5rem; border-radius: 4px; font-size: 0.7rem; font-family: 'JetBrains Mono', monospace; font-weight: 500; width: 48px; text-align: center; flex-shrink: 0; }
  .prio-high { background: #EF444420; color: #EF4444; } .prio-mid { background: #F59E0B20; color: #F59E0B; } .prio-low { background: #22C55E20; color: #22C55E; } .prio-ref { background: #6B728020; color: #6B7280; }
  .project-name { width: 210px; min-width: 210px; flex-shrink: 0; font-weight: 500; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
  .project-next { color: #6B7280; font-size: 0.83rem; flex: 1; min-width: 0; }

  .commit-row { padding: 0.35rem 0; font-size: 0.83rem; display: flex; gap: 0.75rem; border-bottom: 1px solid #2a2a25; }
  .commit-row:last-child { border-bottom: none; }
  .commit-hash { font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; color: #BEFF00; flex-shrink: 0; }
  .commit-msg { color: #EAE7DF; flex: 1; }
  .commit-time { color: #6B7280; font-size: 0.72rem; flex-shrink: 0; }

  .tool-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 1.5rem; }
  .tool-category { font-family: 'JetBrains Mono', monospace; font-size: 0.7rem; color: #BEFF00; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 0.5rem; }
  .tool-row { padding: 0.25rem 0; font-size: 0.83rem; }
  .tool-name { color: #EAE7DF; font-weight: 500; }
  .tool-desc { color: #6B7280; font-size: 0.76rem; }
  .cmd-name { color: #BEFF00; font-family: 'JetBrains Mono', monospace; font-size: 0.76rem; }
  .cmd-desc { color: #6B7280; font-size: 0.76rem; }

  .trading-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; }
  .meta-line { font-size: 0.76rem; color: #6B7280; margin-top: 0.75rem; }
  .lehre-sub-label { font-size: 0.75rem; font-family: 'JetBrains Mono', monospace; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 0.5rem; }

  .day-column { flex: 1; min-width: 0; }
  .day-header { font-family: 'Space Grotesk', sans-serif; font-weight: 500; font-size: 0.85rem; color: #BEFF00; padding: 0.5rem 0; border-bottom: 1px solid #333; margin-bottom: 0.5rem; }
  .day-header.today { color: #BEFF00; }
  .day-header.other { color: #B5B0A5; }
  .cal-event { padding: 0.4rem 0.6rem; margin-bottom: 0.35rem; border-radius: 6px; font-size: 0.82rem; border-left: 3px solid; }
  .cal-event.allday { background: #2F5E0020; border-color: #2F5E00; color: #B5B0A5; font-size: 0.78rem; }
  .cal-event.timed { background: #222019; border-color: #BEFF00; }
  .cal-time { font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; color: #6B7280; }
  .cal-title { color: #EAE7DF; }
  .cal-cal { color: #6B7280; font-size: 0.68rem; font-family: 'JetBrains Mono', monospace; }
  .week-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 0.75rem; }

  .mail-row { display: flex; padding: 0.5rem 0; border-bottom: 1px solid #2a2a25; gap: 0.75rem; align-items: baseline; }
  .mail-row:last-child { border-bottom: none; }
  .mail-account { font-family: 'JetBrains Mono', monospace; font-size: 0.68rem; color: #BEFF00; min-width: 50px; flex-shrink: 0; text-transform: uppercase; }
  .mail-sender { color: #EAE7DF; font-weight: 500; font-size: 0.83rem; min-width: 180px; max-width: 180px; flex-shrink: 0; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
  .mail-subject { color: #6B7280; font-size: 0.83rem; flex: 1; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
  .mail-date { color: #6B7280; font-size: 0.72rem; font-family: 'JetBrains Mono', monospace; flex-shrink: 0; }

  .empty-state { color: #6B7280; padding: 0.5rem 0; font-size: 0.85rem; }
"""

    h = []
    h.append(f'<!DOCTYPE html>\n<html lang="de">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n<title>COWORK Dashboard</title>\n<style>{css}</style>\n</head>\n<body>\n')

    # Header + Stats
    h.append(f'<h1>COWORK</h1>\n<p class="subtitle">Stand {now.strftime("%d.%m.%Y %H:%M")} &mdash; automatisch generiert bei /start</p>\n')
    h.append('<div class="stats-bar">\n')
    for val, label in [(len(deadlines), "Deadlines"), (len(high_prio), "High Prio"), (len(waiting_all), "Wartend"), (len(projects), "Aktiv"), (memory_count, "Memories"), (inbox_count, "Inbox")]:
        h.append(f'  <div class="stat"><div class="count">{val}</div><div class="count-label">{label}</div></div>\n')
    h.append('</div>\n')

    # Main Tabs
    h.append('<div class="main-tabs">\n')
    h.append('  <div class="main-tab active" data-tab="heute">Heute</div>\n')
    h.append('  <div class="main-tab" data-tab="arbeit">Arbeit</div>\n')
    h.append('  <div class="main-tab" data-tab="tooling">Tooling</div>\n')
    h.append('  <div class="main-tab" data-tab="architektur">Architektur</div>\n')
    h.append('  <div class="main-tab" data-tab="trading">Trading</div>\n')
    h.append('</div>\n')

    # ═══════════ TAB: HEUTE ═══════════
    h.append('<div id="tab-heute" class="tab-panel active">\n<div class="grid">\n')

    # Wochenkalender
    h.append('  <div class="card card-full">\n    <h2>Woche</h2>\n')
    h.append('    <div class="week-grid">\n')
    from datetime import timedelta
    week_start = today - timedelta(days=today.weekday())
    day_names = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
    for d in range(7):
        day = week_start + timedelta(days=d)
        day_label = f"{day_names[d]} {day.strftime('%d.')}"
        is_today = day == today
        header_class = "today" if is_today else "other"
        day_events = [e for e in cal_events if e["date"] == day]
        h.append(f'      <div class="day-column">\n')
        h.append(f'        <div class="day-header {header_class}">{"→ " if is_today else ""}{day_label}</div>\n')
        if day_events:
            for evt in day_events:
                if evt["allday"]:
                    h.append(f'        <div class="cal-event allday">{esc(evt["title"])}</div>\n')
                else:
                    time_str = evt["start"].strftime("%H:%M")
                    end_str = evt["end"].strftime("%H:%M")
                    h.append(f'        <div class="cal-event timed"><span class="cal-time">{time_str}–{end_str}</span> <span class="cal-title">{esc(evt["title"])}</span></div>\n')
        else:
            h.append(f'        <div class="empty-state">—</div>\n')
        h.append(f'      </div>\n')
    h.append('    </div>\n  </div>\n')

    # Posteingang
    h.append(f'  <div class="card card-full">\n    <h2>Posteingang ({len(unread_mails)} ungelesen)</h2>\n')
    if unread_mails:
        for m in unread_mails:
            # Sender kürzen (nur Name, nicht Email)
            sender_short = m["sender"]
            if "<" in sender_short:
                sender_short = sender_short.split("<")[0].strip().strip('"')
            # Datum kürzen
            date_short = m["date"]
            if "um" in date_short:
                date_short = date_short.split("um")[1].strip()[:5]
            h.append(f'    <div class="mail-row">\n')
            h.append(f'      <div class="mail-account">{m["account"]}</div>\n')
            h.append(f'      <div class="mail-sender">{esc(sender_short)}</div>\n')
            h.append(f'      <div class="mail-subject">{esc(m["subject"])}</div>\n')
            h.append(f'      <div class="mail-date">{esc(date_short)}</div>\n')
            h.append(f'    </div>\n')
    else:
        h.append('    <div class="empty-state">Keine ungelesenen Mails.</div>\n')
    h.append('  </div>\n')

    # Deadlines diese Woche (Kurzversion für Heute-Tab)
    week_deadlines = []
    for p in deadlines:
        try:
            dl = date.fromisoformat(p["deadline"])
            days_left = (dl - today).days
            if days_left <= 14:
                week_deadlines.append((dl, days_left, p))
        except Exception:
            pass

    h.append('  <div class="card card-full">\n    <h2>Deadlines</h2>\n')
    if week_deadlines:
        for dl, days_left, p in week_deadlines:
            if days_left < 0:
                badge, badge_class = "ÜBERFÄLLIG", "badge-urgent"
            elif days_left == 0:
                badge, badge_class = "HEUTE", "badge-urgent"
            elif days_left == 1:
                badge, badge_class = "MORGEN", "badge-urgent"
            elif days_left <= 7:
                badge, badge_class = f"in {days_left}d", "badge-soon"
            else:
                badge, badge_class = f"in {days_left}d", "badge-later"
            h.append(f'    <div class="fokus-row">\n')
            h.append(f'      <div class="deadline-badge {badge_class}">{badge}</div>\n')
            h.append(f'      <div class="deadline-date">{dl.strftime("%d.%m.")}</div>\n')
            h.append(f'      <div class="fokus-name">{esc(p["name"])}</div>\n')
            h.append(f'      <div class="fokus-next">{esc(p["next"])}</div>\n')
            h.append(f'    </div>\n')
    else:
        h.append('    <div class="empty-state">Keine Deadlines in den nächsten 14 Tagen.</div>\n')
    h.append('  </div>\n')

    h.append('</div>\n</div>\n')  # grid + tab-heute

    # ═══════════ TAB: ARBEIT ═══════════
    h.append('<div id="tab-arbeit" class="tab-panel">\n<div class="grid">\n')

    # Fokus (nächste 7 Tage)
    h.append('  <div class="card card-full">\n    <h2>Fokus &mdash; Diese Woche</h2>\n')
    focus_items = []
    for p in deadlines:
        try:
            dl = date.fromisoformat(p["deadline"])
            days = (dl - today).days
            if days <= 7:
                if days < 0:
                    label, badge = "ÜBERFÄLLIG", "badge-urgent"
                elif days == 0:
                    label, badge = "HEUTE", "badge-urgent"
                elif days == 1:
                    label, badge = "MORGEN", "badge-urgent"
                elif days <= 3:
                    label, badge = f"in {days}d", "badge-soon"
                else:
                    label, badge = f"in {days}d", "badge-soon"
                focus_items.append((dl, label, badge, p))
        except Exception:
            pass

    if focus_items:
        for dl, label, badge, p in focus_items:
            h.append(f'    <div class="fokus-row">\n')
            h.append(f'      <div class="deadline-badge {badge}">{label}</div>\n')
            h.append(f'      <div class="deadline-date">{dl.strftime("%d.%m.")}</div>\n')
            h.append(f'      <div class="fokus-name">{esc(p["name"])}</div>\n')
            h.append(f'      <div class="fokus-next">{esc(p["next"])}</div>\n')
            h.append(f'    </div>\n')
    else:
        h.append('    <div style="color: #22C55E; padding: 0.5rem 0;">Keine Deadlines in den nächsten 7 Tagen.</div>\n')
    h.append('  </div>\n')

    # Wartend + Commits nebeneinander
    h.append('  <div class="card">\n    <h2>Wartend auf</h2>\n')
    if waiting_all:
        for w in waiting_all:
            h.append(f'    <div class="waiting-row"><div class="waiting-project">{esc(w["project"])}</div><div class="waiting-text">{esc(w["text"])}</div></div>\n')
    else:
        h.append('    <div style="color: #6B7280;">Nichts blockiert.</div>\n')
    h.append('  </div>\n')

    h.append('  <div class="card">\n    <h2>Letzte Commits</h2>\n')
    if git_commits:
        for c in git_commits:
            msg_short = c["msg"][:60] + "..." if len(c["msg"]) > 60 else c["msg"]
            h.append(f'    <div class="commit-row"><span class="commit-hash">{c["hash"]}</span><span class="commit-msg">{esc(msg_short)}</span><span class="commit-time">{c["ago"]}</span></div>\n')
    else:
        h.append('    <div style="color: #6B7280;">Keine Commits.</div>\n')
    h.append('  </div>\n')

    # Alle Deadlines gruppiert
    h.append('  <div class="card card-full">\n    <h2>Alle Deadlines</h2>\n')
    current_group = None
    for p in deadlines:
        try:
            dl = date.fromisoformat(p["deadline"])
            days = (dl - today).days
        except Exception:
            dl = None
            days = 999

        # Dot-Farbe
        if days < 0:
            dot = "dot-red"
        elif days <= 3:
            dot = "dot-red"
        elif days <= 7:
            dot = "dot-orange"
        elif days <= 14:
            dot = "dot-yellow"
        else:
            dot = "dot-green"

        # Gruppierung
        if dl:
            group = deadline_group_label(dl, today)
            date_str = dl.strftime("%d.%m.")
        else:
            group = "Sonstige"
            date_str = p["deadline"]

        if group != current_group:
            current_group = group
            h.append(f'    <h3>{group}</h3>\n')

        h.append(f'    <div class="deadline-row">\n')
        h.append(f'      <div class="deadline-dot {dot}"></div>\n')
        h.append(f'      <div class="deadline-date">{date_str}</div>\n')
        h.append(f'      <div class="deadline-name">{esc(p["name"])}</div>\n')
        h.append(f'      <div class="deadline-next">{esc(p["next"])}</div>\n')
        h.append(f'    </div>\n')
    h.append('  </div>\n')

    # Projekte mit Sub-Tabs
    h.append('  <div class="card card-full">\n    <h2>Projekte</h2>\n')
    h.append('    <div class="projekt-tabs">\n')
    first_tab = True
    for tab_id in TAB_ORDER:
        active = " active" if first_tab else ""
        h.append(f'      <div class="projekt-tab{active}" data-ptab="{tab_id}">{TAB_LABELS[tab_id]}</div>\n')
        first_tab = False
    h.append('    </div>\n')

    # Projekte pro Tab
    tab_projects = {t: [] for t in TAB_ORDER}
    for p in projects:
        tab = GRUPPE_TO_TAB.get(p["gruppe"], "system")
        tab_projects[tab].append(p)

    first_panel = True
    for tab_id in TAB_ORDER:
        active = " active" if first_panel else ""
        first_panel = False
        items = tab_projects[tab_id]
        items.sort(key=lambda p: {"high": 0, "mid": 1, "low": 2, "ref": 3}.get(p["prio"], 4))

        h.append(f'    <div id="ptab-{tab_id}" class="projekt-panel{active}">\n')

        if tab_id == "lehre":
            # Sub-Gruppen nach Institution
            sub_groups = {}
            for p in items:
                matched = False
                for prefix, (sub_label, sub_color) in LEHRE_SUB.items():
                    if p["path"].startswith(prefix):
                        if sub_label not in sub_groups:
                            sub_groups[sub_label] = {"color": sub_color, "items": []}
                        sub_groups[sub_label]["items"].append(p)
                        matched = True
                        break
                if not matched:
                    if "Andere" not in sub_groups:
                        sub_groups["Andere"] = {"color": "#6B7280", "items": []}
                    sub_groups["Andere"]["items"].append(p)

            for sub_label, sub_data in sub_groups.items():
                sub_data["items"].sort(key=lambda p: {"high": 0, "mid": 1, "low": 2, "ref": 3}.get(p["prio"], 4))
                h.append(f'      <div class="lehre-sub-label" style="color: {sub_data["color"]}; margin-top: 0.75rem;">{sub_label}</div>\n')
                for p in sub_data["items"]:
                    prio_class = f"prio-{p['prio']}" if p["prio"] in ("high", "mid", "low", "ref") else "prio-ref"
                    h.append(f'      <div class="project-row"><span class="prio-badge {prio_class}">{p["prio"]}</span><span class="project-name">{esc(p["name"])}</span><span class="project-next">{esc(p["next"])}</span></div>\n')
        else:
            for p in items:
                prio_class = f"prio-{p['prio']}" if p["prio"] in ("high", "mid", "low", "ref") else "prio-ref"
                h.append(f'      <div class="project-row"><span class="prio-badge {prio_class}">{p["prio"]}</span><span class="project-name">{esc(p["name"])}</span><span class="project-next">{esc(p["next"])}</span></div>\n')

        h.append('    </div>\n')

    h.append('  </div>\n')  # card
    h.append('</div>\n</div>\n')  # grid + tab-arbeit

    # ═══════════ TAB: TOOLING ═══════════
    h.append('<div id="tab-tooling" class="tab-panel">\n<div class="grid">\n')

    # Skills
    skill_map = {s["name"]: s for s in skills}
    h.append(f'  <div class="card card-full">\n    <h2>Skills ({len(skills)})</h2>\n    <div class="tool-grid">\n')
    categorized = set()
    for cat_name, cat_skills in SKILL_CATEGORIES.items():
        categorized.update(cat_skills)
        h.append(f'      <div>\n        <div class="tool-category">{cat_name}</div>\n')
        for sname in cat_skills:
            s = skill_map.get(sname, {"name": sname, "desc": ""})
            desc_short = s["desc"][:60] + "..." if len(s.get("desc", "")) > 60 else s.get("desc", "")
            h.append(f'        <div class="tool-row"><span class="tool-name">{s["name"]}</span>')
            if desc_short:
                h.append(f' <span class="tool-desc">&mdash; {esc(desc_short)}</span>')
            h.append('</div>\n')
        h.append('      </div>\n')

    uncategorized = [s for s in skills if s["name"] not in categorized]
    if uncategorized:
        h.append('      <div>\n        <div class="tool-category">Andere</div>\n')
        for s in uncategorized:
            h.append(f'        <div class="tool-row"><span class="tool-name">{s["name"]}</span></div>\n')
        h.append('      </div>\n')
    h.append('    </div>\n  </div>\n')

    # Commands
    h.append(f'  <div class="card">\n    <h2>Commands ({len(commands)})</h2>\n')
    for c in commands:
        desc_short = c["desc"][:50] + "..." if len(c["desc"]) > 50 else c["desc"]
        h.append(f'    <div class="tool-row"><span class="cmd-name">/{c["name"]}</span>')
        if desc_short:
            h.append(f' <span class="cmd-desc">&mdash; {esc(desc_short)}</span>')
        h.append('</div>\n')
    h.append('  </div>\n')

    # Plugins + Hooks + Rules
    h.append('  <div class="card">\n    <h2>Plugins &amp; Infrastruktur</h2>\n')
    h.append(f'    <div class="tool-category" style="margin-top: 0;">Plugins ({len(PLUGINS)})</div>\n')
    for p in PLUGINS:
        h.append(f'    <div class="tool-row"><span class="tool-name">{p["name"]}</span> <span class="tool-desc">&mdash; {esc(p["desc"])}</span></div>\n')
    h.append(f'    <div class="tool-category" style="margin-top: 1rem;">Hooks ({len(hooks)})</div>\n')
    for hk in hooks:
        h.append(f'    <div class="tool-row"><span class="tool-name">{hk["event"]}</span> <span class="tool-desc">&mdash; {esc(hk["command"][:40])}</span></div>\n')
    if not hooks:
        h.append('    <div style="color: #6B7280;">Keine Hooks.</div>\n')
    total_lines = sum(r["lines"] for r in rules)
    h.append(f'    <div class="tool-category" style="margin-top: 1rem;">Rules ({len(rules)} Dateien, {total_lines} Zeilen)</div>\n')
    for r in rules:
        h.append(f'    <div class="tool-row"><span class="tool-name">{r["name"]}.md</span> <span class="tool-desc">({r["lines"]})</span></div>\n')
    h.append('  </div>\n')

    # MCP-Server
    h.append(f'  <div class="card card-full">\n    <h2>MCP-Server ({len(MCP_SERVERS)})</h2>\n')
    h.append('    <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 0.25rem 2rem;">\n')
    for m in MCP_SERVERS:
        h.append(f'    <div class="tool-row"><span class="tool-name">{m["name"]}</span> <span class="tool-desc">&mdash; {esc(m["desc"])}</span></div>\n')
    h.append('    </div>\n  </div>\n')
    h.append('</div>\n</div>\n')  # grid + tab-tooling

    # ═══════════ TAB: ARCHITEKTUR ═══════════
    h.append('<div id="tab-architektur" class="tab-panel">\n<div class="grid">\n')

    # Wissens-Pipeline
    h.append("""  <div class="card card-full">
    <h2>Wissens-Pipeline</h2>
    <div style="font-family: monospace; font-size: 0.85rem; line-height: 2; padding: 1rem; background: #111; border-radius: 8px;">
      <span style="color: #BEFF00;">Input</span> (YouTube, Paper, Link, Idee)<br>
      &nbsp;&nbsp;&nbsp;&nbsp;&#x2502;<br>
      &nbsp;&nbsp;&nbsp;&nbsp;&#x25BC;<br>
      <span style="color: #BEFF00;">INBOX</span> &mdash; &laquo;Wissen oder Aufgabe?&raquo;<br>
      &nbsp;&nbsp;&nbsp;&nbsp;&#x2502;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&#x2502;<br>
      &nbsp;&nbsp;&nbsp;&nbsp;&#x2502; Aufgabe&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&#x2502; Wissen<br>
      &nbsp;&nbsp;&nbsp;&nbsp;&#x25BC;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&#x25BC;<br>
      <span style="color: #6B7280;">Projektordner</span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #BEFF00;">ZOTERO</span> (PDF + Metadaten)<br>
      <span style="color: #6B7280;">(COWORK)</span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&#x2502;<br>
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&#x25BC;<br>
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #BEFF00;">WIKI-LLM</span> (Konzepte vernetzen)<br>
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&#x2502;<br>
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&#x25BC;<br>
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #BEFF00;">NOTEBOOKLM</span> (Experten f&uuml;ttern)
    </div>
  </div>
""")

    # 5 Systeme
    h.append("""  <div class="card card-full">
    <h2>5 Systeme &mdash; klare Rollen</h2>
    <table style="width: 100%; border-collapse: collapse; font-size: 0.85rem;">
      <thead><tr style="border-bottom: 1px solid #333; color: #BEFF00;">
        <th style="text-align: left; padding: 0.5rem;">System</th>
        <th style="text-align: left; padding: 0.5rem;">Rolle</th>
        <th style="text-align: left; padding: 0.5rem;">Metapher</th>
      </tr></thead>
      <tbody>
        <tr style="border-bottom: 1px solid #222;"><td style="padding: 0.4rem; color: #BEFF00;">COWORK</td><td style="padding: 0.4rem;">Arbeitsplatz &mdash; Projekte, Deadlines, Material</td><td style="padding: 0.4rem; color: #6B7280;">Schreibtisch</td></tr>
        <tr style="border-bottom: 1px solid #222;"><td style="padding: 0.4rem; color: #BEFF00;">Zotero</td><td style="padding: 0.4rem;">Quellenregister &mdash; PDF, Metadaten, BibTeX</td><td style="padding: 0.4rem; color: #6B7280;">Bibliothekskatalog</td></tr>
        <tr style="border-bottom: 1px solid #222;"><td style="padding: 0.4rem; color: #BEFF00;">Wiki-LLM</td><td style="padding: 0.4rem;">Verstandenes Wissen &mdash; Konzeptseiten mit Quellen</td><td style="padding: 0.4rem; color: #6B7280;">Eigenes Lehrbuch</td></tr>
        <tr style="border-bottom: 1px solid #222;"><td style="padding: 0.4rem; color: #BEFF00;">NotebookLM</td><td style="padding: 0.4rem;">Befragbare Korpora &mdash; quellenbasierte Antworten</td><td style="padding: 0.4rem; color: #6B7280;">Fachgespr&auml;ch</td></tr>
        <tr><td style="padding: 0.4rem; color: #BEFF00;">Inbox</td><td style="padding: 0.4rem;">Eingang &mdash; alles Neue, nichts bleibt hier</td><td style="padding: 0.4rem; color: #6B7280;">Briefkasten</td></tr>
      </tbody>
    </table>
    <p style="margin-top: 1rem; color: #6B7280; font-size: 0.8rem;">Zotero weiss, DASS du eine Quelle hast. Wiki-LLM weiss, WAS drinsteht. NotebookLM kann ANTWORTEN darauf geben.</p>
  </div>
""")

    # Wiki-LLM Aufnahmekriterium
    h.append("""  <div class="card">
    <h2>Wiki-LLM &mdash; was geh&ouml;rt rein?</h2>
    <p style="color: #BEFF00; font-size: 0.85rem; margin-bottom: 0.75rem;">Faustregel: W&uuml;rdest du es in einer Fussnote zitieren?</p>
    <div style="font-size: 0.8rem;">
      <div style="color: #22C55E; margin-bottom: 0.25rem;">&#x2713; Peer-reviewed Papers</div>
      <div style="color: #22C55E; margin-bottom: 0.25rem;">&#x2713; Sachb&uuml;cher mit Empirie/Theorie</div>
      <div style="color: #22C55E; margin-bottom: 0.25rem;">&#x2713; Institutionelle Berichte (OECD, SBFI)</div>
      <div style="color: #22C55E; margin-bottom: 0.25rem;">&#x2713; Rahmenwerke, Lehrpl&auml;ne</div>
      <div style="color: #EF4444; margin-top: 0.5rem; margin-bottom: 0.25rem;">&#x2717; YouTube, Blog-Posts, Meinungsartikel</div>
      <div style="color: #EF4444; margin-bottom: 0.25rem;">&#x2717; Popularwissenschaft ohne Empirie</div>
      <div style="color: #EF4444; margin-bottom: 0.25rem;">&#x2717; Tool-Doku, System-Erkenntnisse</div>
    </div>
  </div>
""")

    # 3 Kern-Experten
    h.append("""  <div class="card">
    <h2>NotebookLM &mdash; 3 Kern-Experten</h2>
    <div style="font-size: 0.85rem;">
      <div style="margin-bottom: 0.75rem;">
        <span style="color: #BEFF00; font-weight: 600;">forschung</span><br>
        <span style="color: #9CA3AF;">EJ, KI-Feedback, Assessment, Methodik</span><br>
        <span style="color: #6B7280;">&#x2192; &laquo;Was sagt die Wissenschaft?&raquo;</span>
      </div>
      <div style="margin-bottom: 0.75rem;">
        <span style="color: #BEFF00; font-weight: 600;">praxis</span><br>
        <span style="color: #9CA3AF;">Berufsbildung, LP-Stimmen, ILB, Mentorat</span><br>
        <span style="color: #6B7280;">&#x2192; &laquo;Was erleben Lehrpersonen?&raquo;</span>
      </div>
      <div>
        <span style="color: #BEFF00; font-weight: 600;">kontext</span><br>
        <span style="color: #9CA3AF;">Markt, Recht, F&ouml;rderung, Governance</span><br>
        <span style="color: #6B7280;">&#x2192; &laquo;Was erlaubt/f&ouml;rdert das System?&raquo;</span>
      </div>
    </div>
  </div>
""")

    # Source of Truth
    h.append("""  <div class="card card-full">
    <h2>Source of Truth</h2>
    <table style="width: 100%; border-collapse: collapse; font-size: 0.8rem;">
      <thead><tr style="border-bottom: 1px solid #333; color: #BEFF00;">
        <th style="text-align: left; padding: 0.4rem;">Was</th>
        <th style="text-align: left; padding: 0.4rem;">Kanonische Quelle</th>
        <th style="text-align: left; padding: 0.4rem;">Nicht</th>
      </tr></thead>
      <tbody>
        <tr style="border-bottom: 1px solid #222;"><td style="padding: 0.3rem;">Projektzustand</td><td style="padding: 0.3rem;">Projekt-CLAUDE.md</td><td style="padding: 0.3rem; color: #6B7280;">Memory</td></tr>
        <tr style="border-bottom: 1px solid #222;"><td style="padding: 0.3rem;">Quellenbesitz</td><td style="padding: 0.3rem;">Zotero</td><td style="padding: 0.3rem; color: #6B7280;">Wiki-LLM raw/</td></tr>
        <tr style="border-bottom: 1px solid #222;"><td style="padding: 0.3rem;">Verstandenes Wissen</td><td style="padding: 0.3rem;">Wiki-LLM wiki/</td><td style="padding: 0.3rem; color: #6B7280;">Training, NLM</td></tr>
        <tr style="border-bottom: 1px solid #222;"><td style="padding: 0.3rem;">Quellenbasierte Antworten</td><td style="padding: 0.3rem;">NotebookLM</td><td style="padding: 0.3rem; color: #6B7280;">Claude direkt</td></tr>
        <tr style="border-bottom: 1px solid #222;"><td style="padding: 0.3rem;">Verhaltensregeln</td><td style="padding: 0.3rem;">rules/arbeitsregeln.md</td><td style="padding: 0.3rem; color: #6B7280;">feedback_*.md</td></tr>
        <tr><td style="padding: 0.3rem;">Inventar</td><td style="padding: 0.3rem;">tool-registry.md (auto)</td><td style="padding: 0.3rem; color: #6B7280;">Benutzerhandbuch</td></tr>
      </tbody>
    </table>
  </div>
""")

    # Benutzerhandbuch-Link
    h.append("""  <div class="card card-full" style="text-align: center; padding: 1.5rem;">
    <a href="15-Organisation/Benutzerhandbuch.md" style="color: #BEFF00; text-decoration: none; font-size: 0.9rem;">&#x1F4D6; Benutzerhandbuch &mdash; vollst&auml;ndige Systemdokumentation</a>
  </div>
""")

    h.append('</div>\n</div>\n')  # grid + tab-architektur

    # ═══════════ TAB: TRADING ═══════════
    kern_color = "#22C55E" if kern_flash >= 4 else "#EF4444"
    h.append(f"""<div id="tab-trading" class="tab-panel">
<div class="trading-grid">
  <div class="card">
    <h2>BTC Short</h2>
    <div id="trading-loading" style="color: #6B7280;">Lade Live-Daten...</div>
    <div id="trading-data" style="display: none;">
      <div class="stats-bar">
        <div class="stat"><div class="count" id="btc-price" style="font-size: 1.6rem;">&mdash;</div><div class="count-label">BTC/USD</div></div>
        <div class="stat"><div class="count" id="pnl-value" style="font-size: 1.6rem;">&mdash;</div><div class="count-label">P/L (USD)</div></div>
        <div class="stat"><div class="count" id="roe-value" style="font-size: 1.4rem;">&mdash;</div><div class="count-label">ROE</div></div>
      </div>
      <div style="margin-top: 1rem; display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem; font-size: 0.82rem;">
        <div><span style="color: #6B7280;">Entry:</span> <span style="color: #EAE7DF;">${short_entry:,}</span></div>
        <div><span style="color: #6B7280;">Liquidation:</span> <span style="color: #EF4444;">${short_lp:,}</span></div>
        <div><span style="color: #6B7280;">Size:</span> <span id="pos-size" style="color: #EAE7DF;">&mdash;</span></div>
        <div><span style="color: #6B7280;">Margin:</span> <span id="pos-margin" style="color: #EAE7DF;">&mdash;</span></div>
      </div>
      <div id="lp-distance" class="meta-line"></div>
    </div>
    <div id="trading-error" style="display: none; color: #EF4444; font-size: 0.85rem;"></div>
  </div>
  <div class="card">
    <h2>Zyklus-Status</h2>
    <div style="display: flex; gap: 2rem; margin-bottom: 1rem;">
      <div>
        <div style="font-family: 'Space Grotesk', sans-serif; font-size: 2rem; font-weight: 700; color: {kern_color};">{kern_flash}/{kern_total}</div>
        <div style="color: #6B7280; font-size: 0.8rem;">Kern</div>
      </div>
      <div>
        <div style="font-family: 'Space Grotesk', sans-serif; font-size: 2rem; font-weight: 700; color: #F59E0B;">{sek_flash}/{sek_total}</div>
        <div style="color: #6B7280; font-size: 0.8rem;">Sekundär</div>
      </div>
    </div>
    <div style="font-size: 0.85rem; color: #EAE7DF; margin-bottom: 0.5rem;">{esc(phase_desc)}</div>
    <div style="font-size: 0.8rem; color: #6B7280; line-height: 1.6;">{esc(next_action)}</div>
  </div>
</div>
</div>
""")

    # JavaScript
    h.append(f"""<script>
document.querySelectorAll('.main-tab').forEach(tab => {{
  tab.addEventListener('click', () => {{
    document.querySelectorAll('.main-tab').forEach(t => t.classList.remove('active'));
    document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
    tab.classList.add('active');
    document.getElementById('tab-' + tab.dataset.tab).classList.add('active');
  }});
}});
document.querySelectorAll('.projekt-tab').forEach(tab => {{
  tab.addEventListener('click', () => {{
    document.querySelectorAll('.projekt-tab').forEach(t => t.classList.remove('active'));
    document.querySelectorAll('.projekt-panel').forEach(p => p.classList.remove('active'));
    tab.classList.add('active');
    document.getElementById('ptab-' + tab.dataset.ptab).classList.add('active');
  }});
}});
(async function() {{
  const wallet = "{hl_wallet}";
  const entry = {short_entry};
  const lp = {short_lp};
  if (!wallet) {{ document.getElementById('trading-loading').textContent = 'Keine Wallet konfiguriert.'; return; }}
  try {{
    const priceRes = await fetch('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd');
    const priceData = await priceRes.json();
    const btcPrice = priceData.bitcoin.usd;
    const hlRes = await fetch('https://api.hyperliquid.xyz/info', {{
      method: 'POST', headers: {{ 'Content-Type': 'application/json' }},
      body: JSON.stringify({{ type: 'clearinghouseState', user: wallet }})
    }});
    const hlData = await hlRes.json();
    const btcPos = hlData.assetPositions?.find(p => p.position?.coin === 'BTC');
    const pos = btcPos?.position;
    document.getElementById('btc-price').textContent = '$' + btcPrice.toLocaleString('de-CH');
    if (pos) {{
      const pnl = parseFloat(pos.unrealizedPnl || 0);
      const size = parseFloat(pos.szi || 0);
      const margin = parseFloat(pos.marginUsed || 0);
      const roe = margin > 0 ? (pnl / margin * 100) : 0;
      const lpDist = ((lp - btcPrice) / btcPrice * 100);
      document.getElementById('pnl-value').textContent = (pnl >= 0 ? '+' : '') + '$' + Math.round(pnl).toLocaleString('de-CH');
      document.getElementById('pnl-value').style.color = pnl >= 0 ? '#22C55E' : '#EF4444';
      document.getElementById('roe-value').textContent = (roe >= 0 ? '+' : '') + roe.toFixed(1) + '%';
      document.getElementById('roe-value').style.color = roe >= 0 ? '#22C55E' : '#EF4444';
      document.getElementById('pos-size').textContent = size.toFixed(5) + ' BTC';
      document.getElementById('pos-margin').textContent = '$' + Math.round(margin).toLocaleString('de-CH');
      document.getElementById('lp-distance').textContent = 'LP-Abstand: ' + lpDist.toFixed(1) + '% (' + (lpDist > 30 ? 'sicher' : lpDist > 15 ? 'ok' : 'ACHTUNG') + ')';
      if (lpDist <= 15) document.getElementById('lp-distance').style.color = '#EF4444';
      else if (lpDist <= 30) document.getElementById('lp-distance').style.color = '#F59E0B';
      else document.getElementById('lp-distance').style.color = '#22C55E';
    }} else {{
      document.getElementById('pnl-value').textContent = 'keine Position';
      document.getElementById('pnl-value').style.fontSize = '0.9rem';
    }}
    document.getElementById('trading-loading').style.display = 'none';
    document.getElementById('trading-data').style.display = 'block';
  }} catch (e) {{
    document.getElementById('trading-loading').style.display = 'none';
    document.getElementById('trading-error').style.display = 'block';
    document.getElementById('trading-error').textContent = 'API-Fehler: ' + e.message;
  }}
}})();
</script>
</body>
</html>
""")

    OUTPUT.write_text("".join(h), encoding="utf-8")
    print(f"Dashboard generiert: {OUTPUT}")
    print(f"  {len(projects)} Projekte, {len(deadlines)} Deadlines, {len(waiting_all)} wartend")


if __name__ == "__main__":
    main()
