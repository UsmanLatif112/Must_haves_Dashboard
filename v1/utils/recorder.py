import cv2
import numpy as np
from mss import mss
import time
import os
import threading


class ScreenRecorder:
    def __init__(self, base_dir="recordings", fps=10, scale_factor=0.5, max_duration=1200):
        self.base_dir = base_dir
        self.fps = fps
        self.scale_factor = scale_factor
        self.max_duration = max_duration  # 20 minutes
        self.recording = False
        self.thread = None

    def _generate_filename(self):
        timestamp = time.strftime("%d-%m-%Y_%H-%M-%S")

        # Create endpoint-specific folder
        self.output_dir = os.path.join(self.base_dir, self.folder_name)
        os.makedirs(self.output_dir, exist_ok=True)

        return os.path.join(
            self.output_dir,
            f"{self.file_prefix}_{timestamp}.mp4"
        )

    def _record(self):
        filename = self.filename

        with mss() as sct:
            monitor = sct.monitors[1]
            width = int(monitor["width"] * self.scale_factor)
            height = int(monitor["height"] * self.scale_factor)

            fourcc = cv2.VideoWriter_fourcc(*"mp4v")
            out = cv2.VideoWriter(filename, fourcc, self.fps, (width, height))

            start_time = time.time()

            try:
                while self.recording:
                    # ⏱ AUTO STOP after max_duration
                    if time.time() - start_time > self.max_duration:
                        print("[Recorder] Max duration reached (20 min). Stopping...")
                        break

                    img = sct.grab(monitor)
                    frame = np.array(img)
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
                    frame = cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)

                    out.write(frame)
                    time.sleep(1 / self.fps)

            finally:
                out.release()
                cv2.destroyAllWindows()
                print(f"[Recorder] Saved: {filename}")

    def start(self, folder_name="default", file_prefix="recording"):
        self.folder_name = folder_name
        self.file_prefix = file_prefix
        self.filename = self._generate_filename()

        self.recording = True
        self.thread = threading.Thread(target=self._record)
        self.thread.start()

        print(f"[Recorder] Started: {self.filename}")

    def stop(self):
        self.recording = False
        if self.thread:
            self.thread.join()
        print(f"[Recorder] Stopped: {self.filename}")
        