# Installing and Running SLURM on ubuntu 16 or 18

```
sudo apt install slurm-wlm
git clone http://github.com/d-w-moore/new_d2c
perl process_slurm_template.pl  | sudo dd of=/etc/slurm-llnl/slurm.conf
sudo systemctl restart slurmctld slurmd
sudo systemctl enable  slurmctld slurmd
```

Data/Compute automated setup


```
cd ~/new_d2c
./process_slurm_template.pl
./slurm_hook_setup.sh
```


to test:
   - sudo apt install bc
   - create batch command file to be run
   - create a file containing
   ```
     #!/bin/bash
     bc -l <<<"scale=4000;a(1)*4"
  ```
   - type: `sbatch ./a.sh`

  irods prolog and epilog scripts will create logs in `/tmp` before/after the job is executed
