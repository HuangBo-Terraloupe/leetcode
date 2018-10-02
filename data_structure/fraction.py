class Fraction:
    def __init__(self, num_top, num_bottol):
        self.num_top = num_top
        self.num_bottol = num_bottol

    def add(self, new_num_top, new_num_bottol):
        output_num_top = self.num_top * new_num_bottol + self.num_bottol * new_num_top
        output_num_bottol = self.num_bottol * new_num_bottol
        gcd = self.find_gcd(output_num_top, output_num_bottol)
        return str(int(output_num_top/gcd)) + '/' + str(int(output_num_bottol/gcd))


    def find_gcd(self, top_num, bottol_num):
        common_factor = 1
        for i in range(min(abs(top_num), abs(bottol_num)), 1, -1):
            if top_num % i == 0 and bottol_num % i == 0:
                common_factor = i
                break
        return common_factor
