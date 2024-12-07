# Version Name Rule
| Symbol            | Meaning                                                     | Example(s)                                                                    |
|-------------------|-------------------------------------------------------------|-------------------------------------------------------------------------------|
| Major.Minor.Patch | Major, Minor, and Patch version numbers                     | 1.0.0 (Major=1, Minor=0, Patch=0)                                             |
| `^`               | More minor version, less than the next major version number | `^1.0.0` (1.0.0 <= version < 2.0.0)                                           |
| `~`               | More patch version, less than the next minor version number | `~1.0.0` (1.0.0 <= version < 1.1.0)                                           |
| `*`               | Any version number                                          | `*` (any version number), `1.*` (1.any version)                               |
| `>=`              | Greater than or equal to the version number                 | `>=1.0.0` (1.0.0 <= version)                                                  |
| `<=`              | Less than or equal to the version number                    | `<=1.0.0` (version <= 1.0.0)                                                  |
| `>`               | Greater than the version number                             | `>1.0.0` (1.0.0 < version)                                                    |
| `<`               | Less than the version number                                | `<1.0.0` (version < 1.0.0)                                                    |
| `==`              | Exactly equal to the version number                         | `==1.0.0` (version == 1.0.0)                                                  |
| `!=`              | Not equal to the version number                             | `!=1.0.0` (version != 1.0.0), `!=1.0.0, !=1.1.0` (version != 1.0.0 and 1.1.0) |
| `1.0.0`           | Only the specified version                                  | `1.0.0` (only version 1.0.0)                                                  |

