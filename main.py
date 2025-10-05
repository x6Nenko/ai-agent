import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from functions.call_function import call_function, available_functions


def main():
    load_dotenv()

    # Parse arguments: separate flags from prompt words
    verbose = "--verbose" in sys.argv
    args = []
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)

    # Show usage if no prompt provided
    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I fix the calculator?"')
        print('Example: python main.py list the files --verbose')
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    # Join multi-word prompts
    user_prompt = " ".join(args)

    if verbose:
        print(f"User prompt: {user_prompt}\n")

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    max_iterations = 20
    for iteration in range(max_iterations):
        try:
            result = generate_content(client, messages, verbose)
            if result:
                print(result)
                break
        except Exception as e:
            print(f"Error: {e}")
            break
    else:
        print("Maximum iterations reached without a final response.")
        sys.exit(1)


def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
        ),
    )

    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)

    # Add all candidates to messages (usually just one)
    if response.candidates:
        for candidate in response.candidates:
            messages.append(candidate.content)

    # Handle responses without function calls
    if not response.function_calls:
        return response.text

    # Process function calls
    function_responses = []
    for function_call_part in response.function_calls:
        function_call_result = call_function(function_call_part, verbose)

        # Verify the result has the expected structure
        if not function_call_result.parts or not function_call_result.parts[0].function_response:
            raise RuntimeError("call_function did not return a valid function response")

        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")

        function_responses.append(function_call_result.parts[0])

    if not function_responses:
        raise RuntimeError("No function responses generated")

    # Convert function responses to a user message and add to conversation
    messages.append(types.Content(role="user", parts=function_responses))

    # Return None to indicate we need another iteration
    return None


if __name__ == "__main__":
    main()
