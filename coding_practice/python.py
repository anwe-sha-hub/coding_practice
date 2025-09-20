import os

README_FILE = "README.md"
START_TAG = "<!-- AUTO-GENERATED-LIST:START -->"
END_TAG = "<!-- AUTO-GENERATED-LIST:END -->"
PROBLEMS_DIR = "coding_practice"   # lowercase since your folder is lowercase
GITHUB_REPO = "https://github.com/anwe-sha-hub/coding_practice/blob/main"  # adjust if your default branch is not 'main'


def get_solved_problems():
    problems = {}
    if not os.path.exists(PROBLEMS_DIR):
        return problems

    for folder in sorted(os.listdir(PROBLEMS_DIR)):
        folder_path = os.path.join(PROBLEMS_DIR, folder)
        if os.path.isdir(folder_path):
            problems[folder] = sorted(os.listdir(folder_path))
    return problems


def generate_list(problems):
    if not problems:
        return "- No problems solved yet."

    result = []
    for folder, files in problems.items():
        result.append(f"### {folder}")
        for f in files:
            # Create a GitHub link to the file
            file_path = f"{PROBLEMS_DIR}/{folder}/{f}"
            file_url = f"{GITHUB_REPO}/{file_path}"
            result.append(f"- [{f}]({file_url})")
        result.append("")  # extra newline
    return "\n".join(result)


def update_readme(problems):
    with open(README_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    start = content.find(START_TAG) + len(START_TAG)
    end = content.find(END_TAG)

    new_content = (
        content[:start]
        + "\n"
        + generate_list(problems)
        + "\n"
        + content[end:]
    )

    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(new_content)


if __name__ == "__main__":
    problems = get_solved_problems()
    update_readme(problems)
