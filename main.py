import pandas as pd

from csvTidy import DataProcessor


class StudentDataProcessor:
    def __init__(self, file_path):
        # 初始化時讀取CSV檔案
        self.df = pd.read_csv(file_path)

    def search_teacher_extension_by_student_id(self, student_id):
        # 功能一：由學生學號查詢教師分機
        return self.df[self.df['學號'] == student_id][['教師分機', '授課教師']].drop_duplicates()

    def search_teacher_extension_by_course_code(self, course_code):
        # 功能二：由課程代號查詢教師分機
        return self.df[self.df['課程編號'] == course_code][['教師分機', '授課教師']].drop_duplicates()

    def search_courses_by_student_id(self, student_id):
        # 功能三：由學生學號查詢所有課程名稱及學分
        return self.df[self.df['學號'] == student_id][['課程名稱', '學分']]

    def calculate_grade_distribution(self):
        # 功能四：統計各科成績並顯示成績分佈
        return self.df['成績'].value_counts().sort_index()

    def calculate_average_grade_by_student_id(self, student_id):
        # 功能五：由學生學號查詢各科成績並計算平均成績
        grades = self.df[self.df['學號'] == student_id]['成績']
        average = grades.mean()
        return grades, average


def action():
    file_path = 'Final_Result.csv'  # 您可以更改此路徑以符合您的檔案位置
    processor = StudentDataProcessor(file_path)

    while True:
        print("\n操作選單:")
        print("1. 查詢教師分機 - 以學生學號")
        print("2. 查詢教師分機 - 以課程代號")
        print("3. 查詢所有課程名稱及學分")
        print("4. 顯示成績分佈")
        print("5. 查詢各科成績並計算平均成績")
        print("6. 合併表單")
        print("0. 退出")

        choice = input("請輸入您的選擇: ")

        if choice == "1":
            student_id = input("請輸入學生學號: ")
            print(processor.search_teacher_extension_by_student_id(student_id))
        elif choice == "2":
            course_code = input("請輸入課程代號: ")
            print(processor.search_teacher_extension_by_course_code(course_code))
        elif choice == "3":
            student_id = input("請輸入學生學號: ")
            print(processor.search_courses_by_student_id(student_id))
        elif choice == "4":
            print(processor.calculate_grade_distribution())
        elif choice == "5":
            student_id = input("請輸入學生學號: ")
            grades, avg_grade = processor.calculate_average_grade_by_student_id(
                student_id)
            print("成績:", grades)
            print("平均成績:", avg_grade)
        elif choice == "6":
            processor = DataProcessor()
            processor.process_data()
        elif choice == "0":
            break
        else:
            print("無效的輸入，請重新輸入。")


if __name__ == '__main__':
    action()
