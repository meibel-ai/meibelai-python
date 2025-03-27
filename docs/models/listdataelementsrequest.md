# ListDataelementsRequest


## Fields

| Field                             | Type                              | Required                          | Description                       |
| --------------------------------- | --------------------------------- | --------------------------------- | --------------------------------- |
| `datasource_id`                   | *int*                             | :heavy_check_mark:                | N/A                               |
| `offset`                          | *Optional[int]*                   | :heavy_minus_sign:                | Number of items to skip           |
| `limit`                           | *Optional[int]*                   | :heavy_minus_sign:                | Maximum number of items to return |
| `sort_by`                         | *OptionalNullable[str]*           | :heavy_minus_sign:                | Field to sort by                  |
| `sort_order`                      | *OptionalNullable[str]*           | :heavy_minus_sign:                | Sort order (asc or desc)          |