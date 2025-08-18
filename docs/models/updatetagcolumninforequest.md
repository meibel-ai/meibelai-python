# UpdateTagColumnInfoRequest


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `datasource_id`                                                      | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `table_name`                                                         | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `column_name`                                                        | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `customer_id`                                                        | *OptionalNullable[str]*                                              | :heavy_minus_sign:                                                   | Customer ID                                                          |
| `update_tag_column_request`                                          | [models.UpdateTagColumnRequest](../models/updatetagcolumnrequest.md) | :heavy_check_mark:                                                   | N/A                                                                  |