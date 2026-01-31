import asyncio
import time
from logger import get_logger

logger = get_logger()

# simulasi tugas berat (misal: panggil API eksternal)
async def fake_api_call(name: str, delay: int):
    logger.info("Task dimulai", name=name)
    await asyncio.sleep(delay) # non-blocking sleep
    logger.info("Task selesai", name=name, duration=delay)
    return f"Hasil dari {name}"

# VERSI LAMBAT (Sequential)
async def run_sequential():
    start = time.perf_counter()

    result1 = await fake_api_call("Task A", 2)
    result2 = await fake_api_call("Task B", 1)
    result3 = await fake_api_call("Task C", 3)

    elapsed = time.perf_counter() - start
    print(f"\n[Sequential] Total waktu: {elapsed:.2f} detik")
    return [result1, result2, result3]

# VERSI CEPAT (parallel)
async def run_parallel():
    start = time.perf_counter()

    results = await asyncio.gather(
        fake_api_call("Task A", 2),
        fake_api_call("Task B", 1),
        fake_api_call("Task C", 3),
    )

    elapsed = time.perf_counter() - start
    print(f"\n[Parallel] Total waktu: {elapsed:.2f} detik")
    return results

# MAIN
if __name__ == "__main__":
    print("===SEQUENTIAL===")
    asyncio.run(run_sequential())

    print("\n===PARALLEL===")
    asyncio.run(run_parallel())