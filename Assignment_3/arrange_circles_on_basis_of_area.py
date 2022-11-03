'''Dictionary was selected over a list as data structure to store information of each circle, 
because it is easier to keep track of which value represents radius, centre or the area using keys
while in list the values will be denoted of basis of their indexes 0-radius, 1-centre, 2- area
the final data will not be readable if the number of circle are more, hence for readability of final output and 
since dictionaries are mutable object, it was used to store information of each circle'''


'''list was selected for store information of all circle, since list are mutables and are ordered, it is useful to 
perform operations like sorting.'''

'''the final data is a list of dictionaries where each dictionary represents a circle'''


from utils.input_utils import get_input_number, get_input_list
from utils.utils import sort_list_of_dictionary

if __name__ == '__main__':
    print('Enter number of circles')
    circle_count = get_input_number()

    circle_info_list = []
    for i in range(0, circle_count):
        circle_info = {}
        print(f'Enter Information for circle {i+1}')

        radius = float(input('Enter the radius: '))
        circle_info['radius'] = radius

        print('Enter x,y co-oridnates of the centre of the cirle')
        centre = get_input_list(2, element_type='float')
        circle_info['centre'] = centre

        area = 3.142 * radius
        circle_info['area'] = area

        circle_info_list.append(circle_info)

    sorted_circle_info = sort_list_of_dictionary(circle_info_list, key = 'area')
    # alternate way to sort list of dictionaries -
    # sorted_circle_info = sorted(circle_info_list , key = lambda x : x['area'])
    print(sorted_circle_info)


