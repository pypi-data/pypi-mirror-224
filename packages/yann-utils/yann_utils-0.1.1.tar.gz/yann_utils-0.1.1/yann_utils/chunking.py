import os
import pickle
import re
import tempfile
from pathlib import Path
from typing import Any, Iterable, Union


def chunk_obj(obj: Any, chunk_size_mb: int) -> Iterable[bytes]:
  """Chunk an object into bytes of a given size."""
  ser = pickle.dumps(obj)
  chunk_size_b = chunk_size_mb * 1024**2
  return (ser[i : i + chunk_size_b] for i in range(0, len(ser), chunk_size_b))


def reconstruct_obj(chunks: Iterable[bytes]) -> Any:
  """Reconstruct an object from its chunks of bytes."""
  acc = []
  for chunk in chunks:
    with open(chunk, "rb") as file:
      acc.append(file.read())

  return b"".join(acc)


def persist_chunks(chunks: Iterable[bytes], dir: str) -> None:
  """Persist chunks to disk and return directory."""
  os.makedirs(dir, exist_ok=True)
  for i, chunk in enumerate(chunks):
    with open(f"{dir}/pkl.part{i}", "wb") as file:
      file.write(chunk)


def get_numeric_suffix(file_name: str) -> None:
  """Get the numeric suffix of a file name."""
  match = re.search(r"\d+$", file_name)
  if not match:
    raise ValueError(f"File name {file_name} does not contain a numeric suffix")

  return int(match.group())


def get_chunks(dir: str) -> Iterable[str]:
  """Get the chunks of an object from a directory."""
  chunks = Path(dir).glob("pkl.part*")
  chunks = [str(path) for path in chunks]
  chunks = sorted(chunks, key=get_numeric_suffix)
  return chunks
