from functools import wraps
from flask import request
from v1.utils.recorder import ScreenRecorder
import time


def record_screen(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        
        # 🔹 Extract endpoint name
        endpoint_name = request.path.strip("/").replace("-", " ").title().replace(" ", "-")

        # Example:
        # /CE-traffic-must-haves-run-script
        # → CE-Traffic-Must-Haves-Run-Script

        folder_name = endpoint_name
        file_prefix = endpoint_name.split("-Run")[0]  # cleaner name

        recorder = ScreenRecorder()

        recorder.start(
            folder_name=folder_name,
            file_prefix=file_prefix
        )

        start_time = time.time()

        try:
            return func(*args, **kwargs)

        except Exception as e:
            print("[Recorder] Exception during test:", e)
            raise

        finally:
            # Ensure minimum recording time (avoid corrupt video)
            elapsed = time.time() - start_time
            if elapsed < 5:
                time.sleep(5 - elapsed)
            time.sleep(5)
            recorder.stop()

    return wrapper