
USE phase2;
CREATE TABLE user (
  fname     varchar(35) not null,
  lname     varchar(35) not null,
  uname     varchar(35),
  pword   varchar(35)
);

INSERT INTO user (fname,lname,uname,pword) VALUES ('Test','Prof','test','prof');


CREATE TABLE student (

  university_ID    varchar(10) not null,
  fname   varchar(20) not null,
  lname   varchar(20) not null,
  address   varchar(50) not null,
  phone_num   varchar(20),
  degree   varchar(20) not null,
  enrollment_year    varchar(10) not null,
  GPA       varchar(10) not null,

  primary key (university_ID),
  foreign key (university_ID) references student (university_ID)
);

INSERT INTO student(university_ID, fname, lname, address, phone_num, degree, enrollment_year, GPA) VALUES ('00000000','Test','User','2135 F st NW','000-000-1000','MS','2014','3.52');
INSERT INTO student(university_ID, fname, lname, address, phone_num, degree, enrollment_year, GPA) VALUES ('88888888','Billie','Holliday','2135 F st NW','000-000-1000','MS','2015','3.25');
INSERT INTO student(university_ID, fname, lname, address, phone_num, degree, enrollment_year, GPA) VALUES ('99999999','Diana','Krall','2135 F st NW','000-000-1000','MS','2016','3.47');


INSERT INTO user(fname, lname,uname,pword) VALUES ('Billie', 'Holliday', 'billie', 'billie1');
INSERT INTO user(fname, lname,uname,pword) VALUES ('Diana', 'Krall', 'diana', 'diana1');



CREATE TABLE transcript (
  
university_ID    varchar(10) not null,
courses   varchar(20) not null,
grades   varchar(10) not null,
semester_and_years   varchar(30) not null,
credit_hours        int(2) not null,

primary key (ç),
foreign key (university_ID) references student (university_ID)
);


CREATE TABLE testuserTranscript (

  university_ID    varchar(10) not null,
  course   varchar(20) not null,
  grade   varchar(10) not null,
  semester_and_year   varchar(30) not null,
  credit_hours       int(2) not null
);



INSERT INTO testuserTranscript (university_ID, course, grade, semester_and_year, credit_hours) VALUES('00000000','CSCI 6221','B-','Fall 2012','4');
INSERT INTO testuserTranscript (university_ID, course, grade, semester_and_year, credit_hours) VALUES('00000000','CSCI 6461','A-','Fall 2012','3');
INSERT INTO testuserTranscript (university_ID, course, grade, semester_and_year, credit_hours) VALUES('00000000','CSCI 6212','B','Spring 2012','3');
INSERT INTO testuserTranscript (university_ID, course, grade, semester_and_year, credit_hours) VALUES('00000000','CSCI 6220','A-','Spring 2012','3');
INSERT INTO testuserTranscript (university_ID, course, grade, semester_and_year, credit_hours) VALUES('00000000','CSCI 6232','B+','Spring 2012','4');
INSERT INTO testuserTranscript (university_ID, course, grade, semester_and_year, credit_hours) VALUES('00000000','CSCI 6233','B','Spring 2012','3');
INSERT INTO testuserTranscript (university_ID, course, grade, semester_and_year, credit_hours) VALUES('00000000','CSCI 6241','B-','Fall 2013','3');
INSERT INTO testuserTranscript (university_ID, course, grade, semester_and_year, credit_hours) VALUES('00000000','CSCI 6242','C+','Fall 2013','3');
INSERT INTO testuserTranscript (university_ID, course, grade, semester_and_year, credit_hours) VALUES('00000000','CSCI 6246','A','Fall 2013','3');
INSERT INTO testuserTranscript (university_ID, course, grade, semester_and_year, credit_hours) VALUES('00000000','CSCI 6260','A','Fall 2013','3');
INSERT INTO testuserTranscript (university_ID, course, grade, semester_and_year, credit_hours) VALUES('00000000','CSCI 6251','A-','Spring 2013','4');
INSERT INTO testuserTranscript (university_ID, course, grade, semester_and_year, credit_hours) VALUES('00000000','CSCI 6252','B','Spring 2013','3');
INSERT INTO testuserTranscript (university_ID, course, grade, semester_and_year, credit_hours) VALUES('00000000','CSCI 6262','B','Spring 2013','3');
INSERT INTO testuserTranscript (university_ID, course, grade, semester_and_year, credit_hours) VALUES('00000000','CSCI 6283','B-','Spring 2013','3');
INSERT INTO testuserTranscript (university_ID, course, grade, semester_and_year, credit_hours) VALUES('00000000','CSCI 6284','B+','Spring 2013','3');
INSERT INTO testuserTranscript (university_ID, course, grade, semester_and_year, credit_hours) VALUES('00000000','CSCI 6286','C+','Fall 2014','3');
INSERT INTO testuserTranscript (university_ID, course, grade, semester_and_year, credit_hours) VALUES('00000000','CSCI 6221','A-','Fall 2014','3');
INSERT INTO testuserTranscript (university_ID, course, grade, semester_and_year, credit_hours) VALUES('00000000','CSCI 6325','B-','Fall 2014','4');
INSERT INTO testuserTranscript (university_ID, course, grade, semester_and_year, credit_hours) VALUES('00000000','ECE 6241','B','Fall 2014','3');

INSERT INTO testuserTranscript (university_ID, course, grade, semester_and_year, credit_hours) VALUES('88888888','CSCI 6221','B-','Fall 2012','4');
INSERT INTO testuserTranscript (university_ID, course, grade, semester_and_year, credit_hours) VALUES('88888888','CSCI 6220','A-','Spring 2012','3');
INSERT INTO testuserTranscript (university_ID, course, grade, semester_and_year, credit_hours) VALUES('88888888','CSCI 6232','B+','Spring 2012','4');
INSERT INTO testuserTranscript (university_ID, course, grade, semester_and_year, credit_hours) VALUES('88888888','CSCI 6233','B','Spring 2012','3');
INSERT INTO testuserTranscript (university_ID, course, grade, semester_and_year, credit_hours) VALUES('88888888','CSCI 6241','B-','Fall 2013','3');
INSERT INTO testuserTranscript (university_ID, course, grade, semester_and_year, credit_hours) VALUES('88888888','CSCI 6242','C+','Fall 2013','3');
INSERT INTO testuserTranscript (university_ID, course, grade, semester_and_year, credit_hours) VALUES('88888888','CSCI 6246','A','Fall 2013','3');
INSERT INTO testuserTranscript (university_ID, course, grade, semester_and_year, credit_hours) VALUES('88888888','CSCI 6260','A','Fall 2013','3');
INSERT INTO testuserTranscript (university_ID, course, grade, semester_and_year, credit_hours) VALUES('88888888','CSCI 6251','A-','Spring 2013','4');
INSERT INTO testuserTranscript (university_ID, course, grade, semester_and_year, credit_hours) VALUES('88888888','CSCI 6252','B','Spring 2013','3');
INSERT INTO testuserTranscript (university_ID, course, grade, semester_and_year, credit_hours) VALUES('88888888','CSCI 6262','B','Spring 2013','3');
INSERT INTO testuserTranscript (university_ID, course, grade, semester_and_year, credit_hours) VALUES('88888888','CSCI 6283','B-','Spring 2013','3');
INSERT INTO testuserTranscript (university_ID, course, grade, semester_and_year, credit_hours) VALUES('88888888','CSCI 6284','B+','Spring 2013','3');
INSERT INTO testuserTranscript (university_ID, course, grade, semester_and_year, credit_hours) VALUES('88888888','CSCI 6286','C+','Fall 2014','3');
INSERT INTO testuserTranscript (university_ID, course, grade, semester_and_year, credit_hours) VALUES('88888888','CSCI 6221','A-','Fall 2014','3');
INSERT INTO testuserTranscript (university_ID, course, grade, semester_and_year, credit_hours) VALUES('88888888','CSCI 6325','B-','Fall 2014','4');
INSERT INTO testuserTranscript (university_ID, course, grade, semester_and_year, credit_hours) VALUES('88888888','ECE 6241','B','Fall 2014','3');

INSERT INTO testuserTranscript (university_ID, course, grade, semester_and_year, credit_hours) VALUES('99999999','CSCI 6221','B-','Fall 2012','4');
INSERT INTO testuserTranscript (university_ID, course, grade, semester_and_year, credit_hours) VALUES('99999999','CSCI 6461','A-','Fall 2012','3');
INSERT INTO testuserTranscript (university_ID, course, grade, semester_and_year, credit_hours) VALUES('99999999','CSCI 6212','B','Spring 2012','3');
INSERT INTO testuserTranscript (university_ID, course, grade, semester_and_year, credit_hours) VALUES('99999999','CSCI 6220','A-','Spring 2012','3');
INSERT INTO testuserTranscript (university_ID, course, grade, semester_and_year, credit_hours) VALUES('99999999','CSCI 6232','B+','Spring 2012','4');
INSERT INTO testuserTranscript (university_ID, course, grade, semester_and_year, credit_hours) VALUES('99999999','CSCI 6233','B','Spring 2012','3');
INSERT INTO testuserTranscript (university_ID, course, grade, semester_and_year, credit_hours) VALUES('99999999','CSCI 6241','B-','Fall 2013','3');
INSERT INTO testuserTranscript (university_ID, course, grade, semester_and_year, credit_hours) VALUES('99999999','CSCI 6242','C+','Fall 2013','3');
INSERT INTO testuserTranscript (university_ID, course, grade, semester_and_year, credit_hours) VALUES('99999999','CSCI 6246','A','Fall 2013','3');
INSERT INTO testuserTranscript (university_ID, course, grade, semester_and_year, credit_hours) VALUES('99999999','CSCI 6260','A','Fall 2013','3');
INSERT INTO testuserTranscript (university_ID, course, grade, semester_and_year, credit_hours) VALUES('99999999','CSCI 6251','A-','Spring 2013','4');
INSERT INTO testuserTranscript (university_ID, course, grade, semester_and_year, credit_hours) VALUES('99999999','CSCI 6252','B','Spring 2013','3');
INSERT INTO testuserTranscript (university_ID, course, grade, semester_and_year, credit_hours) VALUES('99999999','CSCI 6262','B','Spring 2013','3');
INSERT INTO testuserTranscript (university_ID, course, grade, semester_and_year, credit_hours) VALUES('99999999','CSCI 6283','B-','Spring 2013','3');
INSERT INTO testuserTranscript (university_ID, course, grade, semester_and_year, credit_hours) VALUES('99999999','CSCI 6284','B+','Spring 2013','3');
INSERT INTO testuserTranscript (university_ID, course, grade, semester_and_year, credit_hours) VALUES('99999999','CSCI 6286','C+','Fall 2014','3');
INSERT INTO testuserTranscript (university_ID, course, grade, semester_and_year, credit_hours) VALUES('99999999','CSCI 6221','A-','Fall 2014','3');
INSERT INTO testuserTranscript (university_ID, course, grade, semester_and_year, credit_hours) VALUES('99999999','CSCI 6325','B-','Fall 2014','4');
INSERT INTO testuserTranscript (university_ID, course, grade, semester_and_year, credit_hours) VALUES('99999999','ECE 6241','B','Fall 2014','3');


CREATE TABLE verifyCourses (
  dept          varchar(4),
  course_num    int(4),
  course_name         varchar(25),
  credits       int(4),
  prereq_1      varchar(25),
  prereq_2      varchar(25),
  university_ID   varchar(10),
  grade   varchar(10),
  day     varchar(20),
  time    varchar(20)
);


INSERT INTO verifyCourses(dept,course_num,course_name,credits,prereq_1,prereq_2,university_ID,grade,day,time) VALUES ('CSCI',6221,'SW Paradigms','3','None','None','00000000','IP','M','1500-1700');
INSERT INTO verifyCourses(dept,course_num,course_name,credits,prereq_1,prereq_2,university_ID,grade,day,time) VALUES ('CSCI',6461,'Computer Architecture','3','None','None','88888888','IP','T','1500-1730');
INSERT INTO verifyCourses(dept,course_num,course_name,credits,prereq_1,prereq_2,university_ID,grade,day,time) VALUES ('CSCI',6212,'Algorithms','3','None','None','88888888','IP','W','1500-1730');
INSERT INTO verifyCourses(dept,course_num,course_name,credits,prereq_1,prereq_2,university_ID,grade,day,time) VALUES ('CSCI',6232,'Algorithms','3','None','None','00000000','IP','W','1500-1730');





CREATE TABLE CourseCatalog (
  dept          varchar(4),
  course_num    int(4),
  course_name         varchar(25),
  credits       int(4),
  section       int(4),
  prereq_1      varchar(25),
  prereq_2      varchar(25),

  primary key (course_num)
);


CREATE TABLE schedule (
  course_ID     int(2) not null,
  dept          varchar(4),
  course_num    int(4),
  course_name         varchar(25),
  credits       int(4),
  day       varchar(4),
  time      varchar(25),

  primary key (course_ID)
);





CREATE TABLE faculty (

    faculty_ID      varchar(10)not null,
    fname       varchar(20) not null,
    lname       varchar(20) not null,
    department       varchar(15) not null,
    
    primary key (faculty_ID)
);

INSERT INTO faculty (faculty_ID, fname, lname, department) VALUES ('12345678','Bhagirath','Narahari','CSCI');
INSERT INTO faculty (faculty_ID, fname, lname, department) VALUES ('23456789','Professor','Choi','CSCI');

CREATE TABLE gradsec (

    gradsec_ID      varchar(10)not null,
    fname       varchar(20) not null,
    lname       varchar(20) not null,
    
    primary key (gradsec_ID)
);
INSERT INTO gradsec (gradsec_ID, fname, lname) VALUES ('12121212','Grad', 'Secretary');



CREATE TABLE teaches (

    faculty_ID      varchar(10)not null,
    course_name     varchar(15) not null,
    course_num      varchar(10) not null,

    primary key (faculty_ID),
    foreign key (course_num) references course (course_num)
);

INSERT INTO teaches (faculty_ID, course_name, course_num) VALUES ('12345678','CSCI','6461');
INSERT INTO teaches (faculty_ID, course_name, course_num) VALUES ('23456789','CSCI','6212');


CREATE TABLE #prereq (
  university_ID    varchar(10) not null,
  Course1          varchar(10),
  Course2          varchar(10),
  Course3          varchar(10),
  Course4          varchar(10),
  Course5          varchar(10),
  Course6          varchar(10),
  Course7          varchar(10),
  Course8          varchar(10),
  primary key (university_ID),
  foreign key (university_ID) references student (university_ID)
);



--INSERT

INSERT INTO CourseCatalog(dept,course_num,course_name,credits,section,prereq_1,prereq_2) VALUES ('CSCI',6221,'SW Paradigms','3','1','None','None');
INSERT INTO CourseCatalog(dept,course_num,course_name,credits,section,prereq_1,prereq_2) VALUES ('CSCI',6461,'Computer Architecture','3','1','None','None');
INSERT INTO CourseCatalog(dept,course_num,course_name,credits,section,prereq_1,prereq_2) VALUES ('CSCI',6212,'Algorithms','3','1','None', 'None');
INSERT INTO CourseCatalog(dept,course_num,course_name,credits,section,prereq_1,prereq_2) VALUES ('CSCI',6220,'Machine Learning','3','1','None','None');
INSERT INTO CourseCatalog(dept,course_num,course_name,credits,section,prereq_1,prereq_2) VALUES ('CSCI',6232,'Networks 1','3','1','None','None');
INSERT INTO CourseCatalog(dept,course_num,course_name,credits,section,prereq_1,prereq_2) VALUES ('CSCI',6233,'Networks 2','3','1','CSCI 6232','None');
INSERT INTO CourseCatalog(dept,course_num,course_name,credits,section,prereq_1,prereq_2) VALUES ('CSCI',6241,'Database 1','3','1','None','None');
INSERT INTO CourseCatalog(dept,course_num,course_name,credits,section,prereq_1,prereq_2) VALUES ('CSCI',6242,'Database 2','3','1','CSCI 6241','None');
INSERT INTO CourseCatalog(dept,course_num,course_name,credits,section,prereq_1,prereq_2) VALUES ('CSCI',6246,'Compilers','3','1','CSCI 6461','CSCI 6212');
INSERT INTO CourseCatalog(dept,course_num,course_name,credits,section,prereq_1,prereq_2) VALUES ('CSCI',6260,'Multimedia','3','1','None','None');
INSERT INTO CourseCatalog(dept,course_num,course_name,credits,section,prereq_1,prereq_2) VALUES ('CSCI',6251,'Cloud Computing','3','1','CSCI 6461','None');
INSERT INTO CourseCatalog(dept,course_num,course_name,credits,section,prereq_1,prereq_2) VALUES ('CSCI',6254,'SW Engineering','3','1','CSCI 6221','None');
INSERT INTO CourseCatalog(dept,course_num,course_name,credits,section,prereq_1,prereq_2) VALUES ('CSCI',6262,'Graphics 1','3','1','None','None');
INSERT INTO CourseCatalog(dept,course_num,course_name,credits,section,prereq_1,prereq_2) VALUES ('CSCI',6283,'Security 1','3','1','CSCI 6212','None');
INSERT INTO CourseCatalog(dept,course_num,course_name,credits,section,prereq_1,prereq_2) VALUES ('CSCI',6284,'Cryptography','3','1','CSCI 6212','None');
INSERT INTO CourseCatalog(dept,course_num,course_name,credits,section,prereq_1,prereq_2) VALUES ('CSCI',6286,'Network Security','3','1','CSCI 6283','CSCI 6232');
INSERT INTO CourseCatalog(dept,course_num,course_name,credits,section,prereq_1,prereq_2) VALUES ('CSCI',6325,'Algorithms 2','3','1','CSCI 6212','None');
INSERT INTO CourseCatalog(dept,course_num,course_name,credits,section,prereq_1,prereq_2) VALUES ('CSCI',6339,'Embedded Systems','3','1','CSCI 6461','CSCI 6212');
INSERT INTO CourseCatalog(dept,course_num,course_name,credits,section,prereq_1,prereq_2) VALUES ('CSCI',6384,'Cryptography 2','3','1','CSCI 6284','None');
INSERT INTO CourseCatalog(dept,course_num,course_name,credits,section,prereq_1,prereq_2) VALUES ('ECE',6241,'Communication Theory','3','1','None','None');
INSERT INTO CourseCatalog(dept,course_num,course_name,credits,section,prereq_1,prereq_2) VALUES ('ECE',6242,'Information Theory','3','1','None','None');
INSERT INTO CourseCatalog(dept,course_num,course_name,credits,section,prereq_1,prereq_2) VALUES ('MATH',6210,'Logic','3','1','None','None');


INSERT INTO schedule(course_ID,dept,course_num,course_name,credits,day,time) VALUES (1,'CSCI',6221,'SW Paradigms',3,'M','1500—1730');
INSERT INTO schedule(course_ID,dept,course_num,course_name,credits,day,time) VALUES (2,'CSCI',6461,'Computer Architecture',3,'T','1500—1730');
INSERT INTO schedule(course_ID,dept,course_num,course_name,credits,day,time) VALUES (3,'CSCI',6212,'Algorithms',3,'W','1500—1730');
INSERT INTO schedule(course_ID,dept,course_num,course_name,credits,day,time) VALUES (4,'CSCI',6232,'Networks 1',3,'M','1800—2030');
INSERT INTO schedule(course_ID,dept,course_num,course_name,credits,day,time) VALUES (5,'CSCI',6233,'Networks 2',3,'T','1800—2030');
INSERT INTO schedule(course_ID,dept,course_num,course_name,credits,day,time) VALUES (6,'CSCI',6241,'Database 1',3,'W','1800—2030');
INSERT INTO schedule(course_ID,dept,course_num,course_name,credits,day,time) VALUES (7,'CSCI',6242,'Database 2',3,'R','1800—2030');
INSERT INTO schedule(course_ID,dept,course_num,course_name,credits,day,time) VALUES (8,'CSCI',6246,'Compilers',3,'T','1500—1730');
INSERT INTO schedule(course_ID,dept,course_num,course_name,credits,day,time) VALUES (9,'CSCI',6251,'Cloud Computing',3,'M','1800—2030');
INSERT INTO schedule(course_ID,dept,course_num,course_name,credits,day,time) VALUES (10,'CSCI',6254,'SW Engineering',3,'M','1530—1800');
INSERT INTO schedule(course_ID,dept,course_num,course_name,credits,day,time) VALUES (11,'CSCI',6260,'Multimedia',3,'R','1800—2030');
INSERT INTO schedule(course_ID,dept,course_num,course_name,credits,day,time) VALUES (12,'CSCI',6262,'Graphics 1',3,'W','1800—2030');
INSERT INTO schedule(course_ID,dept,course_num,course_name,credits,day,time) VALUES (13,'CSCI',6283,'Security 1',3,'T','1800—2030');
INSERT INTO schedule(course_ID,dept,course_num,course_name,credits,day,time) VALUES (14,'CSCI',6284,'Cryptography',3,'M','1800—2030');
INSERT INTO schedule(course_ID,dept,course_num,course_name,credits,day,time) VALUES (15,'CSCI',6286,'Network Security',3,'W','1800—2030');
INSERT INTO schedule(course_ID,dept,course_num,course_name,credits,day,time) VALUES (16,'CSCI',6384,'Cryptography 2',3,'W','1500—1730');
INSERT INTO schedule(course_ID,dept,course_num,course_name,credits,day,time) VALUES (17,'ECE',6241,'Communication Theory',3,'M','1800—2030');
INSERT INTO schedule(course_ID,dept,course_num,course_name,credits,day,time) VALUES (18,'ECE',6242,'Information Theory',2,'T','1800—2030');
INSERT INTO schedule(course_ID,dept,course_num,course_name,credits,day,time) VALUES (19,'MATH',6210,'Logic',2,'W','1800-2030');
INSERT INTO schedule(course_ID,dept,course_num,course_name,credits,day,time) VALUES (20,'CSCI',6339,'Embedded Systems',3,'R','1600--1830');

INSERT INTO user(fname, lname,uname,pword) VALUES ('Test', 'User', 'testing', 'test1');
INSERT INTO user(fname, lname,uname,pword) VALUES ('Bhagirath', 'Narahari', 'narahari', 'narahari1');
INSERT INTO user(fname, lname,uname,pword) VALUES ('Professor', 'Choi', 'choi', 'choi1');
INSERT INTO user(fname, lname,uname,pword) VALUES ('Grad', 'Secretary', 'gradsec', 'gradsec1');
