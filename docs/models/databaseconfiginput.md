# DatabaseConfigInput

DatabaseConfig


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `anyof_schema_1_validator`                                                 | [OptionalNullable[models.DuckDBConfig]](../models/duckdbconfig.md)         | :heavy_minus_sign:                                                         | N/A                                                                        |
| `anyof_schema_2_validator`                                                 | [OptionalNullable[models.ClickhouseConfig]](../models/clickhouseconfig.md) | :heavy_minus_sign:                                                         | N/A                                                                        |
| `anyof_schema_3_validator`                                                 | [OptionalNullable[models.PostgreSQLConfig]](../models/postgresqlconfig.md) | :heavy_minus_sign:                                                         | N/A                                                                        |
| `actual_instance`                                                          | *Optional[Any]*                                                            | :heavy_minus_sign:                                                         | N/A                                                                        |
| `any_of_schemas`                                                           | List[*str*]                                                                | :heavy_minus_sign:                                                         | N/A                                                                        |