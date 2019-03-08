#!/bin/bash

SLURM_HOOK_DIR=/usr/local/slurm
IRODS_SLURM_DIR=~irods/Slurm

[ `id -u` != 0 ] && { echo >&2 "run sudo or as root"; exit 1; }

mkdir -p $SLURM_HOOK_DIR

echo > $SLURM_HOOK_DIR/unified.sh "#!/bin/bash
IRODS_COMPUTE_DIR='$IRODS_SLURM_DIR'
BASE_NAME=\$(basename \$0)
exec su - irods -c \"\${IRODS_COMPUTE_DIR}/\${BASE_NAME}_script\""

chmod +x $SLURM_HOOK_DIR/unified.sh
ln -sf unified.sh $SLURM_HOOK_DIR/irods_prolog
ln -sf unified.sh $SLURM_HOOK_DIR/irods_epilog
