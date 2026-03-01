import re
from pathlib import Path

# For all-day DTSTART (00:00 local):
# -PT5H    => previous day 19:00
# -PT2H30M => previous day 21:30
VALARMS = "\n".join(
    [
        "BEGIN:VALARM",
        "ACTION:DISPLAY",
        "DESCRIPTION:Erinnerung",
        "TRIGGER:-PT5H",
        "END:VALARM",
        "BEGIN:VALARM",
        "ACTION:DISPLAY",
        "DESCRIPTION:Erinnerung",
        "TRIGGER:-PT2H30M",
        "END:VALARM",
    ]
)


def unfold_ical(text: str) -> str:
    # Normalize to LF, then unfold per RFC 5545 (continuation lines start with space/tab)
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    return re.sub(r"\n[ \t]", "", text)


def fold_line(line: str, limit: int = 75) -> list[str]:
    # Simple folding (character-count, good enough for typical ASCII .ics)
    if len(line) <= limit:
        return [line]
    out = [line[:limit]]
    rest = line[limit:]
    while rest:
        out.append(" " + rest[: limit - 1])
        rest = rest[limit - 1 :]
    return out


def add_alarms_to_all_day_events(ics_text: str) -> str:
    t = unfold_ical(ics_text)

    def patch_event(m: re.Match) -> str:
        vevent = m.group(0)

        # Only all-day events
        if "DTSTART;VALUE=DATE:" not in vevent:
            return vevent

        # If you want to REPLACE existing alarms instead, remove this check and strip old VALARMs.
        if "BEGIN:VALARM" in vevent:
            return vevent

        return vevent.replace("END:VEVENT", VALARMS + "\nEND:VEVENT")

    t = re.sub(r"BEGIN:VEVENT.*?END:VEVENT", patch_event, t, flags=re.DOTALL)

    # Refold and write with CRLF
    folded_lines = []
    for line in t.split("\n"):
        folded_lines.extend(fold_line(line))
    return "\r\n".join(folded_lines) + "\r\n"


# ---- usage ----
in_path = Path("schaeppelewegfreiburgimbreisgau_2026.ics")
out_path = in_path.with_suffix(".with-2-alarms.ics")

ics_in = in_path.read_text(encoding="utf-8", errors="replace")
ics_out = add_alarms_to_all_day_events(ics_in)
out_path.write_text(ics_out, encoding="utf-8")

print(f"Wrote: {out_path}")
