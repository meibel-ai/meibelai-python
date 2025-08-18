# Activity

Activity


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `id`                                                                   | *OptionalNullable[str]*                                                | :heavy_minus_sign:                                                     | N/A                                                                    |
| `blueprint_instance_id`                                                | *str*                                                                  | :heavy_check_mark:                                                     | N/A                                                                    |
| `activity_type`                                                        | *str*                                                                  | :heavy_check_mark:                                                     | N/A                                                                    |
| `status`                                                               | [OptionalNullable[models.ActivityStatus]](../models/activitystatus.md) | :heavy_minus_sign:                                                     | N/A                                                                    |
| `start_time`                                                           | [date](https://docs.python.org/3/library/datetime.html#date-objects)   | :heavy_minus_sign:                                                     | N/A                                                                    |
| `end_time`                                                             | [date](https://docs.python.org/3/library/datetime.html#date-objects)   | :heavy_minus_sign:                                                     | N/A                                                                    |
| `input_data`                                                           | Dict[str, *Any*]                                                       | :heavy_minus_sign:                                                     | N/A                                                                    |
| `output_data`                                                          | Dict[str, *Any*]                                                       | :heavy_minus_sign:                                                     | N/A                                                                    |
| `error`                                                                | *OptionalNullable[str]*                                                | :heavy_minus_sign:                                                     | N/A                                                                    |
| `group_id`                                                             | *OptionalNullable[str]*                                                | :heavy_minus_sign:                                                     | N/A                                                                    |