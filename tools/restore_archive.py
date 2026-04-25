from __future__ import annotations

import argparse
import base64
import io
import zipfile
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description='Restore the archived code45/nlp45 package.')
    parser.add_argument('--archive', default='artifacts/code45_nlp45_full_manualsyn_localbert.zip.b64', help='Path to the base64 archive file in this repository.')
    parser.add_argument('--output', default='restored_nlp45', help='Directory to extract the package into.')
    args = parser.parse_args()

    archive_path = Path(args.archive)
    output_dir = Path(args.output)

    if not archive_path.exists():
        raise FileNotFoundError(f'Archive file not found: {archive_path}')

    b64_text = archive_path.read_text(encoding='utf-8').strip()
    zip_bytes = base64.b64decode(b64_text)

    output_dir.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(io.BytesIO(zip_bytes)) as zf:
        zf.extractall(output_dir)

    print(f'Restored project to: {output_dir.resolve()}')


if __name__ == '__main__':
    main()
