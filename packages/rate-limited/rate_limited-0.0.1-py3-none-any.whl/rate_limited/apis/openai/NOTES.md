Some notes on how OpenAI tracks usage limits


Two resources are tracked: requests per minute and tokens per minute.

They keep a running count of "remaining" resources, it increases smoothly over time, 
until it reaches the quota, then it stays there.

It is not very clear how they decide whether to allow or deny a request if it might over the token limit.
Estimating how many tokens a request will use is not trivial, because it depends on the model, the input, 
and the intermediate output. They sometimes seems to reject requests that would not put them over the limit.
