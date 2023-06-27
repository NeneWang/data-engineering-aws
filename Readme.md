# Data Engineering AWS

https://www.udemy.com/course/data-engineering-using-aws-analytics-services/


Here the data engineering Analytics modification

To make an instance there are things you can run:

```bash
aws ec2 describe-instances --query "Reservations[*].Instances[*].{Instance:InstanceId, Status:State.Name}" --output json
```

To know for example the status.