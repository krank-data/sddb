"""
Compress a single data file without any modification.
"""

import argparse
import hashlib
import lzma
import pathlib
from datetime import datetime, timezone

import pandas as pd
from pandas.testing import assert_frame_equal


parser = argparse.ArgumentParser()
parser.add_argument("filepath", type=str, help="Full filepath to compress")
parser.add_argument("--cleanup", action="store_true", help="Delete original upon completion")
args = parser.parse_args()

filepath = args.filepath
cleanup = args.cleanup

import_path = pathlib.Path(filepath).expanduser()
export_suffix = import_path.suffix + ".xz"
export_path = import_path.with_suffix(export_suffix)

def file_hash(fname, alg, chunksize=65536):
    """Calculate the hash of a given file in chunks to avoid memory overload"""
    hasher = getattr(hashlib, alg)()
    with open(fname, "rb") as f:
        buffer = f.read(chunksize)
        while buffer:
            hasher.update(buffer)
            buffer = f.read(chunksize)
    return hasher.hexdigest()

# Read original file and write it to compressed file
with open(import_path, "rb") as f:
    data = f.read()
    with lzma.open(export_path, "xb") as lzf:
        lzf.write(data)

# Print metadata of import and output files
for fp in [import_path, export_path]:
    print("\n")
    print(f"file: {fp}")
    print(f"size: {fp.stat().st_size / 1e6} Mb")
    print(f"ctime: {fp.stat().st_ctime}")
    print(f"ctime ISO: {datetime.fromtimestamp(fp.stat().st_ctime, tz=timezone.utc).isoformat()}")
    for alg in ["md5", "sha256"]:
        print(f"{alg}:{file_hash(fp, alg=alg)}")
    print("\n")

# Read both files back in and ensure they contain identical content
import_df = pd.read_csv(import_path, low_memory=False)  # low_memory=False to avoid column warnings
export_df = pd.read_csv(export_path, low_memory=False)
assert_frame_equal(import_df, export_df, check_exact=True)

if cleanup:
    import_path.unlink()
