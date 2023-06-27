import random


class Jobposition:
    
    id_description_dict = ["Teaching Assistant", "Professor", "Faculty Lecturer", "Department Chair", "Dean", "Vice Principal", "Principal"]
    
    def __init__(self,job_id,description):
        self.job_id = job_id
        self.description = description
        
        
        
    def id_to_description(self):
        x = self.job_id
        if x>= 0 and x<=99:
            self.description = Jobposition.id_description_dict[0]
            
        elif x>=100 and x<=499:
            self.description = Jobposition.id_description_dict[1]
        
        elif x>=500 and x<=999:
            self.description = Jobposition.id_description_dict[2]
            
        elif x>=1000 and x<=1999:
            self.description = Jobposition.id_description_dict[3]
            
        elif x>=2000 and x<=2999:
            self.description = Jobposition.id_description_dict[4]
            
        elif x>=3000 and x<=3999:
            self.description = Jobposition.id_description_dict[5]
            
        elif x == 4000:
            self.description = Jobposition.id_description_dict[6]

