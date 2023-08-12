"""Package dependencies for clementine."""

from collections import namedtuple
from dataclasses import dataclass
from typing import Union

__all__ = [
    "ClementineExtras",
    "Extra",
    "dependencies",
    "extras",
    "optional_dependencies",
    "python_version",
    "recommended_dependencies",
]

_VERSIONS = {
    "bandit": "bandit[toml]",
    "black": "black",
    "bokeh": "bokeh",
    "build": "build",
    "catppuccin-matplotlib": "catppuccin-matplotlib",
    "click": "click",
    "datasets": "datasets",
    "gradio": "gradio",
    "isort": "isort",
    "mkdocs-walt": "mkdocs-walt",
    "mkdocstrings": "mkdocstrings[python]",
    "mypy": "mypy",
    "numpy": "numpy",
    "notebook": "notebook",
    "pandas": "pandas",
    "pip-tools": "pip-tools",
    "playwright": "playwright",
    "pre-commit": "pre-commit",
    "pyperclip": "pyperclip",
    "pytest": "pytest",
    "rich": "rich",
    "ruff": "ruff",
    "scikit-learn": "scikit-learn",
    "spacy": "spacy",
    "tomlkit": "tomlkit",
    "torch": "torch",
    "transformers": "transformers",
    "twine": "twine",
    "wandb": "wandb",
}


@dataclass(frozen=True)
class Extra:
    """Basic information about an extra dependency."""

    name: str
    description: str
    deps: tuple[str, ...]


ClementineExtras = namedtuple(
    "ClementineExtras",
    ["blossom", "fruit", "leaves", "pulp", "rind", "seeds", "sprout", "tree"],
)


def _make_deps_list(package_names: Union[list[str], tuple[str, ...]]) -> list[str]:
    """Returns a list of dependencies with their constraints.

    Raises: ValueError if a `package_name` is not in the list of known dependencies.
    """
    deps = []
    for package_name in package_names:
        if package_name not in _VERSIONS:
            raise ValueError(
                f"Package '{package_name}' is not in the list of known dependencies: "
                f"{list(_VERSIONS.keys())}"
            )
        deps.append(_VERSIONS[package_name])
    return deps


_blossom = Extra(
    name="blossom",
    description="visualization and demonstration tools",
    deps=("bokeh", "gradio", "playwright"),
)

_fruit = Extra(
    name="fruit",
    description="machine learning libraries and frameworks",
    deps=(
        "catppuccin-matplotlib",
        "numpy",
        "pandas",
        "scikit-learn",
        "torch",
    ),
)

_leaves = Extra(
    name="leaves",
    description="documentation tools",
    deps=("mkdocs-walt", "mkdocstrings"),
)

_pulp = Extra(
    name="pulp",
    description="auxiliary ml libraries and frameworks",
    deps=("datasets", "spacy", "transformers", "wandb"),
)

_rind = Extra(
    name="rind",
    description="packaging tools",
    deps=("build", "tomlkit", "twine"),
)

_seeds = Extra(
    name="seeds",
    description="general development tools",
    deps=(
        "bandit",
        "black",
        "isort",
        "mypy",
        "pip-tools",
        "pre-commit",
        "pytest",
        "ruff",
    ),
)

_sprout = Extra(
    name="sprout",
    description="exploration and prototyping tools",
    deps=("notebook", "rich"),
)

_tree = Extra(
    name="tree",
    description="all optional dependencies",
    deps=(
        *_blossom.deps,
        *_fruit.deps,
        *_leaves.deps,
        *_pulp.deps,
        *_rind.deps,
        *_seeds.deps,
        *_sprout.deps,
    ),
)

extras = ClementineExtras(
    blossom=_blossom,
    fruit=_fruit,
    leaves=_leaves,
    pulp=_pulp,
    rind=_rind,
    seeds=_seeds,
    sprout=_sprout,
    tree=_tree,
)


def dependencies():
    """Returns a list of clementine's required dependencies."""
    return []


def optional_dependencies():
    """Returns a dictionary of clementine's optional dependencies."""
    return {
        "all": _make_deps_list(["click", "playwright", "pyperclip"]),
    }


def recommended_dependencies():
    """Returns a dictionary of recommended dependencies.

    The recommended dependencies are a collection of libraries and frameworks
    you might want to use when starting a new project. These dependencies aren't
    necessarily used in clementine, but they're made available as extra packages
    for easier installation."""
    return {extra.name: _make_deps_list(extra.deps) for extra in extras}


def python_version():
    """Returns clementine's required Python version."""
    return ">=3.9"
