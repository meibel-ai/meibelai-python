# ConfidenceScoring

## Overview

Operations with confidence scoring jobs and summaries

### Available Operations

* [get_scoring_job](#get_scoring_job) - Get Scoring Job
* [get_all_scoring_jobs](#get_all_scoring_jobs) - Get All Scoring Jobs
* [get_scoring_jobs_summary](#get_scoring_jobs_summary) - Get Scoring Jobs Summary

## get_scoring_job

Get a scoring job by ID. Returns 403 if the job does not belong to the caller's customer.

### Example Usage

<!-- UsageSnippet language="python" operationID="getScoringJob" method="get" path="/confidence-scoring/job/{job_id}" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.confidence_scoring.get_scoring_job(job_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `job_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_all_scoring_jobs

Get all scoring jobs for the caller's customer.

### Example Usage

<!-- UsageSnippet language="python" operationID="getAllScoringJobs" method="get" path="/confidence-scoring/jobs" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.confidence_scoring.get_all_scoring_jobs(agent_name="<value>", agent_version=None, agent_execution_id="<id>", agent_workflow_name="<value>", agent_workflow_version="<value>", agent_workflow_execution_id="<id>", tool_id="<id>", tool_instance_id="<id>", tool_execution_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `agent_name`                                                        | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `agent_version`                                                     | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `agent_execution_id`                                                | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `agent_workflow_name`                                               | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `agent_workflow_version`                                            | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `agent_workflow_execution_id`                                       | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `tool_id`                                                           | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `tool_instance_id`                                                  | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `tool_execution_id`                                                 | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_scoring_jobs_summary

Get aggregated scoring summary for the caller's customer.

primary: Required filter in format 'field:value' (e.g., 'agent_execution_id:exec_123').
secondary: Optional secondary filter in format 'field:value' (e.g., 'agent_name:my_agent').
Results are always scoped to the caller's customer_id.

### Example Usage

<!-- UsageSnippet language="python" operationID="getScoringJobsSummary" method="get" path="/confidence-scoring/summary" -->
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.confidence_scoring.get_scoring_jobs_summary(primary="<value>", secondary="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `primary`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `secondary`                                                         | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ScoreSummary](../../models/scoresummary.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |