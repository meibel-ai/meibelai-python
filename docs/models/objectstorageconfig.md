# ObjectStorageConfig

ObjectStorageConfig


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `bucket`                                                                           | *str*                                                                              | :heavy_check_mark:                                                                 | N/A                                                                                |
| `prefix`                                                                           | *Nullable[str]*                                                                    | :heavy_check_mark:                                                                 | N/A                                                                                |
| `filters`                                                                          | [OptionalNullable[models.ObjectStorageFilters]](../models/objectstoragefilters.md) | :heavy_minus_sign:                                                                 | N/A                                                                                |
| `gcs_config`                                                                       | Dict[str, *Any*]                                                                   | :heavy_minus_sign:                                                                 | N/A                                                                                |
| `s3_config`                                                                        | [OptionalNullable[models.S3Config]](../models/s3config.md)                         | :heavy_minus_sign:                                                                 | N/A                                                                                |