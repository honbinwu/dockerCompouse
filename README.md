# Final presentation

# Start all service:

```sh
$ docker-compose up -d
```

# delete all service:

```sh
$docker-compose down

```

# Start one service:

```sh
$docker-compose start $SERVICE_NAME 
```

# Stop one service:

```sh
$docker-compose stop $SERVICE_NAME
```

# Access a running container:

```sh
$docker-compose exec $SERVICE_NAME bash
```
# mongo database Set up 
```sh
cfg = {
  "_id": "RS",
  "members": [{
      "_id": 0,
      "host": "rs1:27041"
    },
    {
      "_id": 1,
      "host": "rs2:27042"
    },
    {
      "_id": 2,
      "host": "rs3:27043"
    }
  ]
};
```
# mongo database Import settings
```sh
rs.initiate(cfg);
```

#mongo database Query the permissions of each database
```sh
rs.status().members.forEach(m =&gt; print (`${m.name} =&gt; ${m.stateStr}`))
```

