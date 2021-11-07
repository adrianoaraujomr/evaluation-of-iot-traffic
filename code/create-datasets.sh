#!/bin/bash

# Experimento 1

./generate-experiment-ds.py ../datasets/experimento-1/iot-mobile-nontor 22000 9 -exp1 -nrodatasets 5
./generate-experiment-ds.py ../datasets/experimento-1/iot-mobile 22000 9 -exp1 -nrodatasets 5 -nrm 0 -mbl 1
./generate-experiment-ds.py ../datasets/experimento-1/iot-nontor 22000 9 -exp1 -nrodatasets 5 -nrm 1 -mbl 0
./generate-experiment-ds.py ../datasets/experimento-1/only-mobile 22000 9 -exp1 -nrodatasets 5 -iot 0 -nrm 0 -mbl 1
./generate-experiment-ds.py ../datasets/experimento-1/only-nontor 22000 9 -exp1 -nrodatasets 5 -iot 0 -nrm 1 -mbl 0


# Experimento 2
# Obs.: As vezes compensa colocar uma opção para setar a classe

./generate-experiment-ds.py ../datasets/experimento-2 22000 10 -exp2 -nrodatasets 5

# Experimento 3

./generate-experiment-ds.py ../datasets/experimento-extra 22000 9 -exp3 -nrodatasets 5

# Clean datasets : Limpar datasets que já tinham sido gerados

#./dataset-cleaner.py datasets/original/benignos/dataset.csv
#./dataset-cleaner.py datasets/original/benignos/iot-per-device.csv

# ./dataset-cleaner.py datasets/experimento-1/iot-mobile-nontor/05_05_05-90-test.csv
# ./dataset-cleaner.py datasets/experimento-1/iot-mobile-nontor/05_05_05-90-train.csv
# ./dataset-cleaner.py datasets/experimento-1/iot-mobile-nontor/05_05_05-91-test.csv
# ./dataset-cleaner.py datasets/experimento-1/iot-mobile-nontor/05_05_05-91-train.csv
# ./dataset-cleaner.py datasets/experimento-1/iot-mobile-nontor/05_05_05-92-test.csv
# ./dataset-cleaner.py datasets/experimento-1/iot-mobile-nontor/05_05_05-92-train.csv
# ./dataset-cleaner.py datasets/experimento-1/iot-mobile-nontor/05_05_05-93-test.csv
# ./dataset-cleaner.py datasets/experimento-1/iot-mobile-nontor/05_05_05-93-train.csv
# ./dataset-cleaner.py datasets/experimento-1/iot-mobile-nontor/05_05_05-94-test.csv
# ./dataset-cleaner.py datasets/experimento-1/iot-mobile-nontor/05_05_05-94-train.csv

# ./dataset-cleaner.py datasets/experimento-1/iot-mobile/05_10_00-90-test.csv
# ./dataset-cleaner.py datasets/experimento-1/iot-mobile/05_10_00-90-train.csv
# ./dataset-cleaner.py datasets/experimento-1/iot-mobile/05_10_00-91-test.csv
# ./dataset-cleaner.py datasets/experimento-1/iot-mobile/05_10_00-91-train.csv
# ./dataset-cleaner.py datasets/experimento-1/iot-mobile/05_10_00-92-test.csv
# ./dataset-cleaner.py datasets/experimento-1/iot-mobile/05_10_00-92-train.csv
# ./dataset-cleaner.py datasets/experimento-1/iot-mobile/05_10_00-93-test.csv
# ./dataset-cleaner.py datasets/experimento-1/iot-mobile/05_10_00-93-train.csv
# ./dataset-cleaner.py datasets/experimento-1/iot-mobile/05_10_00-94-test.csv
# ./dataset-cleaner.py datasets/experimento-1/iot-mobile/05_10_00-94-train.csv

# ./dataset-cleaner.py datasets/experimento-1/iot-nontor/05_00_10-90-test.csv
# ./dataset-cleaner.py datasets/experimento-1/iot-nontor/05_00_10-90-train.csv
# ./dataset-cleaner.py datasets/experimento-1/iot-nontor/05_00_10-91-test.csv
# ./dataset-cleaner.py datasets/experimento-1/iot-nontor/05_00_10-91-train.csv
# ./dataset-cleaner.py datasets/experimento-1/iot-nontor/05_00_10-92-test.csv
# ./dataset-cleaner.py datasets/experimento-1/iot-nontor/05_00_10-92-train.csv
# ./dataset-cleaner.py datasets/experimento-1/iot-nontor/05_00_10-93-test.csv
# ./dataset-cleaner.py datasets/experimento-1/iot-nontor/05_00_10-93-train.csv
# ./dataset-cleaner.py datasets/experimento-1/iot-nontor/05_00_10-94-test.csv
# ./dataset-cleaner.py datasets/experimento-1/iot-nontor/05_00_10-94-train.csv

# ./dataset-cleaner.py datasets/experimento-2/appliences/appliences_05_05_05-90-test.csv
# ./dataset-cleaner.py datasets/experimento-2/appliences/appliences_05_05_05-90-train.csv
# ./dataset-cleaner.py datasets/experimento-2/appliences/appliences_05_05_05-91-test.csv
# ./dataset-cleaner.py datasets/experimento-2/appliences/appliences_05_05_05-91-train.csv
# ./dataset-cleaner.py datasets/experimento-2/appliences/appliences_05_05_05-92-test.csv
# ./dataset-cleaner.py datasets/experimento-2/appliences/appliences_05_05_05-92-train.csv
# ./dataset-cleaner.py datasets/experimento-2/appliences/appliences_05_05_05-93-test.csv
# ./dataset-cleaner.py datasets/experimento-2/appliences/appliences_05_05_05-93-train.csv
# ./dataset-cleaner.py datasets/experimento-2/appliences/appliences_05_05_05-94-test.csv
# ./dataset-cleaner.py datasets/experimento-2/appliences/appliences_05_05_05-94-train.csv

# ./dataset-cleaner.py datasets/experimento-2/cameras/cameras_05_05_05-90-test.csv
# ./dataset-cleaner.py datasets/experimento-2/cameras/cameras_05_05_05-90-train.csv
# ./dataset-cleaner.py datasets/experimento-2/cameras/cameras_05_05_05-91-test.csv
# ./dataset-cleaner.py datasets/experimento-2/cameras/cameras_05_05_05-91-train.csv
# ./dataset-cleaner.py datasets/experimento-2/cameras/cameras_05_05_05-92-test.csv
# ./dataset-cleaner.py datasets/experimento-2/cameras/cameras_05_05_05-92-train.csv
# ./dataset-cleaner.py datasets/experimento-2/cameras/cameras_05_05_05-93-test.csv
# ./dataset-cleaner.py datasets/experimento-2/cameras/cameras_05_05_05-93-train.csv
# ./dataset-cleaner.py datasets/experimento-2/cameras/cameras_05_05_05-94-test.csv
# ./dataset-cleaner.py datasets/experimento-2/cameras/cameras_05_05_05-94-train.csv

# ./dataset-cleaner.py datasets/experimento-2/controller_hubs/controller-hubs_05_05_05-90-test.csv
# ./dataset-cleaner.py datasets/experimento-2/controller_hubs/controller-hubs_05_05_05-90-train.csv
# ./dataset-cleaner.py datasets/experimento-2/controller_hubs/controller-hubs_05_05_05-91-test.csv
# ./dataset-cleaner.py datasets/experimento-2/controller_hubs/controller-hubs_05_05_05-91-train.csv
# ./dataset-cleaner.py datasets/experimento-2/controller_hubs/controller-hubs_05_05_05-92-test.csv
# ./dataset-cleaner.py datasets/experimento-2/controller_hubs/controller-hubs_05_05_05-92-train.csv
# ./dataset-cleaner.py datasets/experimento-2/controller_hubs/controller-hubs_05_05_05-93-test.csv
# ./dataset-cleaner.py datasets/experimento-2/controller_hubs/controller-hubs_05_05_05-93-train.csv
# ./dataset-cleaner.py datasets/experimento-2/controller_hubs/controller-hubs_05_05_05-94-test.csv
# ./dataset-cleaner.py datasets/experimento-2/controller_hubs/controller-hubs_05_05_05-94-train.csv

# ./dataset-cleaner.py datasets/experimento-2/energy_managment/energy-managment_05_05_05-90-test.csv
# ./dataset-cleaner.py datasets/experimento-2/energy_managment/energy-managment_05_05_05-90-train.csv
# ./dataset-cleaner.py datasets/experimento-2/energy_managment/energy-managment_05_05_05-91-test.csv
# ./dataset-cleaner.py datasets/experimento-2/energy_managment/energy-managment_05_05_05-91-train.csv
# ./dataset-cleaner.py datasets/experimento-2/energy_managment/energy-managment_05_05_05-92-test.csv
# ./dataset-cleaner.py datasets/experimento-2/energy_managment/energy-managment_05_05_05-92-train.csv
# ./dataset-cleaner.py datasets/experimento-2/energy_managment/energy-managment_05_05_05-93-test.csv
# ./dataset-cleaner.py datasets/experimento-2/energy_managment/energy-managment_05_05_05-93-train.csv
# ./dataset-cleaner.py datasets/experimento-2/energy_managment/energy-managment_05_05_05-94-test.csv
# ./dataset-cleaner.py datasets/experimento-2/energy_managment/energy-managment_05_05_05-94-train.csv

# ./dataset-cleaner.py datasets/experimento-2/health_monitor/health-monitor_05_05_05-90-train.csv
# ./dataset-cleaner.py datasets/experimento-2/health_monitor/health-monitor_05_05_05-91-train.csv
# ./dataset-cleaner.py datasets/experimento-2/health_monitor/health-monitor_05_05_05-92-train.csv
# ./dataset-cleaner.py datasets/experimento-2/health_monitor/health-monitor_05_05_05-93-train.csv
# ./dataset-cleaner.py datasets/experimento-2/health_monitor/health-monitor_05_05_05-94-train.csv
# ./dataset-cleaner.py datasets/experimento-2/health_monitor/health-monitor_05_05_05-90-test.csv
# ./dataset-cleaner.py datasets/experimento-2/health_monitor/health-monitor_05_05_05-91-test.csv
# ./dataset-cleaner.py datasets/experimento-2/health_monitor/health-monitor_05_05_05-92-test.csv
# ./dataset-cleaner.py datasets/experimento-2/health_monitor/health-monitor_05_05_05-93-test.csv
# ./dataset-cleaner.py datasets/experimento-2/health_monitor/health-monitor_05_05_05-94-test.csv

# ./dataset-cleaner.py datasets/experimento-2/all_iot/all-iot_05_05_05-90-train.csv
# ./dataset-cleaner.py datasets/experimento-2/all_iot/all-iot_05_05_05-91-train.csv
# ./dataset-cleaner.py datasets/experimento-2/all_iot/all-iot_05_05_05-92-train.csv
# ./dataset-cleaner.py datasets/experimento-2/all_iot/all-iot_05_05_05-93-train.csv
# ./dataset-cleaner.py datasets/experimento-2/all_iot/all-iot_05_05_05-94-train.csv

#./dataset-cleaner datasets/experimento-1/iot-mobile/
#./dataset-cleaner datasets/experimento-1/iot-nontor/

#./dataset-cleaner datasets/experimento-2/appliences/
#./dataset-cleaner datasets/experimento-2/cameras/
#./dataset-cleaner datasets/experimento-2/controller_hubs/
#./dataset-cleaner datasets/experimento-2/energy_managment/
#./dataset-cleaner datasets/experimento-2/health_monitor/
