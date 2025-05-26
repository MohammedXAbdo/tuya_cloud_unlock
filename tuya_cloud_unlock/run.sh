#!/usr/bin/with-contenv bashio
ACCESS_ID=$(bashio::config 'access_id')
ACCESS_KEY=$(bashio::config 'access_key')
DEVICE_ID=$(bashio::config 'device_id')
API_REGION=$(bashio::config 'api_region')

python3 /tuya_unlock.py "$ACCESS_ID" "$ACCESS_KEY" "$DEVICE_ID" "$API_REGION"
