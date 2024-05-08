from simModel.fixedSceneCrossing.model import Model
from trafficManager.traffic_manager import TrafficManager

import logger

log = logger.setup_app_level_logger(file_name="app_debug.log",
                                    level="DEBUG",
                                    use_stdout=False)

carlaNetFile = 'networkFiles/CarlaTown05/Town05.net.xml'
carlaRouFile = 'networkFiles/CarlaTown05/Town05.rou.xml'
carlaVtypeFile = 'networkFiles/CarlaTown05/carlavtypes.rou.xml'
carlaRouFile = carlaVtypeFile + ',' + carlaRouFile

def run_model(
    net_file,
    rou_file,
    ego_veh_loc="61",
    data_base="SimulationTest.db",
    SUMOGUI=0,
    sim_note="simulation test, simbad-v-0.1.0.",
    carla_cosim=False,
):  
    # Model将车辆的ego的location放进去
    model = Model(
        ego_veh_loc,
        net_file,
        rou_file,
        dataBase=data_base,
        SUMOGUI=SUMOGUI,
        simNote=sim_note,
        carla_cosim=carla_cosim,
    )
    