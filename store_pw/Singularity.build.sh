#!/bin/bash

case $1 in
  1)# sudo singularity build ubuntu_base.simg ./Singularity.base-4.2.5
      singularity pull --name ubuntu_base.simg "shub://d-w-moore/new_d2c:base-4.2.5"
     ;;

  2) sudo singularity build --sandbox ubuntu_pw_1/ Singularity.pw_encrypt  # builds from ubuntu_base.simg
     ;;

  3) read -p "Enter Secret-Key:" INPUT_KEY
     read -p "Enter Password:  " INPUT_PW
     KEY="$INPUT_KEY" PW="$INPUT_PW" singularity run --app encrypt_pw ubuntu_pw_1 > encoded_password ;;

  4) sudo singularity build ubuntu_pw_2.simg Singularity.pw_embed ;;

  5) read -p "Enter Secret-Key:" INPUT_KEY_AGAIN
     singularity run --app decrypt_pw ubuntu_pw_2.simg -p "$INPUT_KEY_AGAIN"
esac



