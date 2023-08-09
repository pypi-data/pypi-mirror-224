from typing import Any, Optional, Union
from ._iort_engine_ import IORTEngine
from datetime import datetime
import time
import json

class EngineEvaluator:
    def __init__(self, engine:IORTEngine, time_zone_info:Optional[Any]=None) -> None:
        self.engine = engine
        self.process_log = self.create_process_log()
        self.time_zone_info = time_zone_info

    def create_process_log(self):
        # init
        return {
            "start_time":"None",
            "iter_logs":[],
            "number_of_epoch" : 0,
        }
    
    def save_testdata(self, result_test_data_path:str, additional_info:Union[dict, None] = None):
        #init
        path:str = result_test_data_path
        process_log:dict = self.process_log
        infos = {}
        
        infos.update(process_log)
        if additional_info:
            infos.update(additional_info)
        with open(path, 'w') as json_file:
            json.dump(infos, json_file, indent=4)

    def run(self, dataset:Any):
        try:
            _ = iter(dataset)
        except TypeError as te:
            print(dataset, 'is not iterable')
        # init
        time_zone_info = self.time_zone_info
        engine = self.engine
        self.process_log = self.create_process_log()
        process_log = self.process_log
        process_log["number_of_epoch"] = len(dataset)
        process_log["start_time"] = datetime.now(time_zone_info).strftime("%Y-%m-%d-%H-%M-%S")

        # run
        process_start = time.time()
        for idx in range(len(dataset)):
            log = {}
            _key_ = "load_data"
            log[_key_] = time.time()
            loaded_data = dataset[idx]
            log[_key_] = time.time() - log[_key_]

            _key_ = "set_input_data"
            log[_key_] = time.time()
            engine.set_input_data(data=loaded_data)
            log[_key_] = time.time() - log[_key_]

            _key_ = "convert_data2input"
            log[_key_] = time.time()
            engine.convert_data2input()
            log[_key_] = time.time() - log[_key_]

            _key_ = "move_host2device"
            log[_key_] = time.time()
            engine.move_host2device()
            log[_key_] = time.time() - log[_key_]

            _key_ = "inference"
            log[_key_] = time.time()
            engine.inference()
            log[_key_] = time.time() - log[_key_]

            _key_ = "move_device2host"
            log[_key_] = time.time()
            engine.move_device2host()
            log[_key_] = time.time() - log[_key_]

            _key_ = "convert_output2data"
            log[_key_] = time.time()
            engine.convert_output2data()
            log[_key_] = time.time() - log[_key_]

            _key_ = "get_output_data"
            log[_key_] = time.time()
            result_images = engine.get_output_data()
            log[_key_] = time.time() - log[_key_]

            _key_ = "save_data"
            log[_key_] = time.time()
            # TODO!!
            # os.makedirs(result_image_path, exist_ok=True)
            # cv2.imwrite(result_image_path.format(name=f"{idx:08d}.bmp"), result_images[0])
            log[_key_] = time.time() - log[_key_]
            process_log["iter_logs"].append(log)
        process_end = time.time()
        process_log["processing_time"] = process_end - process_start
        process_log["end_time"] = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")