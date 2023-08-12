from typing import List, Union
from uuid import UUID, uuid4

from pydantic import BaseModel


class Primitive(BaseModel):
    id: UUID
    dependencies: List[UUID]
    context_keys: List[str]
    inputs: List[Union[UUID, str]]

    # This is a sample implementation of a custom primitive
    # that takes in an arbitrary number of inputs, each of which
    # can be either a Primitive or a ContextKey.
    # @Hari feel free to change this in your implementation
    def __init__(self, *args):
        from sdk import globals
        from sdk.task import ContextKey, Task

        dependencies = []
        context_keys = []
        # After initialization, inputs will be a list of Primitive IDs
        # and ContextKey keys. Using this info, the backend can
        # run the Primitive with the correct list of inputs.
        inputs = []

        for input_item in args:
            if isinstance(input_item, Primitive):
                dependencies.append(input_item.id)
                inputs.append(input_item.id)
            elif isinstance(input_item, ContextKey):
                context_keys.append(input_item.key)
                inputs.append(input_item.key)
            else:
                raise ValueError("Input must be either of type Primitive or ContextKey")

        super().__init__(
            id=uuid4(), dependencies=dependencies, context_keys=context_keys, inputs=inputs
        )

        # We assume Primitives are always initialized within a task
        assert globals.current_task is not None, "No current task"
        assert isinstance(globals.current_task, Task), "Current task is not a Task"
        globals.current_task.add_primitive(self)
