# ConfidenceScoringConfig

Simplified configuration wrapper that separates module name from config.  This model is shared between confidence-scoring-service and confidence-framework to ensure type consistency without OpenAPI Generator wrapper issues.


## Fields

| Field                                | Type                                 | Required                             | Description                          |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `module`                             | *str*                                | :heavy_check_mark:                   | N/A                                  |
| `config`                             | [models.Config](../models/config.md) | :heavy_check_mark:                   | Config                               |