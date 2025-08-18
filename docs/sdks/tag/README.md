# Tag
(*tag*)

## Overview

### Available Operations

* [add_tag_config](#add_tag_config) - Add Tag Config
* [get_tag_config](#get_tag_config) - Get Tag Config
* [update_tag_config](#update_tag_config) - Update Tag Config
* [delete_tag_config](#delete_tag_config) - Delete Tag Config
* [add_tag_table_info](#add_tag_table_info) - Add Tag Table Info
* [get_tag_table_info](#get_tag_table_info) - Get Tag Table Info
* [update_tag_table_info](#update_tag_table_info) - Update Tag Table Info
* [delete_tag_table_info](#delete_tag_table_info) - Delete Tag Table Info
* [get_all_tag_table_info](#get_all_tag_table_info) - Get All Tag Table Info
* [add_tag_column_info](#add_tag_column_info) - Add Tag Column Info
* [get_tag_column_info](#get_tag_column_info) - Get Tag Column Info
* [update_tag_column_info](#update_tag_column_info) - Update Tag Column Info
* [get_all_tag_column_info](#get_all_tag_column_info) - Get All Tag Column Info
* [delete_tag_column_info](#delete_tag_column_info) - Delete Tag Column Info

## add_tag_config

Add Tag Config

### Example Usage

<!-- UsageSnippet language="python" operationID="add_tag_config" method="post" path="/datasource/{datasource_id}/tag_config" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.tag.add_tag_config(datasource_id="<id>", working_bucket="<value>", customer_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `working_bucket`                                                    | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `customer_id`                                                       | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | Customer ID                                                         |
| `description`                                                       | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `logical_group_regex`                                               | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `db_path`                                                           | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AddTagConfigResponse](../../models/addtagconfigresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_tag_config

Get Tag Config

### Example Usage

<!-- UsageSnippet language="python" operationID="get_tag_config" method="get" path="/datasource/{datasource_id}/tag_config" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.tag.get_tag_config(datasource_id="<id>", customer_id="<id>")

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

**[models.TagConfig](../../models/tagconfig.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## update_tag_config

Update Tag Config

### Example Usage

<!-- UsageSnippet language="python" operationID="update_tag_config" method="put" path="/datasource/{datasource_id}/tag_config" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.tag.update_tag_config(datasource_id="<id>", customer_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `customer_id`                                                       | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | Customer ID                                                         |
| `description`                                                       | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `logical_group_regex`                                               | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `working_bucket`                                                    | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `db_path`                                                           | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UpdateTagConfigResponse](../../models/updatetagconfigresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## delete_tag_config

Delete Tag Config

### Example Usage

<!-- UsageSnippet language="python" operationID="delete_tag_config" method="delete" path="/datasource/{datasource_id}/tag_config" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.tag.delete_tag_config(datasource_id="<id>", customer_id="<id>")

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

**[str](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## add_tag_table_info

Add Tag Table Info

### Example Usage

<!-- UsageSnippet language="python" operationID="add_tag_table_info" method="post" path="/datasource/{datasource_id}/tag_table_info/{table_name}" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.tag.add_tag_table_info(datasource_id="<id>", table_name="<value>", customer_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `table_name`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `customer_id`                                                       | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | Customer ID                                                         |
| `description`                                                       | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AddTagTableResponse](../../models/addtagtableresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_tag_table_info

Get Tag Table Info

### Example Usage

<!-- UsageSnippet language="python" operationID="get_tag_table_info" method="get" path="/datasource/{datasource_id}/tag_table_info/{table_name}" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.tag.get_tag_table_info(datasource_id="<id>", table_name="<value>", customer_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `table_name`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `customer_id`                                                       | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | Customer ID                                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TagTableInfo](../../models/tagtableinfo.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## update_tag_table_info

Update Tag Table Info

### Example Usage

<!-- UsageSnippet language="python" operationID="update_tag_table_info" method="put" path="/datasource/{datasource_id}/tag_table_info/{table_name}" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.tag.update_tag_table_info(datasource_id="<id>", table_name="<value>", customer_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `table_name`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `customer_id`                                                       | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | Customer ID                                                         |
| `description`                                                       | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UpdateTagTableResponse](../../models/updatetagtableresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## delete_tag_table_info

Delete Tag Table Info

### Example Usage

<!-- UsageSnippet language="python" operationID="delete_tag_table_info" method="delete" path="/datasource/{datasource_id}/tag_table_info/{table_name}" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.tag.delete_tag_table_info(datasource_id="<id>", table_name="<value>", customer_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `table_name`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `customer_id`                                                       | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | Customer ID                                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteTagTableResponse](../../models/deletetagtableresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_all_tag_table_info

Get All Tag Table Info

### Example Usage

<!-- UsageSnippet language="python" operationID="get_all_tag_table_info" method="get" path="/datasource/{datasource_id}/tag_table_info" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.tag.get_all_tag_table_info(datasource_id="<id>", offset=0, limit=10, customer_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `offset`                                                            | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Number of items to skip                                             |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Maximum number of items to return                                   |
| `sort_by`                                                           | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | Field to sort by                                                    |
| `sort_order`                                                        | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | Sort order (asc or desc)                                            |
| `customer_id`                                                       | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | Customer ID                                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.TagTableInfo]](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## add_tag_column_info

Add Tag Column Info

### Example Usage

<!-- UsageSnippet language="python" operationID="add_tag_column_info" method="post" path="/datasource/{datasource_id}/tag_table_info/{table_name}/column_info/{column_name}" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.tag.add_tag_column_info(datasource_id="<id>", table_name="<value>", column_name="<value>", customer_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `table_name`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `column_name`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `customer_id`                                                       | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | Customer ID                                                         |
| `description`                                                       | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `dtype`                                                             | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `is_key`                                                            | *OptionalNullable[bool]*                                            | :heavy_minus_sign:                                                  | N/A                                                                 |
| `is_indexed`                                                        | *OptionalNullable[bool]*                                            | :heavy_minus_sign:                                                  | N/A                                                                 |
| `engineered_features`                                               | List[*str*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AddTagColumnResponse](../../models/addtagcolumnresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_tag_column_info

Get Tag Column Info

### Example Usage

<!-- UsageSnippet language="python" operationID="get_tag_column_info" method="get" path="/datasource/{datasource_id}/tag_table_info/{table_name}/column_info/{column_name}" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.tag.get_tag_column_info(datasource_id="<id>", table_name="<value>", column_name="<value>", customer_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `table_name`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `column_name`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `customer_id`                                                       | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | Customer ID                                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TagColumnInfo](../../models/tagcolumninfo.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## update_tag_column_info

Update Tag Column Info

### Example Usage

<!-- UsageSnippet language="python" operationID="update_tag_column_info" method="put" path="/datasource/{datasource_id}/tag_table_info/{table_name}/column_info/{column_name}" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.tag.update_tag_column_info(datasource_id="<id>", table_name="<value>", column_name="<value>", customer_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `table_name`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `column_name`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `customer_id`                                                       | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | Customer ID                                                         |
| `description`                                                       | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `dtype`                                                             | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `is_key`                                                            | *OptionalNullable[bool]*                                            | :heavy_minus_sign:                                                  | N/A                                                                 |
| `is_indexed`                                                        | *OptionalNullable[bool]*                                            | :heavy_minus_sign:                                                  | N/A                                                                 |
| `engineered_features`                                               | List[*str*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UpdateTagColumnResponse](../../models/updatetagcolumnresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_all_tag_column_info

Get All Tag Column Info

### Example Usage

<!-- UsageSnippet language="python" operationID="get_all_tag_column_info" method="get" path="/datasource/{datasource_id}/tag_table_info/{table_name}/column_info" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.tag.get_all_tag_column_info(datasource_id="<id>", table_name="<value>", offset=0, limit=10, customer_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `table_name`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `offset`                                                            | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Number of items to skip                                             |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Maximum number of items to return                                   |
| `sort_by`                                                           | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | Field to sort by                                                    |
| `sort_order`                                                        | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | Sort order (asc or desc)                                            |
| `customer_id`                                                       | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | Customer ID                                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.TagColumnInfo]](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## delete_tag_column_info

Delete Tag Column Info

### Example Usage

<!-- UsageSnippet language="python" operationID="delete_tag_column_info" method="delete" path="/datasource/{datasource_id}/tag_config/{table_name}/column_info/{column_name}" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.tag.delete_tag_column_info(datasource_id="<id>", table_name="<value>", column_name="<value>", customer_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `table_name`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `column_name`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `customer_id`                                                       | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | Customer ID                                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteTagTableResponse](../../models/deletetagtableresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |