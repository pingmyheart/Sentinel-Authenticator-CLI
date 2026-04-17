# Sentinel-Authenticator

Python based CLI to generate otp from given configuration

![Last Commit](https://img.shields.io/github/last-commit/pingmyheart/Sentinel-Authenticator)
![Repo Size](https://img.shields.io/github/repo-size/pingmyheart/Sentinel-Authenticator)
![Issues](https://img.shields.io/github/issues/pingmyheart/Sentinel-Authenticator)
![Pull Requests](https://img.shields.io/github/issues-pr/pingmyheart/Sentinel-Authenticator)
![License](https://img.shields.io/github/license/pingmyheart/Sentinel-Authenticator)
![Top Language](https://img.shields.io/github/languages/top/pingmyheart/Sentinel-Authenticator)
![Language Count](https://img.shields.io/github/languages/count/pingmyheart/Sentinel-Authenticator)

## Features

- **File Based Configuration**: Reads configuration from a txt file, making it easy to manage and update authentication
  settings.
- **OTP Generation**: Generates One-Time Passwords (OTPs) based on the provided configuration, enhancing security for
  authentication processes.
- **Command Line Interface**: Provides a simple CLI for users to interact with the tool, allowing for easy execution and
  integration into existing workflows.
- **Lightweight**: Designed to be lightweight and efficient, ensuring quick OTP generation without unnecessary overhead.
- **Web Server**: Can be run as a web server to provide OTP generation as a service, allowing for integration with other
  applications and systems.

## Required Configuration

To use the Sentinel-Authenticator, you need to provide a configuration in a txt file where each line represent a otpauth
url in the format of `otpauth://TYPE/LABEL?PARAMETERS` where:

- `TYPE` is the type of OTP (e.g., totp or hotp).
- `LABEL` is a human-readable identifier for the OTP (e.g., "My Service").
- `PARAMETERS` are key-value pairs that define the OTP settings (e.g., secret, issuer, algorithm, digits, period).

It is also important to configure environment variables to set configuration file path

```bash
CONFIGURATION_FILE=./target/totp.txt
```

## Usage

### Docker

Pull Docker image and run a container. Container is by default the webserver implementation.  
Swagger endpoint is exposed at relative path `/apidocs`

### CLI

Run the CLI to generate OTPs based on the provided configuration file. The generated OTPs will be printed to the console
and can be used in other applications as needed.