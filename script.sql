create database keywordchecker;

use keywordchecker;


create table payed (
	id int primary key auto_increment,
    name varchar(255),
    payed bool,
    value float
);



create table subscription (
	id int primary key auto_increment,
    name varchar(255),
    description longtext null,
    image longblob null,
    value float,
    startdate date,
    enddate date,
    payment int
);


create table roles (
	id int primary key auto_increment,
    name varchar(255),
    description longtext null
);


create table subscription_payment (
	subscription_id int,
    payment_id int,
    
    foreign key (subscription_id) references subscription(id),
    foreign key (payment_id) references payed(id)
);


create table users (
	id int primary key auto_increment,
    username varchar(255),
    password varchar(255),
	email varchar(255),
    email_verified_at bool,
    image longblob null,
    role_id integer not null,
    subscription_id int not null,
    
	foreign key (role_id) references roles(id),
    foreign key (subscription_id) references subscription(id)
);


create table saved_key_words (
	id int primary key auto_increment,
    name varchar(255),
    user_id int not null,
    
    foreign key (user_id) references users(id)
);


create table settings (
	id int primary key auto_increment,
    name varchar(255),
    value varchar(255),
    user_id integer not null,
    
    foreign key (user_id) references users(id)
);

insert into roles
	(name, description)
    values ("admin", "henk");
    
insert into subscription
	(name, description, image, value, startdate, enddate, payment)
    values ("henk", "henk", "", 2.00, "2021/02/02", "2021/02/02", 1);
    
    insert into users
		(username, password, email, email_verified_at, image, role_id, subscription_id)
        values ("nico", "henkdepotvis", "nicovanommen.nvo@gmail.com", true, "", 1, 1);