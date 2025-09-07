# BodyUploadDatasourceContent


## Fields

| Field                                     | Type                                      | Required                                  | Description                               |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| `files`                                   | List[[models.Files](../models/files.md)]  | :heavy_check_mark:                        | Files to upload to the datasource         |
| `prefix`                                  | *OptionalNullable[str]*                   | :heavy_minus_sign:                        | Path prefix for organizing uploaded files |
| `extract_zip`                             | *OptionalNullable[bool]*                  | :heavy_minus_sign:                        | Auto-extract ZIP archives                 |
| `extract_eml`                             | *OptionalNullable[bool]*                  | :heavy_minus_sign:                        | Extract EML email files                   |
| `max_concurrent`                          | *OptionalNullable[int]*                   | :heavy_minus_sign:                        | Maximum concurrent file uploads           |