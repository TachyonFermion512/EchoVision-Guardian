# Purpose: Entry point of EchoVision Guardian app
# Author: Ahmad Baksh
# Created: July 29, 2025

def main():
    print("✅ EchoVision Guardian app is running successfully!")

if __name__ == "__main__":
    main()

# Purpose: Entry point of EchoVision Guardian app
# Author: Ahmad Baksh
# Created: July 29, 2025

from emergency_assistant import run_emergency_assistant
from navigator import run_navigator
from threat_detector import run_threat_detection
from offline_comm import run_offline_communication

def main():
    print("✅ EchoVision Guardian booting modules...\n")

    # Activate modules (comment out what you don’t want during testing)
    run_emergency_assistant()
    run_navigator()
    run_threat_detection()
    run_offline_communication()

    print("\n✅ All systems online.")

if __name__ == "__main__":
    main()

