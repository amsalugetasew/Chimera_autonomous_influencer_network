import os
import sys

REQUIRED_SPECS = [
    "specs/_meta.md",
    "specs/functional.md",
]

def fail(msg):
    print(f"❌ SPEC CHECK FAILED: {msg}")
    sys.exit(1)

def main():
    for spec in REQUIRED_SPECS:
        if not os.path.exists(spec):
            fail(f"Missing required spec: {spec}")

    print("✅ Spec presence check passed Successfully found all required specs.")

if __name__ == "__main__":
    main()
