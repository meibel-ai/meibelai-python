# SSEProgressEventData


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `type`                                                                   | *str*                                                                    | :heavy_check_mark:                                                       | Progress event subtype                                                   |
| `upload_id`                                                              | *str*                                                                    | :heavy_check_mark:                                                       | Upload ID                                                                |
| `timestamp`                                                              | *float*                                                                  | :heavy_check_mark:                                                       | Event timestamp                                                          |
| `data`                                                                   | [models.SSEProgressEventDataData](../models/sseprogresseventdatadata.md) | :heavy_check_mark:                                                       | Progress data                                                            |