import os
import glob
import pandas as pd


class DataProcessor:
    def __init__(self, work_folder='/app/table', result_folder='/app'):
        self.work_folder = work_folder
        self.result_folder = result_folder

    def get_all_csv_files(self):
        os.chdir(self.work_folder)
        file_list = glob.glob("*.csv")
        return file_list

    def read_all_csv_files(self, file_list):
        df_list = []
        for file in file_list:
            df = pd.read_csv(file, encoding='utf_8_sig')
            df_list.append(df)
        return df_list

    def combine_all_dataframes(self, df_list):
        return pd.concat(df_list)

    def split_data_into_three_parts(self, df):
        students = df[df['姓名'].notna()][['學號', '姓名', '性別']].drop_duplicates()
        courses = df[df['課程名稱'].notna()][['課程編號', '課程名稱', '學分',
                                          '教師分機']].drop_duplicates()
        teachers = df[df['授課教師'].notna()][['教師分機', '授課教師']].drop_duplicates()
        return students, courses, teachers

    def combine_courses_and_teachers(self, courses, teachers):
        return courses.merge(teachers, on='教師分機')

    def combine_students_and_grades(self, students, grades):
        return students.merge(grades, on='學號')

    def combine_result_and_courses(self, result, courses):
        return result.merge(courses, on='課程編號')

    def get_final_result_file_path(self):
        return os.path.join(self.result_folder, 'Final_Result.csv')

    def save_result_to_csv(self, result):
        result_csv_file_path = self.get_final_result_file_path()
        result.to_csv(result_csv_file_path, index=False, encoding='utf_8_sig')

    def process_data(self):
        file_list = self.get_all_csv_files()
        df_list = self.read_all_csv_files(file_list)
        df = self.combine_all_dataframes(df_list)
        students, courses, teachers = self.split_data_into_three_parts(df)
        courses = self.combine_courses_and_teachers(courses, teachers)
        grades = df[df['成績'].notna()][['學號', '課程編號', '成績']].drop_duplicates()
        result = self.combine_students_and_grades(students, grades)
        result = self.combine_result_and_courses(result, courses)
        self.save_result_to_csv(result)


if __name__ == '__main__':
    processor = DataProcessor()
    processor.process_data()
