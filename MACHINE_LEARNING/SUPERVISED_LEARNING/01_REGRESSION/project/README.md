# Threat/Risk Scoring (Regression)

Idea: Predict a continuous risk score or expected MTTR for alerts/incidents based on context (asset criticality, alert metadata, historical outcomes), to prioritize analyst effort.

Key components:
- Features: alert type, source, enrichment (asset tags, user role), historical labels
- Models: Linear/Elastic Net baseline → Gradient Boosted Trees; calibration
- Evaluation: RMSE/MAE + ranking metrics (nDCG@k) for prioritization
- Deliverable: API that returns score + rationale; integration mock with ticketing
- MLOps: model registry, CI/CD, monitoring for drift and label delay

Stretch: cost-sensitive optimization to maximize business impact within SLA.


