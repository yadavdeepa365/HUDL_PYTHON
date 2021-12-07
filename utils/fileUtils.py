import os
from globalConfig import GlobalConfig

def capture_screenshot(driver, target_path=os.path.join(GlobalConfig.SCREENSHOTS_DIR, "screenshot.png")):
    driver.save_screenshot(target_path)
