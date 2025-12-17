# Datasources.Dataelements

## Overview

Operations with data elements

### Available Operations

* [add_data_element](#add_data_element) - Add Data Element
* [get_data_elements](#get_data_elements) - Get Data Elements
* [get_data_element](#get_data_element) - Get Data Element
* [update_data_element](#update_data_element) - Update Data Element
* [delete_data_element](#delete_data_element) - Delete Data Element
* [get_data_elements_by_filters](#get_data_elements_by_filters) - Get Data Elements By Filters

## add_data_element

Add Data Element

### Example Usage

<!-- UsageSnippet language="python" operationID="addDataElement" method="post" path="/datasource/{datasource_id}/data_element" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.datasources.dataelements.add_data_element(datasource_id="<id>", description="round yowza wherever", name="<value>", path="/usr/lib", media_type="<value>", discovery_record={
        "discovery_time": "<value>",
        "last_modified_time": "<value>",
        "size": 740493,
        "element_hash": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `datasource_id`                                                                           | *str*                                                                                     | :heavy_check_mark:                                                                        | N/A                                                                                       |
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

## get_data_elements

Get Data Elements

### Example Usage

<!-- UsageSnippet language="python" operationID="getDataElements" method="get" path="/datasource/{datasource_id}/data_element" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.datasources.dataelements.get_data_elements(datasource_id="<id>", offset=0, limit=10, sort_by="<value>", sort_order="<value>")

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
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.DataElement]](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_data_element

Get Data Element

### Example Usage

<!-- UsageSnippet language="python" operationID="getDataElement" method="get" path="/datasource/{datasource_id}/data_element/{data_element_id}" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.datasources.dataelements.get_data_element(datasource_id="<id>", data_element_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `data_element_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
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

<!-- UsageSnippet language="python" operationID="updateDataElement" method="put" path="/datasource/{datasource_id}/data_element/{data_element_id}" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.datasources.dataelements.update_data_element(datasource_id="<id>", data_element_id="<id>", description="before jealously orient", name="<value>", path="/usr/libexec", media_type="<value>", discovery_record={
        "discovery_time": "<value>",
        "last_modified_time": "<value>",
        "size": 506325,
        "element_hash": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `datasource_id`                                                                                   | *str*                                                                                             | :heavy_check_mark:                                                                                | N/A                                                                                               |
| `data_element_id`                                                                                 | *str*                                                                                             | :heavy_check_mark:                                                                                | N/A                                                                                               |
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

<!-- UsageSnippet language="python" operationID="deleteDataElement" method="delete" path="/datasource/{datasource_id}/data_element/{data_element_id}" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.datasources.dataelements.delete_data_element(datasource_id="<id>", data_element_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `data_element_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteDataElementResponse](../../models/deletedataelementresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_data_elements_by_filters

Get Data Elements By Filters

### Example Usage

<!-- UsageSnippet language="python" operationID="getDataElementsByFilters" method="post" path="/datasource/{datasource_id}/data_elements_by_filters" -->
```python
import meibelai
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.datasources.dataelements.get_data_elements_by_filters(datasource_id="<id>", regex_filter="<value>", media_type_filters=[
        "<value 1>",
        "<value 2>",
    ], offset=0, limit=10, sort_by="<value>", sort_order=None, filters=[
        {
            "key": meibelai.AllowedDataElementFilterKeys.NAME,
            "condition": meibelai.DataElementCondition.STARTS_WITH,
            "value": "<value>",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `regex_filter`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `media_type_filters`                                                | List[*str*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `offset`                                                            | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Number of items to skip                                             |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Maximum number of items to return                                   |
| `sort_by`                                                           | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | Field to sort by                                                    |
| `sort_order`                                                        | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | Sort order (asc or desc)                                            |
| `filters`                                                           | List[[models.DataElementFilter](../../models/dataelementfilter.md)] | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.DataElement]](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |