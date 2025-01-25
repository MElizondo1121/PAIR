#!/bin/bash
#SBATCH --job-name=pre_sdoh
#SBATCH --partition=shared
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --nodes=1
#SBATCH --mem=240Gb
#SBATCH --time=14-00:00:00
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=m_e172@txstate.edu
#SBATCH --output=job_sdoh_output.txt
#SBATCH --error=job_sdoh_error.txt

echo ""
echo "Starting at `date`"
echo "Running on hosts: $SLURM_NODELIST"
echo "Running on $SLURM_NNODES nodes."
echo "Running on $SLURM_NPROCS processors."

# path to the correct directory
cd /home/m_e172/PAIR/
echo "Current working directory is `pwd`"

# Execute the script
# Load the Python module
module load python39

# Create and activate a virtual environment
python -m venv myenv
source myenv/bin/activate

# Install required packages
pip install numpy pandas scikit-learn matplotlib

python sdoh_preprocessing.py

deactivate
echo ""
echo "Program finished with exit code $? at: `date`"
echo ""
