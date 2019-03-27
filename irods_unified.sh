#!/bin/bash
IRODS_COMPUTE_DIR='/var/lib/irods/Slurm'
BASE_NAME=$(basename $0)
script="${IRODS_COMPUTE_DIR}/${BASE_NAME}_script"
su irods -c "test -r '$script' && test -x '$script'" &&\
    exec su irods -c "'$script'"
