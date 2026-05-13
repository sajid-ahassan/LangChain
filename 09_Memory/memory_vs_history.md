# Memory vs Chat History

## Chat history

Chat history is the list of messages in the current conversation.

```text
Human -> AI -> Human -> AI
```

## Memory

Memory is a broader idea: storing useful state and reusing it later.

Types:

1. Short-term memory - recent messages in the current conversation.
2. Summary memory - compressed summary of old messages.
3. Long-term memory - saved facts/preferences in a database/vector store.

## Simple rule

- Use chat history for small chatbots.
- Use summaries when history gets too long.
- Use persistent memory when information must survive across sessions.

## Warning

Do not put unlimited history into prompts. It increases cost and can confuse the model.
