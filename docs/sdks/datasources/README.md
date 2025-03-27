# Datasources
(*datasources*)

## Overview

Operations with datasources

### Available Operations

* [list](#list) - Get Datasources
* [create](#create) - Create Datasource
* [get](#get) - Get Datasource
* [update](#update) - Update Datasource
* [list_dataelements](#list_dataelements) - Get Dataelements
* [create_dataelement](#create_dataelement) - Create Dataelement
* [get_dataelement](#get_dataelement) - Get Dataelement
* [update_dataelement](#update_dataelement) - Update Dataelement
* [delete_dataelement](#delete_dataelement) - Delete Dataelement
* [upload_dataelement](#upload_dataelement) - Upload Dataelement

## list

Get Datasources

### Example Usage

```python
from meibelai import Meibelai


with Meibelai() as m_client:

    res = m_client.datasources.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `offset`                                                            | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Number of items to skip                                             |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Maximum number of items to return                                   |
| `sort_by`                                                           | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | Field to sort by                                                    |
| `sort_order`                                                        | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | Sort order (asc or desc)                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.GatewayDatasourceResponse]](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## create

Create Datasource

### Example Usage

```python
from meibelai import Meibelai


with Meibelai() as m_client:

    res = m_client.datasources.create(description="yuck vice between gee ugh ha", name="<value>", type_="<value>", metadata={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `description`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `name`                                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `type`                                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `metadata`                                                          | [models.GatewayMetadata](../../models/gatewaymetadata.md)           | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GatewayNewDatasourceResponse](../../models/gatewaynewdatasourceresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get

Get Datasource

### Example Usage

```python
from meibelai import Meibelai


with Meibelai() as m_client:

    res = m_client.datasources.get(datasource_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GatewayDatasourceResponse](../../models/gatewaydatasourceresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## update

Update Datasource

### Example Usage

```python
from meibelai import Meibelai


with Meibelai() as m_client:

    res = m_client.datasources.update(datasource_id="<id>", description="awful underneath retention too mobility char innocently dowse restfully", name="<value>", type_="<value>", metadata={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `description`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `name`                                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `type`                                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `metadata`                                                          | [models.GatewayMetadata](../../models/gatewaymetadata.md)           | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## list_dataelements

Get Dataelements

### Example Usage

```python
from meibelai import Meibelai


with Meibelai() as m_client:

    res = m_client.datasources.list_dataelements(datasource_id=756811)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource_id`                                                     | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `offset`                                                            | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Number of items to skip                                             |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Maximum number of items to return                                   |
| `sort_by`                                                           | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | Field to sort by                                                    |
| `sort_order`                                                        | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | Sort order (asc or desc)                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## create_dataelement

Create Dataelement

### Example Usage

```python
from meibelai import Meibelai


with Meibelai() as m_client:

    res = m_client.datasources.create_dataelement(datasource_id=24820)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource_id`                                                     | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_dataelement

Get Dataelement

### Example Usage

```python
from meibelai import Meibelai


with Meibelai() as m_client:

    res = m_client.datasources.get_dataelement(datasource_id=700347, dataelement_id=558834)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource_id`                                                     | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `dataelement_id`                                                    | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## update_dataelement

Update Dataelement

### Example Usage

```python
from meibelai import Meibelai


with Meibelai() as m_client:

    res = m_client.datasources.update_dataelement(datasource_id=857478, dataelement_id=597129)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource_id`                                                     | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `dataelement_id`                                                    | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## delete_dataelement

Delete Dataelement

### Example Usage

```python
from meibelai import Meibelai


with Meibelai() as m_client:

    res = m_client.datasources.delete_dataelement(datasource_id=647715, dataelement_id=424652)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource_id`                                                     | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `dataelement_id`                                                    | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## upload_dataelement

Upload Dataelement

### Example Usage

```python
from meibelai import Meibelai


with Meibelai() as m_client:

    res = m_client.datasources.upload_dataelement(datasource_id=716701)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource_id`                                                     | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |