import point


class data_inquiries:
    def __init__(self):
        self.dict_x = {0: {0: 1}}

    def add_inquiries(self, point_inq):
        # בדיקה אם מפתח ה-x קיים במילון החיצוני
        if point_inq.x not in self.dict_x:
            # יצירת מילון פנימי אם לא קיים
            self.dict_x[point_inq.x] = {}

        # בדיקה אם מפתח ה-y קיים במילון הפנימי
        if point_inq.y not in self.dict_x[point_inq.x]:
            # הגדרת הערך ל-1 אם לא קיים
            self.dict_x[point_inq.x][point_inq.y] = 1
            # חזרה על 1 שמסמל שהערך לא היה קיים קודם
            return 1

        # אם הערך כבר קיים, חזרה על 0 שמסמל שהוא קיים
        return 0



    def printInq(self):
        print(self.dict_x)
