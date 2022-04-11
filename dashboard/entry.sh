#!/bin/bash

echo "balenaBlocks dashboard version: $(cat VERSION)"

# configure Python packages PATH
export PYTHONPATH=/usr/src/python-packages/

# grafana settings
# added org_name wjlove
export GF_PATHS_DATA="${BB_DATA_DIR:=/data}/dashboard"
export GF_SERVER_HTTP_PORT="${BB_DASHBOARD_PORT:=80}"
export GF_AUTH_ANONYMOUS_ENABLED=true
export GF_AUTH_ANONYMOUS_ORG_NAME="IAQ"
export GF_INSTALL_PLUGINS="grafana-clock-panel,grafana-simple-json-datasource"

python3 update-dashboards.py &

exec /usr/sbin/grafana-server -homepath /usr/share/grafana