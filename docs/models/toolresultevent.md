# ToolResultEvent

A server-sent event containing the result of a tool call


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `event`                                                        | *Literal["tool_result"]*                                       | :heavy_check_mark:                                             | N/A                                                            |
| `data`                                                         | [models.ToolResultEventData](../models/toolresulteventdata.md) | :heavy_check_mark:                                             | N/A                                                            |