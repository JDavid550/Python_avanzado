from datetime import datetime
import pytz

bogot_timezone = pytz.timezone("America/Bogota")
now = datetime.now(bogot_timezone)
print(now)