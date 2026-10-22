# philosophy-scout

The guide sends every question to `philosophy-scout`, which returns file paths; the guide reads them whole. The scout must find files whose bearing is an inference, not a resemblance to the question's words.

## Left

- Validate the angles step: run `philosophy-scout` on the bare question, with no hint of angles. Passes if `zoom-levels`, `compounding-decisions` and `model-tiers` come back.
  > My agent keeps forcing itself to find feedback in pull requests. What do I do? (an agent asked to review a PR always produces findings, inventing nitpicks when there is nothing real). Files I already know bear on it: attractors.
- The scout's stop rule still counts passages ("this round added a passage?", "the first round that adds no passage") while its return is files.
- Pin the scout to Opus whatever the session's model. The agent file is shared with opencode, which names models `provider/model-id`; Claude Code takes `opus`. Check both tools' docs for a fallback list or a per-tool override.
- Kaizen group still to take or drop: the guide showed the scout's whole haul, ideas that did not bear on the reader's case included.
