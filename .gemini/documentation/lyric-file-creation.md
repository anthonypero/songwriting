# Lyric File Creation from ChordPro

This document outlines the process for creating a SUNO-formatted lyric file from a ChordPro file.

## SUNO Format

A SUNO-formatted lyric file is a plain text file (`.txt`) that contains only the lyrics of a song and section headers. It should not contain any ChordPro tags or chords.

### Section Headers

ChordPro section headers, which can be in formats like `{comment: Intro}` or `{start_of_intro}`, must be converted to a simple, capitalized format enclosed in square brackets.

- **Example 1:** `{comment: Verse 1}` becomes `[Verse 1]`
- **Example 2:** `{start_of_chorus}` becomes `[Chorus]`
- **Example 3:** `{c: Bridge}` becomes `[Bridge]`

### Chords and Other Tags

All ChordPro chords (e.g., `[A]`, `[G]`, `[C#m]`) and other metadata tags (e.g., `{title:...}`, `{artist:...}`, `{key:...}`) must be removed from the file.

## Workflow

1.  **Open the ChordPro file:** Start with the source `.chordpro` file.
2.  **Convert Section Headers:** Identify all section headers and convert them to the `[Section Name]` format.
3.  **Remove Chords:** Delete all chord indicators from the lyrics.
4.  **Remove Other Tags:** Delete all other ChordPro tags.
5.  **Save as .txt:** Save the resulting plain text as a new file with the `-lyrics.txt` suffix, following the project's naming conventions.

## Example

**Original ChordPro:**
```
{title: My Awesome Song}
{artist: Me}

{comment: Verse 1}
[G]This is the [C]first line of my [G]song.
[D]This is the [G]second line.
```

**Correct SUNO Format:**
```
[Verse 1]
This is the first line of my song.
This is the second line.
```
