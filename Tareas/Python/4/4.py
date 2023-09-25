class Reserva:
    def __init__(self, nombre_del_pasajero, numero_de_vuelo, fecha):
        self.nombre_del_pasajero = nombre_del_pasajero
        self.numero_de_vuelo = numero_de_vuelo
        self.fecha = fecha

    def mostrar_detalle(self):
        pass  # Este método se implementará en las clases derivadas


class ReservaEconómica(Reserva):
    def __init__(self, nombre_del_pasajero, numero_de_vuelo, fecha, asiento):
        super().__init__(nombre_del_pasajero, numero_de_vuelo, fecha)
        self.asiento = asiento

    def mostrar_detalle(self):
        return f"Reserva Económica - Pasajero: {self.nombre_del_pasajero}, Número de vuelo: {self.numero_de_vuelo}, Fecha: {self.fecha}, Asiento: {self.asiento}"


class ReservaBusiness(Reserva):
    def __init__(self, nombre_del_pasajero, numero_de_vuelo, fecha, sala_vip):
        super().__init__(nombre_del_pasajero, numero_de_vuelo, fecha)
        self.sala_vip = sala_vip

    def mostrar_detalle(self):
        return f"Reserva Business - Pasajero: {self.nombre_del_pasajero}, Número de vuelo: {self.numero_de_vuelo}, Fecha: {self.fecha}, Sala VIP: {self.sala_vip}"


class ReservaPrimeraClase(Reserva):
    def __init__(self, nombre_del_pasajero, numero_de_vuelo, fecha, servicio_limo):
        super().__init__(nombre_del_pasajero, numero_de_vuelo, fecha)
        self.servicio_limo = servicio_limo

    def mostrar_detalle(self):
        return f"Reserva Primera Clase - Pasajero: {self.nombre_del
