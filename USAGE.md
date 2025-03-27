<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from meibelai import Meibelai


with Meibelai() as m_client:

    res = m_client.datasources.list()

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from meibelai import Meibelai

async def main():

    async with Meibelai() as m_client:

        res = await m_client.datasources.list_async()

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->