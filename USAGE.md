<!-- Start SDK Example Usage [usage] -->
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