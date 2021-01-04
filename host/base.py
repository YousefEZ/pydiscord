class DummyNation:
    """Dummy nation that contains random data for demonstration purposes"""

    def __init__(self):
        """attributes to a player would be set here. Add required attributes and appropriate
           random data that can be used to demonstrate the embed."""

        self.userid = 251351879408287744
        self.money = 3489123
        self.name = "Palestine"
        self.login = 1608841443
        self.infrastructure = 30000
        self.technology = 340
        self.spent_technology = 200
        self.available_technology = self.technology - self.spent_technology
        self.land = 3000

        self.citizens = 300000
        self.taxrate = 27.5
        self.flag = "https://thumbs.dreamstime.com/b/palestine-flag-fabric-texture-waving-181571390.jpg"
        self.government = "democracy"
        self.alliancename = "Arab League"
        self.vote = False  # whether they are able to get a reward for voting
        self.ban = False  # whether the user has been banned

        # ...


if __name__ == "__main__":
    pass
