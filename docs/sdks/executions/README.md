# Blueprints.Executions

## Overview

work with executions of blueprints

### Available Operations

* [start_blueprint_instance](#start_blueprint_instance) - Start Blueprint Instance
* [cancel_blueprint_instance](#cancel_blueprint_instance) - Cancel Blueprint Instance
* [send_signal](#send_signal) - Send Signal
* [query_workflow](#query_workflow) - Query Workflow
* [get_blueprint_instance_workflow_status](#get_blueprint_instance_workflow_status) - Get Blueprint Instance Workflow Status
* [send_chat_message](#send_chat_message) - Send Chat Message
* [send_chat_message_stream_blueprint_instance_id_chat_stream_post](#send_chat_message_stream_blueprint_instance_id_chat_stream_post) - Send a chat message and stream the response via SSE

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
    }, enable_streaming=True)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                           | Type                                                                                                                                                                | Required                                                                                                                                                            | Description                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `blueprint_instance_id`                                                                                                                                             | *str*                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                  | Unique identifier for the workflow instance                                                                                                                         |
| `workflow_args`                                                                                                                                                     | List[*Any*]                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                  | N/A                                                                                                                                                                 |
| `workflow_kwargs`                                                                                                                                                   | Dict[str, *Any*]                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                  | N/A                                                                                                                                                                 |
| `enable_streaming`                                                                                                                                                  | *OptionalNullable[bool]*                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                  | Enable streaming responses to Redis for chat workflows. When True, chat responses are streamed to Redis streams that can be consumed via the /chat/stream endpoint. |
| `retries`                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                    | :heavy_minus_sign:                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                 |

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

## get_blueprint_instance_workflow_status

Get Blueprint Instance Workflow Status

### Example Usage

<!-- UsageSnippet language="python" operationID="getBlueprintInstanceWorkflowStatus" method="get" path="/{blueprint_instance_id}/workflow-status" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.blueprints.executions.get_blueprint_instance_workflow_status(blueprint_instance_id="<id>")

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

## send_chat_message

Send Chat Message

### Example Usage

<!-- UsageSnippet language="python" operationID="sendChatMessage" method="post" path="/{blueprint_instance_id}/chat" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.blueprints.executions.send_chat_message(blueprint_instance_id="<id>", user_message="<value>", timeout_seconds=None, include_thinking=True, include_tool_activity=True)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `blueprint_instance_id`                                             | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `user_message`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The user's chat message                                             |
| `timeout_seconds`                                                   | *OptionalNullable[int]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `include_thinking`                                                  | *OptionalNullable[bool]*                                            | :heavy_minus_sign:                                                  | N/A                                                                 |
| `include_tool_activity`                                             | *OptionalNullable[bool]*                                            | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ChatMessageResponse](../../models/chatmessageresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## send_chat_message_stream_blueprint_instance_id_chat_stream_post

Send a chat message to a running chat agent workflow and stream the response as Server-Sent Events.

### Example Usage

<!-- UsageSnippet language="python" operationID="send_chat_message_stream__blueprint_instance_id__chat_stream_post" method="post" path="/{blueprint_instance_id}/chat/stream" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.blueprints.executions.send_chat_message_stream_blueprint_instance_id_chat_stream_post(blueprint_instance_id="<id>", user_message="<value>", timeout_seconds=290915, include_thinking=False, include_tool_activity=None)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `blueprint_instance_id`                                             | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `user_message`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The user's chat message                                             |
| `timeout_seconds`                                                   | *OptionalNullable[int]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `include_thinking`                                                  | *OptionalNullable[bool]*                                            | :heavy_minus_sign:                                                  | N/A                                                                 |
| `include_tool_activity`                                             | *OptionalNullable[bool]*                                            | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |