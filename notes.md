In root hooks in /usr/local/slurm, adding this line:
```
env|grep SLURM
```
can produce helpful environment vars list
(in compute/data, these vars are passed on to the irods hooks):

example from  prolog:
```
SLURM_NODELIST=ubuntu16
SLURMD_NODENAME=ubuntu16
SLURM_JOBID=4
SLURM_STEP_ID=4294967294
SLURM_CONF=/etc/slurm-llnl/slurm.conf
SLURM_JOB_ID=4
SLURM_JOB_USER=danielm
SLURM_UID=1000
SLURM_JOB_UID=1000
SLURM_CLUSTER_NAME=ubuntu16
SLURM_JOB_PARTITION=long
SLURM_JOB_CONSTRAINTS=(null)
```

example from epilog:
```
SLURM_NODELIST=ubuntu16
SLURMD_NODENAME=ubuntu16
SLURM_JOBID=3
SLURM_CONF=/etc/slurm-llnl/slurm.conf
SLURM_JOB_ID=3
SLURM_JOB_USER=danielm
SLURM_UID=1000
SLURM_JOB_UID=1000
SLURM_CLUSTER_NAME=ubuntu16
```
