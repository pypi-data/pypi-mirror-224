import inspect
from typing import Dict, Optional
from uuid import UUID

from pydantic import BaseModel

from sdk import globals
from sdk.constants.enums import Mode
from sdk.primitive import Primitive


class ContextKey(BaseModel):
    key: str


class Context:
    def __getitem__(self, key):
        return ContextKey(key=key)


class Task(BaseModel):
    name: str
    mode: Mode
    primitives: Dict[UUID, Primitive] = {}
    result: Optional[UUID] = None

    def add_primitive(self, primitive):
        self.primitives[primitive.id] = primitive

    # TODO (LLM-616): We need to issue a request to the backend to actually run the task.
    def __call__(self, context: Optional[Dict] = None) -> Dict:
        if self.mode == Mode.BATCH:
            assert context is None, "Batch task must not have a context"
        elif self.mode == Mode.REAL_TIME:
            assert context is not None, "Real-time task must have a context"
            assert isinstance(context, Dict), "Context must be a dictionary"

            # Extracting all keys required by primitives
            required_keys = {
                key for primitive in self.primitives.values() for key in primitive.context_keys
            }

            # Checking if all required keys are present in context
            if not all(key in context for key in required_keys):
                missing_keys = [key for key in required_keys if key not in context]
                raise ValueError(f"Context is missing the following required keys: {missing_keys}")

        data = self.dict(exclude_none=True)
        if context:
            data["context"] = context

        return data


def task(name: str, mode: str):
    mode = Mode(mode)  # Convert the string to the Mode enum
    if mode not in Mode:  # Check if the mode is valid
        raise ValueError(f"Invalid mode: {mode}")

    def decorator(func):
        sig = inspect.signature(func)
        if mode == Mode.REAL_TIME:
            if len(sig.parameters) != 1 or "context" not in sig.parameters:
                raise TypeError("Real-time task function must accept a single argument 'context'")
        elif mode == Mode.BATCH:
            if len(sig.parameters) != 0:
                raise TypeError("Batch task function must accept no arguments")

        try:
            globals.current_task = Task(name=name, mode=mode)
            if mode == Mode.REAL_TIME:
                context = Context()
                result = func(context)
                assert isinstance(result, Primitive), "Real-time task must return a Primitive"
                globals.current_task.result = result.id
            else:
                result = func()
                assert result is None, "Batch task must not return anything"
            task_instance = globals.current_task
        finally:
            # Always set current_task to None, even if an exception was thrown
            globals.current_task = None
        return task_instance

    return decorator
