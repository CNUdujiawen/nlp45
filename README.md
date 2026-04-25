# nlp45

This repository stores the `code45` / `nlp45` project package prepared for CoDE-style reproduction.

## Contents

- `artifacts/code45_nlp45_full_manualsyn_localbert.zip.b64` — base64-encoded archive of the full project package.
- `tools/restore_archive.py` — restores the archive into a normal working tree.

## Restore the project

```bash
python tools/restore_archive.py
```

By default, this writes the extracted project into:

```bash
./restored_nlp45
```

You can also choose another output directory:

```bash
python tools/restore_archive.py --output /path/to/nlp45
```

The restored package includes:

- `code45/` source code
- `resources/` with manual Chinese and English synonym lexicons
- `scripts/`
- `requirements.txt`
- project `README.md`

The package has been configured to use local BERT directories:

- `/home/ecs-user/NLPd14/models/bert-base-chinese`
- `/home/ecs-user/NLPd14/models/bert-base-english`
