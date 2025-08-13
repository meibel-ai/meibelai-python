# DataElements
(*data_elements*)

## Overview

### Available Operations

* [add_data_element](#add_data_element) - Add Data Element
* [get_data_element](#get_data_element) - Get Data Element
* [update_data_element](#update_data_element) - Update Data Element
* [delete_data_element](#delete_data_element) - Delete Data Element
* [get_all_data_elements](#get_all_data_elements) - Get All Data Elements
* [get_data_element_by_path](#get_data_element_by_path) - Get Data Element By Path
* [get_new_and_updated_elements](#get_new_and_updated_elements) - Get New And Updated Elements

## add_data_element

Add Data Element

### Example Usage

<!-- UsageSnippet language="python" operationID="add_data_element" method="post" path="/datasource/{datasource_id}/data_element" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.data_elements.add_data_element(datasource_id="<id>", customer_id="<id>", description="mmm slip punctual whether fooey", name="<value>", path="/dev", media_type="<value>", discovery_record={
        "discovery_time": "<value>",
        "last_modified_time": "<value>",
        "size": 643019,
        "element_hash": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `datasource_id`                                                                           | *str*                                                                                     | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `customer_id`                                                                             | *str*                                                                                     | :heavy_check_mark:                                                                        | Customer ID                                                                               |
| `description`                                                                             | *Nullable[str]*                                                                           | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `name`                                                                                    | *str*                                                                                     | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `path`                                                                                    | *str*                                                                                     | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `media_type`                                                                              | *str*                                                                                     | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `discovery_record`                                                                        | [Nullable[models.DataElementDiscoveryRecord]](../../models/dataelementdiscoveryrecord.md) | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |

### Response

**[models.AddDataElementResponse](../../models/adddataelementresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_data_element

Get Data Element

### Example Usage

<!-- UsageSnippet language="python" operationID="get_data_element" method="get" path="/datasource/{datasource_id}/data_element/{data_element_id}" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.data_elements.get_data_element(datasource_id="<id>", data_element_id="<id>", customer_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `data_element_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `customer_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Customer ID                                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DataElement](../../models/dataelement.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## update_data_element

Update Data Element

### Example Usage

<!-- UsageSnippet language="python" operationID="update_data_element" method="put" path="/datasource/{datasource_id}/data_element/{data_element_id}" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.data_elements.update_data_element(datasource_id="<id>", data_element_id="<id>", customer_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `datasource_id`                                                                                   | *str*                                                                                             | :heavy_check_mark:                                                                                | N/A                                                                                               |
| `data_element_id`                                                                                 | *str*                                                                                             | :heavy_check_mark:                                                                                | N/A                                                                                               |
| `customer_id`                                                                                     | *str*                                                                                             | :heavy_check_mark:                                                                                | Customer ID                                                                                       |
| `description`                                                                                     | *OptionalNullable[str]*                                                                           | :heavy_minus_sign:                                                                                | N/A                                                                                               |
| `name`                                                                                            | *OptionalNullable[str]*                                                                           | :heavy_minus_sign:                                                                                | N/A                                                                                               |
| `path`                                                                                            | *OptionalNullable[str]*                                                                           | :heavy_minus_sign:                                                                                | N/A                                                                                               |
| `media_type`                                                                                      | *OptionalNullable[str]*                                                                           | :heavy_minus_sign:                                                                                | N/A                                                                                               |
| `discovery_record`                                                                                | [OptionalNullable[models.DataElementDiscoveryRecord]](../../models/dataelementdiscoveryrecord.md) | :heavy_minus_sign:                                                                                | N/A                                                                                               |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |

### Response

**[models.UpdateDataElementResponse](../../models/updatedataelementresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## delete_data_element

Delete Data Element

### Example Usage

<!-- UsageSnippet language="python" operationID="delete_data_element" method="delete" path="/datasource/{datasource_id}/data_element/{data_element_id}" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.data_elements.delete_data_element(datasource_id="<id>", data_element_id="<id>", customer_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `data_element_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `customer_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Customer ID                                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteDataElementResponse](../../models/deletedataelementresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_all_data_elements

Get All Data Elements

### Example Usage

<!-- UsageSnippet language="python" operationID="get_all_data_elements" method="get" path="/datasource/{datasource_id}/all_data_elements" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.data_elements.get_all_data_elements(datasource_id="<id>", customer_id="<id>", offset=0, limit=10)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `customer_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Customer ID                                                         |
| `regex_filter`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `media_type_filters`                                                | List[*str*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `offset`                                                            | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Number of items to skip                                             |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Maximum number of items to return                                   |
| `sort_by`                                                           | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | Field to sort by                                                    |
| `sort_order`                                                        | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | Sort order (asc or desc)                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.DataElement]](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_data_element_by_path

Get Data Element By Path

### Example Usage

<!-- UsageSnippet language="python" operationID="get_data_element_by_path" method="post" path="/datasource/{datasource_id}/data_element_by_path" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.data_elements.get_data_element_by_path(datasource_id="<id>", customer_id="<id>", path="/var/tmp")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `customer_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Customer ID                                                         |
| `path`                                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DataElement](../../models/dataelement.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_new_and_updated_elements

Get new and updated data elements since the last ingest time using the method specified.

### Example Usage

<!-- UsageSnippet language="python" operationID="get_new_and_updated_elements" method="get" path="/datasource/{datasource_id}/new_and_updated_elements" -->
```python
import meibelai
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.data_elements.get_new_and_updated_elements(datasource_id="<id>", ingest_method=meibelai.IngestMethod.RAG, customer_id="<id>", offset=0, limit=10)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `ingest_method`                                                     | [models.IngestMethod](../../models/ingestmethod.md)                 | :heavy_check_mark:                                                  | IngestMethod                                                        |
| `customer_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Customer ID                                                         |
| `regex_filter`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `media_type_filters`                                                | List[*str*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `offset`                                                            | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Number of items to skip                                             |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Maximum number of items to return                                   |
| `sort_by`                                                           | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | Field to sort by                                                    |
| `sort_order`                                                        | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | Sort order (asc or desc)                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetNewAndUpdatedDataElementsResponse](../../models/getnewandupdateddataelementsresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |