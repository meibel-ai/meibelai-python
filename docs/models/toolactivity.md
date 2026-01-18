# ToolActivity

Record of a tool call and its result.


## Fields

| Field              | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `tool_id`          | *str*              | :heavy_check_mark: | N/A                |
| `tool_name`        | *str*              | :heavy_check_mark: | N/A                |
| `arguments`        | Dict[str, *Any*]   | :heavy_check_mark: | N/A                |
| `result`           | Dict[str, *Any*]   | :heavy_minus_sign: | N/A                |
| `timestamp`        | *str*              | :heavy_check_mark: | N/A                |