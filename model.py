from peewee import *


db = SqliteDatabase('dht.db', check_same_thread=False)


# 데이터 베이스 테이블 만들기 - 센서
class DHTSensor(Model):
    name = CharField()  # 센서 이름
    dht_type = IntegerField()   # 센서 유형
    pin = IntegerField()    # 센서 핀

    class Meta:
        database = db

# 데이터 베이스 테이블 만들기 - 센서 읽은 값


class SensorReading(Model):
    time = DateTimeField()  # 날짜
    name = CharField()  # 온도 / 습도
    value = FloatField()    # 측정 값

    class Meta:
        database = db


# DB테이블 값에 접근 객체
class DHTData(object):

    # 객체 초기화
    def __init__(self):
        # DB에 연결
        db.connect()

        # 테이블 만들기 센서DB, 센서값 저장 DB
        db.create_tables([DHTSensor, SensorReading],
                         safe=True)  # safe=True  테이블 생성 확인

    # DB에 센서 추가하기
    def define_sensor(self, name, dht_type, pin):
        DHTSensor.get_or_create(name=name, dht_type=dht_type, pin=pin)

    # 센서 테이블 값 가져오기
    def get_sensors(self):
        return DHTSensor.select()

    # 센서 최근 측정값 가져오기 디폴트 30개
    def get_recent_readings(self, name, limit=30):
        return SensorReading.select() \
                            .where(SensorReading.name == name) \
                            .order_by(SensorReading.time.desc()) \
                            .limit(limit)

    # 센서 측정값 DB에 값을 저장하기
    def add_reading(self, time, name, value):
        SensorReading.create(time=time, name=name, value=value)

    # DB 닫기
    def close(self):
        db.close()
