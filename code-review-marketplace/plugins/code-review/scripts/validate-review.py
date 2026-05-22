"""
Stop hook: Runs automatically when Claude is about to finish a task.
If review-output.md does not meet quality standards, exits with code 1
to prevent Claude from finishing and prompt rework.

Reads review-output.md from the CURRENT WORKING DIRECTORY (the user's project),
not from the plugin directory.

Two modes:
  - normal review: requires the 4-section review format.
  - pre-commit review (marked with '<!-- mode: pre-commit -->' on line 1):
    additionally requires an Understanding Check with exactly 3 questions
    and a Verdict line. (The PASS-before-commit gate is a skill rule.)
"""

import sys
import os
import re

REVIEW_FILE = "review-output.md"
PRECOMMIT_MARKER = "<!-- mode: pre-commit -->"
UNDERSTANDING_HEADING = "## Understanding Check"
VALID_VERDICTS = ("AWAITING_ANSWERS", "PASS", "NEEDS_REVIEW")

def main():
    if not os.path.exists(REVIEW_FILE):
        print(f"[FAIL] {REVIEW_FILE} file not found.")
        print("Save the review results to review-output.md before finishing.")
        sys.exit(1)

    with open(REVIEW_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    errors = []
    is_precommit = PRECOMMIT_MARKER in content

    # The review part is everything before the Understanding Check section.
    review_part = content.split(UNDERSTANDING_HEADING)[0]

    # --- Normal review checks (always run) ---
    required_sections = {
        "Issue Found":           "Each issue is missing an 'Issue Found' section",
        "Why It's a Problem":    "Each issue is missing a 'Why It's a Problem' section -- learning context is required",
        "Questions to Consider": "Each issue is missing a 'Questions to Consider' section -- use questions instead of corrected code",
        "What Was Done Well":    "'What Was Done Well' section is missing -- at least one item is required",
    }
    for keyword, message in required_sections.items():
        if keyword not in review_part:
            errors.append(message)

    # Corrected code written directly (warn if more than 2 code blocks in the review part)
    code_blocks = re.findall(r"```[\s\S]*?```", review_part)
    if len(code_blocks) > 2:
        errors.append(
            f"There are {len(code_blocks)} code blocks in the review. "
            "Make sure corrected code has not been written directly (forbidden pattern)."
        )

    # Issue count: only count ### headers inside the review part (max 3)
    issue_headers = re.findall(r"^### .+", review_part, re.MULTILINE)
    if len(issue_headers) > 3:
        errors.append(
            f"There are {len(issue_headers)} issues. "
            "Per the Constraints, condense to 3 or fewer core issues."
        )

    # --- Pre-commit-only checks ---
    if is_precommit:
        if UNDERSTANDING_HEADING not in content:
            errors.append(
                "Pre-commit mode: missing an '## Understanding Check' section with 3 questions."
            )
        else:
            questions = re.findall(r"^\*\*Q\d+\.", content, re.MULTILINE)
            if len(questions) != 3:
                errors.append(
                    f"Pre-commit mode: Understanding Check must have exactly 3 questions "
                    f"(found {len(questions)}). Format each as '**Q1.**', '**Q2.**', '**Q3.**'."
                )

        verdict_match = re.search(r"Verdict:\s*([A-Z_]+)", content)
        if not verdict_match:
            errors.append(
                "Pre-commit mode: missing a 'Verdict:' line "
                "(AWAITING_ANSWERS / PASS / NEEDS_REVIEW)."
            )
        elif verdict_match.group(1) not in VALID_VERDICTS:
            errors.append(
                f"Pre-commit mode: invalid Verdict '{verdict_match.group(1)}'. "
                f"Use one of: {', '.join(VALID_VERDICTS)}."
            )

    if errors:
        print("[FAIL] Review validation failed -- please address the items below and finish again:\n")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)

    mode = "pre-commit" if is_precommit else "normal"
    print(f"[OK] Review validation passed ({mode} mode) -- all Done When conditions met")
    sys.exit(0)

if __name__ == "__main__":
    main()
