# GatewayDataElementResponse


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `id`                                                   | *str*                                                  | :heavy_check_mark:                                     | N/A                                                    |
| `customer_id`                                          | *str*                                                  | :heavy_check_mark:                                     | N/A                                                    |
| `project_id`                                           | *str*                                                  | :heavy_check_mark:                                     | N/A                                                    |
| `datasource_id`                                        | *str*                                                  | :heavy_check_mark:                                     | N/A                                                    |
| `name`                                                 | *str*                                                  | :heavy_check_mark:                                     | N/A                                                    |
| `value`                                                | *str*                                                  | :heavy_check_mark:                                     | N/A                                                    |
| `type`                                                 | [models.DataElementType](../models/dataelementtype.md) | :heavy_check_mark:                                     | N/A                                                    |
| `description`                                          | *str*                                                  | :heavy_check_mark:                                     | N/A                                                    |
| `processed`                                            | *str*                                                  | :heavy_check_mark:                                     | N/A                                                    |
| `created_at`                                           | *str*                                                  | :heavy_check_mark:                                     | N/A                                                    |
| `updated_at`                                           | *str*                                                  | :heavy_check_mark:                                     | N/A                                                    |
| `metadata`                                             | [models.GatewayMetadata](../models/gatewaymetadata.md) | :heavy_check_mark:                                     | N/A                                                    |
| `parent_id`                                            | *OptionalNullable[str]*                                | :heavy_minus_sign:                                     | N/A                                                    |
| `is_container_element`                                 | *OptionalNullable[str]*                                | :heavy_minus_sign:                                     | N/A                                                    |