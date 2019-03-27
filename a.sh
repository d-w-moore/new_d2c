#!/bin/bash
bc -l <<<"scale=${1:-4000};a(1)*4"
