# Extraction Strategy

## Change In Place, Then Extract

When introducing a new class (brick, helper, collaborator):

1. **Reshape the existing code** until it looks like the target
2. **Extract** the reshaped code into a new class
3. **Wire** the new class immediately — verify it works before moving on

Never build a new class in isolation and wire it later.
Late integration gives late feedback.

## One At a Time

When extracting multiple collaborators from a large method:

- Extract and wire **one** collaborator per cycle
- Confirm behavior is preserved before starting the next extraction
- Each extraction is its own commit
