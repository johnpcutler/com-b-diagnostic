#!/usr/bin/env python3
"""One-off migration: prefixed lens dimension IDs (PC/PHC/S/RM/AM/PO/SO) with dotted notation."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def transform_capability(text: str) -> str:
    text = re.sub(r"^- \*\*1\.", "- **PC.1.", text, flags=re.MULTILINE)
    text = re.sub(r"^- \*\*2\.", "- **PHC.2.", text, flags=re.MULTILINE)
    return text


def transform_motivation(text: str) -> str:
    text = re.sub(r"^- \*\*1\.", "- **RM.1.", text, flags=re.MULTILINE)
    text = re.sub(r"^- \*\*2\.", "- **AM.2.", text, flags=re.MULTILINE)
    return text


def transform_po(text: str) -> str:
    text = re.sub(r"^- \*\*(\d+)\.(\d+)\*\*", r"- **PO.\1.\2**", text, flags=re.MULTILINE)
    return text


def transform_so(text: str) -> str:
    text = re.sub(r"^- \*\*(\d+)\.(\d+)\*\*", r"- **SO.\1.\2**", text, flags=re.MULTILINE)
    return text


def transform_behavior(text: str) -> str:
    text = re.sub(r"\bS([1-7])\.([1-7])\b", r"S.\1.\2", text)
    text = re.sub(r"\bS([1-7])\b", r"S.\1", text)
    return text


def transform_assessment_form(text: str) -> str:
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    zone = "other"
    for line in lines:
        if line.startswith("## B-LENS"):
            zone = "B"
        elif line.startswith("## C-LENS: Psychological"):
            zone = "PC"
        elif line.startswith("## C-LENS: Physical"):
            zone = "PHC"
        elif line.startswith("## O-LENS: Physical"):
            zone = "PO"
        elif line.startswith("## O-LENS: Social"):
            zone = "SO"
        elif line.startswith("## M-LENS: Reflective"):
            zone = "RM"
        elif line.startswith("## M-LENS: Automatic"):
            zone = "AM"
        elif line.startswith("## Cross-lens") or line.startswith("## BCW"):
            zone = "other"

        if zone == "B" and line.startswith("| S") and re.match(r"^\| S[1-7] \|", line.strip()):
            line = re.sub(r"^\| S([1-7]) \|", r"| S.\1 |", line)
        elif zone == "PC" and line.startswith("| 1."):
            line = re.sub(r"^\| 1\.", "| PC.1.", line)
        elif zone == "PHC" and line.startswith("| 2."):
            line = re.sub(r"^\| 2\.", "| PHC.2.", line)
        elif zone == "PO" and line.startswith("|") and re.match(r"^\| \d+\.\d+ \|", line.strip()):
            if not re.match(r"^\| ID \|", line):
                line = re.sub(r"^\| (\d+)\.(\d+) \|", r"| PO.\1.\2 |", line)
        elif zone == "SO" and line.startswith("|") and re.match(r"^\| \d+\.\d+ \|", line.strip()):
            if not re.match(r"^\| ID \|", line):
                line = re.sub(r"^\| (\d+)\.(\d+) \|", r"| SO.\1.\2 |", line)
        elif zone == "RM" and line.startswith("| 1."):
            line = re.sub(r"^\| 1\.", "| RM.1.", line)
        elif zone == "AM" and line.startswith("| 2."):
            line = re.sub(r"^\| 2\.", "| AM.2.", line)

        out.append(line)

    text = "".join(out)
    # Section headings — dotted sub-lens numbers
    text = re.sub(r"^### PC 1\.", "### PC.1.", text, flags=re.MULTILINE)
    text = re.sub(r"^### PHC 2\.", "### PHC.2.", text, flags=re.MULTILINE)
    text = re.sub(r"^### PO (\d) —", r"### PO.\1 —", text, flags=re.MULTILINE)
    text = re.sub(r"^### SO (\d) —", r"### SO.\1 —", text, flags=re.MULTILINE)
    text = re.sub(r"^### RM 1\.", "### RM.1.", text, flags=re.MULTILINE)
    text = re.sub(r"^### AM 2\.", "### AM.2.", text, flags=re.MULTILINE)
    return text


def transform_scenarios_and_guides(text: str) -> str:
    """Citations and digest lines in SKILL, guide, output-template, README."""
    text = re.sub(r"\bS([1-7]):", r"S.\1:", text)
    text = re.sub(r"state\s*=\s*S([1-7])\b", r"state = S.\1", text, flags=re.IGNORECASE)
    text = re.sub(r"\*\*S([1-7])\.([1-7])\*\*", r"**S.\1.\2**", text)
    text = re.sub(r"\bState S([1-7])\b", r"State S.\1", text)
    # Digest / shorthand hyphen codes → dotted
    text = re.sub(r"PO-(\d+\.\d+)", r"PO.\1", text)
    text = re.sub(r"SO-(\d+\.\d+)", r"SO.\1", text)
    text = re.sub(r"PC-(\d+\.\d+\.\d+)", r"PC.\1", text)
    text = re.sub(r"PHC-(\d+\.\d+\.\d+)", r"PHC.\1", text)
    text = re.sub(r"RM-(\d+\.\d+\.\d+)", r"RM.\1", text)
    text = re.sub(r"AM-(\d+\.\d+\.\d+)", r"AM.\1", text)
    # Lens code + bold ID → single bold ID
    text = re.sub(r"\bPC \*\*(1\.\d+\.\d+)\*\*", r"**PC.\1**", text)
    text = re.sub(r"\bPHC \*\*(2\.\d+\.\d+)\*\*", r"**PHC.\1**", text)
    text = re.sub(r"\bRM \*\*(1\.\d+\.\d+)\*\*", r"**RM.\1**", text)
    text = re.sub(r"\bAM \*\*(2\.\d+\.\d+)\*\*", r"**AM.\1**", text)

    def po_chain_repl(m: re.Match[str]) -> str:
        nums = re.findall(r"\d+\.\d+", m.group(1))
        return ", ".join(f"**PO.{n}**" for n in nums)

    text = re.sub(
        r"PO (\*\*\d+\.\d+\*\*(?:, \*\*\d+\.\d+\*\*)*)",
        po_chain_repl,
        text,
    )

    def so_chain_repl(m: re.Match[str]) -> str:
        nums = re.findall(r"\d+\.\d+", m.group(1))
        return ", ".join(f"**SO.{n}**" for n in nums)

    text = re.sub(
        r"SO (\*\*\d+\.\d+\*\*(?:, \*\*\d+\.\d+\*\*)*)",
        so_chain_repl,
        text,
    )
    # Prose: PC 1.2.1 → PC.1.2.1 (avoid double-prefix if already dotted)
    text = re.sub(r"\bPC (1\.\d+\.\d+)\b(?!\.)", r"PC.\1", text)
    text = re.sub(r"\bPHC (2\.\d+\.\d+)\b(?!\.)", r"PHC.\1", text)
    text = re.sub(r"\bRM (1\.\d+\.\d+)\b(?!\.)", r"RM.\1", text)
    text = re.sub(r"\bAM (2\.\d+\.\d+)\b(?!\.)", r"AM.\1", text)
    text = re.sub(r"\bPO (\d+\.\d+)\b(?!\.)", r"PO.\1", text)
    text = re.sub(r"\bSO (\d+\.\d+)\b(?!\.)", r"SO.\1", text)
    return text


def main() -> None:
    lens_dir = ROOT / "references" / "lenses"
    paths = [
        (lens_dir / "capability-lenses.md", transform_capability),
        (lens_dir / "motivation-lenses.md", transform_motivation),
        (lens_dir / "physical-opportunity-lenses.md", transform_po),
        (lens_dir / "social-opportunity-lenses.md", transform_so),
        (lens_dir / "behavior-lenses.md", transform_behavior),
        (ROOT / "assets" / "assessment-form-template.md", transform_assessment_form),
    ]
    for path, fn in paths:
        raw = path.read_text(encoding="utf-8")
        new = fn(raw)
        path.write_text(new, encoding="utf-8")
        print(f"OK {path.relative_to(ROOT)}")

    extra = [
        ROOT / "SKILL.md",
        ROOT / "references" / "flow.md",
        ROOT / "references" / "guide.md",
        ROOT / "assets" / "output-template.md",
        ROOT / "README.md",
    ]
    for path in extra:
        raw = path.read_text(encoding="utf-8")
        new = transform_scenarios_and_guides(raw)
        path.write_text(new, encoding="utf-8")
        print(f"OK {path.relative_to(ROOT)} (guides)")


if __name__ == "__main__":
    main()
