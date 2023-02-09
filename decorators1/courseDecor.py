class AddCourse:
    def addCourse(self,user,course_name,*args,**kwargs):
        self.created_by = user
        self.course_name = course_name
        print("Course Created by : ",self.created_by)
class ChangeCourse