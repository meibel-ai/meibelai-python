# ChatWithBlueprintRequest


## Fields

| Field                   | Type                    | Required                | Description             |
| ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| `blueprint_instance_id` | *str*                   | :heavy_check_mark:      | N/A                     |
| `user_message`          | *str*                   | :heavy_check_mark:      | N/A                     |
| `signal_name`           | *Optional[str]*         | :heavy_minus_sign:      | N/A                     |
| `query_name`            | *Optional[str]*         | :heavy_minus_sign:      | N/A                     |
| `max_wait_seconds`      | *Optional[int]*         | :heavy_minus_sign:      | N/A                     |
| `poll_interval_seconds` | *Optional[float]*       | :heavy_minus_sign:      | N/A                     |
| `min_new_items`         | *Optional[int]*         | :heavy_minus_sign:      | N/A                     |
| `request_body`          | List[*Any*]             | :heavy_minus_sign:      | N/A                     |