# Bill of exchange app

This app is used to share and keep track of your bills.

## How to create bot

 1) create new telegram bot as described in the documentation https://core.telegram.org/bots
 2) update environment variables in the `telegram.env` file:
    - *TELEGRAM_API_TOKEN* - use access token you got on the previous step
    - *TELEGRAM_ADMIN_ID* - use id of your telegram user

## How to run

1) copy `./config/telegram.env.dist` to `./config/telegram.env` and fill in the env variables;
2) run `docker-compose build`;
3) run `docker-compose up`;

## Troubleshooting

If you are developing on Windows you may face the issue with line endings (LF vs CRLF). To address this you may need to adjust configuration:

- GIT: run `git config core.autocrlf false`;
- VS Code (if using): set setting `{ "files.eol": "\n" }`
