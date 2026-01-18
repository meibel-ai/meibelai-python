# ChatMessageRequest

Request body for chat message endpoints.


## Fields

| Field                    | Type                     | Required                 | Description              |
| ------------------------ | ------------------------ | ------------------------ | ------------------------ |
| `user_message`           | *str*                    | :heavy_check_mark:       | The user's chat message  |
| `timeout_seconds`        | *OptionalNullable[int]*  | :heavy_minus_sign:       | N/A                      |
| `include_thinking`       | *OptionalNullable[bool]* | :heavy_minus_sign:       | N/A                      |
| `include_tool_activity`  | *OptionalNullable[bool]* | :heavy_minus_sign:       | N/A                      |