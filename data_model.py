from google.appengine.ext import db

class EventLog(db.Model):
  date        = db.DateTimeProperty(auto_now_add=True)
  phone       = db.StringProperty()
  body        = db.StringProperty(multiline=True)
  athlete     = db.StringProperty()
  event       = db.StringProperty()
## end phoneLog

    
class NotificationLog(db.Model):
    phone = db.StringProperty()
    eventNumber = db.StringProperty()
    athlete = db.StringProperty()
    eventRank = db.IntegerProperty()
## end NotificationLog

class RegisteredUser(db.Model):
    phone = db.StringProperty()
    athlete = db.StringProperty()
## end RegisteredUsers

class EventTracker(db.Model):
    event = db.IntegerProperty()

class SystemStatus(db.Model):
    status = db.StringProperty()

