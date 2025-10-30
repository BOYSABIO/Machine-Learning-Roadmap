# Association Rules for Attack Pattern Discovery

Idea: Mine frequent itemsets/rules from co-occurring alerts/events to uncover TTP patterns and noisy-rule suppressions.

Key components:
- Data: SIEM-like events; discretized attributes (source, technique, asset)
- Methods: Apriori/FP-Growth; support, confidence, lift; pruning for usefulness
- Outputs: human-readable rules with examples and suppression candidates
- Deliverable: rules explorer (markdown report or lightweight UI)
- MLOps: periodic mining job, change detection, rule versioning

Stretch: align rules with ATT&CK tactics/techniques.


