class OctoprimeTires():
    def __init__(self):
        pass

    def needs_service(self, tires_wear):
        if (sum(tires_wear) >= 3):
            return True
        else:
            return False