---
name: mad-exam-note-writer
description: Use this skill when creating or refining Mobile Application Development exam notes, GTU-style question paper solutions, Android chapter explanations, or revision material. It defines the formatting, depth, code-example, and quality standards followed for this MAD notes repository.
---

# MAD Exam Note Writer

## Purpose

Use this skill to create clear, exam-oriented notes and solutions for Mobile Application Development, especially Android topics.

The output should help a student prepare for GTU-style exams by giving direct theory answers, practical code examples, diagrams where useful, and quick revision points.

## Core Standard

Write notes that are:

1. **Exam-ready**: Answers should match 3, 4, and 7 mark question expectations.
2. **Readable**: Use short paragraphs, bullets, tables, and code blocks.
3. **Practical**: Add Java/XML examples where Android implementation is commonly asked.
4. **Accurate**: Remove vague, absurd, outdated, or unrelated content.
5. **Complete enough**: Cover definitions, uses, steps, advantages, limitations, examples, and short questions.
6. **Consistent**: Follow the same Markdown style across chapters and PYQ solutions.

## Markdown Formatting Rules

1. Use numbered chapter headings:

```markdown
# **3 User Interface**
## **3.1 Android User Interface**
```

2. Use `=>` for explanation lines because the existing notes use that style.

3. Use fenced code blocks with language tags:

````markdown
```java
// Java code
```
````

4. Use tables for comparisons:

```markdown
| Topic A | Topic B |
|---|---|
| Point | Point |
```

5. Keep heading names short and searchable.

6. Add an **Exam Short Questions** section at the end of each chapter.

7. Do not add decorative content, emojis, motivational filler, or unrelated textbook fluff.

## Answer Depth Rules

### 3-mark answer

Include:

1. Definition.
2. 3 to 5 important points.
3. Small example if useful.

### 4-mark answer

Include:

1. Definition.
2. Explanation.
3. Features/uses/steps.
4. Small code example or comparison table where useful.

### 7-mark answer

Include:

1. Definition.
2. Detailed explanation.
3. Diagram or flow where applicable.
4. Steps or lifecycle methods.
5. Complete Java/XML example where the question is practical.
6. Advantages, limitations, or conclusion.

## Code Example Standards

1. Add code when a topic is implementation-focused, such as:
   - Activity lifecycle.
   - Intent.
   - Fragment.
   - Layouts.
   - UI components.
   - Event handling.
   - Toast.
   - Spinner/ListView/RecyclerView.
   - SharedPreferences.
   - SQLite.
   - Content Provider.
   - Location.
   - Google Maps.
   - MediaPlayer.
   - Camera.
   - Animation.
   - AlarmManager.
   - Manifest permissions.

2. Prefer small, exam-writable Java/XML snippets over long production code.

3. Use Java for Android examples unless the repository already uses Kotlin.

4. Include XML layout and Java Activity code for full app questions.

5. Use simple variable names that students can remember.

6. Include permissions in `AndroidManifest.xml` when required.

7. Use modern wording when needed, but keep exam theory compatible.

Example:

```markdown
=> In modern Android, WorkManager or Executor may be preferred, but AsyncTask is still important for exam theory.
```

## Content Cleanup Rules

Remove or rewrite content that is:

1. Over-worded or artificial.
2. Too vague for exam use.
3. Unrelated to Android syllabus.
4. Technically misleading.
5. Old but not marked as old.
6. Repeated without adding value.
7. Written in awkward phrases like "strictly", "perfectly", "flawlessly", "robustly" when not needed.

When older concepts appear, keep them only if useful for exams and clearly label them.

Example:

```markdown
=> Eclipse with ADT plugin was used earlier. Modern Android development mostly uses Android Studio.
```

## Chapter Note Structure

Use this structure when refining chapters:

1. Chapter title.
2. Definitions and basic concept.
3. Important components/classes.
4. Features or advantages.
5. Required permissions or manifest entries.
6. Code examples.
7. Comparison tables if two topics are commonly compared.
8. Practical steps for app-building topics.
9. Exam short questions.

## PYQ Solution Structure

Use this structure when solving previous year papers:

1. File path:

```text
pyq/solutions/<paper-name>.md
```

2. Title:

```markdown
# Summer 2025 - Mobile Application Development Solutions
```

3. Preserve question numbering:

```markdown
## Q.1 (a) Question text. [03]
```

4. Answer every OR option too.

5. Add code for practical questions.

6. Keep answers readable and preparation-focused, not one-line summaries.

## Android Topic Coverage Checklist

When preparing notes, check if these common exam areas are covered:

1. Android definition, features, advantages and disadvantages.
2. Android architecture.
3. Android APIs and framework.
4. Application components.
5. Manifest file and permissions.
6. DVM and ART.
7. Activity and lifecycle.
8. Bundle and orientation handling.
9. Fragment and lifecycle.
10. Intent, intent filter, explicit and implicit intent.
11. AVD and emulator.
12. UI, View, ViewGroup and layouts.
13. Event handling and Toast.
14. RadioButton, CheckBox, Spinner, ListView, RecyclerView.
15. Menus, styles and themes.
16. SharedPreferences.
17. Internal and external storage.
18. SQLite and SQLiteOpenHelper.
19. Content Provider and ContentResolver.
20. Location services and permissions.
21. Google Maps.
22. Geocoding and reverse geocoding.
23. Canvas, Paint, Drawable and ShapeDrawable.
24. Hardware acceleration.
25. Animation.
26. AlarmManager and DownloadManager.
27. MediaPlayer, VideoView, SoundPool and MediaRecorder.
28. Camera and video recording.
29. Publishing, signing, APK/AAB, versioning and deployment.
30. App performance, modifiability, availability and security.

## Quality Check Before Finishing

Before finalizing notes or solutions:

1. Check Markdown headings.
2. Check code fences are balanced.
3. Search for leftover bad wording:

```text
strictly
perfectly
flawlessly
absurd
TODO
TBD
recoding
jscript
phone gap
```

4. Check that code examples are in fenced blocks.
5. Check that practical answers include required XML, Java and permissions where needed.
6. Check that OR questions are also answered in PYQ solutions.
7. Check that unrelated content is removed.

## Tone and Style

1. Write directly for students preparing exams.
2. Prefer simple English.
3. Avoid unnecessary theory expansion.
4. Use Android terms accurately.
5. Keep examples small and memorable.
6. Add tables for differences.
7. Add diagrams using text blocks when image diagrams are not available.
