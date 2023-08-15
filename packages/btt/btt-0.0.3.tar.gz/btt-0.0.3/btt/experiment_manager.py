import json
import os
import threading
from typing import Optional, Dict, Any, List

from .utils import get_uuid


class AlgorithmConfig:
    # for: monitor_rule tuner_hpo assessor_indicator
    # btt的monitor/tuner/assessor其实都只有一个 只是具体可能存在多个(也不一定同时用)的rule/hpo/indicator！
    name: Optional[str] = None
    class_name: Optional[str] = None
    code_directory: Optional[os.PathLike] = None
    class_args: Optional[Dict[str, Any]] = None


class ExperimentConfig:
    # 给用户 方便填写
    # exp_uuid: str = None # 用户不填
    exp_name: Optional[str] = None  # canonicalize 以后再弄
    exp_description: Optional[str] = None
    trial_concurrency: int = 4
    trial_gpu_number: int = 0
    max_trial_number: int = 1000
    max_exp_duration: str = "12h"
    tuner_config: List[AlgorithmConfig] = []
    monitor_config: List[AlgorithmConfig] = []
    assessor_config: List[AlgorithmConfig] = []
    btt_exp_dir: Optional[os.PathLike] = "./btt_experiments"

    def __init__(self, exp_uuid=None, btt_exp_dir=None):
        self.config_file_name = "exp_config.json"
        if type(exp_uuid) is str:
            self.exp_uuid = exp_uuid
            self.btt_exp_dir = btt_exp_dir if btt_exp_dir is not None else self.btt_exp_dir
            self.exp_config = self.load_exp_config()
        pass

    def load_exp_config(self):
        exp_dir = os.path.join(self.btt_exp_dir, self.exp_uuid)
        exp_config_path = os.path.join(exp_dir, self.config_file_name)
        with open(exp_config_path, "r") as f:
            exp_config = json.load(f)
        return exp_config

    def save_exp_config(self):
        exp_config_path = os.path.join(self.btt_exp_dir, self.exp_uuid, self.config_file_name)
        with open(exp_config_path, "w") as f:
            json.dump(self.exp_config, f)


class BttExperimentManager:
    def __init__(self, exp_config_instance):
        # start stop resume view
        # self.exp_config_instance = ExperimentConfig(exp_config_args)  # 用来保存ok 实际使用可以直接哟过exp_manager
        self.exp_id = get_uuid(8)
        if type(exp_config_instance) is str:
            self.exp_uuid = exp_config_instance
            self.btt_exp_dir = "./btt_experiments" if "btt_exp_dir" not in exp_config_instance else exp_config_instance["btt_exp_dir"]
            self.exp_config = self.load_exp_config()

        self.exp_config = exp_config_instance
        self.exp_name = exp_config_instance["exp_name"]
        self.exp_description = exp_config_instance["exp_description"]

        self.btt_exp_dir = exp_config_instance["btt_exp_dir"] if "btt_exp_dir" in exp_config_instance else "./btt_experiments"
        self.exp_config_path = self.btt_exp_dir + "/exp_config.json"

        self.exp_dir = self.btt_exp_dir + "/" + self.exp_id
        self.log_dir = self.exp_dir + "/log"
        self.db_dir = self.exp_dir + "/db"
        self.checkpoint_dir = self.exp_dir + "/checkpoint"
        self.trials_dir = self.exp_dir + "/trials"
        self.create_dir_and_path()

        # self.exp_db = self.create_exp_db() # 暂时不需要db？可以最后再加入
        self.trial_concurrency = exp_config_instance["trial_concurrency"]
        self.trial_gpu_number = exp_config_instance["trial_gpu_number"] if "trial_gpu_number" in exp_config_instance else 0
        self.max_trial_number = exp_config_instance["max_trial_number"] if "max_trial_number" in exp_config_instance else 1000
        self.max_exp_duration = exp_config_instance["max_exp_duration"] if "max_exp_duration" in exp_config_instance else "12h"
        # self.space_path = config_args["space_path"] # 逐步传入，第一次report时确定

        self.monitor_config = exp_config_instance["monitor_config"] if "monitor_config" in exp_config_instance else None
        self.tuner_config = exp_config_instance["tuner_config"] if "tuner_config" in exp_config_instance else None
        self.assessor_config = exp_config_instance["assessor_config"] if "assessor_config" in exp_config_instance else None

    def start_workers(self):
        for i in range(self.num_workers):
            t = threading.Thread(target=self.worker_thread)
            # t.Daemon = True  #### !!!! Daemon 无法join
            t.start()
            self.worker_threads.append(t)

    def worker_thread(self):
        while True:
            try:
                record_idx, d_args = self.task_queue.get(block=True, timeout=1)  # block 问题在于可能block带锁？
            except queue.Empty:
                continue
            if d_args is None:
                self.task_queue.task_done()
                break
            result = self.calc_metric_parallel(d_args)
            if result is not None:
                with self.result_dict_lock:
                    self.result_dict[record_idx] = result
                    self.result_dict = dict(sorted(self.result_dict.items(), key=lambda x: x[0]))
            self.task_queue.task_done()
        self.logger.debug("worker_thread: done")

    def create_dir_and_path(self):
        if not os.path.exists(self.exp_dir):
            os.makedirs(self.exp_dir)
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)
        if not os.path.exists(self.db_dir):
            os.makedirs(self.db_dir)
        if not os.path.exists(self.checkpoint_dir):
            os.makedirs(self.checkpoint_dir)
        if not os.path.exists(self.trials_dir):
            os.makedirs(self.trials_dir)

    def start(self):
        pass

    def stop(self):
        pass

    def resume(self):
        pass

    def view(self):
        pass
