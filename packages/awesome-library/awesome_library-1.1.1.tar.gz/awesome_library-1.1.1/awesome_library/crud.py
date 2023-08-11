import boto3
import pandas as pd
from pydriller import Repository


class AwesomeHandler:

    def __init__(
            self,
            endpoint_url: str,
            region_name: str,
            aws_access_key_id: str,
            aws_secret_access_key: str
    ) -> None:
        self.dynamodb = boto3.resource(
            "dynamodb",
            endpoint_url=endpoint_url,
            region_name=region_name,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key
        )

    def get_code_diff(self, repo_url: str, commit_hash: str) -> str:

        code_diff = {}
        for commit in Repository(repo_url).traverse_commits():
            for modified_file in commit.modified_files:
                code_diff[commit.hash] = modified_file.diff

        commit_hash_code_diff = code_diff[commit_hash]

        return commit_hash_code_diff

    def read_data(self, table_name):
        table = self.dynamodb.Table(table_name)
        scan_response = table.scan(TableName=table_name)["Items"]

        df = pd.DataFrame(scan_response)

        return df

    def convert_to_csv(self, table_name):
        table = self.dynamodb.Table(table_name)
        scan_response = table.scan(TableName=table_name)["Items"]

        df = pd.DataFrame(scan_response)
        csv_name = "data.csv"
        df.to_csv(csv_name)

        print(f"Created {csv_name}")

