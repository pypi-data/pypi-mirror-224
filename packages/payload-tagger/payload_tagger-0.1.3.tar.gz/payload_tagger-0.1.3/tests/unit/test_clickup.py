"""Test clickup."""
from __future__ import annotations

from typing import Any

import pytest

from payload_tagger import clickup, errors


@pytest.mark.unit()
@pytest.mark.parametrize(
    argnames=["payload", "expected"],
    argvalues=[
        (
            {
                "event": "taskCreated",
                "history_items": [
                    {
                        "id": "2800763136717140857",
                        "type": 1,
                        "date": "1642734631523",
                        "field": "status",
                        "parent_id": "162641062",
                        "data": {
                            "status_type": "open",
                        },
                        "source": None,
                        "user": {
                            "id": 183,
                            "username": "John",
                            "email": "john@company.com",
                            "color": "#7b68ee",
                            "initials": "J",
                            "profilePicture": None,
                        },
                        "before": {
                            "status": None,
                            "color": "#000000",
                            "type": "removed",
                            "orderindex": -1,
                        },
                        "after": {
                            "status": "to do",
                            "color": "#f9d900",
                            "orderindex": 0,
                            "type": "open",
                        },
                    },
                    {
                        "id": "2800763136700363640",
                        "type": 1,
                        "date": "1642734631523",
                        "field": "task_creation",
                        "parent_id": "162641062",
                        "data": {},
                        "source": None,
                        "user": {
                            "id": 183,
                            "username": "John",
                            "email": "john@company.com",
                            "color": "#7b68ee",
                            "initials": "J",
                            "profilePicture": None,
                        },
                        "before": None,
                        "after": None,
                    },
                ],
                "task_id": "1vj37mc",
                "webhook_id": "7fa3ec74-69a8-4530-a251-8a13730bd204",
            },
            "taskCreated",
        ),
        (
            {
                "event": "taskUpdated",
                "history_items": [
                    {
                        "id": "2800768061568222238",
                        "type": 1,
                        "date": "1642734925064",
                        "field": "content",
                        "parent_id": "162641062",
                        "data": {},
                        "source": None,
                        "user": {
                            "id": 183,
                            "username": "John",
                            "email": "john@company.com",
                            "color": "#7b68ee",
                            "initials": "J",
                            "profilePicture": None,
                        },
                        "before": None,
                        "after": '{"ops":[{"insert":"This is a task description update to trigger the "},{"insert":"\\n","attributes":{"block-id":"block-24d0457c-908f-412c-8267-da08f8dc93e4"}}]}',  # noqa: E501
                    },
                ],
                "task_id": "1vj37mc",
                "webhook_id": "7fa3ec74-69a8-4530-a251-8a13730bd204",
            },
            "taskUpdated",
        ),
        (
            {
                "event": "taskUpdated",
                "history_items": [
                    {
                        "id": "2800771175285296851",
                        "type": 1,
                        "date": "1642735110657",
                        "field": "custom_field",
                        "parent_id": "162641062",
                        "data": {},
                        "source": None,
                        "user": {
                            "id": 183,
                            "username": "John",
                            "email": "john@company.com",
                            "color": "#7b68ee",
                            "initials": "J",
                            "profilePicture": None,
                        },
                        "before": None,
                        "after": "5048f827-f16a-47b0-afec-5fd0e51b5f50",
                        "custom_field": {
                            "id": "862a38bb-eaba-4b9b-a4b5-c09d2a8c082f",
                            "name": "Selection Dropdown",
                            "type": "drop_down",
                            "type_config": {
                                "default": 0,
                                "placeholder": None,
                                "new_drop_down": True,
                                "options": [
                                    {
                                        "id": "5048f827-f16a-47b0-afec-5fd0e51b5f50",  # noqa: E501
                                        "name": "Monthly",
                                        "value": "Monthly",
                                        "type": "text",
                                        "color": None,
                                        "orderindex": 0,
                                    },
                                    {
                                        "id": "5c69d237-f440-4498-ae46-3b3948db931b",  # noqa: E501
                                        "name": "Quarterly",
                                        "value": "Quarterly",
                                        "type": "text",
                                        "color": None,
                                        "orderindex": 1,
                                    },
                                    {
                                        "id": "fc4b63d1-d4d5-45fc-bee5-3adef2b15dff",  # noqa: E501
                                        "name": "Yearly",
                                        "value": "Yearly",
                                        "type": "text",
                                        "color": None,
                                        "orderindex": 2,
                                    },
                                    {
                                        "id": "8c7a4048-53fd-455a-82ba-ecf2a8a4c74d",  # noqa: E501
                                        "name": "here's a really long long long drop down option with a long line of text",  # noqa: E501
                                        "value": "here's a really long long long drop down option with a long line of text",  # noqa: E501
                                        "type": "text",
                                        "color": None,
                                        "orderindex": 3,
                                    },
                                ],
                            },
                            "values_set": None,
                            "userid": "2770032",
                            "date_created": "1611729648993",
                            "hide_from_guests": False,
                            "team_id": "6931406",
                            "deleted": False,
                            "deleted_by": None,
                            "pinned": True,
                            "required": False,
                            "required_on_subtasks": False,
                            "linked_subcategory": None,
                        },
                    },
                ],
                "task_id": "1vj37mc",
                "webhook_id": "7fa3ec74-69a8-4530-a251-8a13730bd204",
            },
            "taskUpdated",
        ),
        (
            {
                "event": "taskDeleted",
                "task_id": "1vj37mc",
                "webhook_id": "7fa3ec74-69a8-4530-a251-8a13730bd204",
            },
            "taskDeleted",
        ),
        (
            {
                "event": "taskPriorityUpdated",
                "history_items": [
                    {
                        "id": "2800773800802162647",
                        "type": 1,
                        "date": "1642735267148",
                        "field": "priority",
                        "parent_id": "162641062",
                        "data": {},
                        "source": None,
                        "user": {
                            "id": 183,
                            "username": "John",
                            "email": "john@company.com",
                            "color": "#7b68ee",
                            "initials": "J",
                            "profilePicture": None,
                        },
                        "before": None,
                        "after": {
                            "id": "2",
                            "priority": "high",
                            "color": "#ffcc00",
                            "orderindex": "2",
                        },
                    },
                ],
                "task_id": "1vj38vv",
                "webhook_id": "7fa3ec74-69a8-4530-a251-8a13730bd204",
            },
            "taskPriorityUpdated",
        ),
        (
            {
                "event": "taskStatusUpdated",
                "history_items": [
                    {
                        "id": "2800787326392370170",
                        "type": 1,
                        "date": "1642736073330",
                        "field": "status",
                        "parent_id": "162641062",
                        "data": {
                            "status_type": "custom",
                        },
                        "source": None,
                        "user": {
                            "id": 183,
                            "username": "John",
                            "email": "john@company.com",
                            "color": "#7b68ee",
                            "initials": "J",
                            "profilePicture": None,
                        },
                        "before": {
                            "status": "to do",
                            "color": "#f9d900",
                            "orderindex": 0,
                            "type": "open",
                        },
                        "after": {
                            "status": "in progress",
                            "color": "#7C4DFF",
                            "orderindex": 1,
                            "type": "custom",
                        },
                    },
                ],
                "task_id": "1vj38vv",
                "webhook_id": "7fa3ec74-69a8-4530-a251-8a13730bd204",
            },
            "taskStatusUpdated",
        ),
        (
            {
                "event": "taskAssigneeUpdated",
                "history_items": [
                    {
                        "id": "2800789353868594308",
                        "type": 1,
                        "date": "1642736194135",
                        "field": "assignee_add",
                        "parent_id": "162641062",
                        "data": {},
                        "source": None,
                        "user": {
                            "id": 183,
                            "username": "John",
                            "email": "john@company.com",
                            "color": "#7b68ee",
                            "initials": "J",
                            "profilePicture": None,
                        },
                        "after": {
                            "id": 184,
                            "username": "Sam",
                            "email": "sam@company.com",
                            "color": "#7b68ee",
                            "initials": "S",
                            "profilePicture": None,
                        },
                    },
                ],
                "task_id": "1vj38vv",
                "webhook_id": "7fa3ec74-69a8-4530-a251-8a13730bd204",
            },
            "taskAssigneeUpdated",
        ),
        (
            {
                "event": "taskDueDateUpdated",
                "history_items": [
                    {
                        "id": "2800792714143635886",
                        "type": 1,
                        "date": "1642736394447",
                        "field": "due_date",
                        "parent_id": "162641062",
                        "data": {
                            "due_date_time": True,
                            "old_due_date_time": False,
                        },
                        "source": None,
                        "user": {
                            "id": 183,
                            "username": "John",
                            "email": "john@company.com",
                            "color": "#7b68ee",
                            "initials": "J",
                            "profilePicture": None,
                        },
                        "before": "1642701600000",
                        "after": "1643608800000",
                    },
                ],
                "task_id": "1vj38vv",
                "webhook_id": "7fa3ec74-69a8-4530-a251-8a13730bd204",
            },
            "taskDueDateUpdated",
        ),
        (
            {
                "event": "taskTagUpdated",
                "history_items": [
                    {
                        "id": "2800797048554170804",
                        "type": 1,
                        "date": "1642736652800",
                        "field": "tag",
                        "parent_id": "162641062",
                        "data": {},
                        "source": None,
                        "user": {
                            "id": 183,
                            "username": "John",
                            "email": "john@company.com",
                            "color": "#7b68ee",
                            "initials": "J",
                            "profilePicture": None,
                        },
                        "before": None,
                        "after": [
                            {
                                "name": "def",
                                "tag_fg": "#FF4081",
                                "tag_bg": "#FF4081",
                                "creator": 2770032,
                            },
                        ],
                    },
                ],
                "task_id": "1vj38vv",
                "webhook_id": "7fa3ec74-69a8-4530-a251-8a13730bd204",
            },
            "taskTagUpdated",
        ),
        (
            {
                "event": "taskMoved",
                "history_items": [
                    {
                        "id": "2800800851630274181",
                        "type": 1,
                        "date": "1642736879339",
                        "field": "section_moved",
                        "parent_id": "162641285",
                        "data": {
                            "mute_notifications": True,
                        },
                        "source": None,
                        "user": {
                            "id": 183,
                            "username": "John",
                            "email": "john@company.com",
                            "color": "#7b68ee",
                            "initials": "J",
                            "profilePicture": None,
                        },
                        "before": {
                            "id": "162641062",
                            "name": "Webhook payloads",
                            "category": {
                                "id": "96771950",
                                "name": "hidden",
                                "hidden": True,
                            },
                            "project": {
                                "id": "7002367",
                                "name": "This is my API Space",
                            },
                        },
                        "after": {
                            "id": "162641285",
                            "name": "webhook payloads 2",
                            "category": {
                                "id": "96772049",
                                "name": "hidden",
                                "hidden": True,
                            },
                            "project": {
                                "id": "7002367",
                                "name": "This is my API Space",
                            },
                        },
                    },
                ],
                "task_id": "1vj38vv",
                "webhook_id": "7fa3ec74-69a8-4530-a251-8a13730bd204",
            },
            "taskMoved",
        ),
        (
            {
                "event": "taskCommentPosted",
                "history_items": [
                    {
                        "id": "2800803631413624919",
                        "type": 1,
                        "date": "1642737045116",
                        "field": "comment",
                        "parent_id": "162641285",
                        "data": {},
                        "source": None,
                        "user": {
                            "id": 183,
                            "username": "John",
                            "email": "john@company.com",
                            "color": "#7b68ee",
                            "initials": "J",
                            "profilePicture": None,
                        },
                        "before": None,
                        "after": "648893191",
                        "comment": {
                            "id": "648893191",
                            "date": "1642737045116",
                            "parent": "1vj38vv",
                            "type": 1,
                            "comment": [
                                {
                                    "text": "comment abc1234",
                                    "attributes": {},
                                },
                                {
                                    "text": "\n",
                                    "attributes": {
                                        "block-id": "block-4c8fe54f-7bff-4b7b-92a2-9142068983ea",  # noqa: E501
                                    },
                                },
                            ],
                            "text_content": "comment abc1234\n",
                            "x": None,
                            "y": None,
                            "image_y": None,
                            "image_x": None,
                            "page": None,
                            "comment_number": None,
                            "page_id": None,
                            "page_name": None,
                            "view_id": None,
                            "view_name": None,
                            "team": None,
                            "user": {
                                "id": 183,
                                "username": "John",
                                "email": "john@company.com",
                                "color": "#7b68ee",
                                "initials": "J",
                                "profilePicture": None,
                            },
                            "new_thread_count": 0,
                            "new_mentioned_thread_count": 0,
                            "email_attachments": [],
                            "threaded_users": [],
                            "threaded_replies": 0,
                            "threaded_assignees": 0,
                            "threaded_assignees_members": [],
                            "threaded_unresolved_count": 0,
                            "thread_followers": [
                                {
                                    "id": 183,
                                    "username": "John",
                                    "email": "john@company.com",
                                    "color": "#7b68ee",
                                    "initials": "J",
                                    "profilePicture": None,
                                },
                            ],
                            "group_thread_followers": [],
                            "reactions": [],
                            "emails": [],
                        },
                    },
                ],
                "task_id": "1vj38vv",
                "webhook_id": "7fa3ec74-69a8-4530-a251-8a13730bd204",
            },
            "taskCommentPosted",
        ),
        (
            {
                "event": "taskCommentUpdated",
                "history_items": [
                    {
                        "id": "2800803631413624919",
                        "type": 1,
                        "date": "1642737045116",
                        "field": "comment",
                        "parent_id": "162641285",
                        "data": {},
                        "source": None,
                        "user": {
                            "id": 183,
                            "username": "John",
                            "email": "john@company.com",
                            "color": "#7b68ee",
                            "initials": "J",
                            "profilePicture": None,
                        },
                        "before": None,
                        "after": "648893191",
                        "comment": {
                            "id": "648893191",
                            "date": "1642737045116",
                            "parent": "1vj38vv",
                            "type": 1,
                            "comment": [
                                {
                                    "text": "comment abc1234 56789",
                                    "attributes": {},
                                },
                                {
                                    "text": "\n",
                                    "attributes": {
                                        "block-id": "block-4c8fe54f-7bff-4b7b-92a2-9142068983ea",  # noqa: E501
                                    },
                                },
                            ],
                            "text_content": "comment abc1234 56789\n",
                            "x": None,
                            "y": None,
                            "image_y": None,
                            "image_x": None,
                            "page": None,
                            "comment_number": None,
                            "page_id": None,
                            "page_name": None,
                            "view_id": None,
                            "view_name": None,
                            "team": None,
                            "user": {
                                "id": 183,
                                "username": "John",
                                "email": "john@company.com",
                                "color": "#7b68ee",
                                "initials": "J",
                                "profilePicture": None,
                            },
                            "new_thread_count": 0,
                            "new_mentioned_thread_count": 0,
                            "email_attachments": [],
                            "threaded_users": [],
                            "threaded_replies": 0,
                            "threaded_assignees": 0,
                            "threaded_assignees_members": [],
                            "threaded_unresolved_count": 0,
                            "thread_followers": [
                                {
                                    "id": 183,
                                    "username": "John",
                                    "email": "john@company.com",
                                    "color": "#7b68ee",
                                    "initials": "J",
                                    "profilePicture": None,
                                },
                            ],
                            "group_thread_followers": [],
                            "reactions": [],
                            "emails": [],
                        },
                    },
                ],
                "task_id": "1vj38vv",
                "webhook_id": "7fa3ec74-69a8-4530-a251-8a13730bd204",
            },
            "taskCommentUpdated",
        ),
        (
            {
                "event": "taskTimeEstimateUpdated",
                "history_items": [
                    {
                        "id": "2800808904123520175",
                        "type": 1,
                        "date": "1642737359443",
                        "field": "time_estimate",
                        "parent_id": "162641285",
                        "data": {
                            "time_estimate_string": "1 hour 30 minutes",
                            "old_time_estimate_string": None,
                            "rolled_up_time_estimate": 5400000,
                            "time_estimate": 5400000,
                            "time_estimates_by_user": [
                                {
                                    "userid": 2770032,
                                    "user_time_estimate": "5400000",
                                    "user_rollup_time_estimate": "5400000",
                                },
                            ],
                        },
                        "source": None,
                        "user": {
                            "id": 183,
                            "username": "John",
                            "email": "john@company.com",
                            "color": "#7b68ee",
                            "initials": "J",
                            "profilePicture": None,
                        },
                        "before": None,
                        "after": "5400000",
                    },
                ],
                "task_id": "1vj38vv",
                "webhook_id": "7fa3ec74-69a8-4530-a251-8a13730bd204",
            },
            "taskTimeEstimateUpdated",
        ),
        (
            {
                "event": "taskTimeTrackedUpdated",
                "history_items": [
                    {
                        "id": "2800809188061123931",
                        "type": 1,
                        "date": "1642737376354",
                        "field": "time_spent",
                        "parent_id": "162641285",
                        "data": {
                            "total_time": "900000",
                            "rollup_time": "900000",
                        },
                        "source": None,
                        "user": {
                            "id": 183,
                            "username": "John",
                            "email": "john@company.com",
                            "color": "#7b68ee",
                            "initials": "J",
                            "profilePicture": None,
                        },
                        "before": None,
                        "after": {
                            "id": "2800809188061119507",
                            "start": "1642736476215",
                            "end": "1642737376215",
                            "time": "900000",
                            "source": "clickup",
                            "date_added": "1642737376354",
                        },
                    },
                ],
                "task_id": "1vj38vv",
                "data": {
                    "description": "Time Tracking Created",
                    "interval_id": "2800809188061119507",
                },
                "webhook_id": "7fa3ec74-69a8-4530-a251-8a13730bd204",
            },
            "taskTimeTrackedUpdated",
        ),
        (
            {
                "event": "listCreated",
                "list_id": "162641234",
                "webhook_id": "7fa3ec74-69a8-4530-a251-8a13730bd204",
            },
            "listCreated",
        ),
        (
            {
                "event": "spaceUpdated",
                "space_id": "7002367",
                "webhook_id": "7fa3ec74-69a8-4530-a251-8a13730bd204",
            },
            "spaceUpdated",
        ),
        (
            {
                "event": "listUpdated",
                "history_items": [
                    {
                        "id": "8a2f82db-7718-4fdb-9493-4849e67f009d",
                        "type": 6,
                        "date": "1642740510345",
                        "field": "name",
                        "parent_id": "162641285",
                        "data": {},
                        "source": None,
                        "user": {
                            "id": 183,
                            "username": "John",
                            "email": "john@company.com",
                            "color": "#7b68ee",
                            "initials": "J",
                            "profilePicture": None,
                        },
                        "before": "webhook payloads 2",
                        "after": "Webhook payloads round 2",
                    },
                ],
                "list_id": "162641285",
                "webhook_id": "7fa3ec74-69a8-4530-a251-8a13730bd204",
            },
            "listUpdated",
        ),
        (
            {
                "event": "listDeleted",
                "list_id": "162641062",
                "webhook_id": "7fa3ec74-69a8-4530-a251-8a13730bd204",
            },
            "listDeleted",
        ),
        (
            {
                "event": "spaceCreated",
                "space_id": "54650507",
                "webhook_id": "7fa3ec74-69a8-4530-a251-8a13730bd204",
            },
            "spaceCreated",
        ),
        (
            {
                "event": "spaceDeleted",
                "space_id": "54650507",
                "webhook_id": "7fa3ec74-69a8-4530-a251-8a13730bd204",
            },
            "spaceDeleted",
        ),
        (
            {
                "event": "folderCreated",
                "folder_id": "96772212",
                "webhook_id": "7fa3ec74-69a8-4530-a251-8a13730bd204",
            },
            "folderCreated",
        ),
        (
            {
                "event": "folderUpdated",
                "folder_id": "96772212",
                "webhook_id": "7fa3ec74-69a8-4530-a251-8a13730bd204",
            },
            "folderUpdated",
        ),
        (
            {
                "event": "folderDeleted",
                "folder_id": "96772212",
                "webhook_id": "7fa3ec74-69a8-4530-a251-8a13730bd204",
            },
            "folderDeleted",
        ),
        (
            {
                "event": "goalCreated",
                "goal_id": "a23e5a3d-74b5-44c2-ab53-917ebe85045a",
                "webhook_id": "d5eddb2d-db2b-49e9-87d4-bc6cfbe2313b",
            },
            "goalCreated",
        ),
        (
            {
                "event": "goalUpdated",
                "goal_id": "a23e5a3d-74b5-44c2-ab53-917ebe85045a",
                "webhook_id": "d5eddb2d-db2b-49e9-87d4-bc6cfbe2313b",
            },
            "goalUpdated",
        ),
        (
            {
                "event": "goalDeleted",
                "goal_id": "a23e5a3d-74b5-44c2-ab53-917ebe85045a",
                "webhook_id": "d5eddb2d-db2b-49e9-87d4-bc6cfbe2313b",
            },
            "goalDeleted",
        ),
        (
            {
                "event": "keyResultCreated",
                "goal_id": "a23e5a3d-74b5-44c2-ab53-917ebe85045a",
                "key_result_id": "47608e42-ad0e-4934-a39e-950539c77e79",
                "webhook_id": "d5eddb2d-db2b-49e9-87d4-bc6cfbe2313b",
            },
            "keyResultCreated",
        ),
        (
            {
                "event": "keyResultUpdated",
                "goal_id": "a23e5a3d-74b5-44c2-ab53-917ebe85045a",
                "key_result_id": "47608e42-ad0e-4934-a39e-950539c77e79",
                "webhook_id": "d5eddb2d-db2b-49e9-87d4-bc6cfbe2313b",
            },
            "keyResultUpdated",
        ),
        (
            {
                "event": "keyResultDeleted",
                "goal_id": "a23e5a3d-74b5-44c2-ab53-917ebe85045a",
                "key_result_id": "47608e42-ad0e-4934-a39e-950539c77e79",
                "webhook_id": "d5eddb2d-db2b-49e9-87d4-bc6cfbe2313b",
            },
            "keyResultDeleted",
        ),
    ],
)
def test_identify_payload(
    payload: dict[str, Any],
    expected: clickup.SupportedPayloads,
) -> None:
    assert clickup.identify_payload(payload=payload).unwrap() == expected


@pytest.mark.unit()
@pytest.mark.parametrize(
    argnames="payload",
    argvalues=[
        {
            "event": "NotKnown",
            "goal_id": "a23e5a3d-74b5-44c2-ab53-917ebe85045a",
            "key_result_id": "47608e42-ad0e-4934-a39e-950539c77e79",
            "webhook_id": "d5eddb2d-db2b-49e9-87d4-bc6cfbe2313b",
        },
        {
            "goal_id": "a23e5a3d-74b5-44c2-ab53-917ebe85045a",
            "key_result_id": "47608e42-ad0e-4934-a39e-950539c77e79",
            "webhook_id": "d5eddb2d-db2b-49e9-87d4-bc6cfbe2313b",
        },
    ],
)
def test_not_identify_payload(payload: dict[str, Any]) -> None:
    assert isinstance(
        clickup.identify_payload(payload=payload).err(),
        errors.NotIdentifiedPayloadError,
    )
