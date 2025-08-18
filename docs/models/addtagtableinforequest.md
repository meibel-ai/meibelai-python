# AddTagTableInfoRequest


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `datasource_id`                                              | *str*                                                        | :heavy_check_mark:                                           | N/A                                                          |
| `table_name`                                                 | *str*                                                        | :heavy_check_mark:                                           | N/A                                                          |
| `customer_id`                                                | *OptionalNullable[str]*                                      | :heavy_minus_sign:                                           | Customer ID                                                  |
| `add_tag_table_request`                                      | [models.AddTagTableRequest](../models/addtagtablerequest.md) | :heavy_check_mark:                                           | N/A                                                          |