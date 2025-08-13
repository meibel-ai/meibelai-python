# UpdateBlueprintInstanceStatusRequest


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `blueprint_instance_id`                                                | *str*                                                                  | :heavy_check_mark:                                                     | N/A                                                                    |
| `updated_status_value`                                                 | [models.BlueprintInstanceStatus](../models/blueprintinstancestatus.md) | :heavy_check_mark:                                                     | BlueprintInstanceStatus                                                |
| `workflow_run_id`                                                      | *OptionalNullable[str]*                                                | :heavy_minus_sign:                                                     | N/A                                                                    |
| `customer_id`                                                          | *str*                                                                  | :heavy_check_mark:                                                     | Customer ID                                                            |