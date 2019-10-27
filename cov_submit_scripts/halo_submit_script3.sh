#!/bin/bash
#PBS -S /bin/bash
#PBS -V
#PBS -q mediumq
#PBS -l select=1:ncpus=1:mem=1GB
#PBS -l walltime=12:00:00
#PBS -J 1-4753
#PBS -N LSST1
#PBS -e /halo_nobackup/cosmos/teifler/output/
#PBS -o /halo_nobackup/cosmos/teifler/output/

cd $PBS_O_WORKDIR
/home/teifler/CosmoLike/LSST_emu/./compute_covariances_fourier_WFIRST_LSST3 $PBS_ARRAY_INDEX > /halo_nobackup/cosmos/teifler/job_output.log


