# WFDE5 Flux ERA5-Time Source Plugin

Project-local `anemoi-datasets` source plugin for `wfde5_nrt`.

This source wraps a single WFDE5 flux source and retags its `valid_datetime`
metadata so the emitted fields behave like ERA5 end-of-interval fluxes. The
underlying WFDE5 values are not modified.

## Behaviour

- For a requested ERA5-like target time `T`, the plugin loads the wrapped WFDE5
	source at `T - 1h`.
- It re-emits the field with `valid_datetime = T`.
- It may skip the first requested timestamp only when it matches an explicit
	`global_start`.
- It fails loudly if any other shifted source timestamp is unavailable.

## Recipe Shape

```yaml
- wfde5-flux-era5-time:
		global_start: "1979-01-01T00:00:00"
		source:
			netcdf:
				path: "/path/to/LWdown_WFDE5_CRU_{date:strftime(%Y%m)}_v2.1.nc"
```

## Testing

Fast plugin tests:

```bash
pixi run -e test pytest plugins/wfde5-flux-era5-source/tests
```

Optional end-to-end dataset build test:

```bash
pixi run -e test pytest plugins/wfde5-flux-era5-source/tests --run-build-tests
```

The optional build test uses `tests/test-wfde5-anemoi-recipe.yaml` and writes to:

`/ec/res4/scratch/ecm6845/wfde5-ml/anemoi/datasets/wfde5_ml_test.zarr`
