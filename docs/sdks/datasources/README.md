# Datasources
(*datasources*)

## Overview

### Available Operations

* [add_datasource](#add_datasource) - Add Datasource
* [get_datasource](#get_datasource) - Get Datasource
* [update_datasource](#update_datasource) - Update Datasource
* [delete_datasource_datasource_datasource_id_delete](#delete_datasource_datasource_datasource_id_delete) - Delete Datasource
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

    res = m_client.datasources.add_datasource(customer_id="<id>", project_id="<id>", name="<value>", description="smooth hmph geez key", recurrence="<value>", customer_id_param="<value>")

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
| `customer_id_param`                                                                 | *OptionalNullable[str]*                                                             | :heavy_minus_sign:                                                                  | Customer ID                                                                         |
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

    res = m_client.datasources.get_datasource(datasource_id="<id>", customer_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `customer_id`                                                       | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | Customer ID                                                         |
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

    res = m_client.datasources.update_datasource(datasource_id="<id>", customer_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `datasource_id`                                                                     | *str*                                                                               | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `customer_id`                                                                       | *OptionalNullable[str]*                                                             | :heavy_minus_sign:                                                                  | Customer ID                                                                         |
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

## delete_datasource_datasource_datasource_id_delete

Delete Datasource

### Example Usage

<!-- UsageSnippet language="python" operationID="delete_datasource_datasource__datasource_id__delete" method="delete" path="/datasource/{datasource_id}" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.datasources.delete_datasource_datasource_datasource_id_delete(datasource_id="<id>", customer_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `customer_id`                                                       | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | Customer ID                                                         |
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

    res = m_client.datasources.get_all_datasource_ids(customer_id="<id>", project_id="<id>", offset=0, limit=10, customer_id_param="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `customer_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `project_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `offset`                                                            | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Number of items to skip                                             |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Maximum number of items to return                                   |
| `sort_by`                                                           | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | Field to sort by                                                    |
| `sort_order`                                                        | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | Sort order (asc or desc)                                            |
| `customer_id_param`                                                 | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | Customer ID                                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[str]](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |