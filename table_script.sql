-- marquezlucasa_coderhouse.animals definition

-- Drop table

-- DROP TABLE marquezlucasa_coderhouse.animals;

--DROP TABLE marquezlucasa_coderhouse.animals;
CREATE TABLE IF NOT EXISTS marquezlucasa_coderhouse.animals
(
	status VARCHAR(40)   ENCODE lzo
	,_id VARCHAR(50) NOT NULL  ENCODE lzo
	,"user" VARCHAR(50)   ENCODE lzo
	,text VARCHAR(100)   ENCODE lzo
	,__v INTEGER NOT NULL  ENCODE az64
	,source VARCHAR(30)   ENCODE lzo
	,updatedat VARCHAR(100)   ENCODE lzo
	,"type" VARCHAR(30)   ENCODE lzo
	,createdat VARCHAR(100)   ENCODE lzo
	,deleted BOOLEAN   ENCODE RAW
	,used BOOLEAN   ENCODE RAW
	,PRIMARY KEY (_id)
)
DISTSTYLE AUTO
;
ALTER TABLE marquezlucasa_coderhouse.animals owner to marquezlucasa_coderhouse;