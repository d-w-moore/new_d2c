# Installing and Running SLURM on ubuntu 16 or 18

## Install SLURM

```
sudo apt install slurm-wlm
git clone http://github.com/d-w-moore/new_d2c
cd new_d2c
perl process_slurm_template.pl  | sudo dd of=/etc/slurm-llnl/slurm.conf
sudo systemctl restart slurmctld slurmd
sudo systemctl enable  slurmctld slurmd
```

to test:
   - sudo apt install bc
   - locate command file slurm_install_test.sh containing:
   ```
     #!/bin/bash
     bc -l <<<"scale=4000;a(1)*4"
  ```
   - run the above mentioned test script using : `sbatch <script>`
   - type: `squeue` and note the job present (most likely running)
   - when it disappears from queue (`watch -n1 squeue`), look for `slurm-<JOBNUM>.out`
     containing the job's output

## Data/Compute automated setup - install iRODS hook scripts for slurm prolog / epilog

The following command will setup prolog and epilog scripts to be run (pre- and post-, 
respectively) for each job executed by SLURM:

```
sudo ./slurm_hook_setup.sh
```

