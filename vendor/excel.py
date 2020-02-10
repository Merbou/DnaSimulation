# from pandas import DataFrame
import xlsxwriter


class excel():

    def __init__(self, data):
        self.__data = data

    def export_excel(self, path):
        """
        @params String
        export data to excel file
        @return None
        """
        Sequances = self.__data["sequances"]
        Static = self.__data["static"]

        keys = list(Sequances.keys())

        # create Excel
        workbook = xlsxwriter.Workbook(path+"\\"+keys[0]+".xlsx")
        # Open pages Excel
        worksheet = workbook.add_worksheet("Sequance")
        worksheet2 = workbook.add_worksheet("Static")

        # Save content
        self.Create_page(worksheet, Sequances)
        self.Create_page(worksheet2, Static)

        workbook.close()

    def Create_page(self, excel, data):
        """
        @params Object,dict
        Save content from data to excel
        @return None
        """
        row = 0
        # write row by row
        for key, value in data.items():

            # nested dict
            if(isinstance(value, dict)):
                excel.write(row, 0, key)
                row += 1
                for k, v in value.items():
                    excel.write(row, 0, k)
                    excel.write(row, 1, v)
                    row += 1
            else:
                excel.write(row, 0, key)
                excel.write(row, 1, value)

            # incrementing the value of row by one
            row += 1
