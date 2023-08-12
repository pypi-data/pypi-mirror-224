from enum import Enum, EnumMeta
from typing import Any, Iterable, cast

"""
All these enums can be replaced with protobufs for consistency with the backend.
"""


class MetaEnum(EnumMeta):
    """Allows to very easily check if strings are present in the enum, without a helper.

    Eg.
        if "batch" in Mode:
            ...
    """

    def __contains__(cls, item: Any) -> Any:
        return item in [v.value for v in cast(Iterable[Enum], cls.__members__.values())]


class Mode(str, Enum, metaclass=MetaEnum):
    BATCH = "batch"
    REAL_TIME = "real-time"


class NotionDocumentType(str, Enum, metaclass=MetaEnum):
    PAGE = "page"
    DATABASE = "database"


class VectorDBUpdateType(str, Enum, metaclass=MetaEnum):
    APPEND = "append"
    REPLACE = "replace"


class ResourceType(str, Enum, metaclass=MetaEnum):
    LLM = "llm"
    VECTOR_DB = "vector_db"
    NOTION = "notion"
    GOOGLE_DOCS = "google_docs"
    GITHUB = "github"
    RELATIONAL_DB = "relational_db"
