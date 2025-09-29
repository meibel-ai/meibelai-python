# Executions
(*blueprints.executions*)

## Overview

work with executions of blueprints

### Available Operations

* [start_blueprint_instance](#start_blueprint_instance) - Start Blueprint Instance
* [cancel_blueprint_instance](#cancel_blueprint_instance) - Cancel Blueprint Instance
* [send_signal](#send_signal) - Send Signal
* [query_workflow](#query_workflow) - Query Workflow
* [chat_with_blueprint](#chat_with_blueprint) - Chat With Blueprint

## start_blueprint_instance

Start Blueprint Instance

### Example Usage

<!-- UsageSnippet language="python" operationID="startBlueprintInstance" method="post" path="/{blueprint_instance_id}/start-instance" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.blueprints.executions.start_blueprint_instance(blueprint_instance_id="<id>", workflow_args=None, workflow_kwargs={
        "key": "<value>",
        "key1": "<value>",
        "key2": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `blueprint_instance_id`                                             | *str*                                                               | :heavy_check_mark:                                                  | Unique identifier for the workflow instance                         |
| `workflow_args`                                                     | List[*Any*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `workflow_kwargs`                                                   | Dict[str, *Any*]                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## cancel_blueprint_instance

Cancel Blueprint Instance

### Example Usage

<!-- UsageSnippet language="python" operationID="cancelBlueprintInstance" method="post" path="/{blueprint_instance_id}/cancel-instance" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.blueprints.executions.cancel_blueprint_instance(blueprint_instance_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `blueprint_instance_id`                                             | *str*                                                               | :heavy_check_mark:                                                  | Unique identifier for the workflow instance                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## send_signal

Send Signal

### Example Usage

<!-- UsageSnippet language="python" operationID="sendSignal" method="post" path="/{blueprint_instance_id}/signals/{signal_name}" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.blueprints.executions.send_signal(blueprint_instance_id="<id>", signal_name="<value>", request_body=[
        "<value 1>",
        "<value 2>",
        "<value 3>",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `blueprint_instance_id`                                             | *str*                                                               | :heavy_check_mark:                                                  | Unique identifier for the workflow instance                         |
| `signal_name`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Name of the signal to send                                          |
| `request_body`                                                      | List[*Any*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## query_workflow

Query Workflow

### Example Usage

<!-- UsageSnippet language="python" operationID="queryWorkflow" method="post" path="/{blueprint_instance_id}/queries/{query_name}" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.blueprints.executions.query_workflow(blueprint_instance_id="<id>", query_name="<value>", request_body=[
        "<value 1>",
        "<value 2>",
        "<value 3>",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `blueprint_instance_id`                                             | *str*                                                               | :heavy_check_mark:                                                  | Unique identifier for the workflow instance                         |
| `query_name`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Name of the query to execute                                        |
| `request_body`                                                      | List[*Any*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## chat_with_blueprint

Chat endpoint that queries current state, sends a signal, then polls until the list changes.

Args:
    blueprint_instance_id: Unique identifier for the workflow instance
    user_message: User message to send
    query_name: Name of the query to poll
    signal_args: Optional arguments for the signal
    query_args: Optional arguments for the query
    max_wait_seconds: Maximum time to wait for a response (default: 30 seconds)
    poll_interval_seconds: Interval between query polls (default: 1.0 seconds)
    min_new_items: Minimum new items to wait for (default: 2 for signal + response)

Returns:
    The updated query response when the list changes sufficiently

Raises:
    HTTPException: If timeout is reached or other errors occur

### Example Usage

<!-- UsageSnippet language="python" operationID="chatWithBlueprint" method="post" path="/{blueprint_instance_id}/chat" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.blueprints.executions.chat_with_blueprint(blueprint_instance_id="<id>", user_message="<value>", signal_name="incoming_chat_message", query_name="GetWorkflowState", max_wait_seconds=30, poll_interval_seconds=1, min_new_items=1, request_body=[
        "<value 1>",
        "<value 2>",
        "<value 3>",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `blueprint_instance_id`                                             | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `user_message`                                                      | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `signal_name`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `query_name`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `max_wait_seconds`                                                  | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `poll_interval_seconds`                                             | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `min_new_items`                                                     | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `request_body`                                                      | List[*Any*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |