import sys
import os

def trade(asset, amount):
    print(f"Executing trade: {asset} for ${amount}")

def deploy_ai(model):
    print(f"Deploying Keystone AI model: {model}")

def cyber_hunt(target="web"):
    print(f"CyberCop scanning target: {target}")

def mev_snipe(chain, budget):
    print(f"Running MEV snipe on {chain} with budget ${budget}")

commands = {
    "@trade": lambda args: trade(args[0], args[1]),
    "!overlord.deploy": lambda args: deploy_ai(args[0]),
    "!cybercop.hunt": lambda args: cyber_hunt(*args),
    "@snipe": lambda args: mev_snipe(args[0], args[1]),
}

def parse_and_execute(line):
    parts = line.strip().split()
    if not parts: return
    cmd = parts[0]
    args = parts[1:]
    if cmd in commands:
        commands[cmd](args)
    else:
        print("Unknown ArchLang command:", cmd)

def run_script(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            for line in f:
                parse_and_execute(line.strip())
    else:
        print(f"File not found: {file_path}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1].endswith(".arch"):
            run_script(sys.argv[1])
        else:
            parse_and_execute(" ".join(sys.argv[1:]))
    else:
        print("Usage: archlang_core.py '<command>' or archlang_core.py file.arch")