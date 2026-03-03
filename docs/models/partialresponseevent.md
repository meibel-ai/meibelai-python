# PartialResponseEvent

A server-sent event containing an incremental response from the agent


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `event`                                                                  | *Literal["partial_response"]*                                            | :heavy_check_mark:                                                       | N/A                                                                      |
| `data`                                                                   | [models.PartialResponseEventData](../models/partialresponseeventdata.md) | :heavy_check_mark:                                                       | N/A                                                                      |