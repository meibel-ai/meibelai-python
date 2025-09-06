# SSEEvent

Generic Server-Sent Event


## Fields

| Field                                                                     | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `event`                                                                   | *str*                                                                     | :heavy_check_mark:                                                        | Event type (e.g., connected, progress, stream_complete, error, keepalive) |
| `data`                                                                    | [Optional[models.Data]](../models/data.md)                                | :heavy_minus_sign:                                                        | Event data payload                                                        |