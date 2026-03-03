# StatusEvent

A server-sent event containing an agent status update


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `event`                                                | *Literal["status"]*                                    | :heavy_check_mark:                                     | N/A                                                    |
| `data`                                                 | [models.StatusEventData](../models/statuseventdata.md) | :heavy_check_mark:                                     | N/A                                                    |