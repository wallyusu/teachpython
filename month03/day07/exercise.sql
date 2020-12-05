--创建数据库
create database class_test character set utf8;

--创建表
create table student(sid int primary key auto_increment,
sname varchar(30),sbirth datetime,ssex enum('m','w'));

create table course(cid int primary key auto_increment,
cname varchar(50),tid int not null,
constraint teacher_fk foreign key (tid) references teacher(tid));

create table teacher(tid int primary key auto_increment,
tname varchar(30));

create table score(sid int,cid int,sscore decimal(5,2),
constraint score_fk foreign key (sid) references student(sid),
constraint score1_fk foreign key (cid) references course(cid));

--插入表内容
insert into student values(1,'张佳琪','1996-05-02','m'),
(2,'张新蕊','1997-01-06','w'),
(3,'王宝强','1995-12-01','m'),
(4,'王帅','1990-11-20','m'),
(5,'张丽','1990-12-01','w'),
(6,'张天天','1990-01-12','w');

insert into teacher values (1,'张小军'),
(2,'汪峰'),
(3,'张丽'),
(4,'雪莉'),
(5,'尼古拉斯张');

insert into course values (01,'语文',2),
(02,'数学',1),
(03,'英语',5),
(04,'物理',3),
(05,'化学',4);

insert into score values (1,01,80),
(1,02,92),
(1,03,61),
(1,04,100),
(1,05,88),
(2,01,59),
(2,02,90),
(2,03,65),
(2,04,76),
(2,05,61),
(3,01,79),
(3,02,70),
(3,03,89),
(3,04,45),
(3,05,77),
(4,01,55),
(4,02,66),
(4,03,70),
(4,04,56),
(4,05,55),
(5,01,99),
(5,02,89),
(5,03,70),
(5,04,76),
(5,05,55),
(6,01,44),
(6,02,70),
(6,03,65),
(6,04,88),
(6,05,90);

--查询表内容
--查询姓张的老师的个数（知识点 like）
select count(tid) from teacher where tname like '张%';
--查询名字中有“风”字的学生名单
select * from student where sname like '%风%';
--1990年出生的学生名单
select * from student where sbirth like '1990%';
--方法2：
SELECT sname AS '学生姓名' FROM student WHERE year(sbirth) = 1990;
--查询课程编号为02的总成绩
select cid,sum(sscore) from score where cid = 02;
--查询选了课程的学生人数
SELECT COUNT(DISTINCT sid) AS 学生人数 FROM score;
--查询各科成绩最高和最低的分： 以如下的形式显示：课程ID，最高分，最低分
select cid,max(sscore),min(sscore) from score group by cid;
+------+-------------+-------------+
| cid  | max(sscore) | min(sscore) |
+------+-------------+-------------+
|    1 |       99.00 |       44.00 |
|    2 |       92.00 |       66.00 |
|    3 |       89.00 |       61.00 |
|    4 |      100.00 |       45.00 |
|    5 |       90.00 |       55.00 |
+------+-------------+-------------+
--查询每门课程被选修的学生数
select cid as 课程ID,count(sid) as 学生人数 from score group by cid;
+------+------------+
| cid  | count(sid) |
+------+------------+
|    1 |          6 |
|    2 |          6 |
|    3 |          6 |
|    4 |          6 |
|    5 |          6 |
+------+------------+
--查询男生、女生人数
select ssex as 性别,count(sid) as 学生人数 from student group by ssex;
+------+------------+
| ssex | count(sid) |
+------+------------+
| m    |          5 |
| w    |          3 |
+------+------------+
--查询平均成绩大于60分的学生的学号和平均成绩
select sid as 学号,avg(sscore) as 平均成绩 from score group by sid having avg(sscore) > 60;
+------+-------------+
| sid  | avg(sscore) |
+------+-------------+
|    1 |   84.200000 |
|    2 |   70.200000 |
|    3 |   72.000000 |
|    4 |   60.400000 |
|    5 |   77.800000 |
|    6 |   71.400000 |
+------+-------------+
--查询至少选修两门课程的学生学号
select sid as 学号,count(cid) as 课程数 from score group by sid having count(cid) >= 2;
+------+------------+
| sid  | count(cid) |
+------+------------+
|    1 |          5 |
|    2 |          5 |
|    3 |          5 |
|    4 |          5 |
|    5 |          5 |
|    6 |          5 |
+------+------------+
-- *查询两门以上不及格课程的同学的学号及其平均成绩
SELECT sid AS '学号', AVG(sscore) AS '平均成绩'
FROM score
WHERE sscore <60
GROUP BY sid
HAVING COUNT(cid) >=2;

-- *查询同名同性学生名单并统计同名人数
 SELECT sname AS '学生姓名', COUNT(*) AS '学生人数'
FROM student
GROUP BY sname
HAVING COUNT(*) >1;

--查询每门课程的平均成绩，结果按平均成绩升序排序，平均成绩相同时，按课程号降序排列。
select cid as 课程号,avg(sscore) as 平均成绩 from score group by cid order by avg(sscore),cid desc;
+------+-------------+
| cid  | avg(sscore) |
+------+-------------+
|    1 |   69.333333 |
|    3 |   70.000000 |
|    5 |   71.000000 |
|    4 |   73.500000 |
|    2 |   79.500000 |
+------+-------------+
--查询不及格的课程并按课程号从大到小排列
select cid,sscore from score where sscore < 60 order by cid desc,sscore;

-- 检索课程编号为“04”且分数小于60的学生学号，结果按分数降序排列
select sid,sscore from score where cid = 04 and sscore < 60 order by sscore desc;
+------+--------+
| sid  | sscore |
+------+--------+
|    4 |  56.00 |
|    3 |  45.00 |
+------+--------+

--统计每门课程的学生选修人数(超过5人的课程才统计)
select cid,count(sid) from
score group by cid having count(sid) > 5
order by count(sid) desc,cid;
+------+------------+
| cid  | count(sid) |
+------+------------+
|    1 |          6 |
|    2 |          6 |
|    3 |          6 |
|    4 |          6 |
|    5 |          6 |
+------+------------+

-- *查询所有课程成绩小于60分的学生的学号、姓名。（distinct 去除重复）
select sid,sname from
student where sid not in
(select distinct sid from score where sscore > 60);

-- *查询没有学全所有课的学生的学号、姓名
*【解题思路】：学生学习的课程数小于总的课程数。

涉及到三张表student，score，course。

SELECT sid AS '学号', sname AS '姓名'
FROM student
WHERE sid IN
(SELECT sid
FROM score
GROUP BY sid
HAVING COUNT(cid) < (SELECT COUNT(cid)
FROM course)
);

-- 查询出只选修了两门课程的全部学生的学号和姓名。
SELECT sid AS '学号', sname AS '姓名'
FROM student
WHERE sid IN
(SELECT sid
FROM score
GROUP BY sid
HAVING COUNT(cid) = 2
);



--查询课程编号为03且课程成绩在80分以上的学生的学号和姓名
select student.sid,student.sname from
student left join score on student.sid=score.sid
where score.cid=03 and sscore >80;
--方法2，使用谓词 IN：
SELECT sid AS '学号', sname AS '姓名'
FROM student
WHERE sid IN
(SELECT sid
FROM score
WHERE cid = 03 AND sscore > 80
);

-- *查询课程编号为“01”的课程比“02”的课程成绩高的所有学生的学号。
