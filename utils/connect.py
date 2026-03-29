import time
from tqdm  import tqdm

def simulate():
    for _ in tqdm(range(10), mininterval=0.5, desc="connecting", bar_format="{desc}: |{bar}| {percentage:.1f}%"):
            time.sleep(0.2)
    print("connection stablished!")
    time.sleep(1)
