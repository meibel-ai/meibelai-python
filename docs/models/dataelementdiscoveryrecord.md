# DataElementDiscoveryRecord

DataElementDiscoveryRecord


## Fields

| Field                             | Type                              | Required                          | Description                       |
| --------------------------------- | --------------------------------- | --------------------------------- | --------------------------------- |
| `discovery_time`                  | *str*                             | :heavy_check_mark:                | N/A                               |
| `last_modified_time`              | *str*                             | :heavy_check_mark:                | N/A                               |
| `size`                            | [models.Size](../models/size.md)  | :heavy_check_mark:                | N/A                               |
| `element_hash`                    | *str*                             | :heavy_check_mark:                | N/A                               |
| `file_id`                         | *OptionalNullable[str]*           | :heavy_minus_sign:                | N/A                               |
| `file_created_at`                 | *OptionalNullable[str]*           | :heavy_minus_sign:                | N/A                               |
| `file_modified_at`                | *OptionalNullable[str]*           | :heavy_minus_sign:                | N/A                               |
| `extra`                           | Dict[str, *Any*]                  | :heavy_minus_sign:                | Connector-specific extra metadata |