# Lambda with GitHub Actions

[← AI Engineer](../README.md)

## What

The smallest useful deploy pipeline. Push to `main`, and a workflow zips the code and updates an AWS Lambda function.

| Path | Role |
| :--- | :--- |
| `lambda_function.py` | A handler that returns a 200 and a greeting |
| `.github/workflows/lambda_deployment.yaml` | Zips the repo and runs `aws lambda update-function-code` |

## Run

1. Create a Lambda function.
2. In `lambda_deployment.yaml`, replace the function ARN with yours.
3. Add the repository secrets `AWS_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY`, and `AWS_REGION`.
4. Push to `main` from a repository that holds this folder at its root.

GitHub only runs workflows from a repository's root `.github/workflows/`.

## Article

Coming soon.

## Depends on

- An AWS account and a Lambda function.
- A GitHub repository with the three secrets above.
