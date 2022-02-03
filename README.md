# vector-artist
The goal of this project is to produce artwork based on pictures via AI.

Useless and vague as this may sound, I can only cite that 'Imitation is the sincerest form of flattery that mediocrity can pay to greatness'.

Meaning that I'm conscious and glad that an AI won't ever replace human artists, as we can't make an authentically creative process by computer. Alas, we can try to imitate it.

Wrapping up, this project has no real use in mind apart from seeing how far it can get. How well a machine can do art. And that's enough digression by now.


### Scope & Purpose
The goal is, for a given input picture, producing an artwork in the form of a vector graphics file (SVG-like).

This vector art should:
- Be composed by geometric shapes and other elements native of vector graphics
- Resemble the original picture at some degree
- Be beautiful. This is of course a subjective measure

## Process of art

### Pre-processing
1. Load a digitalized picture file as input. This will be our muse.
2. Color palette analysis. Simplification of the color palette to be used. We use a UL clustering technique to pick the most representative colors in the picture.

### Experiment
1. Produce possible strokes we can do. A stroke is a unitary addition to the artwork.
2. Reduce the options to a representative yet small number of alternatives
3. Apply additional thematic decoration configured if any

### Judge
For each possible stroke, evaluate the increase that it would make considering different aspects:
1. Resemblance with the muse
2. Color harmony
3. Previous choices made in current and past artworks
4. Sentiment (human judgement of past artworks)

### Act
Apply the highest rated stroke

### Repeat
Consider the next stroke. We continue adding strokes until we reach a number of them.

### Feedback
Once the artwork is complete, show it in a social media gallery and collect feedback (human sentiment).
