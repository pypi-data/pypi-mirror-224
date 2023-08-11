"""ClickUp payload tagger."""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

from result import Err, Ok
from typing_extensions import Literal, TypeAlias

from payload_tagger.errors import NotIdentifiedPayloadError

if TYPE_CHECKING:
    from result import Result


SupportedPayloads: TypeAlias = Literal[
    "taskCreated",
    "taskUpdated",
    "taskDeleted",
    "taskPriorityUpdated",
    "taskStatusUpdated",
    "taskAssigneeUpdated",
    "taskDueDateUpdated",
    "taskTagUpdated",
    "taskMoved",
    "taskCommentPosted",
    "taskCommentUpdated",
    "taskTimeEstimateUpdated",
    "taskTimeTrackedUpdated",
    "listCreated",
    "listUpdated",
    "listDeleted",
    "spaceCreated",
    "spaceUpdated",
    "spaceDeleted",
    "folderCreated",
    "folderUpdated",
    "folderDeleted",
    "spaceCreated",
    "spaceUpdated",
    "spaceDeleted",
    "goalCreated",
    "goalUpdated",
    "goalDeleted",
    "keyResultCreated",
    "keyResultUpdated",
    "keyResultDeleted",
]


def identify_payload(  # noqa: C901, PLR0912, PLR0915
    payload: dict[str, Any],
) -> Result[SupportedPayloads, NotIdentifiedPayloadError]:
    """Identify ClickUp payload."""
    event_name = payload.get("event", None)
    payload_event: SupportedPayloads
    if event_name is None:
        return Err(NotIdentifiedPayloadError(payload=payload))
    if event_name == "taskCreated":
        payload_event = "taskCreated"
    elif event_name == "taskUpdated":
        payload_event = "taskUpdated"
    elif event_name == "taskDeleted":
        payload_event = "taskDeleted"
    elif event_name == "taskPriorityUpdated":
        payload_event = "taskPriorityUpdated"
    elif event_name == "taskStatusUpdated":
        payload_event = "taskStatusUpdated"
    elif event_name == "taskAssigneeUpdated":
        payload_event = "taskAssigneeUpdated"
    elif event_name == "taskDueDateUpdated":
        payload_event = "taskDueDateUpdated"
    elif event_name == "taskTagUpdated":
        payload_event = "taskTagUpdated"
    elif event_name == "taskMoved":
        payload_event = "taskMoved"
    elif event_name == "taskCommentPosted":
        payload_event = "taskCommentPosted"
    elif event_name == "taskCommentUpdated":
        payload_event = "taskCommentUpdated"
    elif event_name == "taskTimeEstimateUpdated":
        payload_event = "taskTimeEstimateUpdated"
    elif event_name == "taskTimeTrackedUpdated":
        payload_event = "taskTimeTrackedUpdated"
    elif event_name == "listCreated":
        payload_event = "listCreated"
    elif event_name == "listUpdated":
        payload_event = "listUpdated"
    elif event_name == "listDeleted":
        payload_event = "listDeleted"
    elif event_name == "spaceUpdated":
        payload_event = "spaceUpdated"
    elif event_name == "spaceCreated":
        payload_event = "spaceCreated"
    elif event_name == "spaceDeleted":
        payload_event = "spaceDeleted"
    elif event_name == "folderCreated":
        payload_event = "folderCreated"
    elif event_name == "folderUpdated":
        payload_event = "folderUpdated"
    elif event_name == "folderDeleted":
        payload_event = "folderDeleted"
    elif event_name == "goalCreated":
        payload_event = "goalCreated"
    elif event_name == "goalUpdated":
        payload_event = "goalUpdated"
    elif event_name == "goalDeleted":
        payload_event = "goalDeleted"
    elif event_name == "keyResultCreated":
        payload_event = "keyResultCreated"
    elif event_name == "keyResultUpdated":
        payload_event = "keyResultUpdated"
    elif event_name == "keyResultDeleted":
        payload_event = "keyResultDeleted"
    else:
        return Err(NotIdentifiedPayloadError(payload=payload))
    return Ok(payload_event)
