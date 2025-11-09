# ChordPro File Format Documentation

## Table of Contents
- [Introduction to ChordPro](#introduction-to-chordpro)
- [ChordPro Directives](#chordpro-directives)
- [ChordPro Chords](#chordpro-chords)

---

## Introduction to ChordPro

In 1992, Martin Leclerc and Mario Dorion created a simple text file format for writing lead sheets with lyrics and chords. This format, originally for a tool called `chord`, became popularly known as ChordPro.

### Overview

ChordPro files are plain text and can be created with any text editor. Common file extensions include `.cho`, `.crd`, `.chopro`, `.chord`, and `.pro`, with `.cho` being the recommended choice.

### The Basics

A simple ChordPro song looks like this:

```
# A simple ChordPro song.

{title: Swing Low Sweet Chariot}

{start_of_chorus}
Swing [D]low, sweet [G]chari[D]ot,
Comin’ for to carry me [A7]home.
Swing [D7]low, sweet [G]chari[D]ot,
Comin’ for to [A7]carry me [D]home.
{end_of_chorus}

I [D]looked over Jordan, and [G]what did I [D]see,
Comin’ for to carry me [A7]home.
A [D]band of angels [G]comin’ after [D]me,
Comin’ for to [A7]carry me [D]home.

{comment: Chorus}
```

- **Chords**: Encased in square brackets `[]`, placed before the corresponding syllable.
- **Directives**: Encased in curly braces `{}`, used for formatting and metadata.
  - `{title: ...}`: Sets the song's title.
  - `{start_of_chorus}` / `{end_of_chorus}`: Defines the chorus section.
  - `{comment: ...}`: Adds a comment line.
- **Comments**: Lines starting with `#` are ignored.

The output will render chords above the lyrics, for example:

      D          G    D
Swing low, sweet chariot,
                       A7
Comin’ for to carry me home.

### Markup and Annotations

As of ChordPro version 6, you can use markup similar to Pango Markup Language for text styling (size, color, font). Annotations can be added with `[*text]` to place remarks above the lyrics.

### Printing

Originally, ChordPro produced PostScript documents. Today, the standard output is PDF, suitable for viewing on various devices.

---

## ChordPro Directives

ChordPro directives are used to control the appearance of the printed output. They define meta-data like titles, add new chords, control page and column breaks. Therefore it is not always easy to make a distinction between the semantics of a directive, and the way these semantics are implemented in the ChordPro processing program, the formatter.

For example, the title directive:

```
{title: Swing Low Sweet Chariot}
```

The directive name is ‘title’, and its argument is the text ‘Swing Low Sweet Chariot’. This directive defines meta-data, the song title. That is the semantic part. What the formatter does with this meta-data is up to the program and not part of the ChordPro File Format Specification. You can consider directives to be a friendly request, or suggestion, but the actual implementation is left to the formatter. For a meta-data item like the song title it will probably be printed on top of the page and be included in a table of contents, if any.

The Chordpro Program provides a default implementation in the style of the original chord program. It can be used as a reference to what a directive is assumed to do. It must however be emphasised that program can be configured to use different page styles, fonts, sizes, colours, and so on. Where appropriate, this document refers to the default style.

Many directives have long and short names. For example, the long (full) name for the directive title is ‘title’, and the short (abbreviated) name is ‘t’. It is, however, advised to use the full name whenever possible, since the abbreviations may lead to confusion or ambiguity if new directives are added.

### Arguments and Attributes

For directives that take arguments, the arguments are separated from the directive name by a colon `:` and/or whitespace, as can be seen above with the title directive. Some directives require more than a single argument. For these, a syntax familiar to HTML attributes is used, e.g.

```
{image: src="myimage.jpg" scale="50%"}
```

You can use pairs of single and pairs of double quotes, the result is the same.

Some directives with a single argument will also take an attribute instead. For example, the following variants of `start_of_verse` are the same:

```
{start_of_verse Verse 1}
{start_of_verse label="Verse 1"}
```

It is always best to use the variant with explicit attributes. It is less confusing, robust, and future-proof.

Note: In this documentation attributes are often denoted with the less correct term properties. This will be straightened out in the future.

### Preamble Directives

- `new_song` (short: `ns`)

### Meta-data Directives

Each song can have meta-data associated, for example the song title. Meta-data are mostly used by programs that help organizing collections of ChordPro songs.

- `title` (short: `t`)
- `sorttitle`
- `subtitle` (short: `st`)
- `artist`
- `sortartist`
- `composer`
- `lyricist`
- `copyright`
- `album`
- `year`
- `key`
- `time`
- `tempo`
- `duration`
- `capo`
- `tag`
- `meta`

See also Using metadata in texts.

### Formatting Directives

- `comment` (short: `c`)
- `highlight`
- `comment_italic` (short: `ci`)
- `comment_box` (short: `cb`)
- `image`

### Environment Directives

Environment directives always come in pairs, one to start the environment and one to end it.

- Introduction to environments
- `start_of_chorus` (short: `soc`), `end_of_chorus` (short: `eoc`)
- `chorus`
- `start_of_verse` (short: `sov`), `end_of_verse` (short: `eov`)
- `start_of_bridge` (short: `sob`), `end_of_bridge` (short: `eob`)
- `start_of_tab` (short: `sot`), `end_of_tab` (short: `eot`)
- `start_of_grid` (short: `sog`), `end_of_grid` (short: `eog`)

### Delegated Environment Directives

These environment directives turn their content into something else, usually an image, and embed the result in the ChordPro output.

- Introduction to delegated environments
- `start_of_abc` / `end_of_abc`
- `start_of_ly` / `end_of_ly` (Lilypond embedding)
- `start_of_svg` / `end_of_svg`
- `start_of_textblock` / `end_of_textblock`

### Chord Diagrams

- `define`
- `chord`

### Transposition

- `transpose`

### Fonts, Sizes and Colours

These directives can be used to temporarily change the font, size and/or colour for lyrics, chords, and more. To permanently change these the reference implementation uses much more powerful configuration files.

- `chordfont` (short: `cf`), `chordsize` (short: `cs`), `chordcolour`
- `chorusfont`, `chorussize`, `choruscolour`
- `footerfont`, `footersize`, `footercolour`
- `gridfont`, `gridsize`, `gridcolour`
- `tabfont`, `tabsize`, `tabcolour`
- `labelfont`, `labelsize`, `labelcolour`
- `tocfont`, `tocsize`, `toccolour`
- `textfont` (short: `tf`), `textsize` (short: `ts`), `textcolour`
- `titlefont`, `titlesize`, `titlecolour`

### Output Related Directives

- `new_page` (short: `np`)
- `new_physical_page` (short: `npp`)
- `column_break` (short: `colb`)
- `pagetype`

The following directives are legacy from the old chord program. The modern reference implementation uses much more powerful configuration files for this purpose.

- `diagrams`
- `grid` (short: `g`)
- `no_grid` (short: `ng`)
- `titles`
- `columns` (short: `col`)

### Custom Extensions

To facilitate using custom extensions for application specific purposes, any directive with a name starting with `x_` should be completely ignored by applications that do not handle this directive. In particular, no warning should be generated when an unsupported `x_directive` is encountered.

It is advised to follow the `x_` prefix by a tag that identifies the application (namespace). For example, a directive to control a specific pedal setting for the MobileSheetsPro program could be named `x_mspro_pedal_setting`.

### Conditional Directives

All directives can be conditionally selected by postfixing the directive with a dash (hyphen) and a selector.

If a selector is used, ChordPro first tries to match it with the instrument type (as defined in the config file). If this fails, it tries to match it with the user name (as defined in the config file). Finally, it will try it as a meta item, selection will succeed if this item exists and has a ’true’ value (i.e., not empty, zero, false or null). Selection can be reversed by appending a `!` to the selector.

For example, to define chords depending on the instrument used:

```
{define-guitar:  Am base-fret 1 frets 0 2 2 1 0 0}
{define-ukulele: Am base-fret 1 frets 2 0 0 0}
```

An example of comments depending on voices:

```
{comment-alto:  Very softly!}
{comment-tenor: Sing this with power}
```

When used with sections, selection applies to everything in the section, up to and including the final section end directive:

```
{start_of_verse-soprano}
...anything goes, including other directives...
{end_of_verse}
```

Note that the section end must not include the selector.


---

## ChordPro Chords

In ChordPro files, lyrics are interspersed with chords between brackets `[` and `]`. Strictly speaking it doesn’t matter what you put between the `[]`, it is put on top of the syllable whatever it is. But there are situations where it does matter: for chord diagrams and transpositions.

In general, ChordPro will try to interpret what is between the brackets as a valid chord name, unless the first character is an asterisk, `*`. In that case ChordPro will remove the asterisk and treat everything else as a text that will be printed just like the chord names. This can be used to add small annotations, e.g. `[*Coda]` and `[*Rit.]`.

### Parsing Chords — The Chord Properties

ChordPro can parse chord names in two modes: strict and relaxed.

In **strict mode**, enabled by default, chord names are only recognized if they consist of:

- a root note, e.g. `C`, `F#` or `Bb`.
- an optional qualifier, e.g. `m` (minor), `aug` (augmented).
- an optional extension, which must be one of the extension names built-in.
- an optional bass, a slash `/` followed by another root note.

When a chord name is successfully parsed, each of the above constituents is registered with the chord as properties `root`, `qual`, `ext` and `bass`. Its name is registered as property `name`. These properties are referred to as the chord properties of the chord.

Some examples:

| name | root | qual | ext | bass |
|---|---|---|---|---|
| C | C | | | |
| F# | F# | | | |
| Besm | Bes | m | | |
| Am7 | A | m | 7 | |
| C/B | C | | | B |

Note: What is recognized as a root note and what is stored in the root property is controlled by the notes section of the config files. For example, in the common notation B♭, Bb and Bes all designate a B-flat note.

In **relaxed mode**, the same rules apply for root note and qualifier, but the extension is not required to be known. You are free to make up your own. In relaxed mode, `[Coda]` would be a valid chord name: root `C` plus extension `oda`.

| name | root | qual | ext | bass |
|---|---|---|---|---|
| Coda | C | | oda | |
| Gm* | G | m | * | |

Chord properties can be used as metadata for substitutions.

### Chord Diagrams — The Diagram Properties

Many ChordPro implementations (formatters) provide chord diagrams at the end of a song, using a built-in list of known chords and fingerings. Clearly, this can only work when the chords in the ChordPro file can be recognized, either in strict mode, or in relaxed mode. If a chord is known there may be some additional properties that are used internally to produce chord diagrams. This set of properties is referred to as the diagram properties of the chord.

Some examples:

| name | base | frets | fingers | keys |
|---|---|---|---|---|
| Am7 | 1 | x 0 2 0 1 3 | x x 2 3 1 x | 0 3 7 10 |
| B | 2 | 1 1 3 3 3 1 | 1 1 2 3 4 1 | 0 4 7 |

The list of known chords is read from the config files and can be extended by defining chords using the `define` directive.

### Transposition and Transcoding

For transposition and transcoding the chord must have at least a `root` property. This controls what and how can be transposed or transcoded. For example, when you’re transposing from A to C, you can replace everything chord-like that starts with A by C and whatever follows the A. `Am7` becomes `Cm7` and `Alpha` would become `Clpha`, who cares?

### Valid Chord Names

It is recommended to use standard chord names. The ChordPro Reference Implementation supports at least:

- `A`, `B`, `C`, …, `G` (European/Dutch), `H` (German)
- `I`, `II`, `III`, …, `VII` (Roman)
- `1`, `2`, `3`, …, `7` (Nashville)
- `b` for flat, and `#` for sharp
- Common qualifiers like `m`, `dim`, etc.
- Common extensions like `7`, `alt`, etc.

### ChordPro Implementation: Notes

If enabled in the config, ChordPro will understand lowercase root-only chords to mean note names. Note names will be treated (shown, transposed) exactly as chords, but will not account for diagrams.

This can be used for example for intro’s that start with some single notes before the chords:

```
{comment: Intro [f] [g] [a] [E] }
```

### Appendix: List of Known Chord Extensions

Note that extensions here include the qualifier.

The following chord extensions are currently built-in.

#### Extensions for Major Chords

Note that `^` is an alternative for `maj`.

- `2`
- `3`
- `4`
- `5`
- `6`
- `69`
- `7`
- `7-5`
- `7#5 7#9 7#9#5 7#9b5 7#9#11`
- `7b5 7b9 7b9#5 7b9#9 7b9#11 7b9b13 7b9b5 7b9sus 7b13 7b13sus`
- `7-9 7-9#11 7-9#5 7-9#9 7-9-13 7-9-5 7-9sus`
- `711`
- `7#11`
- `7-13 7-13sus`
- `7sus 7susadd3`
- `7+`
- `7alt`
- `9`
- `9+`
- `9#5`
- `9b5`
- `9-5`
- `9sus`
- `9add6`
- `maj7 maj711 maj7#11 maj13 maj7#5 maj7sus2 maj7sus4`
- `^7 ^711 ^7#11 ^7#5 ^7sus2 ^7sus4`
- `maj9 maj911`
- `^9 ^911`
- `^13`
- `^9#11`
- `11`
- `911`
- `9#11`
- `13`
- `13#11`
- `13#9`
- `13b9`
- `alt`
- `add2 add4 add9`
- `sus2 sus4 sus9`
- `6sus2 6sus4`
- `7sus2 7sus4`
- `13sus2 13sus4`

#### Extensions for Minor Chords

Minor chords can use `m`, `mi`, `min` and `-`.

In the list below only the `m` variants are enumerated:

- `m#5`
- `m11`
- `m6`
- `m69`
- `m7b5`
- `m7-5`
- `mmaj7`
- `mmaj9`
- `m9maj7`
- `m9^7`
- `madd9`
- `mb6`
- `m#7`
- `msus4 msus9`
- `m7sus4`

#### Other Extensions

- `aug +`
- `dim 0`
- `dim7`
- `h h7`
- `h9`