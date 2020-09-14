import sqlite3
#创建连接对象
conn = sqlite3.connect("school.db")
cursor = conn.cursor()
#cursor.execute("create table student(sno bigint primary key,sname varchar(30), ssex char(4), password varchar(30), qq bigint, tel bigint, dno int, clsno int,foreign key(dno) references dept(dno),foreign key(clsno) references cls(clsno))")
#cursor.execute("create table teacher(tno bigint primary key, tname varchar(30),tsex char(4),password varchar(30),dept int,foreign key(dept) references dept(dno))")
#cursor.execute("create table course(cno bigint primary key, credit decimal(6,2),tno bigint,coursename varchar(30),foreign key(tno) references teacher(tno))")

#cursor.execute("create table sel(sno bigint,cno bigint, grade decimal(6,2),primary key (sno,cno),foreign key(sno) references student(sno),foreign key(cno) references course(cno))")
#cursor.execute("create table edu(sno bigint, level varchar(30),school varchar(100),sdate varchar(30),primary key(sno,level),foreign key(sno) references student(sno))")
#cursor.execute("create table parents(sno bigint, pname varchar(30), psex char(4),ptel bigint,primary key(sno,pname),foreign key(sno) references student(sno))")
#cursor.execute("create view studentview as select )
#cursor.execute("create table dept(dno int primary key,dname varchar(30))")
cursor.execute("create table cls(clsno int primary key,clsname varchar(30))")

#注意单双引号
#cursor.execute('insert into user values(?,?)',(3,"你好"))
#cursor.execute("select * from user")
#print(cursor.fetchone())
#print(cursor.fetchmany(100))
conn.commit()
cursor.close()
conn.close()