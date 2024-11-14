#!/bin/bash
#SBATCH --partition=CPUQ
#SBATCH --account=share-nv-fys
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --exclusive
#SBATCH --time=01:00:00
#SBATCH --job-name=demo
#SBATCH --mem=5GB

module purge
module load OpenMPI/4.1.4-GCC-12.2.0

srun ./vampire-parallel

