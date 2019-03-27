#!/bin/bash

SLURM_HOOK_DIR=/usr/local/slurm
IRODS_SLURM_DIR=~irods/Slurm
SLURM_CONF_FILE=/etc/slurm-llnl/slurm.conf

[ `id -u` != 0 ] && { echo >&2 "run sudo or as root"; exit 1; }

mkdir -p $SLURM_HOOK_DIR

cp "$(dirname $0)"/irods_unified.sh $SLURM_HOOK_DIR/.
chown root.root $SLURM_HOOK_DIR/irods_unified.sh
chmod 755 $SLURM_HOOK_DIR/irods_unified.sh

ln -sf irods_unified.sh $SLURM_HOOK_DIR/irods_prolog
ln -sf irods_unified.sh $SLURM_HOOK_DIR/irods_epilog

grep -Ei '^(\s|#)*(Epilog|Prolog)=' $SLURM_CONF_FILE >/dev/null || {
  echo "# -- Pre/Post hooks into iRODS"
  echo "Prolog=$SLURM_HOOK_DIR/irods_prolog"
  echo "Epilog=$SLURM_HOOK_DIR/irods_epilog"
  }  >> $SLURM_CONF_FILE

sudo mkdir -p "${IRODS_SLURM_DIR}"
sudo chown irods.irods "${IRODS_SLURM_DIR}"
for script in "${IRODS_SLURM_DIR}"/irods_{pro,epi}log_script
do
    sudo su irods -c "touch '$script' ; chmod 775 '$script'"
done
sudo systemctl restart slurmctld slurmd #--> to enable irods prolog/epilog
