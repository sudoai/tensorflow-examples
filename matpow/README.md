# Matpow
## Dependencies install
```bash
pip install -r requirements.txt
```

## Run cluster
Lunch each node in a different terminal
```bash
$ python server.py --task_index=0
I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:206] Initialize HostPortsGrpcChannelCache for job worker -> {localhost:2222, localhost:2223}
I tensorflow/core/distributed_runtime/rpc/grpc_server_lib.cc:202] Started server with target: grpc://localhost:2222
```

```bash
$ python server.py --task_index=1
I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:206] Initialize HostPortsGrpcChannelCache for job worker -> {localhost:2222, localhost:2223}
I tensorflow/core/distributed_runtime/rpc/grpc_server_lib.cc:202] Started server with target: grpc://localhost:2223
```

## Run matpow example
```bash
$ python matpow.py
I tensorflow/core/kernels/logging_ops.cc:79] Completed mat_pow[0.10386115 0.10386115 0.10386114...]
I tensorflow/core/kernels/logging_ops.cc:79] Completed mat_pow[0.10357855 0.10357856 0.10357855...]
Single node computation time: 0:00:11.888668
Multi node computation time: 0:00:02.120565
```
