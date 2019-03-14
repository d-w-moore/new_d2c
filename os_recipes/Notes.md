# Singularity recipes for building a basic OS

---

For demo purposes, assume we are using the recipes on a Ubuntu >=16.04  system

   - if building debian  or ubuntu container, make sure to have debootstrap installed
     (warning, debootstrap may not work w/ 'singularity build' if host os < Ubuntu-16

   - if building centos , do this before building: 
   ```
   sudo apt install yum
   sudo dd of=/root/.rpmmacros <<<$'%_var /var\n%_dbpath %{_var}/lib/rpm' 
   ```
   - then:
      - `sudo singularity build --sandbox container_directory Singularity.<OS_Type>`
     or
      - `sudo singularity build container image Singularity.<OS_Type>`
   - a sandbox can be
      -  converted to an image - `sudo singularity build fixed.img sandbox.src`
      -  converted from an image back to a sandbox - `sudo singularity build --sandbox sandbox.dst fixed.img`
      -  removed  `sudo rm -fr sandbox/`

   - an image can be used to create a temporary environment (shell/exec) or execute default
     runscripts or apps built into it.

   - OS container build without admin privilege may not work correctly in all situations
     (This may have to do with suid root executables)

