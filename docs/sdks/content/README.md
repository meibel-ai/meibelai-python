# Content
(*content*)

## Overview

Operations with content upload and management

### Available Operations

* [list_content_datasource_datasource_id_content_get](#list_content_datasource_datasource_id_content_get) - List Content
* [upload_content_datasource_datasource_id_content_post](#upload_content_datasource_datasource_id_content_post) - Upload Content
* [get_upload_progress_stream_uploads_upload_id_progress_get](#get_upload_progress_stream_uploads_upload_id_progress_get) - Stream upload progress events
* [get_upload_status_datasource_datasource_id_content_upload_status_upload_id_get](#get_upload_status_datasource_datasource_id_content_upload_status_upload_id_get) - Get Upload Status
* [stream_upload_progress_datasource_datasource_id_content_upload_progress_upload_id_get](#stream_upload_progress_datasource_datasource_id_content_upload_progress_upload_id_get) - Stream upload progress events (legacy)
* [get_content_metadata_datasource_datasource_id_content_path_get](#get_content_metadata_datasource_datasource_id_content_path_get) - Get Content Metadata
* [delete_content_datasource_datasource_id_content_path_delete](#delete_content_datasource_datasource_id_content_path_delete) - Delete Content
* [download_content_datasource_datasource_id_content_path_download_get](#download_content_datasource_datasource_id_content_path_download_get) - Download Content

## list_content_datasource_datasource_id_content_get

Proxy list content request

### Example Usage

<!-- UsageSnippet language="python" operationID="list_content_datasource__datasource_id__content_get" method="get" path="/datasource/{datasource_id}/content" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.content.list_content_datasource_datasource_id_content_get(datasource_id="<id>", prefix="<value>", continuation_token="<value>", limit=1000)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `prefix`                                                            | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `continuation_token`                                                | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListContentResponse](../../models/listcontentresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## upload_content_datasource_datasource_id_content_post

Proxy upload with zero-copy streaming.

This endpoint maintains the multipart form data structure and streams
it directly to the backend service without buffering files in memory.
The multipart parsing happens on the backend service side.

### Example Usage

<!-- UsageSnippet language="python" operationID="upload_content_datasource__datasource_id__content_post" method="post" path="/datasource/{datasource_id}/content" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.content.upload_content_datasource_datasource_id_content_post(datasource_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UploadContentResponse](../../models/uploadcontentresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_upload_progress_stream_uploads_upload_id_progress_get

Subscribe to real-time upload progress updates via Server-Sent Events

### Example Usage

<!-- UsageSnippet language="python" operationID="get_upload_progress_stream_uploads__upload_id__progress_get" method="get" path="/uploads/{upload_id}/progress" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.content.get_upload_progress_stream_uploads_upload_id_progress_get(upload_id="<id>")

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

**[Union[eventstreaming.EventStream[models.GetUploadProgressStreamUploadsUploadIDProgressGetResponseBody], eventstreaming.EventStreamAsync[models.GetUploadProgressStreamUploadsUploadIDProgressGetResponseBody]]](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_upload_status_datasource_datasource_id_content_upload_status_upload_id_get

Proxy upload status request

### Example Usage

<!-- UsageSnippet language="python" operationID="get_upload_status_datasource__datasource_id__content_upload_status__upload_id__get" method="get" path="/datasource/{datasource_id}/content/upload-status/{upload_id}" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.content.get_upload_status_datasource_datasource_id_content_upload_status_upload_id_get(datasource_id="<id>", upload_id="<id>")

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

## stream_upload_progress_datasource_datasource_id_content_upload_progress_upload_id_get

Subscribe to real-time upload progress updates via Server-Sent Events. Consider using /uploads/{upload_id}/progress instead.

### Example Usage

<!-- UsageSnippet language="python" operationID="stream_upload_progress_datasource__datasource_id__content_upload_progress__upload_id__get" method="get" path="/datasource/{datasource_id}/content/upload-progress/{upload_id}" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.content.stream_upload_progress_datasource_datasource_id_content_upload_progress_upload_id_get(datasource_id="<id>", upload_id="<id>")

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

**[Union[eventstreaming.EventStream[models.StreamUploadProgressDatasourceDatasourceIDContentUploadProgressUploadIDGetResponseBody], eventstreaming.EventStreamAsync[models.StreamUploadProgressDatasourceDatasourceIDContentUploadProgressUploadIDGetResponseBody]]](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_content_metadata_datasource_datasource_id_content_path_get

Proxy content metadata request

### Example Usage

<!-- UsageSnippet language="python" operationID="get_content_metadata_datasource__datasource_id__content__path__get" method="get" path="/datasource/{datasource_id}/content/{path}" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.content.get_content_metadata_datasource_datasource_id_content_path_get(datasource_id="<id>", path="/usr/obj")

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

## delete_content_datasource_datasource_id_content_path_delete

Proxy delete request

### Example Usage

<!-- UsageSnippet language="python" operationID="delete_content_datasource__datasource_id__content__path__delete" method="delete" path="/datasource/{datasource_id}/content/{path}" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.content.delete_content_datasource_datasource_id_content_path_delete(datasource_id="<id>", path="/usr/sbin")

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

## download_content_datasource_datasource_id_content_path_download_get

Proxy download request with streaming

### Example Usage

<!-- UsageSnippet language="python" operationID="download_content_datasource__datasource_id__content__path__download_get" method="get" path="/datasource/{datasource_id}/content/{path}/download" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.content.download_content_datasource_datasource_id_content_path_download_get(datasource_id="<id>", path="/proc")

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

**[Any](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |