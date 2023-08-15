from typing import Any, Callable, cast, Mapping, Optional, Tuple, TypeVar
from unittest import SkipTest

from ..types import mywraps, ZAssertionError
from ..ui import make_chars_visible

F = TypeVar("F", bound=Callable[..., Any])
FNone = TypeVar("FNone", bound=Callable[..., None])

__all__ = [
    "assert_equal_found_expected",
    "assert_isinstance",
    "assert_issubclass",
    "istest",
    "known_failure",
    "my_assert",
    "my_assert_contains",
    "my_assert_different",
    "my_assert_equal",
    "my_assert_equal_dict",
    "my_assert_equal_ef",
    "my_assert_false",
    "nottest",
    "relies_on_missing_features",
]

FX = TypeVar("FX")


def known_failure(f: FNone, forbid: Tuple[type, ...] = ()) -> FNone:  # pragma: no cover
    @mywraps(f)
    def run_test(*args: object, **kwargs: object) -> None:
        try:
            f(*args, **kwargs)
        except BaseException as e:
            if forbid:
                if isinstance(e, forbid):
                    msg = f"Known failure test is not supposed to raise {type(e).__name__}"
                    raise ZAssertionError(msg) from e

            from zuper_commons.text import remove_escapes

            raise SkipTest(f"Known failure test failed: {type(e).__name__}\n{remove_escapes(str(e))}") from e
        raise ZAssertionError("test passed but marked as work in progress")

    setattr(run_test, "known_failure", True)
    return cast(FNone, run_test)


def relies_on_missing_features(f: FNone) -> FNone:
    msg = "Test relying on not implemented feature."

    @mywraps(f)
    def run_test(*args: object, **kwargs: object) -> None:  # pragma: no cover
        try:
            f(*args, **kwargs)
        except BaseException as e:
            raise SkipTest(msg) from e
        raise ZAssertionError("test passed but marked as work in progress")

    setattr(run_test, "relies_on_missing_features", True)
    return cast(FNone, run_test)


X = TypeVar("X")


def my_assert(testable: Any, msg: Optional[str] = None, **kwargs: object) -> None:
    if not testable:
        if msg is None:
            msg = "Assertion failed: false instead of true"
        raise ZAssertionError(msg, should_be_true=testable, **kwargs)


def my_assert_false(testable: Any, msg: Optional[str] = None, **kwargs: object) -> None:
    if testable:
        if msg is None:
            msg = "Assertion failed: true instead of false"
        raise ZAssertionError(msg, should_be_false=testable, **kwargs)


def my_assert_equal(a: X, b: X, msg: Optional[str] = None, **kwargs: object) -> None:
    r = a == b
    if not r:
        m = "Not equal"
        if msg is not None:
            m += ": " + msg
        if isinstance(a, str) and isinstance(b, str) and len(a) < 1500 and len(b) < 1500:
            # m += "\n" + "a: " + a + "\n" + "b: " + b
            if "\n" in a or "\n" in b:
                ra = make_chars_visible(a, use_colors=True)
                rb = make_chars_visible(b, use_colors=True)
            else:
                ra = repr(a)
                rb = repr(b)
            raise ZAssertionError(m, a=ra, b=rb, why=r, **kwargs)
        else:
            raise ZAssertionError(m, a=a, b=b, why=r, **kwargs)


def my_assert_different(a: X, b: X, msg: Optional[str] = None, **kwargs: object) -> None:
    r = a == b
    if r:
        m = msg or "Actually equal"

        raise ZAssertionError(m, a=a, b=b, why=r, **kwargs)


def my_assert_equal_ef(*, found: X, expected: X, **kwargs: object) -> None:
    r = found == expected
    if not r:
        msg = "Found != Expected"
        raise ZAssertionError(msg, found=found, expected=expected, why=r, **kwargs)


def my_assert_contains(a: X, b: X, msg: Optional[str] = None, **kwargs: object) -> None:
    Sa = set(a)
    Sb = set(b)
    r = Sa.issuperset(Sb)
    not_contained = Sb - Sa
    if not r:
        m = "First set does not contain the second"
        if msg is not None:
            m += ": " + msg

        raise ZAssertionError(m, a=sorted(a), b=sorted(b), not_contained=not_contained, why=r, **kwargs)


def assert_equal_found_expected(name: str, found: X, expected: X, **kwargs: object) -> None:
    msg = f"inconsistency for {name}"
    return my_assert_equal_dict(dict(found=found, expected=expected), msg=msg, **kwargs)


def my_assert_equal_dict(a: Mapping[str, X], msg: Optional[str] = None, **kwargs: object) -> None:
    assert len(a) >= 2
    first_name, first = next(iter(a.items()))

    ok = True
    res = {}
    failures = []
    for k, v in a.items():
        if k == first_name:
            continue
        res[k] = v == first
        ok = ok and (v == first)
        failures.append(k)

    if not ok:
        if len(failures) == 1:
            s = repr(failures[0])
        else:
            s = repr(failures)
        m = f"The element(s) {s} are not equal to first {first_name!r}"
        if msg is not None:
            m += ": " + msg
        d = dict(a)
        d.update(kwargs)
        # if isinstance(a, str) and isinstance(b, str) and len(a) < 1500 and len(b) < 1500:
        #     # m += "\n" + "a: " + a + "\n" + "b: " + b
        #     if "\n" in a or "\n" in b:
        #         ra = make_chars_visible(a, use_colors=True)
        #         rb = make_chars_visible(b, use_colors=True)
        #     else:
        #         ra = repr(a)
        #         rb = repr(b)
        #     raise ZValueError(m, a=ra, b=rb, **kwargs)
        # else:
        raise ZAssertionError(m, **d)


def assert_isinstance(a: object, C: type) -> None:
    if not isinstance(a, C):  # pragma: no cover
        raise ZAssertionError(
            "not isinstance",
            a=a,
            type_a=type(a),
            type_type_a=type(type(a)),
            C=C,
            type_C=type(C),
        )


def assert_issubclass(A: type, C: type) -> None:
    if not issubclass(A, C):  # pragma: no cover
        raise ZAssertionError("not issubclass", A=A, C=C, type_A=type(A), type_C=type(C))


def nottest(func: F) -> F:
    """Decorator to mark a function or method as *not* a test"""
    func.__test__ = False
    return func


def istest(func: F) -> F:
    """Decorator to mark a function or method as a test"""
    func.__test__ = True
    return func
