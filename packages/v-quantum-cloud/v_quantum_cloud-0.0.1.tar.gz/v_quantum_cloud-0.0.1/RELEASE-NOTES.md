# 0.0.9 - 2022-02-16
## Maintenance
- Add Aspen-m-1 device, Device.AspenM1.

# 0.0.8 - 2021-12-27
## Maintenance
- Due to retirement of machines, only Device.Aspen11 is available for Rigetti device.

# 0.0.7 - 2021-06-22
## Bug fix & destructive changes
- `Api.annealing()` was broken due to annealing server side specifications were changed.
    - Now, it is work but interface is changed.
    - `api.annealing(...).table()` returns Pandas DataFrame.

# 0.0.6 - 2021-06-22
## Destructive changes
- Arguments `group` and `send_email` of `Api.execute()` are removed.
    - Use `option`. Refer "New features" section.
- `Device.Aspen8` is removed because it's retired.

## New features
- `Api.execute()` has `option` argument.
    - The type of `option` is a dictionary.
    - For cloud task, you can use `{ 'group': str, 'send_email': bool }`.
    - For local task, you can use `{ 'backend': str, 'run_option': {...} }`.
- Add new devices, `SimSv1`, `SimTn1`, `SimDm1`.

## Deprecated
- `Api.save_api` is deprecated. Use `Api.save_to_file`.
