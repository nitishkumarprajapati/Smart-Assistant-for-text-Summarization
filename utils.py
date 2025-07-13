def extract_justification(answer, context):
    lines = context.split("\n")
    for i, line in enumerate(lines):
        if answer in line:
            return f"This is supported by line {i+1}: \"{line.strip()}\""
    return "Justification not found in document"
