import os
from django.conf import settings

class LoadDatabaseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        #self.db_data = self.load_file('database.txt')
        self.load_all_data()

    def __call__(self, request):

        #request.db_data = self.db_data
        request.data_01 = self.data_01
        request.data_02 = self.data_02
        request.data_03 = self.data_03
        request.data_04 = self.data_04
        request.data_05 = self.data_05
        request.data_06 = self.data_06
        request.data_07 = self.data_07
        request.data_08 = self.data_08
        request.data_09 = self.data_09
        request.data_10 = self.data_10
        request.data_11 = self.data_11
        request.data_12 = self.data_12
        request.data_13 = self.data_13
        request.data_14 = self.data_14
        request.data_15 = self.data_15
        request.data_16 = self.data_16
        request.data_17 = self.data_17
        request.data_xx = self.data_xx
        request.data_yy = self.data_yy
        # Attach other data as needed

        response = self.get_response(request)

        # Additional processing of the response, if needed

        return response

    def load_all_data(self):
        # Load data from all 17 files
        self.data_01 = self.load_file('SS_SDG01.txt')
        self.data_02 = self.load_file('SS_SDG02.txt')
        self.data_03 = self.load_file('SS_SDG03.txt')
        self.data_04 = self.load_file('SS_SDG04.txt')
        self.data_05 = self.load_file('SS_SDG05.txt')
        self.data_06 = self.load_file('SS_SDG06.txt')
        self.data_07 = self.load_file('SS_SDG07.txt')
        self.data_08 = self.load_file('SS_SDG08.txt')
        self.data_09 = self.load_file('SS_SDG09.txt')
        self.data_10 = self.load_file('SS_SDG10.txt')
        self.data_11 = self.load_file('SS_SDG11.txt')
        self.data_12 = self.load_file('SS_SDG12.txt')
        self.data_13 = self.load_file('SS_SDG13.txt')
        self.data_14 = self.load_file('SS_SDG14.txt')
        self.data_15 = self.load_file('SS_SDG15.txt')
        self.data_16 = self.load_file('SS_SDG16.txt')
        self.data_17 = self.load_file('SS_SDG17.txt')
        self.data_xx = self.load_file('SS_KOP_01.txt')
        self.data_yy = self.load_file('SS_KOP_25.txt')
        
        # Load data for other files as needed
        #return self.get_response(request)

    def load_file(self, filename):
        try:
            file_path = os.path.join(settings.BASE_DIR, 'productionfiles', filename)
            with open(file_path, 'r' , encoding="utf8") as file:

                lines = file.readlines()
                content = [line.strip().lower() for line in lines]

            return content
                
        except Exception as e:
            return f"Error loading {filename}: {e}"
