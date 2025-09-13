from __future__ import annotations
from pathlib import Path
from typing import TextIO, Dict

def _read_text_from_stream(stream: TextIO) -> str:
    return stream.read()

def _read_text_from_file(path: str) -> str:
    return Path(path).read_text(encoding="utf-8", errors="ignore")

def wordcount_source(path: str | None = None, stdin: TextIO | None = None) -> Dict[str, int]:
    """
    Count lines/words/chars from a file path, or from stdin if path is '-' or None.
    """
    if path in (None, "-"):
        if stdin is None:
            raise ValueError("stdin must be provided when path is '-' or None")
        text = _read_text_from_stream(stdin)
    else:
        text = _read_text_from_file(path)

    lines = text.splitlines()
    words = text.split()
    return {"lines": len(lines), "words": len(words), "chars": len(text)}
