import os
import sys

def load_docs(source_dir):
    docs = {}
    if not os.path.isdir(source_dir):
        return docs
    for fname in os.listdir(source_dir):
        if fname.endswith(".rst"):
            fpath = os.path.join(source_dir, fname)
            with open(fpath, "r") as f:
                docs[fname] = f.read()
    return docs

def build_context(docs):
    parts = []
    for name, content in docs.items():
        parts.append("=== " + name + " ===")
        parts.append(content)
    return "\n\n".join(parts)

def query(question, context):
    try:
        import anthropic
        client = anthropic.Anthropic()
        msg = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1024,
            messages=[{
                "role": "user",
                "content": "Documentation:\n\n" + context + "\n\nQuestion: " + question
            }]
        )
        return msg.content[0].text
    except ImportError:
        return "Install anthropic: pip install anthropic"
    except Exception as e:
        return "Error: " + str(e)

def main():
    source_dir = "docs/source"
    docs = load_docs(source_dir)
    print("Loaded " + str(len(docs)) + " docs.")
    context = build_context(docs)
    if len(sys.argv) > 1:
        question = " ".join(sys.argv[1:])
    else:
        question = input("Ask about your docs: ")
    print("")
    answer = query(question, context)
    print(answer)

if __name__ == "__main__":
    main()
