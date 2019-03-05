# Running SLURM on ubuntu 16 or 18

```
sudo apt install slurm-wlm
git clone http://github.com/d-w-moore/new_d2c
perl process_slurm_template.pl  | sudo dd of=/etc/slurm-llnl/slurm.conf
sudo systemctl restart slurmctld slurmd
```
to test:
   - sudo apt install bc
   - create batch command file to be run
     ```
     cat >a.sh <<'EOF'
     #!/bin/bash
     bc -l <<<"scale=4000;a(1)*4"
     EOF
     ```
   - append
     ```
     Prolog='/usr/local/slurm/prolog.bash'
     Epilog='/usr/local/slurm/epilog.bash'
     sudo systemctl restart slurmctld slurmd
     ```
   - create a script  to produce log output
     ```
     cat >>/usr/local/slurm/prolog.bash
     #!/bin/bash
     env | grep SLURM
     echo Ran $0 @ `date`
     ```
   - the epilog can be a symlink in the same directory
