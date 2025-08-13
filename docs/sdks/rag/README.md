# Rag
(*rag*)

## Overview

### Available Operations

* [add_rag_config](#add_rag_config) - Add Rag Config
* [get_rag_config](#get_rag_config) - Get Rag Config
* [update_rag_config](#update_rag_config) - Update Rag Config
* [delete_rag_config](#delete_rag_config) - Delete Rag Config
* [add_chunking_strategy](#add_chunking_strategy) - Add Chunking Strategy
* [get_chunking_strategy](#get_chunking_strategy) - Get Chunking Strategy
* [update_chunking_strategy](#update_chunking_strategy) - Update Chunking Strategy
* [delete_chunking_strategy](#delete_chunking_strategy) - Delete Chunking Strategy

## add_rag_config

Add Rag Config

### Example Usage

<!-- UsageSnippet language="python" operationID="add_rag_config" method="post" path="/datasource/{datasource_id}/rag_config" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.rag.add_rag_config(datasource_id="<id>", customer_id="<id>", collection_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `datasource_id`                                                                       | *str*                                                                                 | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `customer_id`                                                                         | *str*                                                                                 | :heavy_check_mark:                                                                    | Customer ID                                                                           |
| `collection_id`                                                                       | *str*                                                                                 | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `description`                                                                         | *OptionalNullable[str]*                                                               | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `extractor_model`                                                                     | [OptionalNullable[models.ExtractorModel]](../../models/extractormodel.md)             | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `embedding_model`                                                                     | [OptionalNullable[models.EmbeddingModel]](../../models/embeddingmodel.md)             | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `sparse_embedding_model`                                                              | [OptionalNullable[models.SparseEmbeddingModel]](../../models/sparseembeddingmodel.md) | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `collect_metadata`                                                                    | *OptionalNullable[bool]*                                                              | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.AddRagConfigResponse](../../models/addragconfigresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_rag_config

Get Rag Config

### Example Usage

<!-- UsageSnippet language="python" operationID="get_rag_config" method="get" path="/datasource/{datasource_id}/rag_config" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.rag.get_rag_config(datasource_id="<id>", customer_id="<id>")

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

**[models.RagConfig](../../models/ragconfig.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## update_rag_config

Update Rag Config

### Example Usage

<!-- UsageSnippet language="python" operationID="update_rag_config" method="put" path="/datasource/{datasource_id}/rag_config" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.rag.update_rag_config(datasource_id="<id>", customer_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `datasource_id`                                                                       | *str*                                                                                 | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `customer_id`                                                                         | *str*                                                                                 | :heavy_check_mark:                                                                    | Customer ID                                                                           |
| `description`                                                                         | *OptionalNullable[str]*                                                               | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `collection_id`                                                                       | *OptionalNullable[str]*                                                               | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `extractor_model`                                                                     | [OptionalNullable[models.ExtractorModel]](../../models/extractormodel.md)             | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `embedding_model`                                                                     | [OptionalNullable[models.EmbeddingModel]](../../models/embeddingmodel.md)             | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `sparse_embedding_model`                                                              | [OptionalNullable[models.SparseEmbeddingModel]](../../models/sparseembeddingmodel.md) | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `collect_metadata`                                                                    | *OptionalNullable[bool]*                                                              | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.UpdateRagConfigResponse](../../models/updateragconfigresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## delete_rag_config

Delete Rag Config

### Example Usage

<!-- UsageSnippet language="python" operationID="delete_rag_config" method="delete" path="/datasource/{datasource_id}/rag_config" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.rag.delete_rag_config(datasource_id="<id>", customer_id="<id>")

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

**[str](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## add_chunking_strategy

Add Chunking Strategy

### Example Usage

<!-- UsageSnippet language="python" operationID="add_chunking_strategy" method="post" path="/datasource/{datasource_id}/chunking_strategy" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.rag.add_chunking_strategy(datasource_id="<id>", customer_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `datasource_id`                                                                       | *str*                                                                                 | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `customer_id`                                                                         | *str*                                                                                 | :heavy_check_mark:                                                                    | Customer ID                                                                           |
| `code_splitter`                                                                       | [OptionalNullable[models.CodeChunking]](../../models/codechunking.md)                 | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `html_node_parser`                                                                    | [OptionalNullable[models.HTMLChunking]](../../models/htmlchunking.md)                 | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `json_node_parser`                                                                    | [OptionalNullable[models.JSONNodeChunking]](../../models/jsonnodechunking.md)         | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `markdown_node_parser`                                                                | [OptionalNullable[models.MarkdownNodeChunking]](../../models/markdownnodechunking.md) | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `semantic_splitter_node_parser`                                                       | [OptionalNullable[models.SemanticChunking]](../../models/semanticchunking.md)         | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `sentence_splitter`                                                                   | [OptionalNullable[models.SentenceChunking]](../../models/sentencechunking.md)         | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `token_text_splitter`                                                                 | [OptionalNullable[models.TokenTextChunking]](../../models/tokentextchunking.md)       | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.AddChunkingStrategyResponse](../../models/addchunkingstrategyresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_chunking_strategy

Get Chunking Strategy

### Example Usage

<!-- UsageSnippet language="python" operationID="get_chunking_strategy" method="get" path="/datasource/{datasource_id}/chunking_strategy" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.rag.get_chunking_strategy(datasource_id="<id>", customer_id="<id>")

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

**[models.RagChunkingStrategy](../../models/ragchunkingstrategy.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## update_chunking_strategy

Update Chunking Strategy

### Example Usage

<!-- UsageSnippet language="python" operationID="update_chunking_strategy" method="put" path="/datasource/{datasource_id}/chunking_strategy" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.rag.update_chunking_strategy(datasource_id="<id>", customer_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `datasource_id`                                                                       | *str*                                                                                 | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `customer_id`                                                                         | *str*                                                                                 | :heavy_check_mark:                                                                    | Customer ID                                                                           |
| `code_splitter`                                                                       | [OptionalNullable[models.CodeChunking]](../../models/codechunking.md)                 | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `html_node_parser`                                                                    | [OptionalNullable[models.HTMLChunking]](../../models/htmlchunking.md)                 | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `json_node_parser`                                                                    | [OptionalNullable[models.JSONNodeChunking]](../../models/jsonnodechunking.md)         | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `markdown_node_parser`                                                                | [OptionalNullable[models.MarkdownNodeChunking]](../../models/markdownnodechunking.md) | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `semantic_splitter_node_parser`                                                       | [OptionalNullable[models.SemanticChunking]](../../models/semanticchunking.md)         | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `sentence_splitter`                                                                   | [OptionalNullable[models.SentenceChunking]](../../models/sentencechunking.md)         | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `token_text_splitter`                                                                 | [OptionalNullable[models.TokenTextChunking]](../../models/tokentextchunking.md)       | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.UpdateChunkingStrategyResponse](../../models/updatechunkingstrategyresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## delete_chunking_strategy

Delete Chunking Strategy

### Example Usage

<!-- UsageSnippet language="python" operationID="delete_chunking_strategy" method="delete" path="/datasource/{datasource_id}/chunking_strategy" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.rag.delete_chunking_strategy(datasource_id="<id>", customer_id="<id>")

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

**[models.DeleteChunkingStrategyResponse](../../models/deletechunkingstrategyresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |