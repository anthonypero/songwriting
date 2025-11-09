You can use special codes when editing Lyrics & Chords to specify chords, sections, pages, stylize text, and add notes. Using these codes tells Planning Center which content to strip out of Lyric PDFs and Chord Charts.

## **Lyrics & Chords**

| Code | Description |
| :---- | :---- |
| SECTION HEADING | Type section headings, like CHORUS 1 or INSTRUMENTAL, in all caps. |
| \[ Chord \] | Chords in square brackets are [Chord Pro](https://pcoservices.zendesk.com/hc/en-us/articles/115013738628#UUID-a83e4140-bed8-18d8-e0e9-403b86c44b1e), and they are transposed and placed on the line above the corresponding lyrics. Anything in square brackets will only appear in Chord Chart PDFs. If it is on the same line as a SECTION HEADING, it will still be shifted to the line above, so make sure NOT to use the Chord Pro brackets in this header. |

## **Key changes**

| Code | Description |
| :---- | :---- |
| TRANSPOSE KEY \+1 | To insert a key change but still type chords in the original key, add TRANSPOSE KEY plus or minus the number of half-steps. When choosing a key, the following scale will be used: Ab, A, Bb, B, C, Db, D, Eb, E, F, F\#, G. |
| REDEFINE KEY \+1 | To insert a key change where you have already typed the chords in the new transposed key, add REDEFINE KEY plus or minus the number of half-steps. This does not transpose chords for chord charts, but for Number and Numeral charts, it remaps the numbers to the new key. When choosing a key, the following scale will be used: Ab, A, Bb, B, C, Db, D, Eb, E, F, F\#, G. |

## **Notes**

| Code | Description |
| :---- | :---- |
| { note } | Text in single curly braces is a note that will show in Chords Chart PDFs and Lyric PDFs. Unlike square brackets, it will not be shifted up a line. |
| {{ note }} | Text in double curly braces is a note that will only show in Chord Chart PDFs and will be removed from Lyric PDFs. |

## **Layout**

| Code | Description |
| :---- | :---- |
| COLUMN\_BREAK | Starts a new column. |
| PAGE\_BREAK | Starts a new page. |

To have a column or page break only apply to chord charts and not lyrics, put it in double curly braces. {{ PAGE\_BREAK }}

## **Style**

| Code | Description |
| :---- | :---- |
| \<b\>Bolded Text\</b\> | Text placed between \<b\> and \</b\> is bolded for Lyric & Chord PDFs. |
| \<i\>Italicized Text\</i\> | Text placed between \<i\> and \</i\> is italicized for Lyric & Chord PDFs. |
| \<strong\>Bolded Text\</strong\> | Text placed between \<strong\> and \</strong\> is bolded for Lyric & Chord PDFs. |
| \<u\>Underlined Text\</u\> | Text placed between \<u\> and \</u\> is underlined for Lyric & Chord PDFs. |
| \<em\>Italicized Text\</em\> | Text placed between \<em\> and \</em\> is italicized for Lyric & Chord PDFs. |

## **Chord symbols**

| Select from the options menu | Description |
| :---- | :---- |
| ∆ | Major |
| ♭ | Flat |
| ° | Diminished |
| ø | Half-diminished |

