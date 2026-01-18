# ChatMessageResponse

Response from the non-streaming chat endpoint.


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `signal_id`                                            | *str*                                                  | :heavy_check_mark:                                     | Unique ID for this message exchange                    |
| `response`                                             | [models.ChatResponse](../models/chatresponse.md)       | :heavy_check_mark:                                     | The structured chat response.                          |
| `assistant_response`                                   | *str*                                                  | :heavy_check_mark:                                     | The assistant response in text-format                  |
| `tool_activity`                                        | List[[models.ToolActivity](../models/toolactivity.md)] | :heavy_minus_sign:                                     | N/A                                                    |
| `thinking`                                             | *OptionalNullable[str]*                                | :heavy_minus_sign:                                     | N/A                                                    |
| `token_usage`                                          | Dict[str, *int*]                                       | :heavy_minus_sign:                                     | N/A                                                    |