# Clustering for Threat Surface Mapping (Unsupervised)

Idea: Cluster hosts/users/netflows into behavioral groups to highlight unusual entities and aid asset inventory hygiene.

Key components:
- Data: Zeek conn/auth logs or synthetic features; scaling and PCA options
- Methods: K-Means/DBSCAN/GMM comparisons; silhouette and stability checks
- Outputs: cluster summaries, outlier lists, and suggested investigation pivots
- Deliverable: report/API with cluster labels and exemplar entities
- MLOps: reproducible pipeline, config-driven preprocessing, batch scoring

Stretch: incremental clustering or streaming-friendly sketching.


