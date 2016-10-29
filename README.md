# last.fm prepare-commit-msg

git prepare-commit-msg with last.fm now playing

## Usage

1) setup your credentials

```bash
export LAST_API_KEY=""
export LAST_API_SECRET=""
export LAST_USERNAME=""
export LAST_PASSWORD_HASH=""
```

you can make your hash with pylast:
https://github.com/pylast/pylast/blob/develop/README.md#getting-started

2) run `pip install -r requirements.txt`

3) copy `prepare-commit-msg` to your `.git/hooks/`
