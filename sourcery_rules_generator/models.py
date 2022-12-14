import re
from typing import List, Optional

from pydantic import ConstrainedStr, BaseModel, Field

RULE_ID_REGEX = re.compile("^[A-Za-z][A-Za-z0-9-_/:]*$")


class RuleString(ConstrainedStr):
    max_length = 88
    regex = RULE_ID_REGEX


class PathsConfig(BaseModel):
    include: Optional[List[str]]
    exclude: Optional[List[str]]


class SourceryCustomRule(BaseModel):
    id: RuleString = Field()
    description: str = Field()
    pattern: str = Field()
    replacement: Optional[str] = None
    condition: Optional[str] = None
    explanation: Optional[str] = None
    paths: Optional[PathsConfig] = None
    # tests: tuple[RuleTestConfig, ...] = ()
    tags: tuple[RuleString, ...] = ()
