# QueryWorkflowRequest


## Fields

| Field                                       | Type                                        | Required                                    | Description                                 |
| ------------------------------------------- | ------------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| `blueprint_instance_id`                     | *str*                                       | :heavy_check_mark:                          | Unique identifier for the workflow instance |
| `query_name`                                | *str*                                       | :heavy_check_mark:                          | Name of the query to execute                |
| `customer_id`                               | *OptionalNullable[str]*                     | :heavy_minus_sign:                          | Customer ID                                 |
| `request_body`                              | List[*Any*]                                 | :heavy_minus_sign:                          | N/A                                         |