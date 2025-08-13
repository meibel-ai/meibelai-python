# Event

Event


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `id`                                                                 | *OptionalNullable[str]*                                              | :heavy_minus_sign:                                                   | N/A                                                                  |
| `activity_id`                                                        | *OptionalNullable[str]*                                              | :heavy_minus_sign:                                                   | N/A                                                                  |
| `blueprint_instance_id`                                              | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `event_type`                                                         | [OptionalNullable[models.EventType]](../models/eventtype.md)         | :heavy_minus_sign:                                                   | N/A                                                                  |
| `timestamp`                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |
| `details`                                                            | [OptionalNullable[models.Details]](../models/details.md)             | :heavy_minus_sign:                                                   | N/A                                                                  |
| `group_id`                                                           | *OptionalNullable[str]*                                              | :heavy_minus_sign:                                                   | N/A                                                                  |
| `is_signal`                                                          | *OptionalNullable[bool]*                                             | :heavy_minus_sign:                                                   | N/A                                                                  |
| `is_internal`                                                        | *OptionalNullable[bool]*                                             | :heavy_minus_sign:                                                   | N/A                                                                  |
| `originating_signal_id`                                              | *OptionalNullable[str]*                                              | :heavy_minus_sign:                                                   | N/A                                                                  |