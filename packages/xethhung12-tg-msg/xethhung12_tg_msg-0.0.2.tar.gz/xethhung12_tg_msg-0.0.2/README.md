# Build and deploy
```shell
rm -fr dist/*
python -m build
python twine upload dist/* -u __token__ -p {token}
```

# Usage of simple sending
```shell
python -m xethhung12_tg_msg_send \
    --receiver-id {receiver-id} \
    --bot-token {bot-token} \
    --msg {message} 
```

# Usage  of sending through STDIN
```shell
python -m xethhung12_tg_msg_send \
    --receiver-id {receiver-id} \
    --bot-token {bot-token} \
    --from-stdin {stdin input} 
```