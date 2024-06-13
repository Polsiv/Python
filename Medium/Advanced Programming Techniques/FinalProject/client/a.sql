-- Generado por Oracle SQL Developer Data Modeler 21.4.2.059.0838
--   en:        2022-09-27 16:10:06 COT
--   sitio:      Oracle Database 11g
--   tipo:      Oracle Database 11g



DROP TABLE booking CASCADE CONSTRAINTS;

DROP TABLE guest CASCADE CONSTRAINTS;

DROP TABLE hotel CASCADE CONSTRAINTS;

DROP TABLE room CASCADE CONSTRAINTS;

-- predefined type, no DDL - MDSYS.SDO_GEOMETRY

-- predefined type, no DDL - XMLTYPE

CREATE TABLE booking (
    roomno   INTEGER NOT NULL,
    guestno  INTEGER NOT NULL,
    datefrom DATE NOT NULL,
    dateto   DATE NOT NULL,
    hotelno  INTEGER NOT NULL
);

ALTER TABLE booking ADD CONSTRAINT booking_pk PRIMARY KEY ( hotelno,
                                                            guestno,
                                                            datefrom );

CREATE TABLE guest (
    guestno      INTEGER NOT NULL,
    guestname    VARCHAR2(30) NOT NULL,
    guestaddress VARCHAR2(30) NOT NULL
);

ALTER TABLE guest ADD CONSTRAINT guest_pk PRIMARY KEY ( guestno );

CREATE TABLE hotel (
    hotelno   INTEGER NOT NULL,
    hotelname VARCHAR2(30) NOT NULL,
    city      VARCHAR2(15) NOT NULL
);

ALTER TABLE hotel ADD CONSTRAINT hotel_pk PRIMARY KEY ( hotelno );

CREATE TABLE room (
    roomno  INTEGER NOT NULL,
    hotelno INTEGER NOT NULL,
    type    VARCHAR2(10) NOT NULL,
    price   NUMBER NOT NULL
);

ALTER TABLE room ADD CONSTRAINT room_pk PRIMARY KEY ( roomno,
                                                      hotelno );

ALTER TABLE booking
    ADD CONSTRAINT booking_guest_fk FOREIGN KEY ( guestno )
        REFERENCES guest ( guestno );

ALTER TABLE booking
    ADD CONSTRAINT booking_room_fk FOREIGN KEY ( roomno,
                                                 hotelno )
        REFERENCES room ( roomno,
                          hotelno );

ALTER TABLE room
    ADD CONSTRAINT room_hotel_fk FOREIGN KEY ( hotelno )
        REFERENCES hotel ( hotelno );



-- Informe de Resumen de Oracle SQL Developer Data Modeler: 
-- 
-- CREATE TABLE                             4
-- CREATE INDEX                             0
-- ALTER TABLE                              7
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           0
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          0
-- CREATE MATERIALIZED VIEW                 0
-- CREATE MATERIALIZED VIEW LOG             0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
-- 
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
-- 
-- REDACTION POLICY                         0
-- 
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
-- 
-- ERRORS                                   0
-- WARNINGS                                 0


INSERT INTO hotel (hotelno,hotelname,city)
VALUES (1,'Hotel Intercontinental','Bogota');


INSERT INTO hotel (hotelno,hotelname,city)
VALUES (2,'Hotel Intercontinental','Cali');


INSERT INTO hotel (hotelno,hotelname,city)
VALUES (3,'Hotel Intercontinental','Medellin');


INSERT INTO hotel (hotelno,hotelname,city)
VALUES (4,'Hotel Intercontinental','Barranquilla');


INSERT INTO hotel (hotelno,hotelname,city)
VALUES (5,'Hotel Melia','Bogota');

INSERT INTO hotel (hotelno,hotelname,city)
VALUES (6,'Hotel Melia','Cartagena');


COMMIT;


INSERT into room (roomno,hotelno,type,price)
VALUES (1,1,'Sencilla',100000);

INSERT into room (roomno,hotelno,type,price)
VALUES (2,1,'Doble',150000);

INSERT into room (roomno,hotelno,type,price)
VALUES (3,1,'Triple',175000);

INSERT into room (roomno,hotelno,type,price)
VALUES (4,1,'Cuatruple',200000);

INSERT into room (roomno,hotelno,type,price)
VALUES (5,1,'Especial',200000);


INSERT into room (roomno,hotelno,type,price)
VALUES (1,2,'Sencilla',100000);

INSERT into room (roomno,hotelno,type,price)
VALUES (2,2,'Doble',150000);

INSERT into room (roomno,hotelno,type,price)
VALUES (3,2,'Triple',175000);

INSERT into room (roomno,hotelno,type,price)
VALUES (4,2,'Cuatruple',200000);

INSERT into room (roomno,hotelno,type,price)
VALUES (5,2,'Especial',200000);


INSERT into room (roomno,hotelno,type,price)
VALUES (1,3,'Sencilla',100000);

INSERT into room (roomno,hotelno,type,price)
VALUES (2,3,'Doble',150000);

INSERT into room (roomno,hotelno,type,price)
VALUES (3,3,'Triple',175000);

INSERT into room (roomno,hotelno,type,price)
VALUES (4,3,'Cuatruple',200000);

INSERT into room (roomno,hotelno,type,price)
VALUES (5,3,'Especial',200000);


INSERT into room (roomno,hotelno,type,price)
VALUES (1,4,'Sencilla',100000);

INSERT into room (roomno,hotelno,type,price)
VALUES (2,4,'Doble',150000);

INSERT into room (roomno,hotelno,type,price)
VALUES (3,4,'Triple',175000);

INSERT into room (roomno,hotelno,type,price)
VALUES (4,4,'Cuatruple',200000);

INSERT into room (roomno,hotelno,type,price)
VALUES (5,4,'Especial',200000);

INSERT into room (roomno,hotelno,type,price)
VALUES (1,5,'Sencilla',100000);

INSERT into room (roomno,hotelno,type,price)
VALUES (2,5,'Doble',150000);

INSERT into room (roomno,hotelno,type,price)
VALUES (3,5,'Triple',175000);

INSERT into room (roomno,hotelno,type,price)
VALUES (4,5,'Cuatruple',200000);

INSERT into room (roomno,hotelno,type,price)
VALUES (5,5,'Especial',200000);


INSERT into room (roomno,hotelno,type,price)
VALUES (1,6,'Sencilla',100000);

INSERT into room (roomno,hotelno,type,price)
VALUES (2,6,'Doble',150000);

INSERT into room (roomno,hotelno,type,price)
VALUES (3,6,'Triple',175000);

INSERT into room (roomno,hotelno,type,price)
VALUES (4,6,'Cuatruple',200000);

INSERT into room (roomno,hotelno,type,price)
VALUES (5,6,'Especial',200000);


COMMIT;

INSERT INTO guest (guestno,guestname,guestaddress)
VALUES (123,'Pedro Picapiedra','Calle 1');

INSERT INTO guest (guestno,guestname,guestaddress)
VALUES (456,'Pablo Marmol','Calle 2');

INSERT INTO guest (guestno,guestname,guestaddress)
VALUES (789,'Vilma Picapiedra','Calle 1');

INSERT INTO guest (guestno,guestname,guestaddress)
VALUES (111,'Betty Marmol','Calle 2');

INSERT INTO guest (guestno,guestname,guestaddress)
VALUES (222,'Bamban','Calle 1');

INSERT INTO guest (guestno,guestname,guestaddress)
VALUES (333,'Peebles','Calle 1');


COMMIT;

INSERT INTO booking (hotelno,roomno,guestno,datefrom,dateto)
VALUES(1,5,123,to_date(to_char(sysdate+1,'yyyy-mm-dd'),'yyyy-mm-dd'),to_date(to_char(sysdate+5,'yyyy-mm-dd'),'yyyy-mm-dd'));


INSERT INTO booking (hotelno,roomno,guestno,datefrom,dateto)
VALUES(1,3,123,to_date(to_char(sysdate+1,'yyyy-mm-dd'),'yyyy-mm-dd'),to_date(to_char(sysdate+5,'yyyy-mm-dd'),'yyyy-mm-dd'));

INSERT INTO booking (hotelno,roomno,guestno,datefrom,dateto)
VALUES(1,3,789,to_date(to_char(sysdate+1,'yyyy-mm-dd'),'yyyy-mm-dd'),to_date(to_char(sysdate+5,'yyyy-mm-dd'),'yyyy-mm-dd'));

INSERT INTO booking (hotelno,roomno,guestno,datefrom,dateto)
VALUES(1,3,222,to_date(to_char(sysdate+1,'yyyy-mm-dd'),'yyyy-mm-dd'),to_date(to_char(sysdate+5,'yyyy-mm-dd'),'yyyy-mm-dd'));


INSERT INTO booking (hotelno,roomno,guestno,datefrom,dateto)
VALUES(1,2,456,to_date(to_char(sysdate+1,'yyyy-mm-dd'),'yyyy-mm-dd'),to_date(to_char(sysdate+5,'yyyy-mm-dd'),'yyyy-mm-dd'));

INSERT INTO booking (hotelno,roomno,guestno,datefrom,dateto)
VALUES(1,2,111,to_date(to_char(sysdate+1,'yyyy-mm-dd'),'yyyy-mm-dd'),to_date(to_char(sysdate+5,'yyyy-mm-dd'),'yyyy-mm-dd'));


INSERT INTO booking (hotelno,roomno,guestno,datefrom,dateto)
VALUES(6,3,123,to_date(to_char(sysdate+6,'yyyy-mm-dd'),'yyyy-mm-dd'),to_date(to_char(sysdate+11,'yyyy-mm-dd'),'yyyy-mm-dd'));

INSERT INTO booking (hotelno,roomno,guestno,datefrom,dateto)
VALUES(6,3,789,to_date(to_char(sysdate+6,'yyyy-mm-dd'),'yyyy-mm-dd'),to_date(to_char(sysdate+11,'yyyy-mm-dd'),'yyyy-mm-dd'));

INSERT INTO booking (hotelno,roomno,guestno,datefrom,dateto)
VALUES(6,3,222,to_date(to_char(sysdate+6,'yyyy-mm-dd'),'yyyy-mm-dd'),to_date(to_char(sysdate+11,'yyyy-mm-dd'),'yyyy-mm-dd'));


COMMIT;



