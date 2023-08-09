#!/bin/sh
source /etc/profile
source /home/hadoop/.hive_config.sh
#############################################
process_start
#########################################################以上不用修改

write_cgr "根据地址匹配出省市区"
write_log "使用高德地图api，存在db_name"
sql_1="use ${db_name};
add file /home/lijicong/gaodeApi.py;
insert into table kn1_zx_need_city
select transform (t.zx_need_id,t.need_time,t.house_address) using 'python gaodeApi.py' as (col1,col2,col3,col4,col5,col6,col7) from (select zx_need_id,need_time,house_address from dw.kn1_zx_need where house_station = '钓鱼岛' and need_time >= from_unixtime(unix_timestamp('${date}','yyyyMMdd'), 'yyyy-MM-dd')) as t;
"
hive_txt "$sql_1"

#########################################################以下不用修改
process_end
