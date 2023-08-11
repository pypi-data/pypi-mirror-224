import time
from typing import TypeVar, List, Any
import itertools
import functools
import matplotlib as mpl
from typing import Dict, Generator, Tuple
import pickle
from tqdm import tqdm

A = TypeVar("A")
B = TypeVar("B")
T = TypeVar("T")


def timer(func):
  """Simple timer decorator which outputs execution time in ms."""

  def timed(*args, **kwargs):
    t0 = time.time()
    res = func(*args, **kwargs)
    tf = time.time()

    print(f"{(tf - t0) * 1000:.1f}ms")
    return res

  return timed


def time_elapsed(t0: float) -> float:
  t_elapsed = (time.time() - t0) * 1000
  print(f"{t_elapsed}ms")
  return t_elapsed


def flatten(list_o_list: List[List[T]]) -> List[T]:
  """
    >>> flatten([[1, 2], [3, 4]])
    [1, 2, 3, 4]
    """
  return list(itertools.chain(*list_o_list))


def compose(*functions) -> Any:
  def operation(f, g):
    return lambda x: f(g(x))

  return functools.reduce(operation, functions, lambda x: x)


def clusters_to_cmap(clusters: List[int]) -> List[Any]:
  color_wheel = mpl.colormaps["gist_ncar"]
  N = len(set(clusters))
  return [color_wheel(cls / N) for cls in clusters]


def invert_dict(d: Dict[A, List[B]]) -> Dict[B, A]:
  """Convert dictionary of lists to flat dictionary with values as keys."""
  return {v: k for k, vs in d.items() for v in vs}


def reassign_dict(ds: Dict[Any, Any], values: List[Any]) -> Dict[Any, Any]:
  """
    >>> reassign_dict({"a": 1, "b": 2}, [2, 1])
    {'a': 2, 'b': 1}
    """
  assert len(ds) == len(values)
  keys = list(ds.keys())
  return {keys[i]: values[i] for i in range(len(ds))}


def multiprocess_apply(func, args, n_jobs: int = 8) -> List[Any]:
  """Macro for multicore iteration."""
  from multiprocessing import Pool

  with Pool(n_jobs) as pool:
    return list(tqdm.tqdm(pool.imap(func, args), total=len(args)))


def list_set(xs: List) -> List:
  """
    >>> list_set([1, 2, 3, 1, 2, 3])
    [1, 2, 3]
    """
  return list(set(xs))


def list_accessor(objects: List[O], field: str) -> List[A]:
  """
    >>> list_accessor([{"a": 1}, {"a": 2}], "a")
    [1, 2]
    """
  return [o.__getattribute__(field) for o in objects]


def enumerate_flipped(xs: List["E"]) -> Generator[Tuple["E", int], None, None]:
  """
    >>> list(enumerate_flipped(["a", "b", "c"]))
    [('a', 0), ('b', 1), ('c', 2)]
    """
  return ((x, i) for i, x in enumerate(xs))


class Cache:
  """Persistent and automated caching of objects."""

  locs: List[str] = []

  def __init__(self) -> None:
    if os.path.exists("cache/_cache.pkl"):
      with open("cache/_cache.pkl", "rb") as f:
        mem = pickle.load(f)
        self.locs = mem.locs

  def save(self, obj: Any, name: str) -> None:
    self.locs.append(name)
    with open(f"cache/{name}.pkl", "wb") as f:
      pickle.dump(obj, f)

    with open(f"cache/_cache.pkl", "wb") as f:
      pickle.dump(self, f)

  def load(self, name: str) -> Any:
    with open(f"cache/{name}.pkl", "rb") as f:
      return pickle.load(f)

  def __repr__(self):
    return "\n".join(self.locs)
