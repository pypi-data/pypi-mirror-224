import os
from typing import List, Tuple

__all__ = [
    "friendly_path",
]


def friendly_path(path: str, use_environment: bool = True) -> str:
    """
    Gets a friendly representation of the given path,
    using relative paths or environment variables
    (if use_environment = True).
    """
    # TODO: send extra rules

    # always prefer getcwd
    cwd = os.getcwd()
    if path.startswith(cwd + "/"):
        return path.replace(cwd + "/", "")

    options = [os.path.relpath(path, cwd)]

    rules = [("~", os.path.expanduser("~")), (".", cwd), (".", os.path.realpath(cwd))]

    if use_environment:
        envs = dict(os.environ)
        # remove unwanted
        for e in list(envs.keys()):
            if "PWD" in e:
                del envs[e]

        for k, v in envs.items():
            if v:
                if v and v[-1] == "/":
                    v = v[:-1]
                if v and v[0] == "/":
                    rules.append(("${%s}" % k, v))

    # apply longest first
    rules.sort(key=lambda x: (-len(x[1])))
    path = replace_variables(path, rules)

    options.append(path)

    weight_doubledot = 5

    def score(s: str) -> int:
        # penalize '..' a lot
        s = s.replace("..", "*" * weight_doubledot)
        return len(s)

    options.sort(key=score)
    result = options[0]

    # print('Converted %s  => %s' % (original, result))

    return result


def replace_variables(path: str, rules: List[Tuple[str, str]]) -> str:
    for k, v in rules:
        if path.startswith(v):
            # print("  applied %s => %s" % (v, k))
            path = path.replace(v, k)
    return path
