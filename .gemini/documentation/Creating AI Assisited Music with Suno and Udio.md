# Creating AI-Assisted Music with Udio

This document serves as an unofficial manual for creating music and/or songs using the Udio AI music generation platform. There is a lot of testing that still needs to be completed to find out what reliably works and what doesn’t.

Please keep in mind that because of the sheer volume of what is possible, nothing can be reliably reproduced in its entirety.

## Music Breakdown Testing Methodology

*   Tested each tag on a single genre prompt.
*   Each tag was tested multiple times individually.
*   Modifier tags such as `[Des]` or `[Et]` were tested multiple times with a single tag to be modified.
*   Listened to whether the tag affected the music, vocals, or both within the genre.
*   Some tags may have a more heavy affect or increased stability in other genres of music.

**Overall prompt used for test:**
```
pop, pop music, male vocalist, female vocalists
```

**Basic verse used for test:**
```
[Verse]
We've been waiting for this night.
To break free, feel alive.
The energy's electric, can you feel it?
It's time to move, don't resist it.
```

## Structure

### Rhyme Structure

The structure of a song appears to play a key role in how Udio constructs the output. Following a common structure that is recognized seems to have a higher quality output with a smooth flowing song rhyme structure.

*   **AAAA - Monorhyme:** All the lines in a stanza end with the same rhyme.
*   **AABB - Coupled rhyme:** The first two and second two lines rhyme at the end.
*   **ABBA - Enclosed rhyme:** The first and last line and the two middle lines rhyme at the end.
*   **ABCB - Quatrain:** Second and fourth line rhyme. First and third do not. This is a ballad form.
*   **ABAB - Alternate rhyme:** The first and third lines rhyme at the end, and the second and fourth lines rhyme at the end.

### Line Count and Syllable Impact on Song Structure Generation

Udio's FAQ suggests an average of 6 lines per verse per 32sec generation. However, testing reveals that syllable count per line significantly affects the final output.

**Here's what testing has revealed:**
*   6 lines with 4 syllables each: Renders easily.
*   6 lines with 8 syllables each: More challenging to render completely.
*   6 lines with 10 syllables each: Will not fully render.

Rendering success will also depend on the song's tempo. Faster tempo songs can move through words quickly. Slower tempo songs will end up with words being cut off.

**Key takeaway:** Consider both song pacing and syllables per line, as tonal fluctuations or stresses often occur on patterned syllables.

**Example of a difficult structure to render:**
```
[Verse: tag1, tag2]
Line 1 scheme A (9 syllables)
Line 2 scheme A (11 syllables)
Line 3 scheme B (10 syllables)
Line 4 scheme A (12 syllables)
```

## Song Structure Tags

The structure of the song tags will play a role in how Udio puts together the final rendering. Different tags seem to represent different types of general instructions to the AI. Using common types of song structures appear to generate better results. Here are some of the more common types of song structures.

*   `[Verse] - [Verse] - [Bridge] - [Verse]`
*   `[Verse] - [Chorus] - [Verse] - [Chorus] - [Bridge] - [Chorus]`
*   `[Verse] - [Chorus] - [Verse] - [Chorus]`
*   `[Verse] - [Pre-Chorus] - [Chorus] - [Verse] - [Pre-Chorus] - [Chorus]`

The following are some of the more common parts of a song structure that are known to work:

*   **[Opening Theme]:** Sets the tone and introduces key musical motifs or themes. If working from “Chorus” backwards to the beginning, this can bring in instrumentation and vocals previously used.
*   **[Introduction]:** Sets the mood and prepares listeners for the main sections of the song.
*   **[Hook]:** The most memorable and catchy part of the song, designed to grab the listener's attention.
*   **[Pre-Verse]:** A link section used as an interlude between the Intro and the first Verse.
*   **[Verse]:** Presents the main lyrical content and melody of the song.
*   **[Pre-Chorus]:** Builds anticipation and tension leading into the chorus.
*   **[Chorus]:** The focal point of the song, featuring a catchy melody and often the main message or theme.
*   **[Drop]:** The climax of the song, featuring a sudden release of energy and often a change in rhythm or instrumentation.
*   **[Breakdown]:** Reduces the intensity temporarily, providing contrast and allowing for buildup towards another climax.
*   **[Solo]:** Showcases instrumental virtuosity or improvisation, often featuring a single instrument.
*   **[Interlude]:** Offers a brief musical break or transition between sections.
*   **[Build-Up]:** Increases tension and anticipation, typically leading into a drop or chorus.
*   **[Chorus Variation]:** A modified version of the chorus, adding variation to keep the song interesting.
*   **[Instrumental Break]:** Allows for instrumental exploration or variation without vocals.
*   **[Breakdown]:** Where instruments are stripped back to minimal levels. Typically happens before drop or build-up.
*   **[Build-Up 2]:** Similar to the first build-up, but often with added elements or variations.
*   **[Second Drop]:** Another climactic moment, often with variations or developments from the first drop.
*   **[Bridge]:** Provides a departure from the main structure of the song, adding variety and interest.
*   **[Final Chorus]:** A climactic repetition of the chorus, often with added intensity or emotion.
*   **[Outro]:** Concludes the song, often by revisiting key themes or motifs and providing a sense of resolution.

When structuring your song, put commands AFTER structure tags (i.e., Verse, Chorus, etc.). Otherwise, the commands seem to have little or no influence and the AI can insert content ahead of structure tags.

**Example:**
```
[Pre-Chorus: tag1, tag2, tag3, etc.]
```

## Tags

Tags play an important role as they can take the final output in a different direction while affecting the music and vocals produced within a section. Some tags are stable while others are unstable or not recognized. Some tags will have more effect on the output depending on the genre, mood, and theme or combination of genre, mood, theme.

There is now a listing of 993 tags available. The majority of which still need to be tested.

Tags can be used for global application, in the main prompt. This means they will be applied to the entire song. Or, you can target them to be applied to a specific section, in the custom lyric section.

Further experiments show that tags can be used in their English equivalent versus using the traditional Italian, French, and German terminology.

*   **[harmonize]**: Vocals cross over each other with the same words. (Stable. Difficult to dictate which voices)
*   **[fade to end]**: Fades to end of generation. (Reasonably stable. Difficult to dictate when fade will begin.)
*   **[fade]**: Produces a fade. (Reasonably stable. Difficult to dictate when or how long fade will progress.)
*   **[dolby atmos]**: Increased stereophonics. (Stable.)
*   **[wall of sound]**: Blended instruments with noticeable panning. (Stable.)
*   **[composition]**: Polished and refined output. Good for symphonic songs. (Stable.)
*   **[complex]**: Instruments and vocals interweave. (Stable.)
*   **[a due]**: Duet (Unstable. Decent results, best if used in prompt and in custom.)
*   **[a deux]**: Duet (Unstable. Decent results, may get harmonized background vocals)
*   **[a cappella]**: Vocals without music backing. (Stable)
*   **[a capriccio]**: Freedom to create (May change lyrics into another random language)
*   **[a niente]**: Quick sudden fade at end. (Unstable. Fade is very quick. 1s or less.)
*   **[a piacere]**: Vocals don’t necessarily follow musical rhythm. (Stable.)
*   **[a tempo]**: Keep tempo with rhythm. (Return to proper rhythm). (Unstable.)
*   **[abafando]**: Muffled or muted. (Unstable. Spotty but works most of the time).
*   **[abbandonatamente]**: Freeflowing and passionate
*   **[accarezzevole]**: Expressive (May affect lyrics)
*   **[accelerando]**: Gradually increase tempo (May affect lyrics)
*   **[accelerato]**: Accelerate (May affect lyrics - interesting results)
*   **[accentato]**: Emphasis (May affect lyrics)
*   **[accent]**: Emphasis (May affect lyrics - good results)
*   **[acciaccato]**: Broken down or crushed. (Unstable. Hit-n-miss)
*   **[acciaccatura]**: Crushing (May affect lyrics)
*   **[accuratezza]**: With accompaniment that may move fast or slow (May affect lyrics)
*   **[affannato]**: Anguished
*   **[affettuoso]**: With emotion
*   **[affrettando]**: Hurrying or pressing forwards
*   **[agitato]**: Agitated (Stable.)
*   **[alla polacca]**: In ¾ dance time (Spotty)
*   **[allargando]**: Progressively slower (Spotty - may affect lyrics)
*   **[allegretto]**: Lively, moderately fast
*   **[allegrezza]**: Cheery, joyful
*   **[allegrissimo]**: Very fast (Interesting results)
*   **[allegro]**: Cheerful or brisk
*   **[alzate sordini]**: Remove the mutes (Interesting results)
*   **[amabile]**: Pleasant (Very interesting results)
*   **[ambitus]**: Between highest and lowest note (Interesting results)
*   **[amore]**: Love
*   **[con amore]**: With love.
*   **[andante]**: Moderate pace
*   **[ängstlich]**: Anxiously (Results not what I expected)
*   **[anima]**: With feeling (Interesting results, nice)
*   **[animandosi]**: Progressively more animated
*   **[antiphonal]**: Same, may affect lyrics
*   **[apaisé]**: Calmed (Interesting results)
*   **[appassionato]**: Passionate (Interesting results)
*   **[aria]**: Self contained section for one voice (Nice results)
*   **[arioso]**: Airy (Very interesting on music structure)
*   **[Arpeggio]**: Notes are played or sprung one after another rather than together. (Stable.)
*   **[articulato]**: Articulate (Very interesting on music structure)
*   **[attacca]**: Attack
*   **[Ausdruck]**: Expression
*   **[avec]**: With (a connector/modifier)
*   **[Avoir]**: Own or have. (Modifier. Good results, mostly stable)
*   **[ballabile]**: Danceable (Good results, mostly stable)
*   **[barbaro]**: Uses pentatonic scale that is chromatic
*   **[Barcarola]**: Song in 6/8 or 12/8 time (Somewhat stable)
*   **[Basso continuo]**: Continuous bass supporting harmonic structure (Stable)
*   **[Bedächtig]**: Deliberately slow (Stable, works dependant on genre)
*   **[Bellicoso]**: Warlike (Stable. Affects music, not lyrics)
*   **[Beschleunigend]**: Speeding up (Stable. Gradual depending on lyric length)
*   **[Bestimmt]**: Decisively (Stable. Works with lyrics and music.)
*   **[Betont]**: Accented or stressed (Stable. Works with lyrics and music.)
*   **[Beweglich]**: Nimble, nimbly, or agile (Stable. Works with lyrics and music.)
*   **[Bewegt]**: Agitated (Stable. Works with lyrics and music.)
*   **[Bien]**: Fine, good, well. (Stable. Works with lyrics and music.)
*   **[Binary]**: Consisting of two parts (Stable. Will hear break or music/lyrics will be different.)
*   **[Bis]**: Twice. (Interesting results - not exactly a repeat effect)
*   **[Blasinstrument]**: Wind instruments (Interesting results - can contain more strings depending on prompt).
*   **[Blech]**: Brass instruments (Interesting results - can contain more brass depending on prompt)
*   **[Blechinstrumente]**: Brass instruments (Interesting results - genre specific)
*   **[Blechmusik]**: Brass instruments (Interesting results - genre specific)
*   **[Bol]**: Muted (Stable. Works mainly with music)
*   **[Bolero]**: Dance music in ¾ time. (Not stable. Hit and miss)
*   **[Bravura]**: Virtuostic style. (Stable, genre and lyric specific)
*   **[Breit]**: Broad. (Stable. More body included in generated music.)
*   **[Breve]**: Short. (Stable. Generated music is choppier.)
*   **[Brillante]**: Brilliant. (Stable. Generated music has a brightness to it.)
*   **[Brioso]**: Vivacious or spirited. (Stable. Generated music is more uplifted.)
*   **[Cadenza]**: Show artists technique. (Stable)
*   **[Caesura]**: Pause. (Stable. Adds pauses depending on lyrics)
*   **[Calando]**: Decreasing in loudness and usually in tempo. (Stable. Will result in quieter section. May affect tempo.)
*   **[Calmato]**: Calming becoming quiet. (Stable. Will result in quieter section. May affect tempo.)
*   **[Caloroso]**: Warm, warmth, passionately. (Stable. May affect lyrics.)
*   **[Calore]**: Warm, warmth, passionately. (Stable. Better results than above, does not affect lyrics.)
*   **[Cambiare]**: To change. (Stable. Change is noticeable within section produced.)
*   **[Camminando]**: Moving evenly. (Stable. Tempo and vocals move at same speed.)
*   **[Cantabile]**: Singable. (Stable. Adds something of an accapella to vocals.)
*   **[Cantando]**: Singing. (Stable. Adds more of a singsong to vocals.)
*   **[Capriccio]**: At the performers pleasure. (Interesting results.)
*   **[Capriccioso]**: At the performers pleasure. (Interesting results.)
*   **[Carazzendo]**: Soothingly, caressingly. (Stable. Does have a soothing feel to generated section.)
*   **[Cedando]**: Slowing down. (Stable. Temp is slowed. Lyrics may have a slowing part. Does not start fast then slows.)
*   **[Cédez]**: Slow down. (Somewhat stable. Will add a slight slowing effect to lyrics.)
*   **[Celare]**: Fast, quickly. (Somewhat stable. Will pick up pace of song and hold pace.)
*   **[Cesura]**: Pause. (Not stable. May affect lyrics. May not place pause where wanted.)
*   **[Chalau]**: Warm or passionately. (Stable)
*   **[Chanté]**: Singing. (Stable. Does add a singsong like effect.)
*   **[Chasse]**: Chase or hunt like. (Stable. Adds an element of drama to generated section.)
*   **[Chiaramente]**: Clear. (Stable. Vocals are more pronounced within music.)
*   **[Chiaro]**: Clear. (Stable. Vocals have more room within composition.)
*   **[Chiuso]**: Muted. (Stable. Music is slightly pulled back. Lyrics are clear.)
*   **[Cinq]**: Five. (Not stable. Interesting effect on vocals.)
*   **[Clos]**: Shut or closed. (Stable. Staccato effect on vocals.)
*   **[Coda]**: Tail section. (Stable. Quick fade at end of section. Less than a second.)
*   **[Colla parte]**: One voice double’s another voices part. (Stable. Places in various parts. Hit & miss for specific parts. Adds a harmony.)
*   **[Colossale]**: Colossal. (Stable. Genre specific. Adds more of a widening to generated section.)
*   **[Comdamente]**: Comfortable, easy (Stable. Fits within genre specific music spectrum.)
*   **[Commosso]**: Moved, touched. (Stable. Adds a different feeling to music and vocals.)
*   **[Comodo]**: Comfortable, easy - refers to tempo. (Stable. Works with vocals. Does adjust tempo.)
*   **[Con]**: With.
*   **[Cuarteto]**: (Quartet) Ensemble of four players. (Stable. Adds harmonized backing vocals.)
*   **[Cuivre]**: Brassy and harsh. (Stable. Adds harshness to rendering. Genre specific for brassy.)
*   **[Da Capo]**: From the beginning. (Stable. Will affect the entire rendering with whatever follows.)
*   **[Dal]**: From the. (Stable.)
*   **[Dämpfer]**: Mute. (Mostly stable. Adds a slight pause where placed. May affect lyric output.)
*   **[Dʹattaque]**: Attack. (Stable. Adds emphasis to the beginning of beat and lyrics.)
*   **[Dauernd]**: Duration. (Stable. Will affect the entire rendering with whatever follows.)
*   **[Debole]**: Weak, faint. (Mostly stable. Affects music, not vocals.)
*   **[Décidé]**: Decisively. (Stable. Adds an element of urgency to music and vocals.)
*   **[Decisamente]**: Decisively. (Stable. Gives a different feel to music and vocals.)
*   **[Deciso]**: Decisively. (Stable. Music and lyrics are more staccato.)
*   **[Declamato]**: Declamatory. (Stable. Music is more staccato, lyrics are not affected.)
*   **[Decrescendo]**: Decreasing in volume. (Unstable. Might have a small volume drop in certain areas, only to have volume return later.)
*   **[Dehors]**: In the open, prominent. (Stable. Brings vocals more to the front of the music.)
*   **[Delicatamente]**: Delicate, delicately. (Stable. Vocals have a smoothing element added to them.)
*   **[Delicatezza]**: Delicate, delicately. (Stable. Both vocals and music have smoothing element added.)
*   **[Delicato]**: Delicate, delicately. (Stable. Adds an almost romantic quality to music and voice.)
*   **[Délié]**: Sharp, detached. (Stable. Music and lyrics have a sharpness added to them.)
*   **[Derb]**: Rough, robust. (Unstable. Adds more of a dreamlike smoothing to rendering.)
*   **[Des]**: Some. (Stable. Adds some of whatever follows behind.)
*   **[Détaché]**: Detached; unconcerned. (Stable.)
*   **[Deutlich]**: Clear, distinct. (Stable. Brings vocals forward of music.)
*   **[Deux]**: Two. (Used by itself, stable. Brings in more background vocals and echoing effect.)
*   **[Devoto]**: Devout, devoutly, faithful. (Stable. May affect genre, beat, or tempo.)
*   **[Di molto]**: Very. (Stable. Adds to whatever follows.)
*   **[Di nuovo]**: New, again. (Stable. Will add a change in the music and vocals. Exact placement is hit and miss.)
*   **[Diluendo]**: Dilute, thinning; dying away. (Stable. May affect genre. Reduces amount of instruments and voices in rendering.)
*   **[Diminuendo]**: Decreasing in volume. (Unstable. May only affect a single line in verse.)
*   **[Disinvolto]**: Confident. (Stable.)
*   **[Dissonante]**: Dissonant. (Stable. Excellent results.)
*   **[Divisi]**: Part, divide. (Stable. Can work to create duets.)
*   **[Doigté]**: Fingering. (Unstable. Adds a staccato effect to rendering.)
*   **[Dolce]**: Sweet. (Stable.)
*   **[Dolcezza]**: Sweetness, gentleness. (Stable. Adds a ballad type of feel.)
*   **[Dolcissimo]**: Much sweetness, gentleness. (Stable. Rendering is more ballad-like.)
*   **[Dolente]**: Sad. (Stable. Does add a down feeling to music and vocals.)
*   **[Doloroso]**: Painful, mournful. (Stable. Down feeling is more prominent.)
*   **[Doppelt]**: Double. (Unstable.)
*   **[Doppelt so schnell]**: Twice as fast. (No effect on either music or vocals.)
*   **[Doppio]**: Double. (Unstable. May affect lyrics. May bring in backup vocals.)
*   **[Doppio movimento]**: Twice as fast. (Unstable. Hit and miss on doubling effects.)
*   **[Doucement]**: Gently, softly. (Stable.)
*   **[Douloureux]**: Painful, sorrowful. (Stable.)
*   **[Doux]**: Gentle, sweet, soft. (Stable.)
*   **[Drammatico]**: Dramatically. (Stable. May affect genre. Amazing results.)
*   **[Drängend]**: Pressing, quickening. (Mostly Stable. Tempo or beat does pick up or drops in with most renderings.)
*   **[Duolo]**: Grief. (Stable.)
*   **[Dur]**: Major. (Stable. Has an effect on vocals making them more dramatic.)
*   **[Duramente]**: Severely. (Stable.)
*   **[Durchdringend]**: Piercing, shrill. (Stable.)
*   **[Dureté]**: Harshness, toughness. (Stable.)
*   **[Durezza]**: Hardness, toughness. (Stable.)
*   **[E]**: And. (Stable. Combines what comes before and after. Does not work for creating duets.)
*   **[Éclatant]**: Brilliant, dazzling. (Stable. Not as dramatic as would be expected.)
*   **[Eco]**: Echo. (Stable. Adds transients to vocals and music.)
*   **[Ègalement]**: Too, same. (Stable. Mainly holds how vocals sound. Does not hold music.)
*   **[Égalité]**: Equality. (Stable. Heard more high range in renderings.)
*   **[Eile]**: Hurry. (Stable. Tempo pick up. May affect lyrics.)
*   **[Eilend]**: Hurrying. (Stable. Tempo picks up. Does not affect lyrics.)
*   **[Ein Heldenleben]**: Poetic. (Stable. Adds a cinematic and poetic vibe to rendering.)
*   **[Ein wenig]**: A little. (Stable. Adds a small amount of whatever follows.)
*   **[Eine Alpensinfonie]**: Poetic. (Stable. Adds a cinematic and poetic vibe to rendering.)
*   **[Einfacht]**: Simple. (Stable.)
*   **[Einhlang]**: Unison. (Stable.)
*   **[Élargissant]**: Broaden. (Stable.)
*   **[Élégant]**: Elegant, graceful. (Stable.)
*   **[Elegante]**: Elegant. (Stable.)
*   **[Empfindsamkeit]**: Sentimentality. (Stable.)
*   **[Empfindung]**: Sensitivity, feeling. (Stable. Nice effect on vocals.)
*   **[Empressé]**: Avid, eager. (Stable. Can give a 70s feel to music.)
*   **[Ému]**: Moved with emotion. (Stable.)
*   **[En]**: In, into. (Mostly stable. Moves in or into whatever follows. May affect lyrics.)
*   **[En dehors]**: Prominent; prominently. (Stable. Brings focus to vocals.)
*   **[En pressant]**: Pressing forward. (Stable.)
*   **[En retenant]**: Holding back. (Unstable. Hit and miss. May affect lyrics.)
*   **[Enchaînez]**: Chain, restrain. (Unstable. Interesting results. May affect lyrics.)
*   **[Energico]**: Energetic, stirring. (Stable.)
*   **[Energique]**: Energetic, stirring, vigorous. (Stable.)
*   **[Enfatico]**: Emphatic. (Stable.)
*   **[Enlevez]**: Take off. (Stable but struggles for effect.)
*   **[Entendre]**: To hear. (Stable.)
*   **[Entendu]**: Heard. (Stable. Vocals are focused.)
*   **[Entfernt]**: Distant. (Unstable. Interesting overall effects on vocals.)
*   **[Entrain]**: Pep. (Stable.)
*   **[Entscheiden]**: Resolute. (Stable.)
*   **[Entschlössen]**: Decided, determined. (Stable.)
*   **[Epilogue]**: Concluding section. (Stable. Does not do a fade at end.)
*   **[Ergriffen]**: Moved, stirred. (Stable.)
*   **[Erhaben]**: Sublime, noble. (Stable.)
*   **[Erhabenhei]**: Sublime, noble. (Stable.)
*   **[Erlöschend]**: Extinguishing, dying away. (Stable. Affects tempo and beat. Does not adjust volume levels.)
*   **[Ermattend]**: Tiring, weakening. (Stable. Affects tempo and beat. Does not adjust volume levels.)
*   **[Ernst]**: Earnest, serious. (Stable. Nice effect on vocals.)
*   **[Ernsthaft]**: Earnest, serious. (Stable. Nice effect on vocals. Gives a ballad feel.)
*   **[Eroica]**: Heroic. (Stable. More of a cinematic feel than a heroic feel.)
*   **[Ersatz]**: Replace.