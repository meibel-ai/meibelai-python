# Executions
(*blueprints.executions*)

## Overview

work with executions of blueprints

### Available Operations

* [start_blueprint_instance](#start_blueprint_instance) - Start Blueprint Instance
* [cancel_blueprint_instance](#cancel_blueprint_instance) - Cancel Blueprint Instance
* [send_signal](#send_signal) - Send Signal
* [query_workflow](#query_workflow) - Query Workflow

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