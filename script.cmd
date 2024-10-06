echo|set /p="... Radionet CI/CD process ..."
echo "... This process does the following steps ..."
echo " 1. Test python code standards"
echo " 2. Unit tests"
echo " 3. Build and deploy to AWS Cloud formation lambda"

echo "Unit test execution ..."
flake8 .\service\app.py

echo "Code review execution ..."
pytest

echo "Build microservice"
sam build

echo "Deploy microservice to AWS Cloudformation stack in lambda"
sam deploy --stack-name samis --region us-east-2 --on-failure ROLLBACK --resolve-s3 --capabilities CAPABILITY_IAM CAPABILITY_AUTO_EXPAND