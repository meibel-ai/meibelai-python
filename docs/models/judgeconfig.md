# JudgeConfig

Configuration for judge-based confidence scoring (LLM-as-judge patterns).


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `prompt`                                                                 | *str*                                                                    | :heavy_check_mark:                                                       | N/A                                                                      |
| `temperature_max`                                                        | [OptionalNullable[models.TemperatureMax]](../models/temperaturemax.md)   | :heavy_minus_sign:                                                       | N/A                                                                      |
| `temperature_step`                                                       | [OptionalNullable[models.TemperatureStep]](../models/temperaturestep.md) | :heavy_minus_sign:                                                       | N/A                                                                      |