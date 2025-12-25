import psutil
import logging

# ================= CONFIG =================
CPU_THRESHOLD = 75        # %
RAM_THRESHOLD = 80        # %
DISK_THRESHOLD = 85       # %

LOG_FILE = "system_monitor.log"

# =============== LOGGING ==================
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ============== FUNCTIONS =================
def check_cpu():
    cpu = psutil.cpu_percent(interval=1)
    if cpu > CPU_THRESHOLD:
        logging.warning(f"CPU ALERT: {cpu}% > {CPU_THRESHOLD}%")
    else:
        logging.info(f"CPU OK: {cpu}%")
    return cpu


def check_ram():
    ram = psutil.virtual_memory().percent
    if ram > RAM_THRESHOLD:
        logging.warning(f"RAM ALERT: {ram}% > {RAM_THRESHOLD}%")
    else:
        logging.info(f"RAM OK: {ram}%")
    return ram


def check_disk(path="/"):
    disk = psutil.disk_usage(path).percent
    if disk > DISK_THRESHOLD:
        logging.warning(f"DISK ALERT ({path}): {disk}% > {DISK_THRESHOLD}%")
    else:
        logging.info(f"DISK OK ({path}): {disk}%")
    return disk


# ================= MAIN ===================
def main():
    cpu = check_cpu()
    ram = check_ram()
    disk = check_disk("C:\\")

    print(f"CPU: {cpu}% | RAM: {ram}% | Disk: {disk}%")


if __name__ == "__main__":
    main()
