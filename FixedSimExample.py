from simModel.fixedScene.model import Model
from trafficManager.traffic_manager import TrafficManager

import logger
# config a logger, set use_stdout=True to output log to terminal
log = logger.setup_app_level_logger(file_name="app_debug.log",
                                    level="DEBUG",
                                    use_stdout=False)


carlaNetFile = 'networkFiles/CarlaTown05/Town05.net.xml'
carlaRouFile = 'networkFiles/CarlaTown05/Town05.rou.xml'
carlaVtypeFile = 'networkFiles/CarlaTown05/carlavtypes.rou.xml'
carlaRouFile = carlaVtypeFile + ',' + carlaRouFile

if __name__ == '__main__':
    fmodel = Model(
        (300, 198),
        50,
        carlaNetFile,
        carlaRouFile,
        dataBase='fixedSceneTest.db',
        SUMOGUI=0,
        simNote='local model first testing.',
    )

    fmodel.start()
    planner = TrafficManager(fmodel)

    # 当本次仿真没有结束
    while not fmodel.simEnd:

        fmodel.moveStep()
        if fmodel.timeStep % 5 == 0:
            # 这个函数相当于导出信息
            # 通过导出的信息求解轨迹
            roadgraph, vehicles = fmodel.exportSce()
            if roadgraph:
                trajectories = planner.plan(
                    fmodel.timeStep * 0.1, roadgraph, vehicles)
                # 将轨迹作用于fmodel
                fmodel.setTrajectories(trajectories)

        fmodel.updateVeh()

    fmodel.destroy()