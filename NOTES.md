# Variant A — version history (memory / attention bug lane)

Concept: the brain's doorway amnesia — walking into a room and instantly forgetting why. The strongest lane pick: universal, instantly recognisable, and it maps perfectly onto software language (task queue, buffering, reload).

- **v1** — "v1.0.0: Fixed a bug where walking into a room made you forget why you went there." (89 chars) — Plain statement of the bug, no release-note craft, no second beat; reads like a description, not a shipped fix.
- **v2** — "v2.3.1: Fixed a bug where entering a room cleared the task queue." (66 chars) — Added a real version number and engineering register ("task queue"), but too short and no punchline; wastes most of the 160-char budget.
- **v3** — "v2.3.1: Fixed a bug where entering a room cleared the task queue; users no longer stand in doorways buffering." (110 chars) — Added the visible symptom (standing in the doorway buffering) as the payoff; "buffering" is the joke's second idea. Still 50 chars of budget unused.
- **v4** — "v2.3.1: Fixed a bug where entering a room wiped the task queue; users no longer stand in doorways buffering while the brain reloads why they came in." (149 chars) — "wiped" is punchier than "cleared"; added the brain reloading the reason as a third beat that explains the buffering. Nearly full budget.
- **v5** — "v2.3.1: Fixed a bug where entering a room wiped the task queue; affected users stood in doorways buffering until the brain reloaded why they came in." (149 chars) — Tried past-tense "affected users stood" for a changelog feel; weaker — the present-tense "no longer stand" in v4 reads more like a fix that shipped.
- **v6 (FINAL)** — "v2.3.1: Fixed a bug where entering a room wiped the task queue; users no longer stand in doorways buffering while the brain re-downloads why they came in." (154 chars) — "re-downloads" instead of "reloads": a sharper engineering verb that lands the joke twice (buffering + re-downloading a thought you already had). Every word works; no padding.

## Final line (154 characters)

```
v2.3.1: Fixed a bug where entering a room wiped the task queue; users no longer stand in doorways buffering while the brain re-downloads why they came in.
```

Validation: `python3 main.py` run twice from a clean /output — byte-identical output, single line, 154 characters (limit 160).
