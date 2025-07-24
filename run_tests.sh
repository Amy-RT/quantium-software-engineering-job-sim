# ensure the script is always executed using the Bash interpreter
# to prevent potential issues if the CI runner's default shell is different
#!/bin/bas

# If pytests fail, 'set -e' will cause the script to exit with 1 automatically.
set -e

# --- Conda Initialization for the script's subshell ---
CONDA_BASE_PATH="/opt/anaconda3" 

# Check if the conda.sh script exists before sourcing
if [ -f "$CONDA_BASE_PATH/etc/profile.d/conda.sh" ]; then
    echo "Sourcing Conda initialization script..."
    source "$CONDA_BASE_PATH/etc/profile.d/conda.sh"
else
    echo "Error: Conda initialization script not found at $CONDA_BASE_PATH/etc/profile.d/conda.sh"
    echo "Please ensure CONDA_BASE_PATH is set correctly in run_tests.sh."
    exit 1
fi

# activate virtual environment
ENV_PATH="/Users/lutra10/Documents/CV Builders/Quantium Software Engineering Job Sim/env"
echo "Activating Conda environment: $ENV_PATH"
conda activate "$ENV_PATH"

# run tests
echo "Running pytest..."
pytest

# deactivate virtual environment 
conda deactivate

echo "Test suite completed successfully!"
exit 0






# command to make the script executable 
# chmod +x run_tests.sh

# execute bash script from project root 
# ./run_tests.sh