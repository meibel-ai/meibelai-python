# Completions
(*completions*)

## Overview

Operations with completions

### Available Operations

* [create_stream](#create_stream) - Create Completion Stream

## create_stream

Create Completion Stream

### Example Usage

```python
from meibelai import Meibelai


with Meibelai() as m_client:

    res = m_client.completions.create_stream()

    with res as event_stream:
        for event in event_stream:
            # handle event
            print(event, flush=True)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Union[eventstreaming.EventStream[models.CreateStreamResponseBody], eventstreaming.EventStreamAsync[models.CreateStreamResponseBody]]](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |