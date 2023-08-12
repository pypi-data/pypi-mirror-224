import boto3
import pandas as pd
from pandas import DataFrame
from pydriller import Repository


class DockerHandler:

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

    def read_data(self, table_name: str) -> DataFrame:
        table = self.dynamodb.Table(table_name)
        scan_response = table.scan(TableName=table_name)
        items = scan_response["Items"]

        while "LastEvaluatedKey" in scan_response:
            scan_response = table.scan(ExclusiveStartKey=scan_response["LastEvaluatedKey"])
            items.extend(scan_response["Items"])

        df = pd.DataFrame(items)

        return df

    def convert_to_csv(self, table_name: str) -> None:
        table = self.dynamodb.Table(table_name)
        scan_response = table.scan(TableName=table_name)["Items"]

        df = pd.DataFrame(scan_response)
        csv_name = "data.csv"
        df.to_csv(csv_name)

        print(f"Created {csv_name}")


class GitHandler:

    def __init__(self, repo_url: str, commit_hash: str) -> None:
        self.repo_url = repo_url
        self.commit_hash = commit_hash

    def get_code_diff(self) -> str:

        code_diff = {}
        for commit in Repository(self.repo_url).traverse_commits():
            for modified_file in commit.modified_files:
                code_diff[commit.hash] = modified_file.diff

        commit_hash_code_diff = code_diff[self.commit_hash]

        return commit_hash_code_diff

    def get_commit_metadata(self) -> dict[dict]:
        commits = Repository(self.repo_url).traverse_commits()

        meta_data = {commit.hash: {
            "committer": commit.committer.name,
            "commit_date": commit.committer_date.strftime('%Y-%m-%d %H:%M:%S %Z').replace(' fixed', '')
        } for commit in commits}

        return meta_data[self.commit_hash]

