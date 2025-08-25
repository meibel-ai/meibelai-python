# Datasources
(*datasources*)

## Overview

Operations with datasources

### Available Operations

* [add_datasource](#add_datasource) - Add Datasource
* [get_datasource](#get_datasource) - Get Datasource
* [update_datasource](#update_datasource) - Update Datasource
* [delete_datasource](#delete_datasource) - Delete Datasource
* [get_all_datasource_ids](#get_all_datasource_ids) - Get All Datasource Ids

## add_datasource

Add Datasource

### Example Usage

<!-- UsageSnippet language="python" operationID="add_datasource" method="post" path="/datasource" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.datasources.add_datasource(customer_id="<id>", project_id="<id>", name="<value>", description="smooth hmph geez key", recurrence="<value>", object_storage_config={
        "bucket": "<value>",
        "prefix": "<value>",
        "filters": {
            "included_prefixes": [
                "<value 1>",
                "<value 2>",
            ],
            "included_file_types": [
                "<value 1>",
                "<value 2>",
                "<value 3>",
            ],
            "recursive_prefixes": True,
            "modified_date_start": "<value>",
            "modified_date_end": "<value>",
            "min_file_size": 110821,
            "max_file_size": 861343,
        },
        "gcs_config": {
            "key": "<value>",
            "key1": "<value>",
            "key2": "<value>",
        },
        "s3_config": None,
    }, web_config={
        "base_url": "https://soupy-department.biz",
        "javascript_render": False,
        "wait_for_selector": "<value>",
        "domains": [
            {
                "domain": "well-made-hygienic.com",
                "limit_pattern": "<value>",
                "exclude_pattern": "<value>",
                "ingestible": True,
                "expandable": True,
            },
        ],
        "authentication": {
            "username": "Amir_Schaden",
            "password": "Qgqx_NgZXn9ZOj5",
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

<!-- UsageSnippet language="python" operationID="get_datasource" method="get" path="/datasource/{datasource_id}" -->
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

<!-- UsageSnippet language="python" operationID="update_datasource" method="put" path="/datasource/{datasource_id}" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.datasources.update_datasource(datasource_id="<id>", name="<value>", description="amongst coordinated all", recurrence="<value>", object_storage_config={
        "bucket": "<value>",
        "prefix": None,
        "filters": {
            "included_prefixes": [
                "<value 1>",
                "<value 2>",
                "<value 3>",
            ],
            "included_file_types": [
                "<value 1>",
            ],
            "recursive_prefixes": True,
            "modified_date_start": "<value>",
            "modified_date_end": "<value>",
            "min_file_size": 289575,
            "max_file_size": 208282,
        },
        "gcs_config": {
            "key": "<value>",
            "key1": "<value>",
        },
        "s3_config": {
            "role_arn": "<value>",
            "region": "<value>",
        },
    }, web_config={
        "base_url": "https://giving-pendant.net",
        "javascript_render": True,
        "wait_for_selector": "<value>",
        "domains": [],
        "authentication": {
            "username": "Audie94",
            "password": "lD3r6ZuNUApWlV4",
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

<!-- UsageSnippet language="python" operationID="delete_datasource" method="delete" path="/datasource/{datasource_id}" -->
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

<!-- UsageSnippet language="python" operationID="get_all_datasource_ids" method="post" path="/project_datasource_ids" -->
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