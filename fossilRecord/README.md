# fossilRecord — bluegate-tenancy

Frozen documents organized by epoch. Once fossilized, a document is **read-only reference** —
it is never edited, only superseded by a new version in `filing-ready/` or `strategy/active/`.

## Epochs

| Epoch | Period | Contents |
|-------|--------|----------|
| `epoch0_foundation_sep4-sep10` | Sep 4–10 | Original complaint frameworks, RICO drafts, agency templates, preservation notices, checklists |
| `epoch1_agency_blitz_sep10-sep16` | Sep 10–16 | JTC supplements, bar complaints, FOIAs, agency notifications, cease & desist |
| `epoch2_service_battle_sep17-sep21` | Sep 17–21 | Alt service motions (v1), PPO materials, federal packets, press materials, interrogatories |

## Convention

- Each epoch has its own `README.md` listing every fossil with a one-line reason
- Documents are **moved**, not copied — git tracks the rename
- Active versions stay in `01-case/filing-ready/` or `01-case/strategy/active/`
- If a fossilized doc is later updated, the new version gets a new date suffix and stays in `filing-ready/`
- Cross-references use the relational index at `01-case/_index/CASE_REGISTRY.md`

## Naming

Files keep their original names. The epoch directory provides the temporal context.
