![Company logo](https://www.siri-cen.eu/2018/img/logo.png)

# SIRI Stop Monitoring integration for Home Assistant

## Compatible services
Services using the SIRI (Service Interface for Real time Information) specification are supported, including:

* [Environment Canterbury Metro](https://apidevelopers.metroinfo.co.nz/api-details#api=siri-service&operation=et)

Possibly others - let me know if you find one that works.

## Getting started
In your configuration.yaml file, add the following:

```
sensor:
  - platform: siri
    name: My Bus Stop
    id: 50001 # Your Bus Stop Id
    url: https://apis.metroinfo.co.nz/rti/siri/v1/et?routecode=100
    token: my-secret-api-key
```

## Installation
### HACS (recommended)
1. [Install HACS](https://hacs.xyz/docs/setup/download), if you did not already
2. [![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=codyc1515&repository=ha-siri&category=integration)
3. Install the SIRI integration
4. Restart Home Assistant

### Manually
Copy all files in the custom_components/siri folder to your Home Assistant folder *config/custom_components/siri*.

## Known issues
None known.

## Future enhancements
Your support is welcomed.
