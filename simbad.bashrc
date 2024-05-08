export CONDA_HOME=/software/adaconda3
export CONDA_NAME=limsim

conda activate $CONDA_NAME

# carla API
export CARLA_ROOT=/software/CARLA_0.9.15
export PYTHONPATH=$PYTHONPATH:${CARLA_ROOT}/PythonAPI
export PYTHONPATH=$PYTHONPATH:${CARLA_ROOT}/PythonAPI/util
export PYTHONPATH=$PYTHONPATH:${CARLA_ROOT}/PythonAPI/carla
export PYTHONPATH=$PYTHONPATH:${CARLA_ROOT}/PythonAPI/carla/agents
alias go_carla="cd /software/CARLA_0.9.15"
alias open_carla="$CARLA_ROOT/CarlaUE4.sh -quality-level=Epic -world-port=2000 -resx=800 -resy=600"

# sumo API:
export SUMO_HOME=$CONDA_HOME/envs/$CONDA_NAME/lib/python3.9/site-packages/sumo
export PATH=$PATH:$SUMO_HOME/bin
export PYTHONPATH=$PYTHONPATH:$SUMO_HOME/tools