# CompletionEvent

A server-sent event containing the final complete response from the agent, sent once at the end of the stream


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `event`                                                        | *Literal["completion"]*                                        | :heavy_check_mark:                                             | N/A                                                            |
| `data`                                                         | [models.CompletionEventData](../models/completioneventdata.md) | :heavy_check_mark:                                             | N/A                                                            |