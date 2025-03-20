# ChatEvent

A server-sent event containing chat completion content


## Fields

| Field                            | Type                             | Required                         | Description                      |
| -------------------------------- | -------------------------------- | -------------------------------- | -------------------------------- |
| `id`                             | *str*                            | :heavy_check_mark:               | N/A                              |
| `data`                           | [models.Data](../models/data.md) | :heavy_check_mark:               | N/A                              |
| `event`                          | *Literal["completion"]*          | :heavy_check_mark:               | N/A                              |