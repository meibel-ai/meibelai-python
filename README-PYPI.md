# meibelai

Developer-friendly & type-safe Python SDK specifically catered to leverage *meibelai* API.

<div align="left">
    <a href="https://www.speakeasy.com/?utm_source=meibelai&utm_campaign=python"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>


<br /><br />
> [!IMPORTANT]
> This SDK is not yet ready for production use. To complete setup please follow the steps outlined in your [workspace](https://app.speakeasy.com/org/meibel/console). Delete this section before > publishing to a package manager.

<!-- Start Summary [summary] -->
## Summary

Meibel AI API: Meibel Gateway Service

Our API allows you to interact with our services.  Read the[docs](https://docs.mistral.ai) to learn how to use it.
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [meibelai](https://github.com/meibel-ai/meibelai-python/blob/master/#meibelai)
  * [SDK Installation](https://github.com/meibel-ai/meibelai-python/blob/master/#sdk-installation)
  * [IDE Support](https://github.com/meibel-ai/meibelai-python/blob/master/#ide-support)
  * [SDK Example Usage](https://github.com/meibel-ai/meibelai-python/blob/master/#sdk-example-usage)
  * [Authentication](https://github.com/meibel-ai/meibelai-python/blob/master/#authentication)
  * [Available Resources and Operations](https://github.com/meibel-ai/meibelai-python/blob/master/#available-resources-and-operations)
  * [Server-sent event streaming](https://github.com/meibel-ai/meibelai-python/blob/master/#server-sent-event-streaming)
  * [Retries](https://github.com/meibel-ai/meibelai-python/blob/master/#retries)
  * [Error Handling](https://github.com/meibel-ai/meibelai-python/blob/master/#error-handling)
  * [Server Selection](https://github.com/meibel-ai/meibelai-python/blob/master/#server-selection)
  * [Custom HTTP Client](https://github.com/meibel-ai/meibelai-python/blob/master/#custom-http-client)
  * [Resource Management](https://github.com/meibel-ai/meibelai-python/blob/master/#resource-management)
  * [Debugging](https://github.com/meibel-ai/meibelai-python/blob/master/#debugging)
* [Development](https://github.com/meibel-ai/meibelai-python/blob/master/#development)
  * [Maturity](https://github.com/meibel-ai/meibelai-python/blob/master/#maturity)
  * [Contributions](https://github.com/meibel-ai/meibelai-python/blob/master/#contributions)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!TIP]
> To finish publishing your SDK to PyPI you must [run your first generation action](https://www.speakeasy.com/docs/github-setup#step-by-step-guide).


> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with *uv*, *pip*, or *poetry* package managers.

### uv

*uv* is a fast Python package installer and resolver, designed as a drop-in replacement for pip and pip-tools. It's recommended for its speed and modern Python tooling capabilities.

```bash
uv add git+https://github.com/meibel-ai/meibelai-python.git
```

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install git+https://github.com/meibel-ai/meibelai-python.git
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add git+https://github.com/meibel-ai/meibelai-python.git
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from meibelai python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "meibelai",
# ]
# ///

from meibelai import Meibelai

sdk = Meibelai(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.datasources.add_datasource(customer_id="<id>", project_id="<id>", name="<value>", description="smooth hmph geez key", recurrence="<value>", object_storage_config={
        "bucket": "<value>",
        "prefix": "<value>",
        "filters": {
            "included_prefixes": [
                "<value 1>",
                "<value 2>",
            ],
            "included_file_types": [
                "<value 1>",
                "<value 2>",
                "<value 3>",
            ],
            "recursive_prefixes": True,
            "modified_date_start": "<value>",
            "modified_date_end": "<value>",
            "min_file_size": 110821,
            "max_file_size": 861343,
        },
        "gcs_config": {
            "key": "<value>",
            "key1": "<value>",
            "key2": "<value>",
        },
        "s3_config": None,
    }, web_config={
        "base_url": "https://soupy-department.biz",
        "javascript_render": False,
        "wait_for_selector": "<value>",
        "domains": [
            {
                "domain": "well-made-hygienic.com",
                "limit_pattern": "<value>",
                "exclude_pattern": "<value>",
                "ingestible": True,
                "expandable": True,
            },
        ],
        "authentication": {
            "username": "Amir_Schaden",
            "password": "Qgqx_NgZXn9ZOj5",
        },
    })

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from meibelai import Meibelai
import os

async def main():

    async with Meibelai(
        api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
    ) as m_client:

        res = await m_client.datasources.add_datasource_async(customer_id="<id>", project_id="<id>", name="<value>", description="smooth hmph geez key", recurrence="<value>", object_storage_config={
            "bucket": "<value>",
            "prefix": "<value>",
            "filters": {
                "included_prefixes": [
                    "<value 1>",
                    "<value 2>",
                ],
                "included_file_types": [
                    "<value 1>",
                    "<value 2>",
                    "<value 3>",
                ],
                "recursive_prefixes": True,
                "modified_date_start": "<value>",
                "modified_date_end": "<value>",
                "min_file_size": 110821,
                "max_file_size": 861343,
            },
            "gcs_config": {
                "key": "<value>",
                "key1": "<value>",
                "key2": "<value>",
            },
            "s3_config": None,
        }, web_config={
            "base_url": "https://soupy-department.biz",
            "javascript_render": False,
            "wait_for_selector": "<value>",
            "domains": [
                {
                    "domain": "well-made-hygienic.com",
                    "limit_pattern": "<value>",
                    "exclude_pattern": "<value>",
                    "ingestible": True,
                    "expandable": True,
                },
            ],
            "authentication": {
                "username": "Amir_Schaden",
                "password": "Qgqx_NgZXn9ZOj5",
            },
        })

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name             | Type   | Scheme  | Environment Variable      |
| ---------------- | ------ | ------- | ------------------------- |
| `api_key_header` | apiKey | API key | `MEIBELAI_API_KEY_HEADER` |

To authenticate with the API the `api_key_header` parameter must be set when initializing the SDK client instance. For example:
```python
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.datasources.add_datasource(customer_id="<id>", project_id="<id>", name="<value>", description="smooth hmph geez key", recurrence="<value>", object_storage_config={
        "bucket": "<value>",
        "prefix": "<value>",
        "filters": {
            "included_prefixes": [
                "<value 1>",
                "<value 2>",
            ],
            "included_file_types": [
                "<value 1>",
                "<value 2>",
                "<value 3>",
            ],
            "recursive_prefixes": True,
            "modified_date_start": "<value>",
            "modified_date_end": "<value>",
            "min_file_size": 110821,
            "max_file_size": 861343,
        },
        "gcs_config": {
            "key": "<value>",
            "key1": "<value>",
            "key2": "<value>",
        },
        "s3_config": None,
    }, web_config={
        "base_url": "https://soupy-department.biz",
        "javascript_render": False,
        "wait_for_selector": "<value>",
        "domains": [
            {
                "domain": "well-made-hygienic.com",
                "limit_pattern": "<value>",
                "exclude_pattern": "<value>",
                "ingestible": True,
                "expandable": True,
            },
        ],
        "authentication": {
            "username": "Amir_Schaden",
            "password": "Qgqx_NgZXn9ZOj5",
        },
    })

    # Handle response
    print(res)

```
<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [blueprint_instances](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/blueprintinstances/README.md)

* [add_blueprint_instance](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/blueprintinstances/README.md#add_blueprint_instance) - Add Blueprint Instance
* [get_all_blueprint_instances](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/blueprintinstances/README.md#get_all_blueprint_instances) - Get All Blueprint Instances
* [get_blueprint_instance](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/blueprintinstances/README.md#get_blueprint_instance) - Get Blueprint Instance
* [delete_blueprint_instance](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/blueprintinstances/README.md#delete_blueprint_instance) - Delete Blueprint Instance
* [update_blueprint_instance_status](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/blueprintinstances/README.md#update_blueprint_instance_status) - Update Blueprint Instance Status
* [complete_blueprint_instance](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/blueprintinstances/README.md#complete_blueprint_instance) - Complete a Blueprint Instance
* [fail_blueprint_instance](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/blueprintinstances/README.md#fail_blueprint_instance) - Fail a Blueprint Instance
* [add_activity_by_blueprint_instance](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/blueprintinstances/README.md#add_activity_by_blueprint_instance) - Add Activity By Blueprint Instance
* [get_activity_by_blueprint_instance](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/blueprintinstances/README.md#get_activity_by_blueprint_instance) - Get Activity By Blueprint Instance
* [get_activities_by_blueprint_instance](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/blueprintinstances/README.md#get_activities_by_blueprint_instance) - Get Activities By Blueprint Instance
* [update_activity_status](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/blueprintinstances/README.md#update_activity_status) - Update Activity Status
* [get_event_by_blueprint_instance](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/blueprintinstances/README.md#get_event_by_blueprint_instance) - Get Event By Blueprint Instance
* [create_event_by_blueprint_instance_id](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/blueprintinstances/README.md#create_event_by_blueprint_instance_id) - Create Event By Blueprint Instance Id
* [get_events_by_blueprint_instance](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/blueprintinstances/README.md#get_events_by_blueprint_instance) - Get Events By Blueprint Instance
* [start_blueprint_instance](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/blueprintinstances/README.md#start_blueprint_instance) - Start Blueprint Instance
* [cancel_blueprint_instance](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/blueprintinstances/README.md#cancel_blueprint_instance) - Cancel Blueprint Instance
* [send_signal](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/blueprintinstances/README.md#send_signal) - Send Signal
* [query_workflow](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/blueprintinstances/README.md#query_workflow) - Query Workflow

### [content](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/content/README.md)

* [list_content_datasource_datasource_id_content_get](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/content/README.md#list_content_datasource_datasource_id_content_get) - List Content
* [upload_content_datasource_datasource_id_content_post](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/content/README.md#upload_content_datasource_datasource_id_content_post) - Upload Content
* [get_upload_progress_stream_uploads_upload_id_progress_get](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/content/README.md#get_upload_progress_stream_uploads_upload_id_progress_get) - Stream upload progress events
* [get_upload_status_datasource_datasource_id_content_upload_status_upload_id_get](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/content/README.md#get_upload_status_datasource_datasource_id_content_upload_status_upload_id_get) - Get Upload Status
* [stream_upload_progress_datasource_datasource_id_content_upload_progress_upload_id_get](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/content/README.md#stream_upload_progress_datasource_datasource_id_content_upload_progress_upload_id_get) - Stream upload progress events (legacy)
* [get_content_metadata_datasource_datasource_id_content_path_get](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/content/README.md#get_content_metadata_datasource_datasource_id_content_path_get) - Get Content Metadata
* [delete_content_datasource_datasource_id_content_path_delete](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/content/README.md#delete_content_datasource_datasource_id_content_path_delete) - Delete Content
* [download_content_datasource_datasource_id_content_path_download_get](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/content/README.md#download_content_datasource_datasource_id_content_path_download_get) - Download Content

### [data_elements](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/dataelements/README.md)

* [add_data_element](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/dataelements/README.md#add_data_element) - Add Data Element
* [get_data_elements](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/dataelements/README.md#get_data_elements) - Get Data Elements
* [get_data_element](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/dataelements/README.md#get_data_element) - Get Data Element
* [update_data_element](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/dataelements/README.md#update_data_element) - Update Data Element
* [delete_data_element](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/dataelements/README.md#delete_data_element) - Delete Data Element
* [get_data_elements_by_filters](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/dataelements/README.md#get_data_elements_by_filters) - Get Data Elements By Filters

### [datasources](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/datasources/README.md)

* [add_datasource](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/datasources/README.md#add_datasource) - Add Datasource
* [get_datasource](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/datasources/README.md#get_datasource) - Get Datasource
* [update_datasource](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/datasources/README.md#update_datasource) - Update Datasource
* [delete_datasource](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/datasources/README.md#delete_datasource) - Delete Datasource
* [get_all_datasource_ids](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/datasources/README.md#get_all_datasource_ids) - Get All Datasource Ids


### [rag](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/rag/README.md)

* [add_rag_config](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/rag/README.md#add_rag_config) - Add Rag Config
* [get_rag_config](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/rag/README.md#get_rag_config) - Get Rag Config
* [update_rag_config](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/rag/README.md#update_rag_config) - Update Rag Config
* [delete_rag_config](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/rag/README.md#delete_rag_config) - Delete Rag Config
* [add_chunking_strategy](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/rag/README.md#add_chunking_strategy) - Add Chunking Strategy
* [get_chunking_strategy](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/rag/README.md#get_chunking_strategy) - Get Chunking Strategy
* [update_chunking_strategy](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/rag/README.md#update_chunking_strategy) - Update Chunking Strategy
* [delete_chunking_strategy](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/rag/README.md#delete_chunking_strategy) - Delete Chunking Strategy

### [tag](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/tag/README.md)

* [add_tag_config](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/tag/README.md#add_tag_config) - Add Tag Config
* [get_tag_config](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/tag/README.md#get_tag_config) - Get Tag Config
* [update_tag_config](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/tag/README.md#update_tag_config) - Update Tag Config
* [delete_tag_config](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/tag/README.md#delete_tag_config) - Delete Tag Config
* [add_tag_table_info](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/tag/README.md#add_tag_table_info) - Add Tag Table Info
* [get_tag_table_info](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/tag/README.md#get_tag_table_info) - Get Tag Table Info
* [update_tag_table_info](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/tag/README.md#update_tag_table_info) - Update Tag Table Info
* [delete_tag_table_info](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/tag/README.md#delete_tag_table_info) - Delete Tag Table Info
* [get_all_tag_table_info](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/tag/README.md#get_all_tag_table_info) - Get All Tag Table Info
* [add_tag_column_info](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/tag/README.md#add_tag_column_info) - Add Tag Column Info
* [get_tag_column_info](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/tag/README.md#get_tag_column_info) - Get Tag Column Info
* [update_tag_column_info](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/tag/README.md#update_tag_column_info) - Update Tag Column Info
* [get_all_tag_column_info](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/tag/README.md#get_all_tag_column_info) - Get All Tag Column Info
* [delete_tag_column_info](https://github.com/meibel-ai/meibelai-python/blob/master/docs/sdks/tag/README.md#delete_tag_column_info) - Delete Tag Column Info

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Server-sent event streaming [eventstream] -->
## Server-sent event streaming

[Server-sent events][mdn-sse] are used to stream content from certain
operations. These operations will expose the stream as [Generator][generator] that
can be consumed using a simple `for` loop. The loop will
terminate when the server no longer has any events to send and closes the
underlying connection.  

The stream is also a [Context Manager][context-manager] and can be used with the `with` statement and will close the
underlying connection when the context is exited.

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

[mdn-sse]: https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events
[generator]: https://book.pythontips.com/en/latest/generators.html
[context-manager]: https://book.pythontips.com/en/latest/context_managers.html
<!-- End Server-sent event streaming [eventstream] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from meibelai import Meibelai
from meibelai.utils import BackoffStrategy, RetryConfig
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.datasources.add_datasource(customer_id="<id>", project_id="<id>", name="<value>", description="smooth hmph geez key", recurrence="<value>", object_storage_config={
        "bucket": "<value>",
        "prefix": "<value>",
        "filters": {
            "included_prefixes": [
                "<value 1>",
                "<value 2>",
            ],
            "included_file_types": [
                "<value 1>",
                "<value 2>",
                "<value 3>",
            ],
            "recursive_prefixes": True,
            "modified_date_start": "<value>",
            "modified_date_end": "<value>",
            "min_file_size": 110821,
            "max_file_size": 861343,
        },
        "gcs_config": {
            "key": "<value>",
            "key1": "<value>",
            "key2": "<value>",
        },
        "s3_config": None,
    }, web_config={
        "base_url": "https://soupy-department.biz",
        "javascript_render": False,
        "wait_for_selector": "<value>",
        "domains": [
            {
                "domain": "well-made-hygienic.com",
                "limit_pattern": "<value>",
                "exclude_pattern": "<value>",
                "ingestible": True,
                "expandable": True,
            },
        ],
        "authentication": {
            "username": "Amir_Schaden",
            "password": "Qgqx_NgZXn9ZOj5",
        },
    },
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from meibelai import Meibelai
from meibelai.utils import BackoffStrategy, RetryConfig
import os


with Meibelai(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.datasources.add_datasource(customer_id="<id>", project_id="<id>", name="<value>", description="smooth hmph geez key", recurrence="<value>", object_storage_config={
        "bucket": "<value>",
        "prefix": "<value>",
        "filters": {
            "included_prefixes": [
                "<value 1>",
                "<value 2>",
            ],
            "included_file_types": [
                "<value 1>",
                "<value 2>",
                "<value 3>",
            ],
            "recursive_prefixes": True,
            "modified_date_start": "<value>",
            "modified_date_end": "<value>",
            "min_file_size": 110821,
            "max_file_size": 861343,
        },
        "gcs_config": {
            "key": "<value>",
            "key1": "<value>",
            "key2": "<value>",
        },
        "s3_config": None,
    }, web_config={
        "base_url": "https://soupy-department.biz",
        "javascript_render": False,
        "wait_for_selector": "<value>",
        "domains": [
            {
                "domain": "well-made-hygienic.com",
                "limit_pattern": "<value>",
                "exclude_pattern": "<value>",
                "ingestible": True,
                "expandable": True,
            },
        ],
        "authentication": {
            "username": "Amir_Schaden",
            "password": "Qgqx_NgZXn9ZOj5",
        },
    })

    # Handle response
    print(res)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

[`MeibelaiError`](https://github.com/meibel-ai/meibelai-python/blob/master/./src/meibelai/models/meibelaierror.py) is the base class for all HTTP error responses. It has the following properties:

| Property           | Type             | Description                                                                             |
| ------------------ | ---------------- | --------------------------------------------------------------------------------------- |
| `err.message`      | `str`            | Error message                                                                           |
| `err.status_code`  | `int`            | HTTP response status code eg `404`                                                      |
| `err.headers`      | `httpx.Headers`  | HTTP response headers                                                                   |
| `err.body`         | `str`            | HTTP body. Can be empty string if no body is returned.                                  |
| `err.raw_response` | `httpx.Response` | Raw HTTP response                                                                       |
| `err.data`         |                  | Optional. Some errors may contain structured data. [See Error Classes](https://github.com/meibel-ai/meibelai-python/blob/master/#error-classes). |

### Example
```python
import meibelai
from meibelai import Meibelai, models
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:
    res = None
    try:

        res = m_client.datasources.add_datasource(customer_id="<id>", project_id="<id>", name="<value>", description="smooth hmph geez key", recurrence="<value>", object_storage_config={
            "bucket": "<value>",
            "prefix": "<value>",
            "filters": {
                "included_prefixes": [
                    "<value 1>",
                    "<value 2>",
                ],
                "included_file_types": [
                    "<value 1>",
                    "<value 2>",
                    "<value 3>",
                ],
                "recursive_prefixes": True,
                "modified_date_start": "<value>",
                "modified_date_end": "<value>",
                "min_file_size": 110821,
                "max_file_size": 861343,
            },
            "gcs_config": {
                "key": "<value>",
                "key1": "<value>",
                "key2": "<value>",
            },
            "s3_config": None,
        }, web_config={
            "base_url": "https://soupy-department.biz",
            "javascript_render": False,
            "wait_for_selector": "<value>",
            "domains": [
                {
                    "domain": "well-made-hygienic.com",
                    "limit_pattern": "<value>",
                    "exclude_pattern": "<value>",
                    "ingestible": True,
                    "expandable": True,
                },
            ],
            "authentication": {
                "username": "Amir_Schaden",
                "password": "Qgqx_NgZXn9ZOj5",
            },
        })

        # Handle response
        print(res)


    except models.MeibelaiError as e:
        # The base class for HTTP error responses
        print(e.message)
        print(e.status_code)
        print(e.body)
        print(e.headers)
        print(e.raw_response)

        # Depending on the method different errors may be thrown
        if isinstance(e, models.HTTPValidationError):
            print(e.data.detail)  # Optional[List[meibelai.ValidationError]]
```

### Error Classes
**Primary errors:**
* [`MeibelaiError`](https://github.com/meibel-ai/meibelai-python/blob/master/./src/meibelai/models/meibelaierror.py): The base class for HTTP error responses.
  * [`HTTPValidationError`](https://github.com/meibel-ai/meibelai-python/blob/master/./src/meibelai/models/httpvalidationerror.py): Validation Error. Status code `422`.

<details><summary>Less common errors (5)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`MeibelaiError`](https://github.com/meibel-ai/meibelai-python/blob/master/./src/meibelai/models/meibelaierror.py)**:
* [`ResponseValidationError`](https://github.com/meibel-ai/meibelai-python/blob/master/./src/meibelai/models/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| #   | Server                  | Description              |
| --- | ----------------------- | ------------------------ |
| 0   | `http://api.meibel.ai`  | Meibel API               |
| 1   | `http://localhost:8000` | Local Development Server |

#### Example

```python
from meibelai import Meibelai
import os


with Meibelai(
    server_idx=1,
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.datasources.add_datasource(customer_id="<id>", project_id="<id>", name="<value>", description="smooth hmph geez key", recurrence="<value>", object_storage_config={
        "bucket": "<value>",
        "prefix": "<value>",
        "filters": {
            "included_prefixes": [
                "<value 1>",
                "<value 2>",
            ],
            "included_file_types": [
                "<value 1>",
                "<value 2>",
                "<value 3>",
            ],
            "recursive_prefixes": True,
            "modified_date_start": "<value>",
            "modified_date_end": "<value>",
            "min_file_size": 110821,
            "max_file_size": 861343,
        },
        "gcs_config": {
            "key": "<value>",
            "key1": "<value>",
            "key2": "<value>",
        },
        "s3_config": None,
    }, web_config={
        "base_url": "https://soupy-department.biz",
        "javascript_render": False,
        "wait_for_selector": "<value>",
        "domains": [
            {
                "domain": "well-made-hygienic.com",
                "limit_pattern": "<value>",
                "exclude_pattern": "<value>",
                "ingestible": True,
                "expandable": True,
            },
        ],
        "authentication": {
            "username": "Amir_Schaden",
            "password": "Qgqx_NgZXn9ZOj5",
        },
    })

    # Handle response
    print(res)

```

### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from meibelai import Meibelai
import os


with Meibelai(
    server_url="http://localhost:8000",
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.datasources.add_datasource(customer_id="<id>", project_id="<id>", name="<value>", description="smooth hmph geez key", recurrence="<value>", object_storage_config={
        "bucket": "<value>",
        "prefix": "<value>",
        "filters": {
            "included_prefixes": [
                "<value 1>",
                "<value 2>",
            ],
            "included_file_types": [
                "<value 1>",
                "<value 2>",
                "<value 3>",
            ],
            "recursive_prefixes": True,
            "modified_date_start": "<value>",
            "modified_date_end": "<value>",
            "min_file_size": 110821,
            "max_file_size": 861343,
        },
        "gcs_config": {
            "key": "<value>",
            "key1": "<value>",
            "key2": "<value>",
        },
        "s3_config": None,
    }, web_config={
        "base_url": "https://soupy-department.biz",
        "javascript_render": False,
        "wait_for_selector": "<value>",
        "domains": [
            {
                "domain": "well-made-hygienic.com",
                "limit_pattern": "<value>",
                "exclude_pattern": "<value>",
                "ingestible": True,
                "expandable": True,
            },
        ],
        "authentication": {
            "username": "Amir_Schaden",
            "password": "Qgqx_NgZXn9ZOj5",
        },
    })

    # Handle response
    print(res)

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from meibelai import Meibelai
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Meibelai(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from meibelai import Meibelai
from meibelai.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = Meibelai(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `Meibelai` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from meibelai import Meibelai
import os
def main():

    with Meibelai(
        api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
    ) as m_client:
        # Rest of application here...


# Or when using async:
async def amain():

    async with Meibelai(
        api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
    ) as m_client:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from meibelai import Meibelai
import logging

logging.basicConfig(level=logging.DEBUG)
s = Meibelai(debug_logger=logging.getLogger("meibelai"))
```

You can also enable a default debug logger by setting an environment variable `MEIBELAI_DEBUG` to true.
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation. 
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release. 

### SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=meibelai&utm_campaign=python)
