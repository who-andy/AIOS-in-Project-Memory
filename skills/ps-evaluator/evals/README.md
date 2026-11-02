# Evaluation protocol (manual model testing)

Use **synthetic** text or applicant-consented anonymized PS drafts only.

1. Before comparing outputs, freeze the Rubric/major profile versions and save the exact prompt and document hash.
2. Run each model independently with the same target university and major; do not expose the other model's score during initial rating.
3. Run pairwise comparisons twice with A/B order reversed; note whether the preference flips.
4. Edit one input at a time: cosmetic prose polishing, a genuinely deeper reflection, and an irrelevant major term insertion. Record which rubric components moved.
5. Repeat under the second major profile; unchanged universal scores should stay fixed across majors.
6. Add human ratings only if assessors follow the same guidelines, and report exact qualifications, sample size, adjudication rules and limitations.

No human evaluation and no real multi-model trials are included in v0.1. The bundled JSON examples are synthetic contract fixtures.
