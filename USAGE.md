<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from meibelai import Meibelai
import os


with Meibelai(
    api_key_header=os.getenv("MEIBELAI_API_KEY_HEADER", ""),
) as m_client:

    res = m_client.datasources.add_datasource(customer_id="<id>", project_id="<id>", name="<value>", description="kindly kookily biodegrade after helpfully mushy unlike", recurrence="<value>", object_storage_config={
        "bucket": "<value>",
        "prefix": "<value>",
        "filters": None,
        "gcs_config": {
            "key": "<value>",
            "key1": "<value>",
        },
        "s3_config": {
            "role_arn": "<value>",
            "region": "<value>",
        },
    }, web_config={
        "base_url": "https://neighboring-fen.net/",
        "javascript_render": True,
        "wait_for_selector": "<value>",
        "domains": None,
        "authentication": {
            "username": "Eulalia35",
            "password": "VKK1aONN4LAHFVF",
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

        res = await m_client.datasources.add_datasource_async(customer_id="<id>", project_id="<id>", name="<value>", description="kindly kookily biodegrade after helpfully mushy unlike", recurrence="<value>", object_storage_config={
            "bucket": "<value>",
            "prefix": "<value>",
            "filters": None,
            "gcs_config": {
                "key": "<value>",
                "key1": "<value>",
            },
            "s3_config": {
                "role_arn": "<value>",
                "region": "<value>",
            },
        }, web_config={
            "base_url": "https://neighboring-fen.net/",
            "javascript_render": True,
            "wait_for_selector": "<value>",
            "domains": None,
            "authentication": {
                "username": "Eulalia35",
                "password": "VKK1aONN4LAHFVF",
            },
        })

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->