from typing import Optional

from pydantic import BaseModel

from sdk.constants.enums import NotionDocumentType, VectorDBUpdateType

"""Resource parameters for Read primitive"""


class NotionReadParams(BaseModel):
    document_type: NotionDocumentType
    url: str


class GoogleDocsReadParams(BaseModel):
    url: str


class GitHubReadParams(BaseModel):
    owner: str
    repo: str
    branch: Optional[str] = None


class RelationalDBReadParams(BaseModel):
    query: str


"""Resource parameters for Write primitive
Note that in the current design, we only support writing to Vector databases"""


class VectorDBWriteParams(BaseModel):
    index_name: str
    mode: VectorDBUpdateType


"""Resource parameters for Embed primitive"""


class LLMEmbedParams(BaseModel):
    model: str


"""Resource parameters for Retrieve primitive"""


class VectorDBRetrieveParams(BaseModel):
    index_name: str
    max_num_documents: Optional[int] = None


"""Resource parameters for Generate primitive"""


class LLMGenerateParams(BaseModel):
    model: str
