select Class
from Courses group by Class having count(student)>=5;