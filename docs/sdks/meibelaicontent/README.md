# MeibelaiContent
(*datasources.content*)

## Overview

Operations with content upload and management

### Available Operations

* [list_datasource_content](#list_datasource_content) - List datasource content
* [upload_datasource_content](#upload_datasource_content) - Upload Content
* [stream_upload_progress](#stream_upload_progress) - Stream upload progress events
* [get_datasource_upload_status](#get_datasource_upload_status) - Get upload status
* [stream_datasource_upload_progress](#stream_datasource_upload_progress) - Stream upload progress events (legacy)
* [get_datasource_content_metadata](#get_datasource_content_metadata) - Get content metadata
* [delete_datasource_content](#delete_datasource_content) - Delete content
* [download_datasource_content](#download_datasource_content) - Download content file

## list_datasource_content

List files and directories in a datasource with optional filtering and pagination

### Example Usage

<!-- UsageSnippet language="python" operationID="listDatasourceContent" method="get" path="/datasource/{datasource_id}/content" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.datasources.content.list_datasource_content(datasource_id="<id>", prefix="<value>", continuation_token="<value>", limit=1000)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `prefix`                                                            | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | Filter content by path prefix                                       |
| `continuation_token`                                                | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | Token for pagination to get next page of results                    |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Maximum number of items to return (1-10000)                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListContentResponse](../../models/listcontentresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## upload_datasource_content

Proxy upload with zero-copy streaming.

This endpoint maintains the multipart form data structure and streams
it directly to the backend service without buffering files in memory.
The multipart parsing happens on the backend service side.

### Example Usage

<!-- UsageSnippet language="python" operationID="uploadDatasourceContent" method="post" path="/datasource/{datasource_id}/content" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.datasources.content.upload_datasource_content(datasource_id="<id>", files=[], prefix="<value>", extract_zip=False, extract_eml=True, max_concurrent=655255)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `files`                                                             | List[[models.Files](../../models/files.md)]                         | :heavy_check_mark:                                                  | Files to upload to the datasource                                   |
| `prefix`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Path prefix for organizing uploaded files                           |
| `extract_zip`                                                       | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Auto-extract ZIP archives                                           |
| `extract_eml`                                                       | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Extract EML email files                                             |
| `max_concurrent`                                                    | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Maximum concurrent file uploads                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UploadContentResponse](../../models/uploadcontentresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## stream_upload_progress

Subscribe to real-time upload progress updates via Server-Sent Events

### Example Usage

<!-- UsageSnippet language="python" operationID="streamUploadProgress" method="get" path="/uploads/{upload_id}/progress" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.datasources.content.stream_upload_progress(upload_id="<id>")

    with res as event_stream:
        for event in event_stream:
            # handle event
            print(event, flush=True)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `upload_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Union[eventstreaming.EventStream[models.SSEEvent], eventstreaming.EventStreamAsync[models.SSEEvent]]](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_datasource_upload_status

Get the current status of a content upload operation

### Example Usage

<!-- UsageSnippet language="python" operationID="getDatasourceUploadStatus" method="get" path="/datasource/{datasource_id}/content/upload-status/{upload_id}" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.datasources.content.get_datasource_upload_status(datasource_id="<id>", upload_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `upload_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## stream_datasource_upload_progress

Subscribe to real-time upload progress updates via Server-Sent Events. Consider using /uploads/{upload_id}/progress instead.

### Example Usage

<!-- UsageSnippet language="python" operationID="streamDatasourceUploadProgress" method="get" path="/datasource/{datasource_id}/content/upload-progress/{upload_id}" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.datasources.content.stream_datasource_upload_progress(datasource_id="<id>", upload_id="<id>")

    with res as event_stream:
        for event in event_stream:
            # handle event
            print(event, flush=True)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `upload_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Union[eventstreaming.EventStream[models.SSEEvent], eventstreaming.EventStreamAsync[models.SSEEvent]]](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_datasource_content_metadata

Get metadata information for a file or directory in the datasource

### Example Usage

<!-- UsageSnippet language="python" operationID="getDatasourceContentMetadata" method="get" path="/datasource/{datasource_id}/content/{path}" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.datasources.content.get_datasource_content_metadata(datasource_id="<id>", path="/opt/include")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `path`                                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetContentResponse](../../models/getcontentresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## delete_datasource_content

Delete a file or directory from the datasource

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteDatasourceContent" method="delete" path="/datasource/{datasource_id}/content/{path}" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.datasources.content.delete_datasource_content(datasource_id="<id>", path="/usr/local/bin")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `path`                                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteContentResponse](../../models/deletecontentresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## download_datasource_content

Download a file from the datasource with streaming support for large files

### Example Usage

<!-- UsageSnippet language="python" operationID="downloadDatasourceContent" method="get" path="/datasource/{datasource_id}/content/{path}/download" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.datasources.content.download_datasource_content(datasource_id="<id>", path="/usr/src")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `path`                                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[httpx.Response](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |