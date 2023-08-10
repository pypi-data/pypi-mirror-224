#!/usr/bin/env python3

from __future__ import annotations

import fileinput
import itertools
import math
import os
import random
import re
import shutil
import subprocess
import sys
from collections import ChainMap, Counter, defaultdict, deque
from collections.abc import Callable, Collection, Iterable, Mapping, Sequence
from copy import deepcopy
from dataclasses import asdict, dataclass, field
from functools import cache, partial, reduce
from itertools import accumulate, chain, combinations, product
from os import PathLike
from pathlib import Path
from typing import Any, Literal, NamedTuple, Optional, Protocol, TypedDict

@dataclass
class Args:
    ...


def main(args: Args) -> None:
    ...


