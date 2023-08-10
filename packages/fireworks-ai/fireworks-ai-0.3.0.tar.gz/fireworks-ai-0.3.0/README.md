# Fireworks.ai Python library

Fireworks.ai Python Library provides a convenient API for accessing Fireworks supported LLMs. We are targeting our API to be very similar to OpenAI's API so you can replace OpenAI usage with minimal modifications

## Installation

```sh
pip install --upgrade fireworks-ai
```

## Example code
### List
```python
import fireworks.client
fireworks.client.api_key = "your-key"
print(fireworks.client.Models.list())
```

```
object='list' data=[Model(id="accounts/fireworks/models/llama-v2-7b", object="model", created=0), ...]
```

### Completion

```python
import fireworks.client
fireworks.client.api_key = "your-key"
completion = fireworks.client.Completion.create("accounts/fireworks/models/llama-v2-7b", "Once upon a time", temperature=0.7, n=2, max_tokens=16)
print(completion)
```

```
id='cmpl-988e179fa14fbaebdf17c713' object='text_completion' created=1691602259 model='accounts/fireworks/models/llama-v2-7b' choices=[Choice(text=', there was an emperor who reigned over all the kingdoms of the', index=0, finish_reason='length'), Choice(text=', a boy lived in a small house with his mom and dad. His', index=1, finish_reason='length')]
```

### Async completion

```python
import asyncio
import fireworks.client
fireworks.client.api_key = "your-key"
async def main():
    response = await fireworks.client.Completion.acreate("accounts/fireworks/models/llama-v2-7b", "Once upon a time", echo=True, max_tokens=16)
    print(response.choices[0].text)
asyncio.run(main())
```

then run the script
```
$ python test.py
Once upon a time, there used to be a huge mountain that was the most famous mou
```


## Requirements

- Python 3.9
