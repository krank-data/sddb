# Sleep and Dream Database

Dream reports collected from a variety of sources and aggregated in the public
[Sleep and Dream Database](https://sleepanddreamdatabase.org).

| | Summary |
|--:|:--|
| File | `sddb.tsv.xz` |
| Size | 4 Mb |
| Version | [v1-alpha.1](https://github.com/krank-data/sddb/releases/latest) |
| MD5 | `md5:f05c3615c978a16dcf0ddb2440c56914` |
| SHA256 | `sha256:df9e9cc5db89fc28ddb20d5d38153c56d1c77f971626646bb1a1b963e39f607e` |
| Source | [Sleep and Dream Database](https://sleepanddreamdatabase.org/library) |
| References | Bulkeley, K. (2014). Digital dream analysis: A revised method. _Conscious Cogn_. doi:[10.1016/j.concog.2014.08.015](https://doi.org/10.1016/j.concog.2014.08.015) <br> Bulkeley, K. (2023). New approaches in the empirical study of dreams. _Poligrafi_. doi:[10.35469/poligrafi.2023.412](https://doi.org/10.35469/poligrafi.2023.412) |
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