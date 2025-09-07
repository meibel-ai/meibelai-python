# Blueprints
(*blueprints*)

## Overview

Operations with blueprints

### Available Operations

* [get_blueprints](#get_blueprints) - Get Blueprints
* [create_blueprint](#create_blueprint) - Create Blueprint
* [get_blueprint](#get_blueprint) - Get Blueprint
* [update_blueprint](#update_blueprint) - Update Blueprint
* [delete_blueprint](#delete_blueprint) - Delete Blueprint
* [create_blueprint_task](#create_blueprint_task) - Create Blueprint Task
* [get_blueprint_tasks](#get_blueprint_tasks) - Get Blueprint Tasks
* [update_blueprint_task](#update_blueprint_task) - Update Blueprint Task
* [delete_blueprint_task](#delete_blueprint_task) - Delete Blueprint Task

## get_blueprints

Get Blueprints

### Example Usage

<!-- UsageSnippet language="python" operationID="getBlueprints" method="get" path="/blueprint/" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.blueprints.get_blueprints()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetBlueprintsResponse](../../models/getblueprintsresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## create_blueprint

Create Blueprint

### Example Usage

<!-- UsageSnippet language="python" operationID="createBlueprint" method="post" path="/blueprint/" -->
```python
import meibelai
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.blueprints.create_blueprint(name="<value>", dsl_definition=meibelai.DslDefinition.SERVERLESS_WORKFLOW_V1_0_0, version="<value>", description="hoot mmm tinted wealthy brr as inasmuch malfunction", yaml_spec_content="<value>", json_spec_content={
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
| `name`                                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `dsl_definition`                                                    | [models.DslDefinition](../../models/dsldefinition.md)               | :heavy_check_mark:                                                  | DslDefinition                                                       |
| `version`                                                           | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `description`                                                       | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `yaml_spec_content`                                                 | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `json_spec_content`                                                 | Dict[str, *Any*]                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AddBlueprintResponse](../../models/addblueprintresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_blueprint

Get Blueprint

### Example Usage

<!-- UsageSnippet language="python" operationID="getBlueprint" method="get" path="/blueprint/{blueprint_id}" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.blueprints.get_blueprint(blueprint_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `blueprint_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Blueprint](../../models/blueprint.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## update_blueprint

Update Blueprint

### Example Usage

<!-- UsageSnippet language="python" operationID="updateBlueprint" method="put" path="/blueprint/{blueprint_id}" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.blueprints.update_blueprint(blueprint_id="<id>", name="<value>", version=None, description="ride sometimes worth although into whenever indeed", dsl_definition=None, yaml_spec_content="<value>", json_spec_content={
        "key": "<value>",
        "key1": "<value>",
        "key2": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `blueprint_id`                                                          | *str*                                                                   | :heavy_check_mark:                                                      | N/A                                                                     |
| `name`                                                                  | *OptionalNullable[str]*                                                 | :heavy_minus_sign:                                                      | N/A                                                                     |
| `version`                                                               | *OptionalNullable[str]*                                                 | :heavy_minus_sign:                                                      | N/A                                                                     |
| `description`                                                           | *OptionalNullable[str]*                                                 | :heavy_minus_sign:                                                      | N/A                                                                     |
| `dsl_definition`                                                        | [OptionalNullable[models.DslDefinition]](../../models/dsldefinition.md) | :heavy_minus_sign:                                                      | N/A                                                                     |
| `yaml_spec_content`                                                     | *OptionalNullable[str]*                                                 | :heavy_minus_sign:                                                      | N/A                                                                     |
| `json_spec_content`                                                     | Dict[str, *Any*]                                                        | :heavy_minus_sign:                                                      | N/A                                                                     |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.Blueprint](../../models/blueprint.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## delete_blueprint

Delete Blueprint

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteBlueprint" method="delete" path="/blueprint/{blueprint_id}" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.blueprints.delete_blueprint(blueprint_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `blueprint_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[str](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## create_blueprint_task

Create Blueprint Task

### Example Usage

<!-- UsageSnippet language="python" operationID="createBlueprintTask" method="post" path="/blueprint/{blueprint_id}/task" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.blueprints.create_blueprint_task(blueprint_id="<id>", name="<value>", input_schema={
        "key": "<value>",
        "key1": "<value>",
    }, output_schema={
        "key": "<value>",
        "key1": "<value>",
    }, description="loyally upon around ick near miserably")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `blueprint_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `name`                                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `input_schema`                                                      | Dict[str, *Any*]                                                    | :heavy_check_mark:                                                  | N/A                                                                 |
| `output_schema`                                                     | Dict[str, *Any*]                                                    | :heavy_check_mark:                                                  | N/A                                                                 |
| `description`                                                       | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_blueprint_tasks

Get Blueprint Tasks

### Example Usage

<!-- UsageSnippet language="python" operationID="getBlueprintTasks" method="get" path="/blueprint/{blueprint_id}/task" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.blueprints.get_blueprint_tasks(blueprint_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `blueprint_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## update_blueprint_task

Update Blueprint Task

### Example Usage

<!-- UsageSnippet language="python" operationID="updateBlueprintTask" method="put" path="/blueprint/{blueprint_id}/task/{task_id}" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.blueprints.update_blueprint_task(blueprint_id="<id>", task_id="<id>", name="<value>", description="artistic degenerate knit chow obnoxiously loosely instead sleepily below", input_schema={
        "key": "<value>",
        "key1": "<value>",
        "key2": "<value>",
    }, output_schema={
        "key": "<value>",
        "key1": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `blueprint_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `task_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `name`                                                              | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `description`                                                       | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `input_schema`                                                      | Dict[str, *Any*]                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `output_schema`                                                     | Dict[str, *Any*]                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## delete_blueprint_task

Delete Blueprint Task

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteBlueprintTask" method="delete" path="/blueprint/{blueprint_id}/task/{task_id}" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.blueprints.delete_blueprint_task(blueprint_id="<id>", task_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `blueprint_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `task_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |