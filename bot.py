import os
import time
from src.path import Path
from src.logger import logger

class Bot:
    def __init__(self, task_processor, input_folder, output_folder, extension, skip_first_line = False, remove_line_breaks = False):
        self.task_processor = task_processor
        self.valid_files = []
        self.tasks = []
        self.can_run = True
        self.reason = ""
        self.skip_first_line = skip_first_line
        self.remove_line_breaks = remove_line_breaks
        
        self.set_input_folder(input_folder)
        self.set_output_folder(output_folder)
        self.set_extension(extension)

    def set_input_folder(self, path):
        if Path(path).exists():
            self.input_folder = path
            logger.info(f"Input folder: <{self.input_folder}>")
        else:
            self.can_run = False
            self.reason = f"<{path}> doesn't exists"
            logger.warning(self.reason)
    
    def set_output_folder(self, path):
        if Path(path).exists():
            self.output_folder = path
            logger.info(f"Output folder: <{self.output_folder}>")
        else:
            self.can_run = False
            self.reason = f"<{path}> doesn't exists"
            logger.warning(self.reason)

    def set_extension(self, ext):
        self.ext = ext
        logger.info(f"Extension: <{self.ext}>")

    def set_valid_files(self):
        self.input_amount = len(os.listdir(self.input_folder))
        if self.input_amount > 0:
            for file in os.listdir(self.input_folder):
                file_extension = file.split(".")[1]
                if(file_extension == self.ext):
                    self.valid_files.append(f"{self.input_folder}\\{file}")

    def set_tasks(self):
        logger.debug("Setting tasks...")
        for file in self.valid_files:
            logger.info(f"File: <{file}>")
            f = open(file, "r")
            count = 0
            for line in f.readlines():
                if self.skip_first_line and count == 0:
                    count += 1
                    continue
                task = line.replace("\n", "") if self.remove_line_breaks == True else line
                logger.info(f"Line: {count}")
                logger.info(f"Task: {task}\n")
                self.tasks.append([task, file])
                count += 1

    def start(self):
        if not self.can_run:
            return logger.error(f"Couldn't run bot properly. Reason: <{self.reason}>")

        self.set_valid_files()
        self.set_tasks()

        if len(self.tasks) > 0:
            logger.info(f"Tasks: <{str(self.tasks)}>")
            logger.warning("Running tasks...")
            for task in self.tasks:
                try:
                    logger.info(f"Case: <{task[0]}>")
                    start = time.time()
                    logger.debug
                    self.task_processor(task[0])
                except Exception as err:
                    logger.info(f"<BOT>: Failed to run task <{task}>. Error: <{err}>")
                finally:
                    end = time.time()
                    elapsed = end - start
                    logger.info(f"Elapsed: {elapsed}")