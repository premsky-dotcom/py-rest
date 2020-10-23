GRANT ALL privileges ON `metadata_schema`.* TO 'local_dev_fid';

use metadata_schema;

drop table Product;

create table Product
(
	id int auto_increment primary key,
	name nvarchar(100) unique not null,
	description nvarchar(200) null,
	price float null,
	quantity int null
);