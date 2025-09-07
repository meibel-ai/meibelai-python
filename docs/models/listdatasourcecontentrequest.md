# ListDatasourceContentRequest


## Fields

| Field                                            | Type                                             | Required                                         | Description                                      |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `datasource_id`                                  | *str*                                            | :heavy_check_mark:                               | N/A                                              |
| `prefix`                                         | *OptionalNullable[str]*                          | :heavy_minus_sign:                               | Filter content by path prefix                    |
| `continuation_token`                             | *OptionalNullable[str]*                          | :heavy_minus_sign:                               | Token for pagination to get next page of results |
| `limit`                                          | *Optional[int]*                                  | :heavy_minus_sign:                               | Maximum number of items to return (1-10000)      |