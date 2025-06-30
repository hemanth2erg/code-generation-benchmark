import openai

def evaluate(model_name, prompt):
    # Dummy function placeholder
    return {"passed": True, "exec_time": 0.45}

if __name__ == "__main__":
    prompts = ["Write a Python function to reverse a list.", "Implement binary search."]
    for prompt in prompts:
        result = evaluate("gpt-4", prompt)
        print(f"Prompt: {prompt}\nResult: {result}\n")
