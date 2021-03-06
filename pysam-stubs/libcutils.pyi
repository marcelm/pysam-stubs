from array import array
from typing import Iterable, Optional, Tuple, Union

def get_encoding_error_handler() -> str: ...
def set_encoding_error_handler(name: str) -> str: ...
def _pysam_dispatch(
    collection: str,
    method: str,
    args: Optional[Iterable[str]],
    catch_stdout: bool = ...,
    is_usage: bool = ...,
    save_stdout: Optional[str] = ...,
) -> Tuple[int, Union[bytes, str], Union[bytes, str]]: ...
def parse_region(
    contig: Optional[str] = ...,
    start: Optional[int] = ...,
    stop: Optional[int] = ...,
    region: Optional[str] = ...,
    reference: Optional[str] = ...,
    end: Optional[int] = ...,
) -> Tuple[str, int, int]: ...
def qualitystring_to_array(
    input_str: Optional[str], offset: int = ...
) -> Optional[array]: ...
def array_to_qualitystring(qualities: array, offset: int = ...) -> Optional[str]: ...
def qualities_to_qualitystring(
    qualities: Union[array, Iterable[str]], offset: int = ...
) -> Optional[str]: ...
