# ToolCallEvent

A server-sent event indicating the agent is calling a tool


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `event`                                                    | *Literal["tool_call"]*                                     | :heavy_check_mark:                                         | N/A                                                        |
| `data`                                                     | [models.ToolCallEventData](../models/toolcalleventdata.md) | :heavy_check_mark:                                         | N/A                                                        |