from pydantic import BaseModel

from sdk.constants.enums import ResourceType


class Resource(BaseModel):
    # We can add an ID field here if it's more convenient for the backend.
    name: str
    type: ResourceType
