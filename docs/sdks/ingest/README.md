# Ingest
(*ingest*)

## Overview

### Available Operations

* [upsert_ingest_record](#upsert_ingest_record) - Upsert Ingest Record
* [get_ingest_record](#get_ingest_record) - Get Ingest Record
* [delete_ingest_record](#delete_ingest_record) - Delete Ingest Record
* [get_all_ingest_records](#get_all_ingest_records) - Get All Ingest Records

## upsert_ingest_record

Upsert Ingest Record

### Example Usage

<!-- UsageSnippet language="python" operationID="upsert_ingest_record" method="post" path="/ingest/records/{datasource_id}/{data_element_id}/{ingest_method}" -->
```python
import meibelai
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.ingest.upsert_ingest_record(datasource_id="<id>", data_element_id="<id>", ingest_method=meibelai.IngestMethod.RAG, customer_id="<id>", ingest_time="<value>", element_hash="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `data_element_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `ingest_method`                                                     | [models.IngestMethod](../../models/ingestmethod.md)                 | :heavy_check_mark:                                                  | IngestMethod                                                        |
| `customer_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Customer ID                                                         |
| `ingest_time`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `element_hash`                                                      | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UpsertIngestRecordResponse](../../models/upsertingestrecordresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_ingest_record

Get Ingest Record

### Example Usage

<!-- UsageSnippet language="python" operationID="get_ingest_record" method="get" path="/ingest/records/{datasource_id}/{data_element_id}/{ingest_method}" -->
```python
import meibelai
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.ingest.get_ingest_record(datasource_id="<id>", data_element_id="<id>", ingest_method=meibelai.IngestMethod.RAG, customer_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `data_element_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `ingest_method`                                                     | [models.IngestMethod](../../models/ingestmethod.md)                 | :heavy_check_mark:                                                  | IngestMethod                                                        |
| `customer_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Customer ID                                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.IngestRecord](../../models/ingestrecord.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## delete_ingest_record

Delete Ingest Record

### Example Usage

<!-- UsageSnippet language="python" operationID="delete_ingest_record" method="delete" path="/ingest/records/{datasource_id}/{data_element_id}/{ingest_method}" -->
```python
import meibelai
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.ingest.delete_ingest_record(datasource_id="<id>", data_element_id="<id>", ingest_method=meibelai.IngestMethod.REF_GRAPH, customer_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `data_element_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `ingest_method`                                                     | [models.IngestMethod](../../models/ingestmethod.md)                 | :heavy_check_mark:                                                  | IngestMethod                                                        |
| `customer_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Customer ID                                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteIngestRecordResponse](../../models/deleteingestrecordresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_all_ingest_records

Get All Ingest Records

### Example Usage

<!-- UsageSnippet language="python" operationID="get_all_ingest_records" method="get" path="/ingest/records/{datasource_id}" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.ingest.get_all_ingest_records(datasource_id="<id>", customer_id="<id>", offset=0, limit=10)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `datasource_id`                                                       | *str*                                                                 | :heavy_check_mark:                                                    | N/A                                                                   |
| `customer_id`                                                         | *str*                                                                 | :heavy_check_mark:                                                    | Customer ID                                                           |
| `method_filter`                                                       | [OptionalNullable[models.IngestMethod]](../../models/ingestmethod.md) | :heavy_minus_sign:                                                    | IngestMethod                                                          |
| `offset`                                                              | *Optional[int]*                                                       | :heavy_minus_sign:                                                    | Number of items to skip                                               |
| `limit`                                                               | *Optional[int]*                                                       | :heavy_minus_sign:                                                    | Maximum number of items to return                                     |
| `sort_by`                                                             | *OptionalNullable[str]*                                               | :heavy_minus_sign:                                                    | Field to sort by                                                      |
| `sort_order`                                                          | *OptionalNullable[str]*                                               | :heavy_minus_sign:                                                    | Sort order (asc or desc)                                              |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[List[models.IngestRecord]](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |