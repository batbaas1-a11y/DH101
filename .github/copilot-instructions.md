# Copilot Instructions for DH101

## Project Overview
This is a **Digital Humanities course portfolio** for DH 101 Spring 2026. Students document critical making projects exploring AI's social, ethical, and cultural implications. The repository combines creative artifacts with reflective writing about AI use, authorship, and ethics.

**Core Purpose:** Balance critical thinking about AI with hands-on experimentation—students make things WITH and ABOUT AI while openly documenting that process.

## Repository Structure

| Folder | Purpose |
|--------|---------|
| `makes/` | Weekly projects: artifacts + process notes (week01–week13, plus comic.md). Templates provided in each file. |
| `reflections/` | Weekly written reflections responding to course prompts (week01–week13). Prompt questions provided in template headers. |
| `pages/` | Static content: about, accessibility statement, AI use philosophy, sustainability statement, markdown guide. |
| `make/` | Pilot/example projects (currently selfie.md with detailed example of AI reflection). |
| `ai-log/` | Individual AI use logs tracking each tool interaction. |
| `assets/` | Images and media supporting makes and reflections. |

## Key Patterns & Conventions

### 1. Attribution & Transparency (Essential)
Every make includes mandatory **Attribution & AI Use** section:
```markdown
## Attribution & AI Use
- Tools used: [name specific tools]
- AI prompts (summary): [what did you ask?]
- What AI generated: [specific outputs]
- What you changed or decided: [your creative choices]
```

**Why:** The course demands radical honesty about AI collaboration. This isn't hiding AI use—it's claiming authorship through deliberate choice and editing.

### 2. Make Template Structure
All weekly makes follow this standard:
1. **The Artifact** - What did you create? (embed images/links/media)
2. **Process Notes** - How? What tools? What decisions?
3. **Reflection** - Connect to weekly prompt (200–300 words typical)
4. **Attribution & AI Use** - Full transparency (see above)

**Example file:** [make/selfie.md](../make/selfie.md) shows mature reflection work—notice how the student analyzes what AI *cannot* capture (complexity, intent, lived experience).

### 3. Markdown Conventions
- **Filenames:** lowercase with hyphens (e.g., `week05.md`, `markdown-guide.md`)
- **Images:** stored in `assets/` subdirectories, linked via relative paths
- **Alt text:** Descriptive (describes what someone misses if image fails to load)
- **Heading order:** No skipping levels (don't jump from # to ###)
- **Line breaks:** Two spaces at end of line for soft breaks

**Reference:** [pages/markdown-guide.md](../pages/markdown-guide.md) contains full formatting guide and weekly reflection template.

### 4. Reflection Prompts (Weekly Themes)
Weeks 1–13 explore distinct AI topics:
- W1: Authorship & making | W2: Humanity & patterns | W3: Authenticity & identity
- W4: Collaboration vs. plagiarism | W5: Ownership & remix | W6: Reading & machines
- W7: Power & geographies | W8: Visibility & networks | W9: Creativity & generation
- W10: Play & narrative | W11: Labor & invisibility | W12: Ecology & ethics | W13: Future visions

**Pattern:** Each reflection pair (make + reflection) tackles the same week's theme from different angles—reflection is analytical, make is creative/experimental.

## Development Workflows

### Updating a Weekly Entry
When a student revises a weekly make or reflection:
1. Keep existing section headers (e.g., "## Attribution & AI Use")
2. Update only the content, not structure
3. Ensure attribution is always present and current
4. Verify relative paths to assets work from the file's location
5. Test markdown rendering in VS Code preview

### Creating New Weeks
Future weeks should follow the established template. Copy structure from [makes/week13.md](../makes/week13.md) or [reflections/week13.md](../reflections/week13.md).

### Adding Assets
- Place images in folder-specific subdirectories: `makes/assets/` or `pages/assets/`
- Link from markdown with relative paths: `../assets/images/filename.png`
- Example: [make/selfie.md](../make/selfie.md) references `assets/selfie.jpg` in its folder

## Critical Values (When Editing)

1. **Transparency over polish.** Show the messy AI interactions, not just polished results.
2. **Critical distance.** Don't celebrate AI—interrogate it. What does it enable? What does it erase?
3. **Authorship through intentionality.** AI is a tool you *actively choose and edit*, not something that replaces your thinking.
4. **Accessibility & inclusion.** Alt text on images. Clear language. Linked references instead of vague mentions.
5. **Evidence, not assertion.** "AI generated [specific output], and I changed [specific detail]"—not "I used AI."

## Common AI Tasks in This Repo

- **Drafting dialogue or text:** Student prompts AI, then edits for voice and accuracy
- **Generating visual layouts:** AI image tools produce initial composition; student refines/reframes
- **Brainstorming prompts:** AI suggests prompt variations; student selects and adapts
- **Explaining concepts:** AI summarizes complex ideas for student reflection

**All outputs must be transparently attributed and thoughtfully revised.**

## Files to Understand the Course Philosophy
- [make/selfie.md](../make/selfie.md) — Exemplary AI reflection + detailed process
- [makes/comic.md](../makes/comic.md) — Comic storytelling with AI collaboration analysis
- [pages/markdown-guide.md](../pages/markdown-guide.md) — Writing standards for this repo
- [pages/how-i-use-ai.md](../pages/how-i-use-ai.md) — Student statement on AI integration approach
