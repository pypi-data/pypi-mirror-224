import git
import openai
import argparse
import os
from typing import Optional
import json

CONFIG_FILE = "gitlex_config.json"


def get_api_key_from_config() -> Optional[str]:
    """
    Fetch the OpenAI API key from the config file.

    :return: None if the file or key doesn't exist, otherwise the API key.
    """
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            config = json.load(f)
            return config.get("OPENAI_API_KEY")
    return None


def save_api_key_to_config(api_key: str) -> None:
    """
    Save the OpenAI API key to the config file.

    :param api_key: The API key to save.
    :return: None
    """
    with open(CONFIG_FILE, "w") as f:
        json.dump({"OPENAI_API_KEY": api_key}, f)


API_KEY = get_api_key_from_config()

if not API_KEY:
    print(
        "The OpenAI API key is not set. Please enter it below.\n"
        "For instructions on obtaining an API key, please check the README.md file.\n"
    )
    API_KEY = input("Enter your OpenAI API key: ").strip()
    save_api_key_to_config(API_KEY)

# You can then use the API_KEY in your OpenAI calls
openai.api_key = API_KEY


def get_git_changes(repo_path: str = ".") -> str:
    """
    Fetch the changes (diff) from a given repository.

    :param repo_path: Path to the git repository. Default is the current directory.
    :return: A string containing the git diff.
    """
    try:
        repo = git.Repo(repo_path)
        diff = repo.git.diff(None)
        if not diff:
            raise Exception(f"No changes detected in {repo_path}")
        return diff
    except git.exc.InvalidGitRepositoryError:
        raise Exception(f"{repo_path} is not a valid git repository")
    except git.exc.NoSuchPathError:
        raise Exception(f"{repo_path} is not a valid path")


def truncate_diff(diff: str, max_size: int = 4000) -> str:
    """
    Truncate the git diff to ensure it's within a certain size, while trying to maintain content.

    :param diff: The git diff string.
    :param max_size: Maximum allowed size of the truncated diff.
    :return: A truncated version of the diff.
    """
    if len(diff) <= max_size:
        return diff

    truncation_point = diff.rfind("\n\n", 0, max_size)
    if truncation_point == -1:
        # No complete change found within threshold, return a default message.
        return "Large number of changes, please review."

    return diff[:truncation_point]


def generate_commit_message(diff: str) -> str:
    """
    Generate a commit message using the OpenAI API based on the provided git diff.

    :param diff: The git diff string.
    :return: A string containing the suggested commit message.
    """
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Suggest a commit message for the following changes:\n{diff}",
            max_tokens=50,
        )
    except openai.error.OpenAIError as e:
        raise Exception(f"OpenAI API Error: {e}")

    return response.choices[0].text.strip()


def check_api_key() -> None:
    """
    Check if the API key is stored in the config file and inform the user.

    :return: None
    """
    if get_api_key_from_config():
        print(f"An OpenAI API key is stored in the {CONFIG_FILE} file.")
    else:
        print("No OpenAI API key is stored in the config file.")


def main():
    """
    The main execution funtion to generate an AI-based commit message.
    """
    parser = argparse.ArgumentParser(description="Generate AI-based commit messages")
    parser.add_argument(
        "--path",
        default=".",
        help="Path to git repository. Default is current directory",
    )
    parser.add_argument(
        "--check-api-key",
        action="store_true",
        help="Check if an OpenAI API key is stored in the config file",
    )
    args = parser.parse_args()

    if args.check_key:
        check_api_key()
        return

    diff = get_git_changes(args.path)
    if diff:
        truncated_diff = truncate_diff(diff)
        commit_message = generate_commit_message(truncated_diff)
        print(f"Suggested commit message: {commit_message}")


if __name__ == "__main__":
    main()
