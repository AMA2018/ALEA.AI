#!/usr/bin/env python3
import subprocess
import os
import random
import re

# List of professional commit messages for the Alea AI Bot project
commit_messages = [
    "Initial commit for Alea AI Bot Quant Framework",
    "Feature: Implement RSI-based trading algorithm",
    "Feature: Add basic plotting functionality",
    "Bugfix: Fix data processing in backtesting engine",
    "Feature: Implement take-profit and stop-loss in trading logic",
    "Optimization: Improve backtesting performance",
    "Refactoring: Simplify API interface",
    "Feature: Integrate with TensorFlow for ML-based strategies",
    "Documentation: Add basic usage examples",
    "Feature: Implement EMA indicator",
    "Bugfix: Fix memory leaks with large datasets",
    "Feature: Add Bollinger Bands indicator",
    "Improvement: Extend backtesting reporting functions",
    "Feature: Implement real-time data processing",
    "Refactoring: Overhaul core architecture for better extensibility",
    "Feature: Integrate with Binance API",
    "Optimization: Improve memory usage during backtest process",
    "Feature: Add MACD indicators",
    "Bugfix: Fix timezone issues with historical data",
    "Feature: Implement flexible configuration system",
    "Feature: Add DQN-based reinforcement learning model",
    "Improvement: Extend plotting options for visual analysis",
    "Bugfix: Fix issues with high-frequency data processing",
    "Feature: Introduce modular tendrils system",
    "Optimization: Reduce CPU usage during simulation",
    "Feature: Implement portfolio management system",
    "Documentation: Create comprehensive API documentation",
    "Refactoring: Separate backtesting and live trading logic",
    "Feature: Add simple dashboard system",
    "Bugfix: Fix race conditions in asynchronous trading",
    "Feature: Implement Fibonacci retracement strategies",
    "Improvement: Enhance error handling and logging",
    "Feature: Add Kelly criterion for position sizing",
    "CI/CD: Set up automated testing",
    "Feature: Implement Monte Carlo simulations for risk assessment",
    "Improvement: Add advanced strategy validation methods",
    "Feature: Multi-asset optimization for portfolios",
    "Refactoring: Simplify internal data structures",
    "Feature: Introduce custom indicators support",
    "Bugfix: Fix data integrity issues in simulations"
]

# Get all commit IDs and assign a random message to each
commit_ids = subprocess.check_output(['git', 'log', '--format=%H']).decode().strip().split('\n')
assignments = {}

for commit_id in commit_ids:
    assignments[commit_id] = random.choice(commit_messages)

# Create a temporary file with the filter commands
with open('message_map.txt', 'w') as f:
    for commit_id, message in assignments.items():
        # Escape special characters in the message
        escaped_message = re.sub(r'[/&]', r'\\\g<0>', message)
        f.write(f"{commit_id} {escaped_message}\n")

# Run git-filter-repo with the --replace-refs option
filter_repo_path = './git-filter-repo'
if not os.path.exists(filter_repo_path):
    print("Error: git-filter-repo not found in the current directory")
    exit(1)

print("Rewriting commit messages...")
subprocess.run([
    filter_repo_path,
    '--force',
    '--replace-message', 'message_map.txt'
])

# Clean up
os.remove('message_map.txt')
print("History has been successfully rewritten!") 