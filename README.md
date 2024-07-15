# Graspnet

## Instalation

Первым делом нужно установить graspnet-baseline


```bash
cd graspnet-baseline
pip install -r requirements.txt
```

Устанавливаем pointnet2

```bash
cd pointnet2
python setup.py install
```

Устанавливаем knn

```bash
cd knn
python setup.py install
```

Возвращаемся в корневую папку и устанавливаем graspnetAPI

```bash
cd graspnetAPI
pip install .
```

ВАЖНО!

Нужно установить версию numpy=1.23.0

```bash
pip install numpy=1.23.0
```

Также требуется установить ur-env только для RemoteEnvClient

https://github.com/RQC-Robotics/ur5-env


## Работа с демо

Для начала в фале comand_demo.sh меняем путь до нужного чекпоинта (либо для Kinect либо для Realsense). По умолчанию выбран Realsens

Запускаем RemoteControle на роботе и запускаем файл comand_demo.sh

```bash
sh comand_demo.sh
```

