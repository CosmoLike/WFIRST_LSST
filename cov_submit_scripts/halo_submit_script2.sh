#!/bin/bash
#PBS -S /bin/bash
#PBS -V
#PBS -q shortq
#PBS -l select=1:ncpus=1:mem=1GB
#PBS -l walltime=3:00:00
#PBS -J 1-6903
#PBS -N LSST1
#PBS -e /halo_nobackup/cosmos/teifler/output/
#PBS -o /halo_nobackup/cosmos/teifler/output/

cd $PBS_O_WORKDIR
/home/teifler/CosmoLike/LSST_emu/./compute_covariances_fourier_WFIRST_LSST2 $PBS_ARRAY_INDEX > /halo_nobackup/cosmos/teifler/job_output.log


