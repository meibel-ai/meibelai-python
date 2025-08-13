# ReferenceGraph
(*reference_graph*)

## Overview

### Available Operations

* [add_reference_graph_config](#add_reference_graph_config) - Add Reference Graph Config
* [get_reference_graph_config](#get_reference_graph_config) - Get Reference Graph Config
* [update_reference_graph_config](#update_reference_graph_config) - Update Reference Graph Config
* [delete_reference_graph_config](#delete_reference_graph_config) - Delete Reference Graph Config

## add_reference_graph_config

Add Reference Graph Config

### Example Usage

<!-- UsageSnippet language="python" operationID="add_reference_graph_config" method="post" path="/datasource/{datasource_id}/reference_graph_config" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.reference_graph.add_reference_graph_config(datasource_id="<id>", customer_id="<id>", endpoint="<value>", db_name="<value>", doc_collection="<value>", ref_collection="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `customer_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Customer ID                                                         |
| `endpoint`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `db_name`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `doc_collection`                                                    | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `ref_collection`                                                    | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AddReferenceGraphConfigResponse](../../models/addreferencegraphconfigresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_reference_graph_config

Get Reference Graph Config

### Example Usage

<!-- UsageSnippet language="python" operationID="get_reference_graph_config" method="get" path="/datasource/{datasource_id}/reference_graph_config" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.reference_graph.get_reference_graph_config(datasource_id="<id>", customer_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `customer_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Customer ID                                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ReferenceGraphConfig](../../models/referencegraphconfig.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## update_reference_graph_config

Update Reference Graph Config

### Example Usage

<!-- UsageSnippet language="python" operationID="update_reference_graph_config" method="put" path="/datasource/{datasource_id}/reference_graph_config" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.reference_graph.update_reference_graph_config(datasource_id="<id>", customer_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `customer_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Customer ID                                                         |
| `endpoint`                                                          | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `db_name`                                                           | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `doc_collection`                                                    | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `ref_collection`                                                    | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UpdateReferenceGraphConfigResponse](../../models/updatereferencegraphconfigresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## delete_reference_graph_config

Delete Reference Graph Config

### Example Usage

<!-- UsageSnippet language="python" operationID="delete_reference_graph_config" method="delete" path="/datasource/{datasource_id}/reference_graph_config" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.reference_graph.delete_reference_graph_config(datasource_id="<id>", customer_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `customer_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Customer ID                                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteReferenceGraphConfigResponse](../../models/deletereferencegraphconfigresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |