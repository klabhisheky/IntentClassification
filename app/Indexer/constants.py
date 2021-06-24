
# API related constants
STATUS_CODE = {
	"SUCCESS" 		: 200,
	"FAIL"			: 500,
	"BAD_REQUEST"	: 400
}

CROSS_ORIGIN_POLICY = {'Access-Control-Allow-Origin': '*'}

# Class related mapping - 2-way HashTable as constant
MAP_TABLE = {
    "Procedure" : 1,
    "Doctors"   : 2,
    "General"   : 3,
    "Desirable" : 4,
    "Hospital"  : 5,
    "Location"  : 6,
    "Cost"      : 7, 
    1           : "Procedure",
    2           : "Doctor",
    3           : "General",
    4           : "Desirable",
    5           : "Hospital",
    6           : "Location",
    7           : "Cost"
}