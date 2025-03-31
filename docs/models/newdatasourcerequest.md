# NewDatasourceRequest


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          | Example                                              |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `description`                                        | *str*                                                | :heavy_check_mark:                                   | A description of the datasource                      | A datasource                                         |
| `name`                                               | *str*                                                | :heavy_check_mark:                                   | The name of the datasource                           | My Datasource                                        |
| `type`                                               | [models.DatasourceType](../models/datasourcetype.md) | :heavy_check_mark:                                   | N/A                                                  |                                                      |
| `metadata`                                           | [Optional[models.Metadata]](../models/metadata.md)   | :heavy_minus_sign:                                   | N/A                                                  |                                                      |