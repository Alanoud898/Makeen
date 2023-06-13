IF OBJECT_ID('ISSUING', 'U') IS NOT NULL
  DROP TABLE ISSUING;

IF OBJECT_ID('REGIST', 'U') IS NOT NULL
  DROP TABLE REGIST;

IF OBJECT_ID('CBLink', 'U') IS NOT NULL
  DROP TABLE CBLink;

IF OBJECT_ID('COURSE', 'U') IS NOT NULL
  DROP TABLE COURSE;

IF OBJECT_ID('STUDENT', 'U') IS NOT NULL
  DROP TABLE STUDENT;

IF OBJECT_ID('EMPLOYEE', 'U') IS NOT NULL
  DROP TABLE EMPLOYEE;

IF OBJECT_ID('BORROWER', 'U') IS NOT NULL
  DROP TABLE BORROWER;

IF OBJECT_ID('BOOKTOPIC', 'U') IS NOT NULL
  DROP TABLE BOOKTOPIC;

IF OBJECT_ID('BOOK', 'U') IS NOT NULL
  DROP TABLE BOOK;

IF OBJECT_ID('DEPARTMENT', 'U') IS NOT NULL
  DROP TABLE DEPARTMENT;

IF OBJECT_ID('College', 'U') IS NOT NULL
  DROP TABLE College;


CREATE TABLE College (
  Cl_Code CHAR(3) PRIMARY KEY,
  Cl_Name VARCHAR(40) NOT NULL,
  Cl_Dean VARCHAR(30)NOT NULL,
);

CREATE TABLE department (
  Dp_Code CHAR(4) PRIMARY KEY,
  Dp_Name VARCHAR(40) NOT NULL,
  Dp_HoD VARCHAR(30) NOT NULL,
  Dp_Col CHAR(3),
  FOREIGN KEY (Dp_Col) REFERENCES College(Cl_Code)
);

CREATE TABLE BOOK (
  Bk_ID NUMERIC(6) PRIMARY KEY,
  Bk_Title VARCHAR(50) NOT NULL,
  Bk_Edition NUMERIC(2) NOT NULL,
  Bk_#ofPages NUMERIC(4) CHECK (Bk_#ofPages > 0),
  Bk_TotalCopies NUMERIC(5) NOT NULL,
  Bk_RemCopies NUMERIC(5) NOT NULL
  );

CREATE TABLE BOOKTOPIC (
  Tp_BkID NUMERIC(6),
  Tp_Desc VARCHAR(30) NOT NULL,
  FOREIGN KEY (Tp_BkID) REFERENCES BOOK(Bk_ID)
);

CREATE TABLE BORROWER (
  Br_ID NUMERIC(6) PRIMARY KEY,
  Br_Name VARCHAR(30) NOT NULL,
  Br_Dept CHAR(4),
  Br_Mobile CHAR(8) CHECK (Br_Mobile >= '90000000'),
  Br_City VARCHAR(20) NOT NULL,
  Br_House# CHAR(4) NOT NULL,
  Br_Type CHAR(1) CHECK (Br_Type IN ('S', 'E')),
  FOREIGN KEY (Br_Dept) REFERENCES DEPARTMENT(Dp_Code)
);

CREATE TABLE EMPLOYEE (
  Em_ID NUMERIC(6) PRIMARY KEY,
  Em_Office# CHAR(4) NOT NULL,
  Em_Ext# NUMERIC(4) CHECK (Em_Ext# > 1000)
);

CREATE TABLE STUDENT (
  St_ID NUMERIC(6) PRIMARY KEY,
  St_Major VARCHAR(30) NOT NULL,
  St_Cohort NUMERIC(4) NOT NULL
);

CREATE TABLE COURSE (
  Cr_Code CHAR(8) PRIMARY KEY,
  Cr_Title VARCHAR(40) NOT NULL,
  Cr_CH NUMERIC(2) CHECK (Cr_CH > 0),
  Cr_#ofSec NUMERIC(2) CHECK (Cr_#ofSec > 0),
  Cr_Dept CHAR(4),
  FOREIGN KEY (Cr_Dept) REFERENCES DEPARTMENT(Dp_Code)
);

CREATE TABLE CBLink (
  Li_CrCode CHAR(8),
  Li_BkID NUMERIC(6),
  Li_usage CHAR(1) CHECK (Li_usage IN ('T', 'R')),
  FOREIGN KEY (Li_CrCode) REFERENCES COURSE(Cr_Code),
  FOREIGN KEY (Li_BkID) REFERENCES BOOK(Bk_ID)
);

CREATE TABLE REGIST (
  Re_BrID NUMERIC(6),
  Re_CrCode CHAR(8),
  Re_Semester CHAR(6) NOT NULL,
  FOREIGN KEY (Re_BrID) REFERENCES BORROWER(Br_ID),
  FOREIGN KEY (Re_CrCode) REFERENCES COURSE(Cr_Code)
);

-- Table11: ISSUING
CREATE TABLE ISSUING (
  is_BrID NUMERIC(6),
  is_BkID NUMERIC(6),
  is_DateTaken DATE NOT NULL,
  is_DateReturn DATE,
  CONSTRAINT CHK_DateReturn CHECK (is_DateReturn > is_DateTaken),
  FOREIGN KEY (is_BrID) REFERENCES BORROWER(Br_ID),
  FOREIGN KEY (is_BkID) REFERENCES BOOK(Bk_ID)
);


SELECT * FROM College;
SELECT* FROM department;
SELECT * FROM REGIST;
SELECT * FROM COURSE;

INSERT INTO College (Cl_Code, Cl_Name, Cl_Dean)
VALUES('SCI', 'Science', 'Prof. Salma'),
       ('EDU', 'Education', 'Dr. Hamad'),
	    ('ART', 'Arts', 'Dr. Abdullah');

INSERT INTO department (Dp_Code, Dp_Name, Dp_Col, Dp_HoD)
VALUES('INFS', 'Information Systems', 'COM', 'Dr. Kamla'),
       ('FINA', 'Finance', 'COM', 'Dr. Salim'),
	   ('COMP', 'Computer Science', 'SCI', 'Dr. Zuhoor'),
	    ('BIOL', 'Biology', 'SCI', 'Dr. Othman'),
		('HIST', 'History', 'EDU', 'Dr. Said');



);