import os
customer_db = {"Acme": "Priority", "Globex": "Standard"}

def get_customer_status(name):
    return customer_db.get(name, "Unknown Customer")

def read_documentation(filename="README.md"):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return f.read()
    return "Error: File not found."

def run_agent(input_text):
    print(f"Agent: Analyzing '{input_text}'...")
    text = input_text.lower()
    if "status" in text:
        args = input_text.split()[-1]
        result = get_customer_status(args)
    elif "read" in text:
        result = read_documentation()
    else:
        result = "Command not recognized."
    print(f"Agent result: {result}")

run_agent("Check status of Acme")
run_agent("Read documentation")
