from ai_engine import get_ai_response
from prompts import build_prompt

def main():

    print("\nAI RESUME JOB MATCHER\n")

    print("Paste Resume:")
    resume = input()

    print("\nPaste Job Description:")
    job = input()

    prompt = build_prompt(resume, job)

    result = get_ai_response(prompt)

    print("\nRESULT:\n")
    print(result)


if __name__ == "__main__":
    main()