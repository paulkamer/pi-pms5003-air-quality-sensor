#!/bin/bash

# Outputs CPU temperature in InfluxDB line protocol
temp=$(cat /sys/class/thermal/thermal_zone0/temp)
echo "cpu,host=$(hostname) cpu_temp=$(echo "scale=1; $temp/1000" | bc)"
