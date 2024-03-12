"""this file is generated by tools/generate_sql_functions.py"""

from sqlalchemy import column
from sqlalchemy import func
from sqlalchemy import Integer
from sqlalchemy import select
from sqlalchemy import Sequence
from sqlalchemy import String

# START GENERATED FUNCTION TYPING TESTS

# code within this block is **programmatically,
# statically generated** by tools/generate_sql_functions.py

stmt1 = select(func.aggregate_strings(column("x", String), ","))

# EXPECTED_RE_TYPE: .*Select\[.*str\]
reveal_type(stmt1)


stmt2 = select(func.char_length(column("x")))

# EXPECTED_RE_TYPE: .*Select\[.*int\]
reveal_type(stmt2)


stmt3 = select(func.coalesce(column("x", Integer)))

# EXPECTED_RE_TYPE: .*Select\[.*int\]
reveal_type(stmt3)


stmt4 = select(func.concat())

# EXPECTED_RE_TYPE: .*Select\[.*str\]
reveal_type(stmt4)


stmt5 = select(func.count(column("x")))

# EXPECTED_RE_TYPE: .*Select\[.*int\]
reveal_type(stmt5)


stmt6 = select(func.cume_dist())

# EXPECTED_RE_TYPE: .*Select\[.*Decimal\]
reveal_type(stmt6)


stmt7 = select(func.current_date())

# EXPECTED_RE_TYPE: .*Select\[.*date\]
reveal_type(stmt7)


stmt8 = select(func.current_time())

# EXPECTED_RE_TYPE: .*Select\[.*time\]
reveal_type(stmt8)


stmt9 = select(func.current_timestamp())

# EXPECTED_RE_TYPE: .*Select\[.*datetime\]
reveal_type(stmt9)


stmt10 = select(func.current_user())

# EXPECTED_RE_TYPE: .*Select\[.*str\]
reveal_type(stmt10)


stmt11 = select(func.dense_rank())

# EXPECTED_RE_TYPE: .*Select\[.*int\]
reveal_type(stmt11)


stmt12 = select(func.localtime())

# EXPECTED_RE_TYPE: .*Select\[.*datetime\]
reveal_type(stmt12)


stmt13 = select(func.localtimestamp())

# EXPECTED_RE_TYPE: .*Select\[.*datetime\]
reveal_type(stmt13)


stmt14 = select(func.max(column("x", Integer)))

# EXPECTED_RE_TYPE: .*Select\[.*int\]
reveal_type(stmt14)


stmt15 = select(func.min(column("x", Integer)))

# EXPECTED_RE_TYPE: .*Select\[.*int\]
reveal_type(stmt15)


stmt16 = select(func.next_value(Sequence("x_seq")))

# EXPECTED_RE_TYPE: .*Select\[.*int\]
reveal_type(stmt16)


stmt17 = select(func.now())

# EXPECTED_RE_TYPE: .*Select\[.*datetime\]
reveal_type(stmt17)


stmt18 = select(func.percent_rank())

# EXPECTED_RE_TYPE: .*Select\[.*Decimal\]
reveal_type(stmt18)


stmt19 = select(func.rank())

# EXPECTED_RE_TYPE: .*Select\[.*int\]
reveal_type(stmt19)


stmt20 = select(func.session_user())

# EXPECTED_RE_TYPE: .*Select\[.*str\]
reveal_type(stmt20)


stmt21 = select(func.sum(column("x", Integer)))

# EXPECTED_RE_TYPE: .*Select\[.*int\]
reveal_type(stmt21)


stmt22 = select(func.sysdate())

# EXPECTED_RE_TYPE: .*Select\[.*datetime\]
reveal_type(stmt22)


stmt23 = select(func.user())

# EXPECTED_RE_TYPE: .*Select\[.*str\]
reveal_type(stmt23)

# END GENERATED FUNCTION TYPING TESTS