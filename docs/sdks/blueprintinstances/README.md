# BlueprintInstances
(*blueprint_instances*)

## Overview

### Available Operations

* [add_blueprint_instance](#add_blueprint_instance) - Add Blueprint Instance
* [get_all_blueprint_instances](#get_all_blueprint_instances) - Get All Blueprint Instances
* [get_blueprint_instance](#get_blueprint_instance) - Get Blueprint Instance
* [delete_blueprint_instance](#delete_blueprint_instance) - Delete Blueprint Instance
* [update_blueprint_instance_status](#update_blueprint_instance_status) - Update Blueprint Instance Status
* [complete_blueprint_instance](#complete_blueprint_instance) - Complete a Blueprint Instance
* [fail_blueprint_instance](#fail_blueprint_instance) - Fail a Blueprint Instance
* [add_activity_by_blueprint_instance](#add_activity_by_blueprint_instance) - Add Activity By Blueprint Instance
* [get_activity_by_blueprint_instance](#get_activity_by_blueprint_instance) - Get Activity By Blueprint Instance
* [get_activities_by_blueprint_instance](#get_activities_by_blueprint_instance) - Get Activities By Blueprint Instance
* [update_activity_status](#update_activity_status) - Update Activity Status
* [get_event_by_blueprint_instance](#get_event_by_blueprint_instance) - Get Event By Blueprint Instance
* [create_event_by_blueprint_instance_id](#create_event_by_blueprint_instance_id) - Create Event By Blueprint Instance Id
* [get_events_by_blueprint_instance](#get_events_by_blueprint_instance) - Get Events By Blueprint Instance

## add_blueprint_instance

Add Blueprint Instance

### Example Usage

<!-- UsageSnippet language="python" operationID="add_blueprint_instance" method="post" path="/blueprint-instance/" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.blueprint_instances.add_blueprint_instance(customer_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `customer_id`                                                                 | *str*                                                                         | :heavy_check_mark:                                                            | Customer ID                                                                   |
| `blueprint_id`                                                                | *OptionalNullable[str]*                                                       | :heavy_minus_sign:                                                            | N/A                                                                           |
| `workflow_type`                                                               | *OptionalNullable[str]*                                                       | :heavy_minus_sign:                                                            | N/A                                                                           |
| `task_queue`                                                                  | *OptionalNullable[str]*                                                       | :heavy_minus_sign:                                                            | N/A                                                                           |
| `instance_metadata`                                                           | [OptionalNullable[models.InstanceMetadata]](../../models/instancemetadata.md) | :heavy_minus_sign:                                                            | N/A                                                                           |
| `parent_id`                                                                   | *OptionalNullable[str]*                                                       | :heavy_minus_sign:                                                            | N/A                                                                           |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.AddBlueprintInstanceResponse](../../models/addblueprintinstanceresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_all_blueprint_instances

Get All Blueprint Instances

### Example Usage

<!-- UsageSnippet language="python" operationID="get_all_blueprint_instances" method="get" path="/blueprint-instance/" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.blueprint_instances.get_all_blueprint_instances(customer_id="<id>", include_children=False, include_activities=False, include_events=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `customer_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Customer ID                                                         |
| `include_children`                                                  | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `include_activities`                                                | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `include_events`                                                    | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetBlueprintInstancesResponse](../../models/getblueprintinstancesresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_blueprint_instance

Get Blueprint Instance

### Example Usage

<!-- UsageSnippet language="python" operationID="get_blueprint_instance" method="get" path="/blueprint-instance/{blueprint_instance_id}" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.blueprint_instances.get_blueprint_instance(blueprint_instance_id="<id>", customer_id="<id>", include_children=False, include_activities=False, include_events=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `blueprint_instance_id`                                             | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `customer_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Customer ID                                                         |
| `include_children`                                                  | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `include_activities`                                                | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `include_events`                                                    | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetBlueprintInstancesResponse](../../models/getblueprintinstancesresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## delete_blueprint_instance

Delete Blueprint Instance

### Example Usage

<!-- UsageSnippet language="python" operationID="delete_blueprint_instance" method="delete" path="/blueprint-instance/{blueprint_instance_id}" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    m_client.blueprint_instances.delete_blueprint_instance(blueprint_instance_id="<id>", customer_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `blueprint_instance_id`                                             | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `customer_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Customer ID                                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## update_blueprint_instance_status

Update Blueprint Instance Status

### Example Usage

<!-- UsageSnippet language="python" operationID="update_blueprint_instance_status" method="put" path="/blueprint-instance/{blueprint_instance_id}/status" -->
```python
import meibelai
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    m_client.blueprint_instances.update_blueprint_instance_status(blueprint_instance_id="<id>", updated_status_value=meibelai.BlueprintInstanceStatus.CANCELLED, customer_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `blueprint_instance_id`                                                   | *str*                                                                     | :heavy_check_mark:                                                        | N/A                                                                       |
| `updated_status_value`                                                    | [models.BlueprintInstanceStatus](../../models/blueprintinstancestatus.md) | :heavy_check_mark:                                                        | BlueprintInstanceStatus                                                   |
| `customer_id`                                                             | *str*                                                                     | :heavy_check_mark:                                                        | Customer ID                                                               |
| `workflow_run_id`                                                         | *OptionalNullable[str]*                                                   | :heavy_minus_sign:                                                        | N/A                                                                       |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## complete_blueprint_instance

This endpoint is used to mark a Blueprint Instance as completed. It will update the status of the Blueprint Instance to 'COMPLETED' and log the completion event.

### Example Usage

<!-- UsageSnippet language="python" operationID="complete_blueprint_instance" method="put" path="/blueprint-instance/{blueprint_instance_id}/complete-instance" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.blueprint_instances.complete_blueprint_instance(blueprint_instance_id="<id>", customer_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `blueprint_instance_id`                                             | *str*                                                               | :heavy_check_mark:                                                  | Unique identifier for the workflow instance                         |
| `customer_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Customer ID                                                         |
| `result`                                                            | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## fail_blueprint_instance

This endpoint is used to mark a Blueprint Instance as failed. It will update the status of the Blueprint Instance to 'FAILED' and log the failure event.

### Example Usage

<!-- UsageSnippet language="python" operationID="fail_blueprint_instance" method="put" path="/blueprint-instance/{blueprint_instance_id}/fail-instance" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.blueprint_instances.fail_blueprint_instance(blueprint_instance_id="<id>", customer_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `blueprint_instance_id`                                               | *str*                                                                 | :heavy_check_mark:                                                    | Unique identifier for the workflow instance                           |
| `customer_id`                                                         | *str*                                                                 | :heavy_check_mark:                                                    | Customer ID                                                           |
| `error`                                                               | *OptionalNullable[str]*                                               | :heavy_minus_sign:                                                    | Error message for failure                                             |
| `error_details`                                                       | [OptionalNullable[models.ErrorDetails]](../../models/errordetails.md) | :heavy_minus_sign:                                                    | N/A                                                                   |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## add_activity_by_blueprint_instance

Add Activity By Blueprint Instance

### Example Usage

<!-- UsageSnippet language="python" operationID="add_activity_by_blueprint_instance" method="post" path="/blueprint-instance/{blueprint_instance_id}/activity" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.blueprint_instances.add_activity_by_blueprint_instance(blueprint_instance_id="<id>", customer_id="<id>", activity_type="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `blueprint_instance_id`                                                                               | *str*                                                                                                 | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `customer_id`                                                                                         | *str*                                                                                                 | :heavy_check_mark:                                                                                    | Customer ID                                                                                           |
| `activity_type`                                                                                       | *str*                                                                                                 | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `input_data`                                                                                          | [OptionalNullable[models.AddActivityRequestInputData]](../../models/addactivityrequestinputdata.md)   | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `output_data`                                                                                         | [OptionalNullable[models.AddActivityRequestOutputData]](../../models/addactivityrequestoutputdata.md) | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `group_id`                                                                                            | *OptionalNullable[str]*                                                                               | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |

### Response

**[models.AddActivityResponse](../../models/addactivityresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_activity_by_blueprint_instance

Get Activity By Blueprint Instance

### Example Usage

<!-- UsageSnippet language="python" operationID="get_activity_by_blueprint_instance" method="get" path="/blueprint-instance/{blueprint_instance_id}/activity/{activity_id}" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.blueprint_instances.get_activity_by_blueprint_instance(blueprint_instance_id="<id>", activity_id="<id>", customer_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `blueprint_instance_id`                                             | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `activity_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `customer_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Customer ID                                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetActivitiesResponse](../../models/getactivitiesresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_activities_by_blueprint_instance

Get Activities By Blueprint Instance

### Example Usage

<!-- UsageSnippet language="python" operationID="get_activities_by_blueprint_instance" method="get" path="/blueprint-instance/{blueprint_instance_id}/activities" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.blueprint_instances.get_activities_by_blueprint_instance(blueprint_instance_id="<id>", customer_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `blueprint_instance_id`                                             | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `customer_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Customer ID                                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetActivitiesResponse](../../models/getactivitiesresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## update_activity_status

Update Activity Status

### Example Usage

<!-- UsageSnippet language="python" operationID="update_activity_status" method="put" path="/blueprint-instance/{blueprint_instance_id}/activity/{activity_id}/status" -->
```python
import meibelai
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    m_client.blueprint_instances.update_activity_status(blueprint_instance_id="<id>", activity_id="<id>", updated_status_value=meibelai.ActivityStatus.RUNNING, customer_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `blueprint_instance_id`                                             | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `activity_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `updated_status_value`                                              | [models.ActivityStatus](../../models/activitystatus.md)             | :heavy_check_mark:                                                  | ActivityStatus                                                      |
| `customer_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Customer ID                                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_event_by_blueprint_instance

Get Event By Blueprint Instance

### Example Usage

<!-- UsageSnippet language="python" operationID="get_event_by_blueprint_instance" method="get" path="/blueprint-instance/{blueprint_instance_id}/event/{event_id}" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.blueprint_instances.get_event_by_blueprint_instance(blueprint_instance_id="<id>", event_id="<id>", customer_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `blueprint_instance_id`                                             | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `event_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `customer_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Customer ID                                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetEventsResponse](../../models/geteventsresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## create_event_by_blueprint_instance_id

Create Event By Blueprint Instance Id

### Example Usage

<!-- UsageSnippet language="python" operationID="create_event_by_blueprint_instance_id" method="post" path="/blueprint-instance/{blueprint_instance_id}/event" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.blueprint_instances.create_event_by_blueprint_instance_id(blueprint_instance_id="<id>", customer_id="<id>", event_name="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `blueprint_instance_id`                                                                         | *str*                                                                                           | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `customer_id`                                                                                   | *str*                                                                                           | :heavy_check_mark:                                                                              | Customer ID                                                                                     |
| `event_name`                                                                                    | *str*                                                                                           | :heavy_check_mark:                                                                              | Name of the custom event being logged.                                                          |
| `activity_id`                                                                                   | *OptionalNullable[str]*                                                                         | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `details`                                                                                       | [OptionalNullable[models.CustomEventRequestDetails]](../../models/customeventrequestdetails.md) | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `group_id`                                                                                      | *OptionalNullable[str]*                                                                         | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `is_signal`                                                                                     | *OptionalNullable[bool]*                                                                        | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `is_internal`                                                                                   | *OptionalNullable[bool]*                                                                        | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `originating_signal_id`                                                                         | *OptionalNullable[str]*                                                                         | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.AddEventResponse](../../models/addeventresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_events_by_blueprint_instance

Get Events By Blueprint Instance

### Example Usage

<!-- UsageSnippet language="python" operationID="get_events_by_blueprint_instance" method="get" path="/blueprint-instance/{blueprint_instance_id}/events" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.blueprint_instances.get_events_by_blueprint_instance(blueprint_instance_id="<id>", customer_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `blueprint_instance_id`                                             | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `customer_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Customer ID                                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetEventsResponse](../../models/geteventsresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |