class ObjectTracker:
    object_created = 0
    def __init__(self):
        ObjectTracker.object_created = ObjectTracker.object_created + 1;
    @classmethod
    def show_no_of_object_created(cls):
        print("{} objects are created already.......!!!".format(cls.object_created))

ot = ObjectTracker()
ot = ObjectTracker()
ot = ObjectTracker()
ot = ObjectTracker()
ot = ObjectTracker()
ot = ObjectTracker()
ot = ObjectTracker()
ot = ObjectTracker()
ot = ObjectTracker()

ObjectTracker.show_no_of_object_created()