"""
Optional helper: start a new review session by resetting review-output.md
in the CURRENT WORKING DIRECTORY (the user's project).

In plugin form this is optional -- the Stop hook will still prompt Claude to
create review-output.md if it is missing. Run it only if you want a clean slate.

Usage (from your project root):
  python "$CLAUDE_PLUGIN_ROOT/scripts/new-review.py"   (macOS/Linux)
  python "%CLAUDE_PLUGIN_ROOT%\\scripts\\new-review.py" (Windows cmd)
"""

import os
import datetime

REVIEW_OUTPUT = "review-output.md"
PROMPT_FILE = os.path.join("docs", "Prompt.md")

def reset_review_output():
    template = """## Review Result

<!-- Claude saves the review results to this file after completing the review -->
<!-- validate-review.py validates this file -->
"""
    with open(REVIEW_OUTPUT, "w", encoding="utf-8") as f:
        f.write(template)
    print(f"[OK] {REVIEW_OUTPUT} has been reset")

def check_prompt():
    # docs/Prompt.md is an optional, project-specific work order. Only check if present.
    if not os.path.exists(PROMPT_FILE):
        print("[INFO] No docs/Prompt.md found -- skipping (optional). "
              "Just ask Claude to review your code.")
        return

    with open(PROMPT_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    missing = []
    if "(paste file path or code here)" in content:
        missing.append("File/code to review")
    if "(e.g., 3-person team" in content:
        missing.append("Team context")
    if "(e.g., Python / FastAPI" in content:
        missing.append("Language/framework in use")

    if missing:
        print("\n[WARN] docs/Prompt.md still has unfilled placeholders:")
        for item in missing:
            print(f"   - {item}")
    else:
        print("[OK] docs/Prompt.md check passed")

def main():
    print(f"=== Starting new code review session ({datetime.date.today()}) ===\n")
    reset_review_output()
    check_prompt()
    print("\nNext step: ask Claude to review your code (e.g., 'review my code before commit').")

if __name__ == "__main__":
    main()
