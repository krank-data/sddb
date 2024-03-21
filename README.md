# Sleep and Dream Database

Dream reports collected from a variety of sources and aggregated in the public
[Sleep and Dream Database](https://sleepanddreamdatabase.org).

| | Summary |
|--:|:--|
| File | `dream-export.tsv.xz` |
| Size | 3 Mb |
| Version | [v1-alpha.1](https://github.com/krank-data/sddb/releases/latest) |
| MD5 | `md5:` |
| SHA256 | `sha256:` |
| Source | [Sleep and Dream Database](https://sleepanddreamdatabase.org/library) |
| Citation | Bulkeley, K. (2014). Digital dream analysis: A revised method. _Consciousness and Cognition_. doi:[10.1016/j.concog.2014.08.015](https://doi.org/10.1016/j.concog.2014.08.015) |
| Processing code | [`prepare.ipynb`](https://nbviewer.org/github/krank-data/sddb/blob/main/prepare.ipynb) |
| Processing environment | [`environment.yaml`](environment.yaml) |

## Changes made

> These are the changes made to the original dataset.

* Remove excess metadata columns
* Clean/standardize dream report text
* Merge related datasets and authors
* Rename datasets
* Replace author names with standardized codes
* Remove entries with extreme word counts
* Remove datasets with small sample sizes
* Convert from comma-separated values (`csv`) to tab-separated values (`tsv`)