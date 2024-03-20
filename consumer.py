import asyncio
import json
import subprocess
import sys

async def consume():
    process = await asyncio.create_subprocess_exec(
        sys.executable,
        'producer.py',
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    while True:
        event_str = (await process.stdout.readline()).decode().strip()
        if not event_str:
            break  # End of file or process terminated
        try:
            event_data = json.loads(event_str)
            event_type = event_data.get('event_type')
            data = event_data.get('data', '')
            # Process event data
            print(f"Event Type: {event_type}, Data: {data}")
        except json.JSONDecodeError:
            print("Corrupt JSON encountered. Skipping.")

async def main():
    await consume()

if __name__ == "__main__":
    asyncio.run(main())