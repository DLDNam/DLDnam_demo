drop table if exists Major;
DROP TABLE IF EXISTS Students;

CREATE TABLE Students(
 Student_ID int(20),
 Student_Name VARCHAR(20),
 Date_Of_Birth DATE,
 Class_ID VARCHAR(20)
);

create table Major(
	Class_ID varchar(6),
	Class_Name varchar(20),
	Number_of_Students int(20)
);

INSERT INTO Students(student_id, student_name, date_of_birth, Class_ID)
VALUES
	(32,'Hary Kane','18/10/2003','INT'),
    (54,'Lionel Messi','23/12/200','INE'),
    (65,'Jordan Pickford','12/04/2002','INP'),
    (12,'Blacka','23/10/2001','MAT'),
    (19,'Coldzy','19/07/2002','INP'),
    (78,'Preanky','12/01/2002','MAT'),
    (89,'Macky','06/05/2003','INS'),
    (36,'Dlow','29/03/2003','INP'),
    (69,'Nesta','07/12/2001','INT'),
    (86,'Madison','12/11/2003','INS'),
    (66,'Siguson','04/09/2003','MAT');

insert into Major (Class_ID,Class_Name,Number_of_Students)
values	
	('INT','Introduction to Informatics 2',54),
	('INE','Macroeconomics',50),
	('INS','Introduction to BDA',40),
	('INE','English',20),
    ('INM','Microeconomics',29),
    ('INP','Programming',60),
	('MAT','Advanced Mathematics',54);
    

SELECT * FROM Major
ORDER BY number_of_students DESC;

DELETE from Major
WHERE number_of_students < 30;

UPDATE Students
SET Student_Name = 'Franky'
WHERE student_id = 78;

 