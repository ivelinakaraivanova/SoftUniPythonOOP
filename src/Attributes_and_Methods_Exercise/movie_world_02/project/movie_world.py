class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        dvd = [d for d in self.dvds if d.id == dvd_id][0]
        customer = [c for c in self.customers if c.id == customer_id][0]
        if dvd.is_rented:
            if dvd.id in customer.rented_dvds:
                return f"{customer.name} has already rented {dvd.name}"
            return f"DVD is already rented"
        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int):
        dvd = [d for d in self.dvds if d.id == dvd_id][0]
        customer = [c for c in self.customers if c.id == customer_id][0]
        if dvd in customer.rented_dvds:
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f"{customer.name} has successfully returned {dvd.name}"
        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        result = ''
        customers_info = '\n'.join([c.__repr__() for c in self.customers])
        result += customers_info + '\n'
        dvds_info = '\n'.join([d.__repr__() for d in self.dvds])
        result += dvds_info + '\n'
        return result
