import os

LINE = "v2.3.1: Fixed a bug where entering a room wiped the task queue; users no longer stand in doorways buffering while the brain re-downloads why they came in."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
