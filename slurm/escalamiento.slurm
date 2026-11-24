#!/bin/bash
# Escalamiento fuerte en el clúster Xi (DIINF-USACH): SLURM 22.05, OpenMPI 4.0.4, Python 3.10.
# Enviar con:  sbatch slurm/escalamiento.slurm
# TODO: confirmar el nombre de la partición de CPU con `sinfo`.

#SBATCH --job-name=mpb-ca
#SBATCH --partition=CAMBIAR_PARTICION
#SBATCH --nodes=1
#SBATCH --ntasks=16
#SBATCH --cpus-per-task=1
#SBATCH --time=01:00:00
#SBATCH --output=resultados/slurm-%j.out
#SBATCH --error=resultados/slurm-%j.err

set -euo pipefail
cd "$SLURM_SUBMIT_DIR"
source .venv/bin/activate

TAM="--rows 800 --cols 800 --steps 10 --inicial uniforme"

python scripts/benchmark.py --modo hilos --max "$SLURM_NTASKS" $TAM
python scripts/benchmark.py --modo mpi   --max "$SLURM_NTASKS" $TAM
