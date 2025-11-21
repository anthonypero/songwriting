# Project: Songwriting

## Directory Overview

This directory is a central repository for songwriting projects. It contains various files related to musical compositions, including lyrics, chord charts, and audio recordings. The structure is organized by song, with each song having its own dedicated folder.

## Key File Types

The directory primarily uses the following file types:

*   **.chordpro:** These files contain the lyrics and chords for songs, formatted using the ChordPro standard. This format allows for easy transposition and clear presentation of musical information.
*   **.txt:** Plain text files are used for lyrics and notes.
*   **.mp3, .wav:** Audio files, including demos, scratch tracks, and final mixes, are stored in these formats.
*   **.md:** Markdown files, like this one, are used for documentation.

## Directory Structure

The general structure of the directory is as follows:

```
Songwriting/
├───[Song Title 1]/
│   ├───lyrics.txt
│   ├───song.chordpro
│   └───audio/
│       ├───demo.mp3
│       └───scratch.wav
├───[Song Title 2]/
│   └───...
└───.gemini/
    └───...
```

Each song is contained within its own folder, named after the song's title. Inside each folder, you will find the relevant files for that song.

## Usage and Conventions

This directory serves as a workspace for developing and organizing songs. When working with the files, please adhere to the following conventions:

*   **File Naming:** All song-related text files (`.chordpro`, `.txt`) should use a "slugified" version of the song's official title. This ensures consistency and avoids issues with special characters in filenames.

    1.  **Get the Title:** Start with the full title from the `{title:...}` directive (e.g., "Gloria! (The Angels Sing)").
    2.  **Create the Slug:**
        *   Convert the title to lowercase.
        *   Remove any characters that are not letters, numbers, or spaces.
        *   Replace all spaces with dashes (`-`).
        *   **Example:** "Gloria! (The Angels Sing)" becomes `gloria-the-angels-sing`.
    3.  **Construct the Filename:** Combine the slug with a type suffix and the extension.
        *   **ChordPro:** `[slug].chordpro` (e.g., `gloria-the-angels-sing.chordpro`)
        *   **Lyrics:** `[slug]-lyrics.txt` (e.g., `gloria-the-angels-sing-lyrics.txt`)
        *   **PCO Chords:** `[slug]-chords.txt` (e.g., `gloria-the-angels-sing-chords.txt`)
        *   **Other:** `[slug]-[type].txt` (e.g., `gloria-the-angels-sing-phonetics.txt`)
*   **ChordPro Format:** When creating or editing `.chordpro` files, follow the standards outlined in the `.gemini/documentation/chordpro/chordpro.md` file. This ensures that the files can be correctly parsed and displayed by ChordPro-compatible software.
*   **Planning Center Integration:** For songs intended for use with Planning Center, refer to the specific formatting guidelines in `.gemini/documentation/chordpro/planning-center-chordpro.md`.
*   **Audio Files:** Store all audio files in an `audio` sub-directory within the song's main folder.
*   **New Songs:** When starting a new song, create a new folder for it and follow the established structure.

## Lyric and ChordPro Workflow

The standard workflow for creating songs is as follows:

1.  **Start with Lyrics:** Lyrics begin in a plain `.txt` file in SUNO format, which means no metadata at the top. This file serves as the initial source of truth for the song's lyrics.
2.  **Create ChordPro File:** From the lyric file, a `.chordpro` file will be created. This process involves:
    *   Adding ChordPro metadata tags (e.g., `{title: ...}`, `{artist: ...}`, `{key: ...}`).
    *   Inserting chords in `[brackets]` next to the corresponding lyrics.
    *   Adding section headers using `{comment: Header Name}` for consistency and maintainability, along with other ChordPro directives as needed.

This workflow establishes the `.chordpro` file as the main source of truth for the song's structure and chords, while the `.txt` file remains the origin of the lyrics.

For more detailed information on the SUNO format and AI music generation, refer to the document: `.gemini/documentation/Creating AI Assisited Music with Suno and Udio.md`.

## Planning Center Workflow

When asked to create a "pco version" or "planning center version" of a song, follow these steps:

1.  **Copy the File:** Copy the `.chordpro` file to a new file named `[Song Title] - chords.txt`.
2.  **Remove Metatags:** Delete all ChordPro metatags from the top of the new file (e.g., `{title: ...}`, `{artist: ...}`, `{key: ...}`, `{tempo: ...}`, `{time: ...}`).
3.  **Convert Markup:** Convert the ChordPro markup to Planning Center's preferred format. This includes:
    *   Changing section headers (e.g., `{comment: Verse 1}` or `{start_of_verse: Verse 1}`) to all-caps text (e.g., `VERSE 1`).
    *   Converting ChordPro's `{transpose: n}` to Planning Center's `TRANSPOSE KEY +n` (or `-n`).
    *   Converting ChordPro comments like `{c: comment}` to PCO notes: `{comment}`.
    *   Converting ChordPro annotations like `[*annotation]` to `[{{<i>annotation</i>}}]`.
        *   **Exception:** `[*N.C.]` is a special case and should be converted to `[N.C.]`.
    *   Converting in-chord annotations like `[CHORD *annotation]` to `[CHORD {{<i>annotation</i>}}]`.
    *   Ensuring chords remain in square brackets `[]`.
    *   For lines containing only chords (e.g., intros, instrumentals), combine the section header and the chord progression onto a single line. Remove the square brackets `[]` from around each individual chord and symbol, but enclose the entire chord progression in a single set of square brackets `[]`. Do not add a colon after the section header. For example:
        ```
        INTRO
        [D] [/] [/] [/] [|] [Bm] [/] [/] [/]
        ```
        Should become:
        ```
        INTRO [D / / / | Bm / / /]
        ```
    *   Adjusting any other ChordPro-specific directives to their Planning Center equivalents as needed.
    *   Removing `end_of_*` tags.

## ChordPro File Boilerplate

When creating a new `.chordpro` file, use the following metadata block as a template:

```
{title: Song Title}
{artist: Anthony Pero}
{composer: Anthony Pero}
{lyricist: Anthony Pero}
{copyright: }
{key: }
{tempo: }
{tag: }
```

## Project Workflow: Git Repository and Google Drive Sync

This project uses a "publish/capture" model to synchronize files between the official Git repository located at `~/Projects/Songwriting` and Google Drive for cross-device access. This workflow is managed by several scripts located in `.gemini/scripts/`.

### 1. Publish Workflow (Repo -> Google Drive)

This process copies the final "output" assets from the local Git repository to a "Published" folder in Google Drive for easy viewing and listening on other devices.

*   **Source:** `/Users/apero/Projects/Songwriting/` (The Git repository)
*   **Destination:** `~/Library/CloudStorage/GoogleDrive-tonygpero@gmail.com/My Drive/Music/Songwriting (Published)/`
*   **Action:**
    1.  Scan the source repository.
    2.  Find all lyrics (`-lyrics.txt`), chord charts (`.chordpro`), and audio files (`.mp3`, `.wav`).
    3.  Copy these files, maintaining the slug-based directory structure, to the destination, overwriting any existing files to ensure the published version is up-to-date.

### 2. Capture Workflow (Google Drive -> Repo)

This process moves new ideas from a "Scratchpad" folder in Google Drive into an `_inbox` folder within the Git repository for manual sorting and integration.

*   **Source:** `~/Library/CloudStorage/GoogleDrive-tonygpero@gmail.com/My Drive/Music/Songwriting (Scratchpad)/`
*   **Destination:** `/Users/apero/Projects/Songwriting/_inbox/`
*   **Action:**
    1.  Scan the source "Scratchpad" folder.
    2.  Move all files found into the destination `_inbox` folder.
    3.  The user can then process these files manually within the Git repository.

## Utility Scripts

This section documents helper scripts used within the project for various tasks.

### `build_song_index.py`

*   **Location:** `.gemini/scripts/build_song_index.py`
*   **Purpose:** Scans the entire songwriting project directory for `.chordpro` files, extracts metadata (title, artist, key, tempo, tags, etc.), and compiles this information into a `song_index.json` file. This index facilitates quick lookup and organization of songs.
*   **Usage:** `python3 .gemini/scripts/build_song_index.py`
    *   The script automatically finds the project root and outputs `song_index.json` in the `.gemini/` directory.

### `extract_lyrics.py`

*   **Location:** `.gemini/scripts/extract_lyrics.py`
*   **Purpose:** Extracts clean lyrics from a ChordPro file, removing all ChordPro-specific elements (chords, most metadata) and formatting section headers (e.g., `{comment: Verse 1}` becomes `[Verse 1]`) for compatibility with platforms like SUNO. It also ensures a blank line precedes each heading, except the first.
*   **Usage:** `python3 .gemini/scripts/extract_lyrics.py <input_chordpro_file_path> <output_lyrics_file_path>`
    *   **Example:** `python3 .gemini/scripts/extract_lyrics.py silent-night-sing-noel/silent-night-sing-noel.chordpro silent-night-sing-noel/silent-night-sing-noel-lyrics.txt`

### `standardize_filenames.py`

*   **Location:** `.gemini/scripts/standardize_filenames.py`
*   **Purpose:** Standardizes song directory and file names based on the song title extracted from its `.chordpro` file. It generates a "slug" from the title and renames the associated folder and files (including the `.chordpro` file itself), also updating the `meta: slug` directive inside the ChordPro file.
*   **Usage:** `python3 .gemini/scripts/standardize_filenames.py <root_directory_of_songs> [--execute]`
    *   By default, the script runs in "dry-run" mode, showing planned changes without making them.
    *   Add `--execute` to apply the renaming operations.
    *   **Example (Dry Run):** `python3 .gemini/scripts/standardize_filenames.py .`
    *   **Example (Execute):** `python3 .gemini/scripts/standardize_filenames.py . --execute`

## GitHub Account

This project is associated with the `anthonypero` GitHub account. When interacting with GitHub for this project, ensure you are using the `github-personal` SSH host.
