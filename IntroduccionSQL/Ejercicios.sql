--Ejercicio1
select * from flights where status = 'On Time'

--Ejercicio2

select * from bookings where total_amount > 1000000

--Ejercicio3

select * from aircrafts_data

--Ejercicio4

select * from flights where aircraft_code = '733'

--Ejercicio5

select * from tickets where UPPER(passenger_name) like UPPER('irina%')