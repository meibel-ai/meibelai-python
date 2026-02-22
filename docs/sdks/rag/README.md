# Datasources.Rag

## Overview

Operations with rag

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

<!-- UsageSnippet language="python" operationID="addRagConfig" method="post" path="/datasource/{datasource_id}/rag_config" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.datasources.rag.add_rag_config(datasource_id="<id>", collection_id="<id>", description="which gloomy regarding rosemary provider vivaciously fat willow", extractor_model={
        "name": "<value>",
        "endpoint": "<value>",
    }, embedding_model={
        "name": "<value>",
        "endpoint": "<value>",
        "dimensions": 66789,
    }, sparse_embedding_model={
        "name": "<value>",
        "endpoint": "<value>",
    }, collect_metadata=False, metadata_options={
        "create_title": None,
        "extract_questions_answers": False,
        "extract_summary": True,
        "has_consumer_content": True,
        "get_bibliographical_information": False,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `datasource_id`                                                                       | *str*                                                                                 | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `collection_id`                                                                       | *str*                                                                                 | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `description`                                                                         | *OptionalNullable[str]*                                                               | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `extractor_model`                                                                     | [OptionalNullable[models.ExtractorModel]](../../models/extractormodel.md)             | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `embedding_model`                                                                     | [OptionalNullable[models.EmbeddingModel]](../../models/embeddingmodel.md)             | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `sparse_embedding_model`                                                              | [OptionalNullable[models.SparseEmbeddingModel]](../../models/sparseembeddingmodel.md) | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `collect_metadata`                                                                    | *OptionalNullable[bool]*                                                              | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `metadata_options`                                                                    | [OptionalNullable[models.MetadataOptions]](../../models/metadataoptions.md)           | :heavy_minus_sign:                                                                    | N/A                                                                                   |
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

<!-- UsageSnippet language="python" operationID="getRagConfig" method="get" path="/datasource/{datasource_id}/rag_config" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.datasources.rag.get_rag_config(datasource_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
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

<!-- UsageSnippet language="python" operationID="updateRagConfig" method="put" path="/datasource/{datasource_id}/rag_config" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.datasources.rag.update_rag_config(datasource_id="<id>", description="scoop version advocate fondly darn who wherever respectful atop snack", collection_id="<id>", extractor_model={
        "name": "<value>",
        "endpoint": "<value>",
    }, embedding_model={
        "name": "<value>",
        "endpoint": "<value>",
        "dimensions": 562748,
    }, sparse_embedding_model={
        "name": "<value>",
        "endpoint": "<value>",
    }, collect_metadata=False, metadata_options={
        "create_title": True,
        "extract_questions_answers": False,
        "extract_summary": True,
        "has_consumer_content": True,
        "get_bibliographical_information": True,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `datasource_id`                                                                       | *str*                                                                                 | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `description`                                                                         | *OptionalNullable[str]*                                                               | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `collection_id`                                                                       | *OptionalNullable[str]*                                                               | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `extractor_model`                                                                     | [OptionalNullable[models.ExtractorModel]](../../models/extractormodel.md)             | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `embedding_model`                                                                     | [OptionalNullable[models.EmbeddingModel]](../../models/embeddingmodel.md)             | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `sparse_embedding_model`                                                              | [OptionalNullable[models.SparseEmbeddingModel]](../../models/sparseembeddingmodel.md) | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `collect_metadata`                                                                    | *OptionalNullable[bool]*                                                              | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `metadata_options`                                                                    | [OptionalNullable[models.MetadataOptions]](../../models/metadataoptions.md)           | :heavy_minus_sign:                                                                    | N/A                                                                                   |
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

<!-- UsageSnippet language="python" operationID="deleteRagConfig" method="delete" path="/datasource/{datasource_id}/rag_config" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.datasources.rag.delete_rag_config(datasource_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[str](../../models/responsedeleteragconfig.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## add_chunking_strategy

Add Chunking Strategy

### Example Usage

<!-- UsageSnippet language="python" operationID="addChunkingStrategy" method="post" path="/datasource/{datasource_id}/chunking_strategy" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.datasources.rag.add_chunking_strategy(datasource_id="<id>", code_splitter={
        "chunk_lines": 638565,
        "chunk_lines_overlap": 656087,
        "max_chars": 448427,
    }, html_node_parser={
        "include_metadata": True,
        "include_prev_next_rel": True,
        "tags": None,
    }, json_node_parser={
        "include_metadata": True,
        "include_prev_next_rel": False,
    }, markdown_node_parser={
        "include_metadata": False,
        "include_prev_next_rel": True,
        "header_path_separator": "<value>",
    }, semantic_splitter_node_parser={
        "buffer_size": 602838,
        "include_metadata": False,
        "include_prev_next_rel": False,
        "breakpoint_percentile_threshold": 688505,
    }, sentence_splitter={
        "chunk_size": 438626,
        "chunk_overlap": 440520,
        "separator": "<value>",
        "paragraph_separator": "<value>",
        "secondary_chunking_regex": "<value>",
    }, token_text_splitter={
        "chunk_size": 974923,
        "chunk_overlap": 269364,
        "separator": "<value>",
        "backup_separators": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
        "keep_whitespaces": True,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `datasource_id`                                                                       | *str*                                                                                 | :heavy_check_mark:                                                                    | N/A                                                                                   |
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

<!-- UsageSnippet language="python" operationID="getChunkingStrategy" method="get" path="/datasource/{datasource_id}/chunking_strategy" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.datasources.rag.get_chunking_strategy(datasource_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
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

<!-- UsageSnippet language="python" operationID="updateChunkingStrategy" method="put" path="/datasource/{datasource_id}/chunking_strategy" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.datasources.rag.update_chunking_strategy(datasource_id="<id>", code_splitter={
        "chunk_lines": 54839,
        "chunk_lines_overlap": None,
        "max_chars": 255540,
    }, html_node_parser={
        "include_metadata": False,
        "include_prev_next_rel": False,
        "tags": [
            "<value 1>",
            "<value 2>",
        ],
    }, json_node_parser={
        "include_metadata": True,
        "include_prev_next_rel": False,
    }, markdown_node_parser={
        "include_metadata": False,
        "include_prev_next_rel": False,
        "header_path_separator": "<value>",
    }, semantic_splitter_node_parser={
        "buffer_size": 612870,
        "include_metadata": True,
        "include_prev_next_rel": False,
        "breakpoint_percentile_threshold": 35666,
    }, sentence_splitter={
        "chunk_size": 991279,
        "chunk_overlap": 203347,
        "separator": "<value>",
        "paragraph_separator": "<value>",
        "secondary_chunking_regex": "<value>",
    }, token_text_splitter={
        "chunk_size": 387919,
        "chunk_overlap": 552454,
        "separator": "<value>",
        "backup_separators": None,
        "keep_whitespaces": True,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `datasource_id`                                                                       | *str*                                                                                 | :heavy_check_mark:                                                                    | N/A                                                                                   |
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

<!-- UsageSnippet language="python" operationID="deleteChunkingStrategy" method="delete" path="/datasource/{datasource_id}/chunking_strategy" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.datasources.rag.delete_chunking_strategy(datasource_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `datasource_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteChunkingStrategyResponse](../../models/deletechunkingstrategyresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |