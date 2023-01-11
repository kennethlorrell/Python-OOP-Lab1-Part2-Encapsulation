class Student:
    def __init__(self, name, surname, rb_number, grades):
        self.name = name
        self.surname = surname
        self.rb_number = rb_number
        self.grades = grades

        self.avg_grade = sum(self.grades.values()) / len(self.grades)

class Group(Student):
    def __init__(self, number, l):
        if any(map(lambda x: not isinstance(x, Student), l)):
            raise Exception('Wrong class instance!')
        elif len(l) > 20: 
            raise Exception('Wrong group size')
          
        self.number = number
        self.l = list(set(l))

    def print_top5(self):
        top5 = sorted(self.l, key=lambda x: x.avg_grade, reverse=True)[:5]    
        print('Best students in group #{}:'.format(self.number))
        for st in top5:
            print(st.name, st.surname, st.avg_grade)
        return None
