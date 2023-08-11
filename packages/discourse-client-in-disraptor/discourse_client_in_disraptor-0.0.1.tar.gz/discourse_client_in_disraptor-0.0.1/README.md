# A Lightweight Discourse Client for Disraptor

Simple access to the discourse API required to use [Disraptor](www.disraptor.org).

Usage:

```
from discourse_client_in_disraptor import DiscourseApiClient
client = DiscourseApiClient(url='https://www.tira.io', api_key='<API-KEY>')
client.generate_api_key('<user>', '<description>')
```

