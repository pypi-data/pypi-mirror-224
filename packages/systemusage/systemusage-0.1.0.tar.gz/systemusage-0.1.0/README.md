## SystemUsage Package

The SystemUsage package allows you to monitor various system resource usage metrics, such as CPU, memory, and disk usage.

## Installation

You can install the package using pip:

```bash
pip install systemusage
```

## Usage

```python
from systemusage import SystemMonitor

# Create an instance of SystemMonitor
sys_monitor = SystemMonitor()

# Get CPU usage percentage
cpu_usage = sys_monitor.get_cpu_usage()
print(f"CPU Usage: {cpu_usage}%")

# Get memory usage in bytes
memory_usage = sys_monitor.get_memory_usage()
print(f"Memory Usage: {memory_usage} bytes")

# Get disk usage in bytes
disk_usage = sys_monitor.get_disk_usage('/')
print(f"Disk Usage: {disk_usage} bytes")

# Monitor system resources for a specific duration
sys_monitor.monitor_resources(duration=10)
```

## License

This package is released under the MIT License.

## Contributing

Contributions are welcome! If you find a bug or have an idea for an improvement, please open an issue or submit a pull request on [GitHub](https://github.com/yourusername/systemmonitor).

## Acknowledgments

This package was inspired by the need to easily monitor system resource usage in Python projects.

## Disclaimer

The SystemMonitor package provides a simplified interface for monitoring system resource usage and may not cover all use cases. Use with caution in production environments.

## Contact

For questions or feedback, you can reach out to the package author at pytechacademy@gmail.com
