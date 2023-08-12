from typing import Dict, List

from sdk.resources.resources import Resource
from sdk.task import Task


class Client:
    def __init__(self):
        # TODO (LLM-615): When the client is initialized, we need to issue a request to the backend
        # to get the list of connected resources.
        self.connected_resources: Dict[str, Resource] = {}

    # TODO (LLM-617): We need to issue a request to the backend to actually publish the application.
    def publish_application(self, name: str, tasks: List[Task]) -> Dict:
        return {"name": name, "tasks": [task.dict() for task in tasks]}

    def resource(self, name: str) -> Resource:
        if name in self.connected_resources:
            return self.connected_resources[name]
        else:
            # TODO (LLM-615): In case self.connected_resources is outdated, we need to issue a request
            # to the backend to get the latest list of connected resources.
            raise ValueError(f"Resource {name} is not connected")
