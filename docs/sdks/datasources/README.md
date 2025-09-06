# Datasources
(*datasources*)

## Overview

### Available Operations

* [add_datasource](#add_datasource) - Add Datasource
* [get_datasource](#get_datasource) - Get Datasource
* [update_datasource](#update_datasource) - Update Datasource
* [delete_datasource](#delete_datasource) - Delete Datasource
* [get_all_datasource_ids](#get_all_datasource_ids) - Get All Datasource Ids

## add_datasource

Add Datasource

### Example Usage

<!-- UsageSnippet language="python" operationID="addDatasource" method="post" path="/datasource" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.datasources.add_datasource(customer_id="<id>", project_id="<id>", name="<value>", description="kindly kookily biodegrade after helpfully mushy unlike", recurrence="<value>", object_storage_config={
        "bucket": "<value>",
        "prefix": "<value>",
        "filters": None,
        "gcs_config": {
            "key": "<value>",
            "key1": "<value>",
        },
        "s3_config": {
            "role_arn": "<value>",
            "region": "<value>",
        },
    }, web_config={
        "base_url": "https://neighboring-fen.net/",
        "javascript_render": True,
        "wait_for_selector": "<value>",
        "domains": None,
        "authentication": {
            "username": "Eulalia35",
            "password": "VKK1aONN4LAHFVF",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `customer_id`                                                                       | *str*                                                                               | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `project_id`                                                                        | *str*                                                                               | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `name`                                                                              | *str*                                                                               | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `description`                                                                       | *str*                                                                               | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `recurrence`                                                                        | *str*                                                                               | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `object_storage_config`                                                             | [OptionalNullable[models.ObjectStorageConfig]](../../models/objectstorageconfig.md) | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `web_config`                                                                        | [OptionalNullable[models.DatasourceWebConfig]](../../models/datasourcewebconfig.md) | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.AddDatasourceResponse](../../models/adddatasourceresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_datasource

Get Datasource

### Example Usage

<!-- UsageSnippet language="python" operationID="getDatasource" method="get" path="/datasource/{datasource_id}" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.datasources.get_datasource(datasource_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Datasource](../../models/datasource.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## update_datasource

Update Datasource

### Example Usage

<!-- UsageSnippet language="python" operationID="updateDatasource" method="put" path="/datasource/{datasource_id}" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.datasources.update_datasource(datasource_id="<id>", name="<value>", description="carelessly now interestingly connect sore outrageous", recurrence="<value>", object_storage_config=None, web_config={
        "base_url": "https://quintessential-masterpiece.info/",
        "javascript_render": False,
        "wait_for_selector": "<value>",
        "domains": [
            {
                "domain": "grown-chairperson.com",
                "limit_pattern": "<value>",
                "exclude_pattern": "<value>",
                "ingestible": False,
                "expandable": True,
            },
        ],
        "authentication": {
            "username": "Craig.Torp",
            "password": "EOnNAiJTwzj27zA",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `datasource_id`                                                                     | *str*                                                                               | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `name`                                                                              | *OptionalNullable[str]*                                                             | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `description`                                                                       | *OptionalNullable[str]*                                                             | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `recurrence`                                                                        | *OptionalNullable[str]*                                                             | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `object_storage_config`                                                             | [OptionalNullable[models.ObjectStorageConfig]](../../models/objectstorageconfig.md) | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `web_config`                                                                        | [OptionalNullable[models.DatasourceWebConfig]](../../models/datasourcewebconfig.md) | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.UpdateDatasourceResponse](../../models/updatedatasourceresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## delete_datasource

Delete Datasource

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteDatasource" method="delete" path="/datasource/{datasource_id}" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.datasources.delete_datasource(datasource_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteDatasourceResponse](../../models/deletedatasourceresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_all_datasource_ids

Get All Datasource Ids

### Example Usage

<!-- UsageSnippet language="python" operationID="getAllDatasourceIds" method="post" path="/project_datasource_ids" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.datasources.get_all_datasource_ids(customer_id="<id>", project_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `customer_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[str]](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |