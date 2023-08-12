from typing import List, Optional

from pydantic import BaseModel, ConfigDict


class Settings(BaseModel):
    """
    Settings for a prompt run that a user can configure.
    """

    model_alias: Optional[str] = None
    temperature: Optional[float] = None
    max_tokens: Optional[int] = None
    stop_sequences: Optional[List[str]] = None

    top_p: Optional[int] = None
    frequency_penalty: Optional[float] = None
    presence_penalty: Optional[float] = None

    # Avoid Pydantic's protected namespace warning since we want to use
    # `model_alias` as a field name.
    model_config = ConfigDict(protected_namespaces=())
