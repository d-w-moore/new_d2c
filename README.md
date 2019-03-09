# Installing and Running SLURM on ubuntu 16 or 18

## Install SLURM

```
sudo apt install slurm-wlm
git clone http://github.com/d-w-moore/new_d2c
perl process_slurm_template.pl  | sudo dd of=/etc/slurm-llnl/slurm.conf
sudo systemctl restart slurmctld slurmd
sudo systemctl enable  slurmctld slurmd
```

## Data/Compute automated setup

Change current directory to this repo and

```
sudo ./slurm_hook_setup.sh
```

to test:
   - sudo apt install bc
   - create batch command file to be run
   - locate test file (`slurm_pre_post_test.sh`)
   ```
     #!/bin/bash
     bc -l <<<"scale=4000;a(1)*4"
  ```
   - type: `sbatch ./a.sh`
   - type: `squeue` and note the job present (most likely running)
   - when it disapperas from queue, look in /tmp for logs produced by prolog / epilog scripts

  irods prolog and epilog scripts will create logs in `/tmp` before/after the job is executed
