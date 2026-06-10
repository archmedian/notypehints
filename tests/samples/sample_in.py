from typing import (
    Annotated,
    Callable,
    ClassVar,
    Dict,
    Final,
    Generic,
    List,
    Literal,
    NamedTuple,
    Optional,
    Protocol,
    Set,
    Tuple,
    TypeVar,
    TypedDict,
)

IntList = List[int]

T = TypeVar("T")

class Person(TypedDict):
    name: str
    age: int

class Point(NamedTuple):
    x: int
    y: int

class Drawable(Protocol):
    def draw(self) -> None: ...

class Container(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value = value


def func_int(x: int) -> None:
    pass


def func_str(x: str) -> None:
    pass


def func_float(x: float) -> None:
    pass


def func_bool(x: bool) -> None:
    pass


def func_bytes(x: bytes) -> None:
    pass


def func_list(x: List[int]) -> None:
    pass


def func_dict(x: Dict[str, int]) -> None:
    pass


def func_set(x: Set[int]) -> None:
    pass


def func_tuple(x: Tuple[int, str]) -> None:
    pass


def func_optional(x: Optional[str]) -> None:
    pass


def func_union(x: int | str) -> None:
    pass


def func_callable(x: Callable[[int], str]) -> None:
    pass


def func_literal(x: Literal["a", "b"]) -> None:
    pass


CONST: Final[int] = 1


class MyClass:
    var: ClassVar[int] = 2


def func_annotated(x: Annotated[int, "meta"]) -> None:
    pass


IntListAlias = List[int]


def func_typealias(x: IntListAlias) -> None:
    pass


def func_typevar(x: T) -> T:
    return x


def func_protocol(x: Drawable) -> None:
    pass


def func_typeddict(x: Person) -> None:
    pass


def func_namedtuple(x: Point) -> None:
    pass


def func_generic(x: Container[int]) -> None:
    pass


def func_nested_list(x: List[List[int]]) -> None:
    pass


def func_nested_dict(x: Dict[str, Dict[str, int]]) -> None:
    pass


def func_nested_tuple(x: Tuple[Tuple[int, str], float]) -> None:
    pass


def func_none() -> None:
    pass

